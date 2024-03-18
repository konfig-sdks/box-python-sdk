# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from box_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from box_python_sdk.api_response import AsyncGeneratorResponse
from box_python_sdk import api_client, exceptions
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

from box_python_sdk.model.sign_request_create_request import SignRequestCreateRequest as SignRequestCreateRequestSchema
from box_python_sdk.model.client_error import ClientError as ClientErrorSchema
from box_python_sdk.model.sign_request import SignRequest as SignRequestSchema
from box_python_sdk.model.folder_mini import FolderMini as FolderMiniSchema
from box_python_sdk.model.sign_request_create_signer import SignRequestCreateSigner as SignRequestCreateSignerSchema
from box_python_sdk.model.sign_request_prefill_tag import SignRequestPrefillTag as SignRequestPrefillTagSchema
from box_python_sdk.model.file_base import FileBase as FileBaseSchema

from box_python_sdk.type.sign_request import SignRequest
from box_python_sdk.type.sign_request_prefill_tag import SignRequestPrefillTag
from box_python_sdk.type.file_base import FileBase
from box_python_sdk.type.sign_request_create_request import SignRequestCreateRequest
from box_python_sdk.type.folder_mini import FolderMini
from box_python_sdk.type.sign_request_create_signer import SignRequestCreateSigner
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.sign_request import SignRequest as SignRequestPydantic
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.file_base import FileBase as FileBasePydantic
from box_python_sdk.pydantic.sign_request_create_signer import SignRequestCreateSigner as SignRequestCreateSignerPydantic
from box_python_sdk.pydantic.folder_mini import FolderMini as FolderMiniPydantic
from box_python_sdk.pydantic.sign_request_create_request import SignRequestCreateRequest as SignRequestCreateRequestPydantic
from box_python_sdk.pydantic.sign_request_prefill_tag import SignRequestPrefillTag as SignRequestPrefillTagPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = SignRequestCreateRequestSchema


request_body_sign_request_create_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'OAuth2Security',
]
SchemaFor201ResponseBodyApplicationJson = SignRequestSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: SignRequest


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: SignRequest


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ClientError


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_request_mapped_args(
        self,
        signers: typing.List[SignRequestCreateSigner],
        is_document_preparation_needed: typing.Optional[bool] = None,
        redirect_url: typing.Optional[typing.Optional[str]] = None,
        declined_redirect_url: typing.Optional[typing.Optional[str]] = None,
        are_text_signatures_enabled: typing.Optional[bool] = None,
        email_subject: typing.Optional[typing.Optional[str]] = None,
        email_message: typing.Optional[typing.Optional[str]] = None,
        are_reminders_enabled: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        prefill_tags: typing.Optional[typing.List[SignRequestPrefillTag]] = None,
        days_valid: typing.Optional[typing.Optional[int]] = None,
        external_id: typing.Optional[typing.Optional[str]] = None,
        is_phone_verification_required_to_view: typing.Optional[typing.Optional[bool]] = None,
        template_id: typing.Optional[typing.Optional[str]] = None,
        source_files: typing.Optional[typing.Optional[typing.List[FileBase]]] = None,
        signature_color: typing.Optional[typing.Optional[str]] = None,
        parent_folder: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if is_document_preparation_needed is not None:
            _body["is_document_preparation_needed"] = is_document_preparation_needed
        if redirect_url is not None:
            _body["redirect_url"] = redirect_url
        if declined_redirect_url is not None:
            _body["declined_redirect_url"] = declined_redirect_url
        if are_text_signatures_enabled is not None:
            _body["are_text_signatures_enabled"] = are_text_signatures_enabled
        if email_subject is not None:
            _body["email_subject"] = email_subject
        if email_message is not None:
            _body["email_message"] = email_message
        if are_reminders_enabled is not None:
            _body["are_reminders_enabled"] = are_reminders_enabled
        if name is not None:
            _body["name"] = name
        if prefill_tags is not None:
            _body["prefill_tags"] = prefill_tags
        if days_valid is not None:
            _body["days_valid"] = days_valid
        if external_id is not None:
            _body["external_id"] = external_id
        if is_phone_verification_required_to_view is not None:
            _body["is_phone_verification_required_to_view"] = is_phone_verification_required_to_view
        if template_id is not None:
            _body["template_id"] = template_id
        if source_files is not None:
            _body["source_files"] = source_files
        if signature_color is not None:
            _body["signature_color"] = signature_color
        if signers is not None:
            _body["signers"] = signers
        if parent_folder is not None:
            _body["parent_folder"] = parent_folder
        args.body = _body
        return args

    async def _acreate_request_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create sign request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/sign_requests',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_sign_request_create_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_request_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create sign request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/sign_requests',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_sign_request_create_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateRequestRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_request(
        self,
        signers: typing.List[SignRequestCreateSigner],
        is_document_preparation_needed: typing.Optional[bool] = None,
        redirect_url: typing.Optional[typing.Optional[str]] = None,
        declined_redirect_url: typing.Optional[typing.Optional[str]] = None,
        are_text_signatures_enabled: typing.Optional[bool] = None,
        email_subject: typing.Optional[typing.Optional[str]] = None,
        email_message: typing.Optional[typing.Optional[str]] = None,
        are_reminders_enabled: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        prefill_tags: typing.Optional[typing.List[SignRequestPrefillTag]] = None,
        days_valid: typing.Optional[typing.Optional[int]] = None,
        external_id: typing.Optional[typing.Optional[str]] = None,
        is_phone_verification_required_to_view: typing.Optional[typing.Optional[bool]] = None,
        template_id: typing.Optional[typing.Optional[str]] = None,
        source_files: typing.Optional[typing.Optional[typing.List[FileBase]]] = None,
        signature_color: typing.Optional[typing.Optional[str]] = None,
        parent_folder: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_request_mapped_args(
            signers=signers,
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
            source_files=source_files,
            signature_color=signature_color,
            parent_folder=parent_folder,
        )
        return await self._acreate_request_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_request(
        self,
        signers: typing.List[SignRequestCreateSigner],
        is_document_preparation_needed: typing.Optional[bool] = None,
        redirect_url: typing.Optional[typing.Optional[str]] = None,
        declined_redirect_url: typing.Optional[typing.Optional[str]] = None,
        are_text_signatures_enabled: typing.Optional[bool] = None,
        email_subject: typing.Optional[typing.Optional[str]] = None,
        email_message: typing.Optional[typing.Optional[str]] = None,
        are_reminders_enabled: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        prefill_tags: typing.Optional[typing.List[SignRequestPrefillTag]] = None,
        days_valid: typing.Optional[typing.Optional[int]] = None,
        external_id: typing.Optional[typing.Optional[str]] = None,
        is_phone_verification_required_to_view: typing.Optional[typing.Optional[bool]] = None,
        template_id: typing.Optional[typing.Optional[str]] = None,
        source_files: typing.Optional[typing.Optional[typing.List[FileBase]]] = None,
        signature_color: typing.Optional[typing.Optional[str]] = None,
        parent_folder: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_request_mapped_args(
            signers=signers,
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
            source_files=source_files,
            signature_color=signature_color,
            parent_folder=parent_folder,
        )
        return self._create_request_oapg(
            body=args.body,
        )

class CreateRequest(BaseApi):

    async def acreate_request(
        self,
        signers: typing.List[SignRequestCreateSigner],
        is_document_preparation_needed: typing.Optional[bool] = None,
        redirect_url: typing.Optional[typing.Optional[str]] = None,
        declined_redirect_url: typing.Optional[typing.Optional[str]] = None,
        are_text_signatures_enabled: typing.Optional[bool] = None,
        email_subject: typing.Optional[typing.Optional[str]] = None,
        email_message: typing.Optional[typing.Optional[str]] = None,
        are_reminders_enabled: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        prefill_tags: typing.Optional[typing.List[SignRequestPrefillTag]] = None,
        days_valid: typing.Optional[typing.Optional[int]] = None,
        external_id: typing.Optional[typing.Optional[str]] = None,
        is_phone_verification_required_to_view: typing.Optional[typing.Optional[bool]] = None,
        template_id: typing.Optional[typing.Optional[str]] = None,
        source_files: typing.Optional[typing.Optional[typing.List[FileBase]]] = None,
        signature_color: typing.Optional[typing.Optional[str]] = None,
        parent_folder: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        validate: bool = False,
        **kwargs,
    ) -> SignRequestPydantic:
        raw_response = await self.raw.acreate_request(
            signers=signers,
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
            source_files=source_files,
            signature_color=signature_color,
            parent_folder=parent_folder,
            **kwargs,
        )
        if validate:
            return RootModel[SignRequestPydantic](raw_response.body).root
        return api_client.construct_model_instance(SignRequestPydantic, raw_response.body)
    
    
    def create_request(
        self,
        signers: typing.List[SignRequestCreateSigner],
        is_document_preparation_needed: typing.Optional[bool] = None,
        redirect_url: typing.Optional[typing.Optional[str]] = None,
        declined_redirect_url: typing.Optional[typing.Optional[str]] = None,
        are_text_signatures_enabled: typing.Optional[bool] = None,
        email_subject: typing.Optional[typing.Optional[str]] = None,
        email_message: typing.Optional[typing.Optional[str]] = None,
        are_reminders_enabled: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        prefill_tags: typing.Optional[typing.List[SignRequestPrefillTag]] = None,
        days_valid: typing.Optional[typing.Optional[int]] = None,
        external_id: typing.Optional[typing.Optional[str]] = None,
        is_phone_verification_required_to_view: typing.Optional[typing.Optional[bool]] = None,
        template_id: typing.Optional[typing.Optional[str]] = None,
        source_files: typing.Optional[typing.Optional[typing.List[FileBase]]] = None,
        signature_color: typing.Optional[typing.Optional[str]] = None,
        parent_folder: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        validate: bool = False,
    ) -> SignRequestPydantic:
        raw_response = self.raw.create_request(
            signers=signers,
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
            source_files=source_files,
            signature_color=signature_color,
            parent_folder=parent_folder,
        )
        if validate:
            return RootModel[SignRequestPydantic](raw_response.body).root
        return api_client.construct_model_instance(SignRequestPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        signers: typing.List[SignRequestCreateSigner],
        is_document_preparation_needed: typing.Optional[bool] = None,
        redirect_url: typing.Optional[typing.Optional[str]] = None,
        declined_redirect_url: typing.Optional[typing.Optional[str]] = None,
        are_text_signatures_enabled: typing.Optional[bool] = None,
        email_subject: typing.Optional[typing.Optional[str]] = None,
        email_message: typing.Optional[typing.Optional[str]] = None,
        are_reminders_enabled: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        prefill_tags: typing.Optional[typing.List[SignRequestPrefillTag]] = None,
        days_valid: typing.Optional[typing.Optional[int]] = None,
        external_id: typing.Optional[typing.Optional[str]] = None,
        is_phone_verification_required_to_view: typing.Optional[typing.Optional[bool]] = None,
        template_id: typing.Optional[typing.Optional[str]] = None,
        source_files: typing.Optional[typing.Optional[typing.List[FileBase]]] = None,
        signature_color: typing.Optional[typing.Optional[str]] = None,
        parent_folder: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_request_mapped_args(
            signers=signers,
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
            source_files=source_files,
            signature_color=signature_color,
            parent_folder=parent_folder,
        )
        return await self._acreate_request_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        signers: typing.List[SignRequestCreateSigner],
        is_document_preparation_needed: typing.Optional[bool] = None,
        redirect_url: typing.Optional[typing.Optional[str]] = None,
        declined_redirect_url: typing.Optional[typing.Optional[str]] = None,
        are_text_signatures_enabled: typing.Optional[bool] = None,
        email_subject: typing.Optional[typing.Optional[str]] = None,
        email_message: typing.Optional[typing.Optional[str]] = None,
        are_reminders_enabled: typing.Optional[bool] = None,
        name: typing.Optional[str] = None,
        prefill_tags: typing.Optional[typing.List[SignRequestPrefillTag]] = None,
        days_valid: typing.Optional[typing.Optional[int]] = None,
        external_id: typing.Optional[typing.Optional[str]] = None,
        is_phone_verification_required_to_view: typing.Optional[typing.Optional[bool]] = None,
        template_id: typing.Optional[typing.Optional[str]] = None,
        source_files: typing.Optional[typing.Optional[typing.List[FileBase]]] = None,
        signature_color: typing.Optional[typing.Optional[str]] = None,
        parent_folder: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_request_mapped_args(
            signers=signers,
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
            source_files=source_files,
            signature_color=signature_color,
            parent_folder=parent_folder,
        )
        return self._create_request_oapg(
            body=args.body,
        )

