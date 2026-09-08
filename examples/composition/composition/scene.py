from fishjam.composition import (
    BoxShadow,
    HorizontalAlign,
    Image,
    ImageType,
    InputStream,
    InputStreamType,
    RescaleMode,
    Rescaler,
    RescalerType,
    Text,
    TextType,
    TextWeight,
    VideoScene,
    View,
    ViewType,
)

from .config import (
    CAMERA_INPUT_ID,
    FONT_FAMILY,
    LOGO_IMAGE_ID,
    MOVIE_INPUT_ID,
    WIDTH,
)

BAR_TEXT = "COMPOSITION DEMO   ///   publish a camera over WHIP to join"

CREAM = "#FCF6E7FF"
CORAL = "#ED716DFF"
BLACK = "#000000FF"
SHADOW = [BoxShadow(color="#00000026", offset_x=0, offset_y=10, blur_radius=24)]

MARGIN = 48
LOGO_SIZE = 72
BAR_HEIGHT = 44
STAGE_HEIGHT = 450
STAGE_WIDTH = STAGE_HEIGHT * 16 // 9


def _tile(input_id: str, **placement) -> View:
    return View(
        type_=ViewType.VIEW,
        background_color=BLACK,
        border_radius=20,
        box_shadow=SHADOW,
        children=[
            Rescaler(
                type_=RescalerType.RESCALER,
                child=InputStream(
                    type_=InputStreamType.INPUT_STREAM, input_id=input_id
                ),
                mode=RescaleMode.FILL,
            )
        ],
        **placement,
    )


def scene() -> VideoScene:
    stage = View(
        type_=ViewType.VIEW,
        top=MARGIN * 2 + LOGO_SIZE,
        left=(WIDTH - STAGE_WIDTH) // 2,
        width=STAGE_WIDTH,
        height=STAGE_HEIGHT,
        children=[
            _tile(
                MOVIE_INPUT_ID,
                top=0,
                left=0,
                width=STAGE_WIDTH,
                height=STAGE_HEIGHT,
            ),
            _tile(
                CAMERA_INPUT_ID,
                top=18,
                right=18,
                width=220,
                height=124,
                border_width=6,
                border_color=CORAL,
            ),
        ],
    )

    logo = View(
        type_=ViewType.VIEW,
        top=MARGIN,
        left=WIDTH - MARGIN - LOGO_SIZE,
        width=LOGO_SIZE,
        height=LOGO_SIZE,
        children=[Image(type_=ImageType.IMAGE, image_id=LOGO_IMAGE_ID)],
    )

    bar = View(
        type_=ViewType.VIEW,
        bottom=0,
        left=0,
        width=WIDTH,
        height=BAR_HEIGHT,
        background_color=CORAL,
        padding_horizontal=MARGIN,
        padding_vertical=12,
        children=[
            Text(
                type_=TextType.TEXT,
                text=BAR_TEXT,
                font_size=20,
                font_family=FONT_FAMILY,
                weight=TextWeight.SEMI_BOLD,
                color=CREAM,
                align=HorizontalAlign.LEFT,
            )
        ],
    )

    return VideoScene(
        root=View(
            type_=ViewType.VIEW,
            background_color=CREAM,
            children=[stage, logo, bar],
        )
    )
