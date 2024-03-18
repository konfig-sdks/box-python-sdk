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


class TrashFileRestored(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Represents a file restored from the trash.
    """


    class MetaOapg:
        required = {
            "sha1",
            "size",
            "modified_by",
            "sequence_id",
            "created_at",
            "description",
            "owned_by",
            "id",
            "item_status",
            "modified_at",
            "type",
            "path_collection",
        }
        
        class properties:
            
            
            class description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 256
            id = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "file": "FILE",
                    }
                
                @schemas.classproperty
                def FILE(cls):
                    return cls("file")
            
            
            class sequence_id(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class all_of_0(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'all_of_0':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
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
                ) -> 'sequence_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            sha1 = schemas.StrSchema
            size = schemas.IntSchema
            
            
            class path_collection(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class all_of_0(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "entries",
                                "total_count",
                            }
                            
                            class properties:
                                total_count = schemas.Int64Schema
                                
                                
                                class entries(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def items() -> typing.Type['FolderMini']:
                                            return FolderMini
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple['FolderMini'], typing.List['FolderMini']],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'entries':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> 'FolderMini':
                                        return super().__getitem__(i)
                                __annotations__ = {
                                    "total_count": total_count,
                                    "entries": entries,
                                }
                        
                        entries: MetaOapg.properties.entries
                        total_count: MetaOapg.properties.total_count
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["entries"]) -> MetaOapg.properties.entries: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_count", "entries", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["entries"]) -> MetaOapg.properties.entries: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_count", "entries", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            entries: typing.Union[MetaOapg.properties.entries, list, tuple, ],
                            total_count: typing.Union[MetaOapg.properties.total_count, decimal.Decimal, int, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'all_of_0':
                            return super().__new__(
                                cls,
                                *args,
                                entries=entries,
                                total_count=total_count,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    all_of_1 = schemas.AnyTypeSchema
                    all_of_2 = schemas.AnyTypeSchema
                    
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
                            cls.all_of_2,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'path_collection':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            created_at = schemas.DateTimeSchema
            modified_at = schemas.DateTimeSchema
            
            
            class modified_by(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    all_of_2 = schemas.AnyTypeSchema
                    
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
                            UserMini,
                            cls.all_of_1,
                            cls.all_of_2,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'modified_by':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class owned_by(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    all_of_2 = schemas.AnyTypeSchema
                    
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
                            UserMini,
                            cls.all_of_1,
                            cls.all_of_2,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'owned_by':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class item_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "active": "ACTIVE",
                        "trashed": "TRASHED",
                        "deleted": "DELETED",
                    }
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("active")
                
                @schemas.classproperty
                def TRASHED(cls):
                    return cls("trashed")
                
                @schemas.classproperty
                def DELETED(cls):
                    return cls("deleted")
            
            
            class etag(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'etag':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            name = schemas.StrSchema
            
            
            class file_version(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
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
                            FileVersionMini,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'file_version':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class trashed_at(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'trashed_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class purged_at(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'purged_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class content_created_at(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'content_created_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class content_modified_at(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'content_modified_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class created_by(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
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
                            UserMini,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'created_by':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class shared_link(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'shared_link':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class parent(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    all_of_2 = schemas.AnyTypeSchema
                    
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
                            FolderMini,
                            cls.all_of_1,
                            cls.all_of_2,
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
            __annotations__ = {
                "description": description,
                "id": id,
                "type": type,
                "sequence_id": sequence_id,
                "sha1": sha1,
                "size": size,
                "path_collection": path_collection,
                "created_at": created_at,
                "modified_at": modified_at,
                "modified_by": modified_by,
                "owned_by": owned_by,
                "item_status": item_status,
                "etag": etag,
                "name": name,
                "file_version": file_version,
                "trashed_at": trashed_at,
                "purged_at": purged_at,
                "content_created_at": content_created_at,
                "content_modified_at": content_modified_at,
                "created_by": created_by,
                "shared_link": shared_link,
                "parent": parent,
            }
    
    sha1: MetaOapg.properties.sha1
    size: MetaOapg.properties.size
    modified_by: MetaOapg.properties.modified_by
    sequence_id: MetaOapg.properties.sequence_id
    created_at: MetaOapg.properties.created_at
    description: MetaOapg.properties.description
    owned_by: MetaOapg.properties.owned_by
    id: MetaOapg.properties.id
    item_status: MetaOapg.properties.item_status
    modified_at: MetaOapg.properties.modified_at
    type: MetaOapg.properties.type
    path_collection: MetaOapg.properties.path_collection
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequence_id"]) -> MetaOapg.properties.sequence_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sha1"]) -> MetaOapg.properties.sha1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path_collection"]) -> MetaOapg.properties.path_collection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified_at"]) -> MetaOapg.properties.modified_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified_by"]) -> MetaOapg.properties.modified_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owned_by"]) -> MetaOapg.properties.owned_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_status"]) -> MetaOapg.properties.item_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["etag"]) -> MetaOapg.properties.etag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_version"]) -> MetaOapg.properties.file_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trashed_at"]) -> MetaOapg.properties.trashed_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purged_at"]) -> MetaOapg.properties.purged_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content_created_at"]) -> MetaOapg.properties.content_created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content_modified_at"]) -> MetaOapg.properties.content_modified_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shared_link"]) -> MetaOapg.properties.shared_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent"]) -> MetaOapg.properties.parent: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "type", "sequence_id", "sha1", "size", "path_collection", "created_at", "modified_at", "modified_by", "owned_by", "item_status", "etag", "name", "file_version", "trashed_at", "purged_at", "content_created_at", "content_modified_at", "created_by", "shared_link", "parent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequence_id"]) -> MetaOapg.properties.sequence_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sha1"]) -> MetaOapg.properties.sha1: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> MetaOapg.properties.size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path_collection"]) -> MetaOapg.properties.path_collection: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified_at"]) -> MetaOapg.properties.modified_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified_by"]) -> MetaOapg.properties.modified_by: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owned_by"]) -> MetaOapg.properties.owned_by: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_status"]) -> MetaOapg.properties.item_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["etag"]) -> typing.Union[MetaOapg.properties.etag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_version"]) -> typing.Union[MetaOapg.properties.file_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trashed_at"]) -> typing.Union[MetaOapg.properties.trashed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purged_at"]) -> typing.Union[MetaOapg.properties.purged_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content_created_at"]) -> typing.Union[MetaOapg.properties.content_created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content_modified_at"]) -> typing.Union[MetaOapg.properties.content_modified_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union[MetaOapg.properties.created_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shared_link"]) -> typing.Union[MetaOapg.properties.shared_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union[MetaOapg.properties.parent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "type", "sequence_id", "sha1", "size", "path_collection", "created_at", "modified_at", "modified_by", "owned_by", "item_status", "etag", "name", "file_version", "trashed_at", "purged_at", "content_created_at", "content_modified_at", "created_by", "shared_link", "parent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sha1: typing.Union[MetaOapg.properties.sha1, str, ],
        size: typing.Union[MetaOapg.properties.size, decimal.Decimal, int, ],
        modified_by: typing.Union[MetaOapg.properties.modified_by, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        sequence_id: typing.Union[MetaOapg.properties.sequence_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        owned_by: typing.Union[MetaOapg.properties.owned_by, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        item_status: typing.Union[MetaOapg.properties.item_status, str, ],
        modified_at: typing.Union[MetaOapg.properties.modified_at, str, datetime, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        path_collection: typing.Union[MetaOapg.properties.path_collection, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        etag: typing.Union[MetaOapg.properties.etag, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        file_version: typing.Union[MetaOapg.properties.file_version, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        trashed_at: typing.Union[MetaOapg.properties.trashed_at, None, str, schemas.Unset] = schemas.unset,
        purged_at: typing.Union[MetaOapg.properties.purged_at, None, str, schemas.Unset] = schemas.unset,
        content_created_at: typing.Union[MetaOapg.properties.content_created_at, None, str, datetime, schemas.Unset] = schemas.unset,
        content_modified_at: typing.Union[MetaOapg.properties.content_modified_at, None, str, datetime, schemas.Unset] = schemas.unset,
        created_by: typing.Union[MetaOapg.properties.created_by, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        shared_link: typing.Union[MetaOapg.properties.shared_link, None, str, schemas.Unset] = schemas.unset,
        parent: typing.Union[MetaOapg.properties.parent, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TrashFileRestored':
        return super().__new__(
            cls,
            *args,
            sha1=sha1,
            size=size,
            modified_by=modified_by,
            sequence_id=sequence_id,
            created_at=created_at,
            description=description,
            owned_by=owned_by,
            id=id,
            item_status=item_status,
            modified_at=modified_at,
            type=type,
            path_collection=path_collection,
            etag=etag,
            name=name,
            file_version=file_version,
            trashed_at=trashed_at,
            purged_at=purged_at,
            content_created_at=content_created_at,
            content_modified_at=content_modified_at,
            created_by=created_by,
            shared_link=shared_link,
            parent=parent,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.file_version_mini import FileVersionMini
from box_python_sdk.model.folder_mini import FolderMini
from box_python_sdk.model.user_mini import UserMini
