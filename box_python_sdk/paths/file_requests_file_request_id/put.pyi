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

from box_python_sdk.model.file_request import FileRequest as FileRequestSchema
from box_python_sdk.model.client_error import ClientError as ClientErrorSchema
from box_python_sdk.model.file_request_update_request import FileRequestUpdateRequest as FileRequestUpdateRequestSchema

from box_python_sdk.type.file_request import FileRequest
from box_python_sdk.type.file_request_update_request import FileRequestUpdateRequest
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.file_request import FileRequest as FileRequestPydantic
from box_python_sdk.pydantic.file_request_update_request import FileRequestUpdateRequest as FileRequestUpdateRequestPydantic
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic

# Header params
IfMatchSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'if-match': typing.Union[IfMatchSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_if_match = api_client.HeaderParameter(
    name="if-match",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IfMatchSchema,
)
# Path params
FileRequestIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'file_request_id': typing.Union[FileRequestIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_file_request_id = api_client.PathParameter(
    name="file_request_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FileRequestIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = FileRequestUpdateRequestSchema


request_body_file_request_update_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = FileRequestSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FileRequest


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FileRequest


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
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
SchemaFor405ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor405(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor405Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
    response_cls_async=ApiResponseFor405Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor405ResponseBodyApplicationJson),
    },
)
SchemaFor412ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor412(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor412Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_412 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor412,
    response_cls_async=ApiResponseFor412Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor412ResponseBodyApplicationJson),
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

    def _update_request_mapped_args(
        self,
        file_request_id: str,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        is_email_required: typing.Optional[bool] = None,
        is_description_required: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        if_match: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if description is not None:
            _body["description"] = description
        if status is not None:
            _body["status"] = status
        if is_email_required is not None:
            _body["is_email_required"] = is_email_required
        if is_description_required is not None:
            _body["is_description_required"] = is_description_required
        if expires_at is not None:
            _body["expires_at"] = expires_at
        args.body = _body
        if if_match is not None:
            _header_params["if-match"] = if_match
        if file_request_id is not None:
            _path_params["file_request_id"] = file_request_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aupdate_request_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update file request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_file_request_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_if_match,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/file_requests/{file_request_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_file_request_update_request.serialize(body, content_type)
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


    def _update_request_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update file request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_file_request_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_if_match,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/file_requests/{file_request_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_file_request_update_request.serialize(body, content_type)
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


class UpdateRequestRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_request(
        self,
        file_request_id: str,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        is_email_required: typing.Optional[bool] = None,
        is_description_required: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        if_match: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_request_mapped_args(
            file_request_id=file_request_id,
            title=title,
            description=description,
            status=status,
            is_email_required=is_email_required,
            is_description_required=is_description_required,
            expires_at=expires_at,
            if_match=if_match,
        )
        return await self._aupdate_request_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def update_request(
        self,
        file_request_id: str,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        is_email_required: typing.Optional[bool] = None,
        is_description_required: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        if_match: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_request_mapped_args(
            file_request_id=file_request_id,
            title=title,
            description=description,
            status=status,
            is_email_required=is_email_required,
            is_description_required=is_description_required,
            expires_at=expires_at,
            if_match=if_match,
        )
        return self._update_request_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class UpdateRequest(BaseApi):

    async def aupdate_request(
        self,
        file_request_id: str,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        is_email_required: typing.Optional[bool] = None,
        is_description_required: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        if_match: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FileRequestPydantic:
        raw_response = await self.raw.aupdate_request(
            file_request_id=file_request_id,
            title=title,
            description=description,
            status=status,
            is_email_required=is_email_required,
            is_description_required=is_description_required,
            expires_at=expires_at,
            if_match=if_match,
            **kwargs,
        )
        if validate:
            return FileRequestPydantic(**raw_response.body)
        return api_client.construct_model_instance(FileRequestPydantic, raw_response.body)
    
    
    def update_request(
        self,
        file_request_id: str,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        is_email_required: typing.Optional[bool] = None,
        is_description_required: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        if_match: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FileRequestPydantic:
        raw_response = self.raw.update_request(
            file_request_id=file_request_id,
            title=title,
            description=description,
            status=status,
            is_email_required=is_email_required,
            is_description_required=is_description_required,
            expires_at=expires_at,
            if_match=if_match,
        )
        if validate:
            return FileRequestPydantic(**raw_response.body)
        return api_client.construct_model_instance(FileRequestPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        file_request_id: str,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        is_email_required: typing.Optional[bool] = None,
        is_description_required: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        if_match: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_request_mapped_args(
            file_request_id=file_request_id,
            title=title,
            description=description,
            status=status,
            is_email_required=is_email_required,
            is_description_required=is_description_required,
            expires_at=expires_at,
            if_match=if_match,
        )
        return await self._aupdate_request_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        file_request_id: str,
        title: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        is_email_required: typing.Optional[bool] = None,
        is_description_required: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        if_match: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_request_mapped_args(
            file_request_id=file_request_id,
            title=title,
            description=description,
            status=status,
            is_email_required=is_email_required,
            is_description_required=is_description_required,
            expires_at=expires_at,
            if_match=if_match,
        )
        return self._update_request_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

