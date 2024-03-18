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

from box_python_sdk.model.session_termination_create_session_termination_jobs_request_user_logins import SessionTerminationCreateSessionTerminationJobsRequestUserLogins as SessionTerminationCreateSessionTerminationJobsRequestUserLoginsSchema
from box_python_sdk.model.client_error import ClientError as ClientErrorSchema
from box_python_sdk.model.session_termination_create_session_termination_jobs_request_user_ids import SessionTerminationCreateSessionTerminationJobsRequestUserIds as SessionTerminationCreateSessionTerminationJobsRequestUserIdsSchema
from box_python_sdk.model.session_termination_create_session_termination_jobs_request import SessionTerminationCreateSessionTerminationJobsRequest as SessionTerminationCreateSessionTerminationJobsRequestSchema
from box_python_sdk.model.session_termination_message import SessionTerminationMessage as SessionTerminationMessageSchema

from box_python_sdk.type.session_termination_create_session_termination_jobs_request_user_logins import SessionTerminationCreateSessionTerminationJobsRequestUserLogins
from box_python_sdk.type.session_termination_create_session_termination_jobs_request_user_ids import SessionTerminationCreateSessionTerminationJobsRequestUserIds
from box_python_sdk.type.session_termination_message import SessionTerminationMessage
from box_python_sdk.type.session_termination_create_session_termination_jobs_request import SessionTerminationCreateSessionTerminationJobsRequest
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.session_termination_message import SessionTerminationMessage as SessionTerminationMessagePydantic
from box_python_sdk.pydantic.session_termination_create_session_termination_jobs_request import SessionTerminationCreateSessionTerminationJobsRequest as SessionTerminationCreateSessionTerminationJobsRequestPydantic
from box_python_sdk.pydantic.session_termination_create_session_termination_jobs_request_user_ids import SessionTerminationCreateSessionTerminationJobsRequestUserIds as SessionTerminationCreateSessionTerminationJobsRequestUserIdsPydantic
from box_python_sdk.pydantic.session_termination_create_session_termination_jobs_request_user_logins import SessionTerminationCreateSessionTerminationJobsRequestUserLogins as SessionTerminationCreateSessionTerminationJobsRequestUserLoginsPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = SessionTerminationCreateSessionTerminationJobsRequestSchema


request_body_session_termination_create_session_termination_jobs_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'OAuth2Security',
]
SchemaFor202ResponseBodyApplicationJson = SessionTerminationMessageSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: SessionTerminationMessage


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: SessionTerminationMessage


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor429ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor429ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
SchemaFor503ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor503(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor503Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_503 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor503,
    response_cls_async=ApiResponseFor503Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor503ResponseBodyApplicationJson),
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
    '202': _response_for_202,
    '400': _response_for_400,
    '403': _response_for_403,
    '404': _response_for_404,
    '429': _response_for_429,
    '500': _response_for_500,
    '503': _response_for_503,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_session_termination_jobs_mapped_args(
        self,
        user_ids: SessionTerminationCreateSessionTerminationJobsRequestUserIds,
        user_logins: SessionTerminationCreateSessionTerminationJobsRequestUserLogins,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if user_ids is not None:
            _body["user_ids"] = user_ids
        if user_logins is not None:
            _body["user_logins"] = user_logins
        args.body = _body
        return args

    async def _acreate_session_termination_jobs_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create jobs to terminate users session
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
            path_template='/users/terminate_sessions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_session_termination_create_session_termination_jobs_request.serialize(body, content_type)
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


    def _create_session_termination_jobs_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor202,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create jobs to terminate users session
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
            path_template='/users/terminate_sessions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_session_termination_create_session_termination_jobs_request.serialize(body, content_type)
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


class CreateSessionTerminationJobsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_session_termination_jobs(
        self,
        user_ids: SessionTerminationCreateSessionTerminationJobsRequestUserIds,
        user_logins: SessionTerminationCreateSessionTerminationJobsRequestUserLogins,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_session_termination_jobs_mapped_args(
            user_ids=user_ids,
            user_logins=user_logins,
        )
        return await self._acreate_session_termination_jobs_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_session_termination_jobs(
        self,
        user_ids: SessionTerminationCreateSessionTerminationJobsRequestUserIds,
        user_logins: SessionTerminationCreateSessionTerminationJobsRequestUserLogins,
    ) -> typing.Union[
        ApiResponseFor202,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_session_termination_jobs_mapped_args(
            user_ids=user_ids,
            user_logins=user_logins,
        )
        return self._create_session_termination_jobs_oapg(
            body=args.body,
        )

class CreateSessionTerminationJobs(BaseApi):

    async def acreate_session_termination_jobs(
        self,
        user_ids: SessionTerminationCreateSessionTerminationJobsRequestUserIds,
        user_logins: SessionTerminationCreateSessionTerminationJobsRequestUserLogins,
        validate: bool = False,
        **kwargs,
    ) -> SessionTerminationMessagePydantic:
        raw_response = await self.raw.acreate_session_termination_jobs(
            user_ids=user_ids,
            user_logins=user_logins,
            **kwargs,
        )
        if validate:
            return SessionTerminationMessagePydantic(**raw_response.body)
        return api_client.construct_model_instance(SessionTerminationMessagePydantic, raw_response.body)
    
    
    def create_session_termination_jobs(
        self,
        user_ids: SessionTerminationCreateSessionTerminationJobsRequestUserIds,
        user_logins: SessionTerminationCreateSessionTerminationJobsRequestUserLogins,
        validate: bool = False,
    ) -> SessionTerminationMessagePydantic:
        raw_response = self.raw.create_session_termination_jobs(
            user_ids=user_ids,
            user_logins=user_logins,
        )
        if validate:
            return SessionTerminationMessagePydantic(**raw_response.body)
        return api_client.construct_model_instance(SessionTerminationMessagePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        user_ids: SessionTerminationCreateSessionTerminationJobsRequestUserIds,
        user_logins: SessionTerminationCreateSessionTerminationJobsRequestUserLogins,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_session_termination_jobs_mapped_args(
            user_ids=user_ids,
            user_logins=user_logins,
        )
        return await self._acreate_session_termination_jobs_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        user_ids: SessionTerminationCreateSessionTerminationJobsRequestUserIds,
        user_logins: SessionTerminationCreateSessionTerminationJobsRequestUserLogins,
    ) -> typing.Union[
        ApiResponseFor202,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_session_termination_jobs_mapped_args(
            user_ids=user_ids,
            user_logins=user_logins,
        )
        return self._create_session_termination_jobs_oapg(
            body=args.body,
        )

