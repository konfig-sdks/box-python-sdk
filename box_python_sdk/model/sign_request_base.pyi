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


class SignRequestBase(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A request to create a sign request object
    """


    class MetaOapg:
        
        class properties:
            is_document_preparation_needed = schemas.BoolSchema
            
            
            class redirect_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'redirect_url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class declined_redirect_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'declined_redirect_url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            are_text_signatures_enabled = schemas.BoolSchema
            
            
            class email_subject(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'email_subject':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class email_message(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'email_message':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            are_reminders_enabled = schemas.BoolSchema
            name = schemas.StrSchema
            
            
            class prefill_tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SignRequestPrefillTag']:
                        return SignRequestPrefillTag
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SignRequestPrefillTag'], typing.List['SignRequestPrefillTag']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'prefill_tags':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SignRequestPrefillTag':
                    return super().__getitem__(i)
            
            
            class days_valid(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'days_valid':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class external_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'external_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class is_phone_verification_required_to_view(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'is_phone_verification_required_to_view':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class template_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'template_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "is_document_preparation_needed": is_document_preparation_needed,
                "redirect_url": redirect_url,
                "declined_redirect_url": declined_redirect_url,
                "are_text_signatures_enabled": are_text_signatures_enabled,
                "email_subject": email_subject,
                "email_message": email_message,
                "are_reminders_enabled": are_reminders_enabled,
                "name": name,
                "prefill_tags": prefill_tags,
                "days_valid": days_valid,
                "external_id": external_id,
                "is_phone_verification_required_to_view": is_phone_verification_required_to_view,
                "template_id": template_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_document_preparation_needed"]) -> MetaOapg.properties.is_document_preparation_needed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> MetaOapg.properties.redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["declined_redirect_url"]) -> MetaOapg.properties.declined_redirect_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["are_text_signatures_enabled"]) -> MetaOapg.properties.are_text_signatures_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_subject"]) -> MetaOapg.properties.email_subject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_message"]) -> MetaOapg.properties.email_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["are_reminders_enabled"]) -> MetaOapg.properties.are_reminders_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefill_tags"]) -> MetaOapg.properties.prefill_tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["days_valid"]) -> MetaOapg.properties.days_valid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_phone_verification_required_to_view"]) -> MetaOapg.properties.is_phone_verification_required_to_view: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template_id"]) -> MetaOapg.properties.template_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_document_preparation_needed", "redirect_url", "declined_redirect_url", "are_text_signatures_enabled", "email_subject", "email_message", "are_reminders_enabled", "name", "prefill_tags", "days_valid", "external_id", "is_phone_verification_required_to_view", "template_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_document_preparation_needed"]) -> typing.Union[MetaOapg.properties.is_document_preparation_needed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> typing.Union[MetaOapg.properties.redirect_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["declined_redirect_url"]) -> typing.Union[MetaOapg.properties.declined_redirect_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["are_text_signatures_enabled"]) -> typing.Union[MetaOapg.properties.are_text_signatures_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_subject"]) -> typing.Union[MetaOapg.properties.email_subject, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_message"]) -> typing.Union[MetaOapg.properties.email_message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["are_reminders_enabled"]) -> typing.Union[MetaOapg.properties.are_reminders_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefill_tags"]) -> typing.Union[MetaOapg.properties.prefill_tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["days_valid"]) -> typing.Union[MetaOapg.properties.days_valid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_phone_verification_required_to_view"]) -> typing.Union[MetaOapg.properties.is_phone_verification_required_to_view, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template_id"]) -> typing.Union[MetaOapg.properties.template_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_document_preparation_needed", "redirect_url", "declined_redirect_url", "are_text_signatures_enabled", "email_subject", "email_message", "are_reminders_enabled", "name", "prefill_tags", "days_valid", "external_id", "is_phone_verification_required_to_view", "template_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_document_preparation_needed: typing.Union[MetaOapg.properties.is_document_preparation_needed, bool, schemas.Unset] = schemas.unset,
        redirect_url: typing.Union[MetaOapg.properties.redirect_url, None, str, schemas.Unset] = schemas.unset,
        declined_redirect_url: typing.Union[MetaOapg.properties.declined_redirect_url, None, str, schemas.Unset] = schemas.unset,
        are_text_signatures_enabled: typing.Union[MetaOapg.properties.are_text_signatures_enabled, bool, schemas.Unset] = schemas.unset,
        email_subject: typing.Union[MetaOapg.properties.email_subject, None, str, schemas.Unset] = schemas.unset,
        email_message: typing.Union[MetaOapg.properties.email_message, None, str, schemas.Unset] = schemas.unset,
        are_reminders_enabled: typing.Union[MetaOapg.properties.are_reminders_enabled, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        prefill_tags: typing.Union[MetaOapg.properties.prefill_tags, list, tuple, schemas.Unset] = schemas.unset,
        days_valid: typing.Union[MetaOapg.properties.days_valid, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        external_id: typing.Union[MetaOapg.properties.external_id, None, str, schemas.Unset] = schemas.unset,
        is_phone_verification_required_to_view: typing.Union[MetaOapg.properties.is_phone_verification_required_to_view, None, bool, schemas.Unset] = schemas.unset,
        template_id: typing.Union[MetaOapg.properties.template_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SignRequestBase':
        return super().__new__(
            cls,
            *args,
            is_document_preparation_needed=is_document_preparation_needed,
            redirect_url=redirect_url,
            declined_redirect_url=declined_redirect_url,
            are_text_signatures_enabled=are_text_signatures_enabled,
            email_subject=email_subject,
            email_message=email_message,
            are_reminders_enabled=are_reminders_enabled,
            name=name,
            prefill_tags=prefill_tags,
            days_valid=days_valid,
            external_id=external_id,
            is_phone_verification_required_to_view=is_phone_verification_required_to_view,
            template_id=template_id,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.sign_request_prefill_tag import SignRequestPrefillTag
