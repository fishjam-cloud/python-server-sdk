from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackForwardingInfo")


@_attrs_define
class TrackForwardingInfo:
    """Information about a track forwarding for a specific peer

    Attributes:
        input_id (str): Input ID used by the composition Example: input-1.
        peer_id (str): Peer ID Example: peer-1.
        audio_track_id (Union[None, Unset, str]): ID of the forwarded audio track Example: track-audio-1.
        video_track_id (Union[None, Unset, str]): ID of the forwarded video track Example: track-video-1.
    """

    input_id: str
    peer_id: str
    audio_track_id: Union[None, Unset, str] = UNSET
    video_track_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_id = self.input_id

        peer_id = self.peer_id

        audio_track_id: Union[None, Unset, str]
        if isinstance(self.audio_track_id, Unset):
            audio_track_id = UNSET
        else:
            audio_track_id = self.audio_track_id

        video_track_id: Union[None, Unset, str]
        if isinstance(self.video_track_id, Unset):
            video_track_id = UNSET
        else:
            video_track_id = self.video_track_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "inputId": input_id,
            "peerId": peer_id,
        })
        if audio_track_id is not UNSET:
            field_dict["audioTrackId"] = audio_track_id
        if video_track_id is not UNSET:
            field_dict["videoTrackId"] = video_track_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_id = d.pop("inputId")

        peer_id = d.pop("peerId")

        def _parse_audio_track_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_track_id = _parse_audio_track_id(d.pop("audioTrackId", UNSET))

        def _parse_video_track_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        video_track_id = _parse_video_track_id(d.pop("videoTrackId", UNSET))

        track_forwarding_info = cls(
            input_id=input_id,
            peer_id=peer_id,
            audio_track_id=audio_track_id,
            video_track_id=video_track_id,
        )

        track_forwarding_info.additional_properties = d
        return track_forwarding_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
