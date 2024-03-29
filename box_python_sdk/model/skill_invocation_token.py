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


class SkillInvocationToken(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The read-only and read-write access tokens for this item
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def read() -> typing.Type['SkillInvocationTokenRead']:
                return SkillInvocationTokenRead
        
            @staticmethod
            def write() -> typing.Type['SkillInvocationTokenWrite']:
                return SkillInvocationTokenWrite
            __annotations__ = {
                "read": read,
                "write": write,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["read"]) -> 'SkillInvocationTokenRead': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["write"]) -> 'SkillInvocationTokenWrite': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["read", "write", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["read"]) -> typing.Union['SkillInvocationTokenRead', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["write"]) -> typing.Union['SkillInvocationTokenWrite', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["read", "write", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        read: typing.Union['SkillInvocationTokenRead', schemas.Unset] = schemas.unset,
        write: typing.Union['SkillInvocationTokenWrite', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SkillInvocationToken':
        return super().__new__(
            cls,
            *args,
            read=read,
            write=write,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.skill_invocation_token_read import SkillInvocationTokenRead
from box_python_sdk.model.skill_invocation_token_write import SkillInvocationTokenWrite
