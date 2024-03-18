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


class FaComment(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Standard representation of a comment.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                    created_at = schemas.DateTimeSchema
                    
                    
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
                                    FileActivityUser,
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
                    is_reply_comment = schemas.BoolSchema
                
                    @staticmethod
                    def item() -> typing.Type['FaCommentBase']:
                        return FaCommentBase
                    message = schemas.StrSchema
                    modified_at = schemas.DateTimeSchema
                
                    @staticmethod
                    def parent() -> typing.Type['FaCommentBase']:
                        return FaCommentBase
                    
                    
                    class replies(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Reply']:
                                return Reply
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['Reply'], typing.List['Reply']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'replies':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Reply':
                            return super().__getitem__(i)
                    
                    
                    class status(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def OPEN(cls):
                            return cls("open")
                        
                        @schemas.classproperty
                        def RESOLVED(cls):
                            return cls("resolved")
                        
                        @schemas.classproperty
                        def DELETED(cls):
                            return cls("deleted")
                    total_reply_count = schemas.NumberSchema
                    __annotations__ = {
                        "created_at": created_at,
                        "created_by": created_by,
                        "is_reply_comment": is_reply_comment,
                        "item": item,
                        "message": message,
                        "modified_at": modified_at,
                        "parent": parent,
                        "replies": replies,
                        "status": status,
                        "total_reply_count": total_reply_count,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_reply_comment"]) -> MetaOapg.properties.is_reply_comment: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["item"]) -> 'FaCommentBase': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["modified_at"]) -> MetaOapg.properties.modified_at: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["parent"]) -> 'FaCommentBase': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["replies"]) -> MetaOapg.properties.replies: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["total_reply_count"]) -> MetaOapg.properties.total_reply_count: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["created_at", "created_by", "is_reply_comment", "item", "message", "modified_at", "parent", "replies", "status", "total_reply_count", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union[MetaOapg.properties.created_by, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_reply_comment"]) -> typing.Union[MetaOapg.properties.is_reply_comment, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["item"]) -> typing.Union['FaCommentBase', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["modified_at"]) -> typing.Union[MetaOapg.properties.modified_at, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["parent"]) -> typing.Union['FaCommentBase', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["replies"]) -> typing.Union[MetaOapg.properties.replies, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["total_reply_count"]) -> typing.Union[MetaOapg.properties.total_reply_count, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created_at", "created_by", "is_reply_comment", "item", "message", "modified_at", "parent", "replies", "status", "total_reply_count", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
                created_by: typing.Union[MetaOapg.properties.created_by, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                is_reply_comment: typing.Union[MetaOapg.properties.is_reply_comment, bool, schemas.Unset] = schemas.unset,
                item: typing.Union['FaCommentBase', schemas.Unset] = schemas.unset,
                message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
                modified_at: typing.Union[MetaOapg.properties.modified_at, str, datetime, schemas.Unset] = schemas.unset,
                parent: typing.Union['FaCommentBase', schemas.Unset] = schemas.unset,
                replies: typing.Union[MetaOapg.properties.replies, list, tuple, schemas.Unset] = schemas.unset,
                status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                total_reply_count: typing.Union[MetaOapg.properties.total_reply_count, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    created_at=created_at,
                    created_by=created_by,
                    is_reply_comment=is_reply_comment,
                    item=item,
                    message=message,
                    modified_at=modified_at,
                    parent=parent,
                    replies=replies,
                    status=status,
                    total_reply_count=total_reply_count,
                    _configuration=_configuration,
                    **kwargs,
                )
        
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
                FaCommentBase,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FaComment':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.fa_comment_base import FaCommentBase
from box_python_sdk.model.file_activity_user import FileActivityUser
from box_python_sdk.model.reply import Reply
