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


class TemplateSigner(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The schema for a Signer for Templates
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
                    class inputs(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['TemplateSignerInput']:
                                return TemplateSignerInput
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['TemplateSignerInput'], typing.List['TemplateSignerInput']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'inputs':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'TemplateSignerInput':
                            return super().__getitem__(i)
                    
                    
                    class email(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'email':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class role(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def SIGNER(cls):
                            return cls("signer")
                        
                        @schemas.classproperty
                        def APPROVER(cls):
                            return cls("approver")
                        
                        @schemas.classproperty
                        def FINAL_COPY_READER(cls):
                            return cls("final_copy_reader")
                    is_in_person = schemas.BoolSchema
                    
                    
                    class order(
                        schemas.IntSchema
                    ):
                        pass
                    
                    
                    class signer_group_id(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'signer_group_id':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    __annotations__ = {
                        "inputs": inputs,
                        "email": email,
                        "role": role,
                        "is_in_person": is_in_person,
                        "order": order,
                        "signer_group_id": signer_group_id,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["inputs"]) -> MetaOapg.properties.inputs: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_in_person"]) -> MetaOapg.properties.is_in_person: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["signer_group_id"]) -> MetaOapg.properties.signer_group_id: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["inputs", "email", "role", "is_in_person", "order", "signer_group_id", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["inputs"]) -> typing.Union[MetaOapg.properties.inputs, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_in_person"]) -> typing.Union[MetaOapg.properties.is_in_person, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["signer_group_id"]) -> typing.Union[MetaOapg.properties.signer_group_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["inputs", "email", "role", "is_in_person", "order", "signer_group_id", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                inputs: typing.Union[MetaOapg.properties.inputs, list, tuple, schemas.Unset] = schemas.unset,
                email: typing.Union[MetaOapg.properties.email, None, str, schemas.Unset] = schemas.unset,
                role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
                is_in_person: typing.Union[MetaOapg.properties.is_in_person, bool, schemas.Unset] = schemas.unset,
                order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                signer_group_id: typing.Union[MetaOapg.properties.signer_group_id, None, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    inputs=inputs,
                    email=email,
                    role=role,
                    is_in_person=is_in_person,
                    order=order,
                    signer_group_id=signer_group_id,
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
                cls.all_of_0,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateSigner':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.template_signer_input import TemplateSignerInput
