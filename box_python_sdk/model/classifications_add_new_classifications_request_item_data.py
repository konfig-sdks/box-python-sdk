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


class ClassificationsAddNewClassificationsRequestItemData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The details of the classification to add.
    """


    class MetaOapg:
        required = {
            "key",
        }
        
        class properties:
            key = schemas.StrSchema
        
            @staticmethod
            def staticConfig() -> typing.Type['ClassificationsAddNewClassificationsRequestItemDataStaticConfig']:
                return ClassificationsAddNewClassificationsRequestItemDataStaticConfig
            __annotations__ = {
                "key": key,
                "staticConfig": staticConfig,
            }
    
    key: MetaOapg.properties.key
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["staticConfig"]) -> 'ClassificationsAddNewClassificationsRequestItemDataStaticConfig': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["key", "staticConfig", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["staticConfig"]) -> typing.Union['ClassificationsAddNewClassificationsRequestItemDataStaticConfig', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key", "staticConfig", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        staticConfig: typing.Union['ClassificationsAddNewClassificationsRequestItemDataStaticConfig', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClassificationsAddNewClassificationsRequestItemData':
        return super().__new__(
            cls,
            *args,
            key=key,
            staticConfig=staticConfig,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.classifications_add_new_classifications_request_item_data_static_config import ClassificationsAddNewClassificationsRequestItemDataStaticConfig
