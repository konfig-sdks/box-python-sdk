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


class WebhookInvocation(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The event that is sent to a webhook address when an event happens.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def WEBHOOK_EVENT(cls):
                    return cls("webhook_event")
            
            
            class webhook(
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
                            Webhook,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'webhook':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
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
            created_at = schemas.DateTimeSchema
            
            
            class trigger(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class all_of_0(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def FILE_UPLOADED(cls):
                            return cls("FILE.UPLOADED")
                        
                        @schemas.classproperty
                        def FILE_PREVIEWED(cls):
                            return cls("FILE.PREVIEWED")
                        
                        @schemas.classproperty
                        def FILE_DOWNLOADED(cls):
                            return cls("FILE.DOWNLOADED")
                        
                        @schemas.classproperty
                        def FILE_TRASHED(cls):
                            return cls("FILE.TRASHED")
                        
                        @schemas.classproperty
                        def FILE_DELETED(cls):
                            return cls("FILE.DELETED")
                        
                        @schemas.classproperty
                        def FILE_RESTORED(cls):
                            return cls("FILE.RESTORED")
                        
                        @schemas.classproperty
                        def FILE_COPIED(cls):
                            return cls("FILE.COPIED")
                        
                        @schemas.classproperty
                        def FILE_MOVED(cls):
                            return cls("FILE.MOVED")
                        
                        @schemas.classproperty
                        def FILE_LOCKED(cls):
                            return cls("FILE.LOCKED")
                        
                        @schemas.classproperty
                        def FILE_UNLOCKED(cls):
                            return cls("FILE.UNLOCKED")
                        
                        @schemas.classproperty
                        def FILE_RENAMED(cls):
                            return cls("FILE.RENAMED")
                        
                        @schemas.classproperty
                        def COMMENT_CREATED(cls):
                            return cls("COMMENT.CREATED")
                        
                        @schemas.classproperty
                        def COMMENT_UPDATED(cls):
                            return cls("COMMENT.UPDATED")
                        
                        @schemas.classproperty
                        def COMMENT_DELETED(cls):
                            return cls("COMMENT.DELETED")
                        
                        @schemas.classproperty
                        def TASK_ASSIGNMENT_CREATED(cls):
                            return cls("TASK_ASSIGNMENT.CREATED")
                        
                        @schemas.classproperty
                        def TASK_ASSIGNMENT_UPDATED(cls):
                            return cls("TASK_ASSIGNMENT.UPDATED")
                        
                        @schemas.classproperty
                        def METADATA_INSTANCE_CREATED(cls):
                            return cls("METADATA_INSTANCE.CREATED")
                        
                        @schemas.classproperty
                        def METADATA_INSTANCE_UPDATED(cls):
                            return cls("METADATA_INSTANCE.UPDATED")
                        
                        @schemas.classproperty
                        def METADATA_INSTANCE_DELETED(cls):
                            return cls("METADATA_INSTANCE.DELETED")
                        
                        @schemas.classproperty
                        def FOLDER_CREATED(cls):
                            return cls("FOLDER.CREATED")
                        
                        @schemas.classproperty
                        def FOLDER_RENAMED(cls):
                            return cls("FOLDER.RENAMED")
                        
                        @schemas.classproperty
                        def FOLDER_DOWNLOADED(cls):
                            return cls("FOLDER.DOWNLOADED")
                        
                        @schemas.classproperty
                        def FOLDER_RESTORED(cls):
                            return cls("FOLDER.RESTORED")
                        
                        @schemas.classproperty
                        def FOLDER_DELETED(cls):
                            return cls("FOLDER.DELETED")
                        
                        @schemas.classproperty
                        def FOLDER_COPIED(cls):
                            return cls("FOLDER.COPIED")
                        
                        @schemas.classproperty
                        def FOLDER_MOVED(cls):
                            return cls("FOLDER.MOVED")
                        
                        @schemas.classproperty
                        def FOLDER_TRASHED(cls):
                            return cls("FOLDER.TRASHED")
                        
                        @schemas.classproperty
                        def WEBHOOK_DELETED(cls):
                            return cls("WEBHOOK.DELETED")
                        
                        @schemas.classproperty
                        def COLLABORATION_CREATED(cls):
                            return cls("COLLABORATION.CREATED")
                        
                        @schemas.classproperty
                        def COLLABORATION_ACCEPTED(cls):
                            return cls("COLLABORATION.ACCEPTED")
                        
                        @schemas.classproperty
                        def COLLABORATION_REJECTED(cls):
                            return cls("COLLABORATION.REJECTED")
                        
                        @schemas.classproperty
                        def COLLABORATION_REMOVED(cls):
                            return cls("COLLABORATION.REMOVED")
                        
                        @schemas.classproperty
                        def COLLABORATION_UPDATED(cls):
                            return cls("COLLABORATION.UPDATED")
                        
                        @schemas.classproperty
                        def SHARED_LINK_DELETED(cls):
                            return cls("SHARED_LINK.DELETED")
                        
                        @schemas.classproperty
                        def SHARED_LINK_CREATED(cls):
                            return cls("SHARED_LINK.CREATED")
                        
                        @schemas.classproperty
                        def SHARED_LINK_UPDATED(cls):
                            return cls("SHARED_LINK.UPDATED")
                        
                        @schemas.classproperty
                        def SIGN_REQUEST_COMPLETED(cls):
                            return cls("SIGN_REQUEST.COMPLETED")
                        
                        @schemas.classproperty
                        def SIGN_REQUEST_DECLINED(cls):
                            return cls("SIGN_REQUEST.DECLINED")
                        
                        @schemas.classproperty
                        def SIGN_REQUEST_EXPIRED(cls):
                            return cls("SIGN_REQUEST.EXPIRED")
                        
                        @schemas.classproperty
                        def SIGN_REQUEST_SIGNER_EMAIL_BOUNCED(cls):
                            return cls("SIGN_REQUEST.SIGNER_EMAIL_BOUNCED")
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
                ) -> 'trigger':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class source(
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
                                    File,
                                    Folder,
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
                ) -> 'source':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "id": id,
                "type": type,
                "webhook": webhook,
                "created_by": created_by,
                "created_at": created_at,
                "trigger": trigger,
                "source": source,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhook"]) -> MetaOapg.properties.webhook: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger"]) -> MetaOapg.properties.trigger: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "webhook", "created_by", "created_at", "trigger", "source", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhook"]) -> typing.Union[MetaOapg.properties.webhook, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union[MetaOapg.properties.created_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger"]) -> typing.Union[MetaOapg.properties.trigger, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "webhook", "created_by", "created_at", "trigger", "source", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        webhook: typing.Union[MetaOapg.properties.webhook, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        created_by: typing.Union[MetaOapg.properties.created_by, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        trigger: typing.Union[MetaOapg.properties.trigger, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebhookInvocation':
        return super().__new__(
            cls,
            *args,
            id=id,
            type=type,
            webhook=webhook,
            created_by=created_by,
            created_at=created_at,
            trigger=trigger,
            source=source,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.file import File
from box_python_sdk.model.folder import Folder
from box_python_sdk.model.user_mini import UserMini
from box_python_sdk.model.webhook import Webhook
