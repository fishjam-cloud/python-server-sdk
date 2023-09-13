# coding: utf-8

"""
    Python API wrapper for Jellyfish Media Server

    The version of the OpenAPI document: 0.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class HlsSkip(str, Enum):
    """
    Is delta manifest requested
    """

    """
    allowed enum values
    """
    TRUE = 'true'

    @classmethod
    def from_json(cls, json_str: str) -> HlsSkip:
        """Create an instance of HlsSkip from a JSON string"""
        return HlsSkip(json.loads(json_str))

