"""Contains all the data models used in inputs/outputs"""

from .api_error import ApiError
from .audio_channels import AudioChannels
from .audio_mixing_strategy import AudioMixingStrategy
from .audio_scene import AudioScene
from .audio_scene_input import AudioSceneInput
from .average_and_max_bitrate import AverageAndMaxBitrate
from .box_shadow import BoxShadow
from .composition_created_response import CompositionCreatedResponse
from .create_composition_request import CreateCompositionRequest
from .easing_function_bounce import EasingFunctionBounce
from .easing_function_bounce_function_name import EasingFunctionBounceFunctionName
from .easing_function_cubic_bezier import EasingFunctionCubicBezier
from .easing_function_cubic_bezier_function_name import (
    EasingFunctionCubicBezierFunctionName,
)
from .easing_function_linear import EasingFunctionLinear
from .easing_function_linear_function_name import EasingFunctionLinearFunctionName
from .empty_response import EmptyResponse
from .font_upload import FontUpload
from .h264_encoder_preset import H264EncoderPreset
from .horizontal_align import HorizontalAlign
from .image import Image
from .image_spec_auto import ImageSpecAuto
from .image_spec_auto_asset_type import ImageSpecAutoAssetType
from .image_spec_gif import ImageSpecGif
from .image_spec_gif_asset_type import ImageSpecGifAssetType
from .image_spec_jpeg import ImageSpecJpeg
from .image_spec_jpeg_asset_type import ImageSpecJpegAssetType
from .image_spec_png import ImageSpecPng
from .image_spec_png_asset_type import ImageSpecPngAssetType
from .image_spec_svg import ImageSpecSvg
from .image_spec_svg_asset_type import ImageSpecSvgAssetType
from .image_type import ImageType
from .input_stream import InputStream
from .input_stream_type import InputStreamType
from .interpolation import Interpolation
from .mp_4_input import Mp4Input
from .mp_4_input_type import Mp4InputType
from .opus_encoder_preset import OpusEncoderPreset
from .output_end_condition import OutputEndCondition
from .output_rtmp_client_audio_options import OutputRtmpClientAudioOptions
from .output_rtmp_client_video_options import OutputRtmpClientVideoOptions
from .output_whip_audio_options import OutputWhipAudioOptions
from .output_whip_video_options import OutputWhipVideoOptions
from .overflow import Overflow
from .pixel_format import PixelFormat
from .register_font_body import RegisterFontBody
from .register_input_response import RegisterInputResponse
from .register_template_output import RegisterTemplateOutput
from .register_template_output_body import RegisterTemplateOutputBody
from .rescale_mode import RescaleMode
from .rescaler import Rescaler
from .rescaler_type import RescalerType
from .resolution import Resolution
from .rtmp_input import RtmpInput
from .rtmp_input_type import RtmpInputType
from .rtmp_output import RtmpOutput
from .rtmp_output_type import RtmpOutputType
from .send_composition_event_body import SendCompositionEventBody
from .text import Text
from .text_style import TextStyle
from .text_type import TextType
from .text_weight import TextWeight
from .text_wrap_mode import TextWrapMode
from .tiles import Tiles
from .tiles_type import TilesType
from .transition import Transition
from .transport_protocol import TransportProtocol
from .unregister_input import UnregisterInput
from .unregister_output import UnregisterOutput
from .unregister_renderer import UnregisterRenderer
from .update_output_request import UpdateOutputRequest
from .vertical_align import VerticalAlign
from .video_scene import VideoScene
from .view import View
from .view_direction import ViewDirection
from .view_type import ViewType
from .whep_input import WhepInput
from .whep_input_type import WhepInputType
from .whip_audio_encoder_options_any import WhipAudioEncoderOptionsAny
from .whip_audio_encoder_options_any_type import WhipAudioEncoderOptionsAnyType
from .whip_audio_encoder_options_opus import WhipAudioEncoderOptionsOpus
from .whip_audio_encoder_options_opus_type import WhipAudioEncoderOptionsOpusType
from .whip_input import WhipInput
from .whip_input_type import WhipInputType
from .whip_output import WhipOutput
from .whip_output_type import WhipOutputType

__all__ = (
    "ApiError",
    "AudioChannels",
    "AudioMixingStrategy",
    "AudioScene",
    "AudioSceneInput",
    "AverageAndMaxBitrate",
    "BoxShadow",
    "CompositionCreatedResponse",
    "CreateCompositionRequest",
    "EasingFunctionBounce",
    "EasingFunctionBounceFunctionName",
    "EasingFunctionCubicBezier",
    "EasingFunctionCubicBezierFunctionName",
    "EasingFunctionLinear",
    "EasingFunctionLinearFunctionName",
    "EmptyResponse",
    "FontUpload",
    "H264EncoderPreset",
    "HorizontalAlign",
    "Image",
    "ImageSpecAuto",
    "ImageSpecAutoAssetType",
    "ImageSpecGif",
    "ImageSpecGifAssetType",
    "ImageSpecJpeg",
    "ImageSpecJpegAssetType",
    "ImageSpecPng",
    "ImageSpecPngAssetType",
    "ImageSpecSvg",
    "ImageSpecSvgAssetType",
    "ImageType",
    "InputStream",
    "InputStreamType",
    "Interpolation",
    "Mp4Input",
    "Mp4InputType",
    "OpusEncoderPreset",
    "OutputEndCondition",
    "OutputRtmpClientAudioOptions",
    "OutputRtmpClientVideoOptions",
    "OutputWhipAudioOptions",
    "OutputWhipVideoOptions",
    "Overflow",
    "PixelFormat",
    "RegisterFontBody",
    "RegisterInputResponse",
    "RegisterTemplateOutput",
    "RegisterTemplateOutputBody",
    "RescaleMode",
    "Rescaler",
    "RescalerType",
    "Resolution",
    "RtmpInput",
    "RtmpInputType",
    "RtmpOutput",
    "RtmpOutputType",
    "SendCompositionEventBody",
    "Text",
    "TextStyle",
    "TextType",
    "TextWeight",
    "TextWrapMode",
    "Tiles",
    "TilesType",
    "Transition",
    "TransportProtocol",
    "UnregisterInput",
    "UnregisterOutput",
    "UnregisterRenderer",
    "UpdateOutputRequest",
    "VerticalAlign",
    "VideoScene",
    "View",
    "ViewDirection",
    "ViewType",
    "WhepInput",
    "WhepInputType",
    "WhipAudioEncoderOptionsAny",
    "WhipAudioEncoderOptionsAnyType",
    "WhipAudioEncoderOptionsOpus",
    "WhipAudioEncoderOptionsOpusType",
    "WhipInput",
    "WhipInputType",
    "WhipOutput",
    "WhipOutputType",
)
