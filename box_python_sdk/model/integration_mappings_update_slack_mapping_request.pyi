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


class IntegrationMappingsUpdateSlackMappingRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def box_item() -> typing.Type['IntegrationMappingBoxItemSlack']:
                return IntegrationMappingBoxItemSlack
        
            @staticmethod
            def options() -> typing.Type['IntegrationMappingSlackOptions']:
                return IntegrationMappingSlackOptions
            __annotations__ = {
                "box_item": box_item,
                "options": options,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["box_item"]) -> 'IntegrationMappingBoxItemSlack': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'IntegrationMappingSlackOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["box_item", "options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["box_item"]) -> typing.Union['IntegrationMappingBoxItemSlack', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union['IntegrationMappingSlackOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["box_item", "options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        box_item: typing.Union['IntegrationMappingBoxItemSlack', schemas.Unset] = schemas.unset,
        options: typing.Union['IntegrationMappingSlackOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IntegrationMappingsUpdateSlackMappingRequest':
        return super().__new__(
            cls,
            *args,
            box_item=box_item,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.integration_mapping_box_item_slack import IntegrationMappingBoxItemSlack
from box_python_sdk.model.integration_mapping_slack_options import IntegrationMappingSlackOptions