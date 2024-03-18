# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from box_python_sdk.pydantic.shield_information_barrier_base import ShieldInformationBarrierBase
from box_python_sdk.pydantic.shield_information_barrier_segment_restrictions_create_barrier_object_request_restricted_segment import ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestRestrictedSegment
from box_python_sdk.pydantic.shield_information_barrier_segment_restrictions_create_barrier_object_request_shield_information_barrier_segment import ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestShieldInformationBarrierSegment

class ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequest(BaseModel):
    # The type of the shield barrier segment restriction for this member.
    type: Literal["shield_information_barrier_segment_restriction"] = Field(alias='type')

    shield_information_barrier_segment: ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestShieldInformationBarrierSegment = Field(alias='shield_information_barrier_segment')

    restricted_segment: ShieldInformationBarrierSegmentRestrictionsCreateBarrierObjectRequestRestrictedSegment = Field(alias='restricted_segment')

    shield_information_barrier: typing.Optional[ShieldInformationBarrierBase] = Field(None, alias='shield_information_barrier')
    class Config:
        arbitrary_types_allowed = True
