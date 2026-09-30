from fishjam._fishjam_openapi_client.models import (
    CompositionSource,
    Recording,
    RecordingStatus,
    TemplateSource,
    TemplateSourceResolution,
)

RecordingSource = CompositionSource | TemplateSource
"""What a recording captures, one member per source type."""

__all__ = [
    "CompositionSource",
    "Recording",
    "RecordingSource",
    "RecordingStatus",
    "TemplateSource",
    "TemplateSourceResolution",
]
