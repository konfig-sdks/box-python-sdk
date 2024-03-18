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

from box_python_sdk.model.post_users_request import PostUsersRequest as PostUsersRequestSchema
from box_python_sdk.model.client_error import ClientError as ClientErrorSchema
from box_python_sdk.model.tracking_code import TrackingCode as TrackingCodeSchema
from box_python_sdk.model.user_full import UserFull as UserFullSchema

from box_python_sdk.type.post_users_request import PostUsersRequest
from box_python_sdk.type.tracking_code import TrackingCode
from box_python_sdk.type.user_full import UserFull
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.tracking_code import TrackingCode as TrackingCodePydantic
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.post_users_request import PostUsersRequest as PostUsersRequestPydantic
from box_python_sdk.pydantic.user_full import UserFull as UserFullPydantic

# Query params


class FieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'fields': typing.Union[FieldsSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
)
# body param
SchemaForRequestBodyApplicationJson = PostUsersRequestSchema


request_body_post_users_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = UserFullSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: UserFull


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: UserFull


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _users_0_mapped_args(
        self,
        name: str,
        login: typing.Optional[str] = None,
        is_platform_access_only: typing.Optional[bool] = None,
        role: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        is_sync_enabled: typing.Optional[bool] = None,
        job_title: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        space_amount: typing.Optional[int] = None,
        tracking_codes: typing.Optional[typing.List[TrackingCode]] = None,
        can_see_managed_users: typing.Optional[bool] = None,
        timezone: typing.Optional[str] = None,
        is_external_collab_restricted: typing.Optional[bool] = None,
        is_exempt_from_device_limits: typing.Optional[bool] = None,
        is_exempt_from_login_verification: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        external_app_user_id: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if login is not None:
            _body["login"] = login
        if is_platform_access_only is not None:
            _body["is_platform_access_only"] = is_platform_access_only
        if role is not None:
            _body["role"] = role
        if language is not None:
            _body["language"] = language
        if is_sync_enabled is not None:
            _body["is_sync_enabled"] = is_sync_enabled
        if job_title is not None:
            _body["job_title"] = job_title
        if phone is not None:
            _body["phone"] = phone
        if address is not None:
            _body["address"] = address
        if space_amount is not None:
            _body["space_amount"] = space_amount
        if tracking_codes is not None:
            _body["tracking_codes"] = tracking_codes
        if can_see_managed_users is not None:
            _body["can_see_managed_users"] = can_see_managed_users
        if timezone is not None:
            _body["timezone"] = timezone
        if is_external_collab_restricted is not None:
            _body["is_external_collab_restricted"] = is_external_collab_restricted
        if is_exempt_from_device_limits is not None:
            _body["is_exempt_from_device_limits"] = is_exempt_from_device_limits
        if is_exempt_from_login_verification is not None:
            _body["is_exempt_from_login_verification"] = is_exempt_from_login_verification
        if status is not None:
            _body["status"] = status
        if external_app_user_id is not None:
            _body["external_app_user_id"] = external_app_user_id
        args.body = _body
        if fields is not None:
            _query_params["fields"] = fields
        args.query = _query_params
        return args

    async def _ausers_0_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Create user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/users',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_post_users_request.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _users_0_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Create user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/users',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_post_users_request.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


class Users0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ausers_0(
        self,
        name: str,
        login: typing.Optional[str] = None,
        is_platform_access_only: typing.Optional[bool] = None,
        role: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        is_sync_enabled: typing.Optional[bool] = None,
        job_title: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        space_amount: typing.Optional[int] = None,
        tracking_codes: typing.Optional[typing.List[TrackingCode]] = None,
        can_see_managed_users: typing.Optional[bool] = None,
        timezone: typing.Optional[str] = None,
        is_external_collab_restricted: typing.Optional[bool] = None,
        is_exempt_from_device_limits: typing.Optional[bool] = None,
        is_exempt_from_login_verification: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        external_app_user_id: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._users_0_mapped_args(
            name=name,
            login=login,
            is_platform_access_only=is_platform_access_only,
            role=role,
            language=language,
            is_sync_enabled=is_sync_enabled,
            job_title=job_title,
            phone=phone,
            address=address,
            space_amount=space_amount,
            tracking_codes=tracking_codes,
            can_see_managed_users=can_see_managed_users,
            timezone=timezone,
            is_external_collab_restricted=is_external_collab_restricted,
            is_exempt_from_device_limits=is_exempt_from_device_limits,
            is_exempt_from_login_verification=is_exempt_from_login_verification,
            status=status,
            external_app_user_id=external_app_user_id,
            fields=fields,
        )
        return await self._ausers_0_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def users_0(
        self,
        name: str,
        login: typing.Optional[str] = None,
        is_platform_access_only: typing.Optional[bool] = None,
        role: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        is_sync_enabled: typing.Optional[bool] = None,
        job_title: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        space_amount: typing.Optional[int] = None,
        tracking_codes: typing.Optional[typing.List[TrackingCode]] = None,
        can_see_managed_users: typing.Optional[bool] = None,
        timezone: typing.Optional[str] = None,
        is_external_collab_restricted: typing.Optional[bool] = None,
        is_exempt_from_device_limits: typing.Optional[bool] = None,
        is_exempt_from_login_verification: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        external_app_user_id: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._users_0_mapped_args(
            name=name,
            login=login,
            is_platform_access_only=is_platform_access_only,
            role=role,
            language=language,
            is_sync_enabled=is_sync_enabled,
            job_title=job_title,
            phone=phone,
            address=address,
            space_amount=space_amount,
            tracking_codes=tracking_codes,
            can_see_managed_users=can_see_managed_users,
            timezone=timezone,
            is_external_collab_restricted=is_external_collab_restricted,
            is_exempt_from_device_limits=is_exempt_from_device_limits,
            is_exempt_from_login_verification=is_exempt_from_login_verification,
            status=status,
            external_app_user_id=external_app_user_id,
            fields=fields,
        )
        return self._users_0_oapg(
            body=args.body,
            query_params=args.query,
        )

class Users0(BaseApi):

    async def ausers_0(
        self,
        name: str,
        login: typing.Optional[str] = None,
        is_platform_access_only: typing.Optional[bool] = None,
        role: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        is_sync_enabled: typing.Optional[bool] = None,
        job_title: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        space_amount: typing.Optional[int] = None,
        tracking_codes: typing.Optional[typing.List[TrackingCode]] = None,
        can_see_managed_users: typing.Optional[bool] = None,
        timezone: typing.Optional[str] = None,
        is_external_collab_restricted: typing.Optional[bool] = None,
        is_exempt_from_device_limits: typing.Optional[bool] = None,
        is_exempt_from_login_verification: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        external_app_user_id: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> UserFullPydantic:
        raw_response = await self.raw.ausers_0(
            name=name,
            login=login,
            is_platform_access_only=is_platform_access_only,
            role=role,
            language=language,
            is_sync_enabled=is_sync_enabled,
            job_title=job_title,
            phone=phone,
            address=address,
            space_amount=space_amount,
            tracking_codes=tracking_codes,
            can_see_managed_users=can_see_managed_users,
            timezone=timezone,
            is_external_collab_restricted=is_external_collab_restricted,
            is_exempt_from_device_limits=is_exempt_from_device_limits,
            is_exempt_from_login_verification=is_exempt_from_login_verification,
            status=status,
            external_app_user_id=external_app_user_id,
            fields=fields,
            **kwargs,
        )
        if validate:
            return RootModel[UserFullPydantic](raw_response.body).root
        return api_client.construct_model_instance(UserFullPydantic, raw_response.body)
    
    
    def users_0(
        self,
        name: str,
        login: typing.Optional[str] = None,
        is_platform_access_only: typing.Optional[bool] = None,
        role: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        is_sync_enabled: typing.Optional[bool] = None,
        job_title: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        space_amount: typing.Optional[int] = None,
        tracking_codes: typing.Optional[typing.List[TrackingCode]] = None,
        can_see_managed_users: typing.Optional[bool] = None,
        timezone: typing.Optional[str] = None,
        is_external_collab_restricted: typing.Optional[bool] = None,
        is_exempt_from_device_limits: typing.Optional[bool] = None,
        is_exempt_from_login_verification: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        external_app_user_id: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> UserFullPydantic:
        raw_response = self.raw.users_0(
            name=name,
            login=login,
            is_platform_access_only=is_platform_access_only,
            role=role,
            language=language,
            is_sync_enabled=is_sync_enabled,
            job_title=job_title,
            phone=phone,
            address=address,
            space_amount=space_amount,
            tracking_codes=tracking_codes,
            can_see_managed_users=can_see_managed_users,
            timezone=timezone,
            is_external_collab_restricted=is_external_collab_restricted,
            is_exempt_from_device_limits=is_exempt_from_device_limits,
            is_exempt_from_login_verification=is_exempt_from_login_verification,
            status=status,
            external_app_user_id=external_app_user_id,
            fields=fields,
        )
        if validate:
            return RootModel[UserFullPydantic](raw_response.body).root
        return api_client.construct_model_instance(UserFullPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        login: typing.Optional[str] = None,
        is_platform_access_only: typing.Optional[bool] = None,
        role: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        is_sync_enabled: typing.Optional[bool] = None,
        job_title: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        space_amount: typing.Optional[int] = None,
        tracking_codes: typing.Optional[typing.List[TrackingCode]] = None,
        can_see_managed_users: typing.Optional[bool] = None,
        timezone: typing.Optional[str] = None,
        is_external_collab_restricted: typing.Optional[bool] = None,
        is_exempt_from_device_limits: typing.Optional[bool] = None,
        is_exempt_from_login_verification: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        external_app_user_id: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._users_0_mapped_args(
            name=name,
            login=login,
            is_platform_access_only=is_platform_access_only,
            role=role,
            language=language,
            is_sync_enabled=is_sync_enabled,
            job_title=job_title,
            phone=phone,
            address=address,
            space_amount=space_amount,
            tracking_codes=tracking_codes,
            can_see_managed_users=can_see_managed_users,
            timezone=timezone,
            is_external_collab_restricted=is_external_collab_restricted,
            is_exempt_from_device_limits=is_exempt_from_device_limits,
            is_exempt_from_login_verification=is_exempt_from_login_verification,
            status=status,
            external_app_user_id=external_app_user_id,
            fields=fields,
        )
        return await self._ausers_0_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        login: typing.Optional[str] = None,
        is_platform_access_only: typing.Optional[bool] = None,
        role: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        is_sync_enabled: typing.Optional[bool] = None,
        job_title: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        space_amount: typing.Optional[int] = None,
        tracking_codes: typing.Optional[typing.List[TrackingCode]] = None,
        can_see_managed_users: typing.Optional[bool] = None,
        timezone: typing.Optional[str] = None,
        is_external_collab_restricted: typing.Optional[bool] = None,
        is_exempt_from_device_limits: typing.Optional[bool] = None,
        is_exempt_from_login_verification: typing.Optional[bool] = None,
        status: typing.Optional[str] = None,
        external_app_user_id: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._users_0_mapped_args(
            name=name,
            login=login,
            is_platform_access_only=is_platform_access_only,
            role=role,
            language=language,
            is_sync_enabled=is_sync_enabled,
            job_title=job_title,
            phone=phone,
            address=address,
            space_amount=space_amount,
            tracking_codes=tracking_codes,
            can_see_managed_users=can_see_managed_users,
            timezone=timezone,
            is_external_collab_restricted=is_external_collab_restricted,
            is_exempt_from_device_limits=is_exempt_from_device_limits,
            is_exempt_from_login_verification=is_exempt_from_login_verification,
            status=status,
            external_app_user_id=external_app_user_id,
            fields=fields,
        )
        return self._users_0_oapg(
            body=args.body,
            query_params=args.query,
        )

