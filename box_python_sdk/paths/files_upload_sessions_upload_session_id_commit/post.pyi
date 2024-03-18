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

from box_python_sdk.model.client_error import ClientError as ClientErrorSchema
from box_python_sdk.model.upload_part import UploadPart as UploadPartSchema
from box_python_sdk.model.uploads_chunked_commit_session_request import UploadsChunkedCommitSessionRequest as UploadsChunkedCommitSessionRequestSchema
from box_python_sdk.model.files import Files as FilesSchema

from box_python_sdk.type.upload_part import UploadPart
from box_python_sdk.type.files import Files
from box_python_sdk.type.uploads_chunked_commit_session_request import UploadsChunkedCommitSessionRequest
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.uploads_chunked_commit_session_request import UploadsChunkedCommitSessionRequest as UploadsChunkedCommitSessionRequestPydantic
from box_python_sdk.pydantic.files import Files as FilesPydantic
from box_python_sdk.pydantic.upload_part import UploadPart as UploadPartPydantic

# Header params
DigestSchema = schemas.StrSchema
IfMatchSchema = schemas.StrSchema
IfNoneMatchSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'digest': typing.Union[DigestSchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'if-match': typing.Union[IfMatchSchema, str, ],
        'if-none-match': typing.Union[IfNoneMatchSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_digest = api_client.HeaderParameter(
    name="digest",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DigestSchema,
    required=True,
)
request_header_if_match = api_client.HeaderParameter(
    name="if-match",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IfMatchSchema,
)
request_header_if_none_match = api_client.HeaderParameter(
    name="if-none-match",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IfNoneMatchSchema,
)
# Path params
UploadSessionIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'upload_session_id': typing.Union[UploadSessionIdSchema, str, ],
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


request_path_upload_session_id = api_client.PathParameter(
    name="upload_session_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UploadSessionIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UploadsChunkedCommitSessionRequestSchema


request_body_uploads_chunked_commit_session_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = FilesSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Files


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Files


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
RetryAfterSchema = schemas.IntSchema
ResponseHeadersFor202 = typing_extensions.TypedDict(
    'ResponseHeadersFor202',
    {
        'Retry-After': RetryAfterSchema,
    }
)


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    headers: ResponseHeadersFor202
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    headers: ResponseHeadersFor202
    body: schemas.Unset = schemas.unset


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    headers=[
        retry_after_parameter,
    ]
)
SchemaFor409ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor409ResponseBodyApplicationJson),
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

    def _commit_session_mapped_args(
        self,
        parts: typing.List[UploadPart],
        upload_session_id: str,
        digest: str,
        if_match: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if parts is not None:
            _body["parts"] = parts
        args.body = _body
        if digest is not None:
            _header_params["digest"] = digest
        if if_match is not None:
            _header_params["if-match"] = if_match
        if if_none_match is not None:
            _header_params["if-none-match"] = if_none_match
        if upload_session_id is not None:
            _path_params["upload_session_id"] = upload_session_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _acommit_session_oapg(
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
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Commit upload session
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_upload_session_id,
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
            request_header_digest,
            request_header_if_match,
            request_header_if_none_match,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/files/upload_sessions/{upload_session_id}/commit',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_uploads_chunked_commit_session_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        host = self._get_host_oapg('commit_session', _servers, host_index)
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            host=host,
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


    def _commit_session_oapg(
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
        ApiResponseFor201,
        ApiResponseFor202,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Commit upload session
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_upload_session_id,
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
            request_header_digest,
            request_header_if_match,
            request_header_if_none_match,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/files/upload_sessions/{upload_session_id}/commit',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_uploads_chunked_commit_session_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        host = self._get_host_oapg('commit_session', _servers, host_index)
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            host=host,
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


class CommitSessionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acommit_session(
        self,
        parts: typing.List[UploadPart],
        upload_session_id: str,
        digest: str,
        if_match: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._commit_session_mapped_args(
            parts=parts,
            upload_session_id=upload_session_id,
            digest=digest,
            if_match=if_match,
            if_none_match=if_none_match,
        )
        return await self._acommit_session_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def commit_session(
        self,
        parts: typing.List[UploadPart],
        upload_session_id: str,
        digest: str,
        if_match: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseFor202,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._commit_session_mapped_args(
            parts=parts,
            upload_session_id=upload_session_id,
            digest=digest,
            if_match=if_match,
            if_none_match=if_none_match,
        )
        return self._commit_session_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class CommitSession(BaseApi):

    async def acommit_session(
        self,
        parts: typing.List[UploadPart],
        upload_session_id: str,
        digest: str,
        if_match: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FilesPydantic:
        raw_response = await self.raw.acommit_session(
            parts=parts,
            upload_session_id=upload_session_id,
            digest=digest,
            if_match=if_match,
            if_none_match=if_none_match,
            **kwargs,
        )
        if validate:
            return FilesPydantic(**raw_response.body)
        return api_client.construct_model_instance(FilesPydantic, raw_response.body)
    
    
    def commit_session(
        self,
        parts: typing.List[UploadPart],
        upload_session_id: str,
        digest: str,
        if_match: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FilesPydantic:
        raw_response = self.raw.commit_session(
            parts=parts,
            upload_session_id=upload_session_id,
            digest=digest,
            if_match=if_match,
            if_none_match=if_none_match,
        )
        if validate:
            return FilesPydantic(**raw_response.body)
        return api_client.construct_model_instance(FilesPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        parts: typing.List[UploadPart],
        upload_session_id: str,
        digest: str,
        if_match: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseFor202Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._commit_session_mapped_args(
            parts=parts,
            upload_session_id=upload_session_id,
            digest=digest,
            if_match=if_match,
            if_none_match=if_none_match,
        )
        return await self._acommit_session_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        parts: typing.List[UploadPart],
        upload_session_id: str,
        digest: str,
        if_match: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseFor202,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._commit_session_mapped_args(
            parts=parts,
            upload_session_id=upload_session_id,
            digest=digest,
            if_match=if_match,
            if_none_match=if_none_match,
        )
        return self._commit_session_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

