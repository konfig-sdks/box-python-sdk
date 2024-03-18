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


class FileOrFolderScope(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A relation between a resource (file or folder) and the scopes for which the resource can be accessed
    """


    class MetaOapg:
        
        class properties:
            
            
            class scope(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ANNOTATION_EDIT(cls):
                    return cls("annotation_edit")
                
                @schemas.classproperty
                def ANNOTATION_VIEW_ALL(cls):
                    return cls("annotation_view_all")
                
                @schemas.classproperty
                def ANNOTATION_VIEW_SELF(cls):
                    return cls("annotation_view_self")
                
                @schemas.classproperty
                def BASE_EXPLORER(cls):
                    return cls("base_explorer")
                
                @schemas.classproperty
                def BASE_PICKER(cls):
                    return cls("base_picker")
                
                @schemas.classproperty
                def BASE_PREVIEW(cls):
                    return cls("base_preview")
                
                @schemas.classproperty
                def BASE_UPLOAD(cls):
                    return cls("base_upload")
                
                @schemas.classproperty
                def ITEM_DELETE(cls):
                    return cls("item_delete")
                
                @schemas.classproperty
                def ITEM_DOWNLOAD(cls):
                    return cls("item_download")
                
                @schemas.classproperty
                def ITEM_PREVIEW(cls):
                    return cls("item_preview")
                
                @schemas.classproperty
                def ITEM_RENAME(cls):
                    return cls("item_rename")
                
                @schemas.classproperty
                def ITEM_SHARE(cls):
                    return cls("item_share")
            
            
            class object(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class all_of_0(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            @classmethod
                            @functools.lru_cache()
                            def one_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    FolderMini,
                                    FileMini,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'all_of_0':
                            return super().__new__(
                                cls,
                                *args,
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
                ) -> 'object':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "scope": scope,
                "object": object,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope"]) -> MetaOapg.properties.scope: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["scope", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope"]) -> typing.Union[MetaOapg.properties.scope, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["scope", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        scope: typing.Union[MetaOapg.properties.scope, str, schemas.Unset] = schemas.unset,
        object: typing.Union[MetaOapg.properties.object, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FileOrFolderScope':
        return super().__new__(
            cls,
            *args,
            scope=scope,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.file_mini import FileMini
from box_python_sdk.model.folder_mini import FolderMini
