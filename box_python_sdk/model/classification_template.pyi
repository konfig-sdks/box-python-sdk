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


class ClassificationTemplate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A metadata template that holds the security classifications
defined by an enterprise.
    """


    class MetaOapg:
        required = {
            "displayName",
            "scope",
            "id",
            "fields",
            "type",
            "templateKey",
        }
        
        class properties:
            id = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def METADATA_TEMPLATE(cls):
                    return cls("metadata_template")
            scope = schemas.StrSchema
            
            
            class templateKey(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SECURITY_CLASSIFICATION6VMVOCHW_UWO(cls):
                    return cls("securityClassification-6VMVochwUWo")
            
            
            class displayName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CLASSIFICATION(cls):
                    return cls("Classification")
        
            @staticmethod
            def fields() -> typing.Type['ClassificationTemplateFields']:
                return ClassificationTemplateFields
            hidden = schemas.BoolSchema
            copyInstanceOnItemCopy = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "type": type,
                "scope": scope,
                "templateKey": templateKey,
                "displayName": displayName,
                "fields": fields,
                "hidden": hidden,
                "copyInstanceOnItemCopy": copyInstanceOnItemCopy,
            }
    
    displayName: MetaOapg.properties.displayName
    scope: MetaOapg.properties.scope
    id: MetaOapg.properties.id
    fields: 'ClassificationTemplateFields'
    type: MetaOapg.properties.type
    templateKey: MetaOapg.properties.templateKey
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateKey"]) -> MetaOapg.properties.templateKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fields"]) -> 'ClassificationTemplateFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hidden"]) -> MetaOapg.properties.hidden: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyInstanceOnItemCopy"]) -> MetaOapg.properties.copyInstanceOnItemCopy: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "scope", "templateKey", "displayName", "fields", "hidden", "copyInstanceOnItemCopy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateKey"]) -> MetaOapg.properties.templateKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> 'ClassificationTemplateFields': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hidden"]) -> typing.Union[MetaOapg.properties.hidden, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyInstanceOnItemCopy"]) -> typing.Union[MetaOapg.properties.copyInstanceOnItemCopy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "scope", "templateKey", "displayName", "fields", "hidden", "copyInstanceOnItemCopy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        displayName: typing.Union[MetaOapg.properties.displayName, str, ],
        scope: typing.Union[MetaOapg.properties.scope, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        fields: 'ClassificationTemplateFields',
        type: typing.Union[MetaOapg.properties.type, str, ],
        templateKey: typing.Union[MetaOapg.properties.templateKey, str, ],
        hidden: typing.Union[MetaOapg.properties.hidden, bool, schemas.Unset] = schemas.unset,
        copyInstanceOnItemCopy: typing.Union[MetaOapg.properties.copyInstanceOnItemCopy, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClassificationTemplate':
        return super().__new__(
            cls,
            *args,
            displayName=displayName,
            scope=scope,
            id=id,
            fields=fields,
            type=type,
            templateKey=templateKey,
            hidden=hidden,
            copyInstanceOnItemCopy=copyInstanceOnItemCopy,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.classification_template_fields import ClassificationTemplateFields