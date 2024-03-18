# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from box_python_sdk import schemas  # noqa: F401


class StatusSkillCard(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A Box Skill metadata card that puts a status message in the metadata sidebar.
    """


    class MetaOapg:
        required = {
            "invocation",
            "skill",
            "type",
            "skill_card_type",
            "status",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SKILL_CARD(cls):
                    return cls("skill_card")
            
            
            class skill_card_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STATUS(cls):
                    return cls("status")
        
            @staticmethod
            def status() -> typing.Type['StatusSkillCardStatus']:
                return StatusSkillCardStatus
        
            @staticmethod
            def skill() -> typing.Type['StatusSkillCardSkill']:
                return StatusSkillCardSkill
        
            @staticmethod
            def invocation() -> typing.Type['StatusSkillCardInvocation']:
                return StatusSkillCardInvocation
            created_at = schemas.DateTimeSchema
        
            @staticmethod
            def skill_card_title() -> typing.Type['StatusSkillCardSkillCardTitle']:
                return StatusSkillCardSkillCardTitle
            __annotations__ = {
                "type": type,
                "skill_card_type": skill_card_type,
                "status": status,
                "skill": skill,
                "invocation": invocation,
                "created_at": created_at,
                "skill_card_title": skill_card_title,
            }
    
    invocation: 'StatusSkillCardInvocation'
    skill: 'StatusSkillCardSkill'
    type: MetaOapg.properties.type
    skill_card_type: MetaOapg.properties.skill_card_type
    status: 'StatusSkillCardStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skill_card_type"]) -> MetaOapg.properties.skill_card_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'StatusSkillCardStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skill"]) -> 'StatusSkillCardSkill': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invocation"]) -> 'StatusSkillCardInvocation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skill_card_title"]) -> 'StatusSkillCardSkillCardTitle': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "skill_card_type", "status", "skill", "invocation", "created_at", "skill_card_title", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skill_card_type"]) -> MetaOapg.properties.skill_card_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'StatusSkillCardStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skill"]) -> 'StatusSkillCardSkill': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invocation"]) -> 'StatusSkillCardInvocation': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skill_card_title"]) -> typing.Union['StatusSkillCardSkillCardTitle', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "skill_card_type", "status", "skill", "invocation", "created_at", "skill_card_title", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        invocation: 'StatusSkillCardInvocation',
        skill: 'StatusSkillCardSkill',
        type: typing.Union[MetaOapg.properties.type, str, ],
        skill_card_type: typing.Union[MetaOapg.properties.skill_card_type, str, ],
        status: 'StatusSkillCardStatus',
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        skill_card_title: typing.Union['StatusSkillCardSkillCardTitle', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatusSkillCard':
        return super().__new__(
            cls,
            *args,
            invocation=invocation,
            skill=skill,
            type=type,
            skill_card_type=skill_card_type,
            status=status,
            created_at=created_at,
            skill_card_title=skill_card_title,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.status_skill_card_invocation import StatusSkillCardInvocation
from box_python_sdk.model.status_skill_card_skill import StatusSkillCardSkill
from box_python_sdk.model.status_skill_card_skill_card_title import StatusSkillCardSkillCardTitle
from box_python_sdk.model.status_skill_card_status import StatusSkillCardStatus