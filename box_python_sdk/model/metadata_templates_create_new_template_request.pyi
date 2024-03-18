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


class MetadataTemplatesCreateNewTemplateRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "displayName",
            "scope",
        }
        
        class properties:
            scope = schemas.StrSchema
            
            
            class displayName(
                schemas.StrSchema
            ):
                pass
            
            
            class templateKey(
                schemas.StrSchema
            ):
                pass
            hidden = schemas.BoolSchema
        
            @staticmethod
            def fields() -> typing.Type['MetadataTemplatesCreateNewTemplateRequestFields']:
                return MetadataTemplatesCreateNewTemplateRequestFields
            copyInstanceOnItemCopy = schemas.BoolSchema
            __annotations__ = {
                "scope": scope,
                "displayName": displayName,
                "templateKey": templateKey,
                "hidden": hidden,
                "fields": fields,
                "copyInstanceOnItemCopy": copyInstanceOnItemCopy,
            }
    
    displayName: MetaOapg.properties.displayName
    scope: MetaOapg.properties.scope
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateKey"]) -> MetaOapg.properties.templateKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hidden"]) -> MetaOapg.properties.hidden: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'MetadataTemplatesCreateNewTemplateRequestFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyInstanceOnItemCopy"]) -> MetaOapg.properties.copyInstanceOnItemCopy: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["scope", "displayName", "templateKey", "hidden", "fields", "copyInstanceOnItemCopy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateKey"]) -> typing.Union[MetaOapg.properties.templateKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hidden"]) -> typing.Union[MetaOapg.properties.hidden, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union['MetadataTemplatesCreateNewTemplateRequestFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyInstanceOnItemCopy"]) -> typing.Union[MetaOapg.properties.copyInstanceOnItemCopy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["scope", "displayName", "templateKey", "hidden", "fields", "copyInstanceOnItemCopy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        displayName: typing.Union[MetaOapg.properties.displayName, str, ],
        scope: typing.Union[MetaOapg.properties.scope, str, ],
        templateKey: typing.Union[MetaOapg.properties.templateKey, str, schemas.Unset] = schemas.unset,
        hidden: typing.Union[MetaOapg.properties.hidden, bool, schemas.Unset] = schemas.unset,
        fields: typing.Union['MetadataTemplatesCreateNewTemplateRequestFields', schemas.Unset] = schemas.unset,
        copyInstanceOnItemCopy: typing.Union[MetaOapg.properties.copyInstanceOnItemCopy, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MetadataTemplatesCreateNewTemplateRequest':
        return super().__new__(
            cls,
            *args,
            displayName=displayName,
            scope=scope,
            templateKey=templateKey,
            hidden=hidden,
            fields=fields,
            copyInstanceOnItemCopy=copyInstanceOnItemCopy,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.metadata_templates_create_new_template_request_fields import MetadataTemplatesCreateNewTemplateRequestFields
