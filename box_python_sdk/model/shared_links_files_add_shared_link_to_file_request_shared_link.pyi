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


class SharedLinksFilesAddSharedLinkToFileRequestSharedLink(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The settings for the shared link to create on the file.
Use an empty object (`{}`) to use the default settings for shared
links.
    """


    class MetaOapg:
        
        class properties:
            
            
            class access(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("open")
                
                @schemas.classproperty
                def COMPANY(cls):
                    return cls("company")
                
                @schemas.classproperty
                def COLLABORATORS(cls):
                    return cls("collaborators")
            password = schemas.StrSchema
            
            
            class vanity_name(
                schemas.StrSchema
            ):
                pass
            unshared_at = schemas.DateTimeSchema
        
            @staticmethod
            def permissions() -> typing.Type['SharedLinksFilesAddSharedLinkToFileRequestSharedLinkPermissions']:
                return SharedLinksFilesAddSharedLinkToFileRequestSharedLinkPermissions
            __annotations__ = {
                "access": access,
                "password": password,
                "vanity_name": vanity_name,
                "unshared_at": unshared_at,
                "permissions": permissions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vanity_name"]) -> MetaOapg.properties.vanity_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unshared_at"]) -> MetaOapg.properties.unshared_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> 'SharedLinksFilesAddSharedLinkToFileRequestSharedLinkPermissions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["access", "password", "vanity_name", "unshared_at", "permissions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> typing.Union[MetaOapg.properties.access, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vanity_name"]) -> typing.Union[MetaOapg.properties.vanity_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unshared_at"]) -> typing.Union[MetaOapg.properties.unshared_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union['SharedLinksFilesAddSharedLinkToFileRequestSharedLinkPermissions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["access", "password", "vanity_name", "unshared_at", "permissions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        access: typing.Union[MetaOapg.properties.access, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        vanity_name: typing.Union[MetaOapg.properties.vanity_name, str, schemas.Unset] = schemas.unset,
        unshared_at: typing.Union[MetaOapg.properties.unshared_at, str, datetime, schemas.Unset] = schemas.unset,
        permissions: typing.Union['SharedLinksFilesAddSharedLinkToFileRequestSharedLinkPermissions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SharedLinksFilesAddSharedLinkToFileRequestSharedLink':
        return super().__new__(
            cls,
            *args,
            access=access,
            password=password,
            vanity_name=vanity_name,
            unshared_at=unshared_at,
            permissions=permissions,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.shared_links_files_add_shared_link_to_file_request_shared_link_permissions import SharedLinksFilesAddSharedLinkToFileRequestSharedLinkPermissions
