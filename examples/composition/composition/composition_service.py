import httpx

from fishjam import CompositionClient, WhipInputTarget
from fishjam.composition import (
    AudioScene,
    AudioSceneInput,
    ImageSpecSvg,
    ImageSpecSvgAssetType,
    OutputWhipAudioOptions,
    OutputWhipVideoOptions,
    Resolution,
)

from .config import (
    CAMERA_INPUT_ID,
    FONT_URL,
    HEIGHT,
    LOGO_IMAGE_ID,
    LOGO_URL,
    MOVIE_INPUT_ID,
    MOVIE_URL,
    OUTPUT_ID,
    WIDTH,
)
from .scene import scene


class CompositionService:
    def __init__(self, management_token: str, composition_url: str | None = None):
        self.compositions = CompositionClient(
            management_token=management_token, composition_url=composition_url
        )
        self.composition_id = self.compositions.create_composition().composition_id
        self._camera: WhipInputTarget | None = None

    def register_assets(self) -> None:
        self.compositions.register_font(
            self.composition_id, httpx.get(FONT_URL, follow_redirects=True).content
        )
        self.compositions.register_image(
            self.composition_id,
            LOGO_IMAGE_ID,
            ImageSpecSvg(
                asset_type=ImageSpecSvgAssetType.SVG,
                url=LOGO_URL,
                resolution=Resolution(width=200, height=200),
            ),
        )

    def play_movie(self) -> None:
        self.compositions.register_mp4_input(
            self.composition_id, MOVIE_INPUT_ID, url=MOVIE_URL, loop=True
        )

    def camera(self) -> WhipInputTarget:
        if self._camera is None:
            self._camera = self.compositions.register_whip_input(
                self.composition_id, CAMERA_INPUT_ID, video=True
            )

        return self._camera

    def stream_to(self, endpoint_url: str, bearer_token: str) -> None:
        self.compositions.register_whip_output(
            self.composition_id,
            OUTPUT_ID,
            endpoint_url=endpoint_url,
            bearer_token=bearer_token,
            video=OutputWhipVideoOptions(
                resolution=Resolution(width=WIDTH, height=HEIGHT), initial=scene()
            ),
            audio=OutputWhipAudioOptions(
                initial=AudioScene(
                    inputs=[
                        AudioSceneInput(input_id=CAMERA_INPUT_ID),
                        AudioSceneInput(input_id=MOVIE_INPUT_ID, volume=0.2),
                    ]
                )
            ),
        )

    def cleanup(self) -> None:
        self.compositions.delete_composition(self.composition_id)
