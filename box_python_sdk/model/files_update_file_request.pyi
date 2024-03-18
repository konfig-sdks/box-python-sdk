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


class FilesUpdateFileRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def tags() -> typing.Type['FilesUpdateFileRequestTags']:
                return FilesUpdateFileRequestTags
            
            
            class description(
                schemas.StrSchema
            ):
                pass
            name = schemas.StrSchema
            
            
            class parent(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class all_of_0(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                id = schemas.StrSchema
                                __annotations__ = {
                                    "id": id,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'all_of_0':
                            return super().__new__(
                                cls,
                                *args,
                                id=id,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    all_of_1 = schemas.AnyTypeSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.all_of_0,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'parent':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class shared_link(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class all_of_0(
                        schemas.DictSchema
                    ):
                    
                    
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
                                vanity_name = schemas.StrSchema
                                unshared_at = schemas.DateTimeSchema
                                
                                
                                class permissions(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        class properties:
                                            can_download = schemas.BoolSchema
                                            __annotations__ = {
                                                "can_download": can_download,
                                            }
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["can_download"]) -> MetaOapg.properties.can_download: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["can_download", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["can_download"]) -> typing.Union[MetaOapg.properties.can_download, schemas.Unset]: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["can_download", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[dict, frozendict.frozendict, ],
                                        can_download: typing.Union[MetaOapg.properties.can_download, bool, schemas.Unset] = schemas.unset,
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'permissions':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            can_download=can_download,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
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
                        def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> MetaOapg.properties.permissions: ...
                        
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
                        def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union[MetaOapg.properties.permissions, schemas.Unset]: ...
                        
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
                            permissions: typing.Union[MetaOapg.properties.permissions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'all_of_0':
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
                    all_of_1 = schemas.AnyTypeSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.all_of_0,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'shared_link':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def lock() -> typing.Type['FilesUpdateFileRequestLock']:
                return FilesUpdateFileRequestLock
            disposition_at = schemas.DateTimeSchema
        
            @staticmethod
            def permissions() -> typing.Type['FilesUpdateFileRequestPermissions']:
                return FilesUpdateFileRequestPermissions
        
            @staticmethod
            def collections() -> typing.Type['FilesUpdateFileRequestCollections']:
                return FilesUpdateFileRequestCollections
            __annotations__ = {
                "tags": tags,
                "description": description,
                "name": name,
                "parent": parent,
                "shared_link": shared_link,
                "lock": lock,
                "disposition_at": disposition_at,
                "permissions": permissions,
                "collections": collections,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'FilesUpdateFileRequestTags': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shared_link"]) -> MetaOapg.properties.shared_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lock"]) -> 'FilesUpdateFileRequestLock': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disposition_at"]) -> MetaOapg.properties.disposition_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permissions"]) -> 'FilesUpdateFileRequestPermissions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collections"]) -> 'FilesUpdateFileRequestCollections': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tags", "description", "name", "parent", "shared_link", "lock", "disposition_at", "permissions", "collections", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['FilesUpdateFileRequestTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union[MetaOapg.properties.parent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shared_link"]) -> typing.Union[MetaOapg.properties.shared_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lock"]) -> typing.Union['FilesUpdateFileRequestLock', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disposition_at"]) -> typing.Union[MetaOapg.properties.disposition_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permissions"]) -> typing.Union['FilesUpdateFileRequestPermissions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collections"]) -> typing.Union['FilesUpdateFileRequestCollections', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tags", "description", "name", "parent", "shared_link", "lock", "disposition_at", "permissions", "collections", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tags: typing.Union['FilesUpdateFileRequestTags', schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        parent: typing.Union[MetaOapg.properties.parent, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        shared_link: typing.Union[MetaOapg.properties.shared_link, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        lock: typing.Union['FilesUpdateFileRequestLock', schemas.Unset] = schemas.unset,
        disposition_at: typing.Union[MetaOapg.properties.disposition_at, str, datetime, schemas.Unset] = schemas.unset,
        permissions: typing.Union['FilesUpdateFileRequestPermissions', schemas.Unset] = schemas.unset,
        collections: typing.Union['FilesUpdateFileRequestCollections', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FilesUpdateFileRequest':
        return super().__new__(
            cls,
            *args,
            tags=tags,
            description=description,
            name=name,
            parent=parent,
            shared_link=shared_link,
            lock=lock,
            disposition_at=disposition_at,
            permissions=permissions,
            collections=collections,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.files_update_file_request_collections import FilesUpdateFileRequestCollections
from box_python_sdk.model.files_update_file_request_lock import FilesUpdateFileRequestLock
from box_python_sdk.model.files_update_file_request_permissions import FilesUpdateFileRequestPermissions
from box_python_sdk.model.files_update_file_request_tags import FilesUpdateFileRequestTags
