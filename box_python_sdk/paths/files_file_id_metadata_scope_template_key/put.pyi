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
from box_python_sdk.model.metadata_full import MetadataFull as MetadataFullSchema
from box_python_sdk.model.metadata_instances_files_update_instance_on_file_request import MetadataInstancesFilesUpdateInstanceOnFileRequest as MetadataInstancesFilesUpdateInstanceOnFileRequestSchema

from box_python_sdk.type.metadata_full import MetadataFull
from box_python_sdk.type.metadata_instances_files_update_instance_on_file_request import MetadataInstancesFilesUpdateInstanceOnFileRequest
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.metadata_instances_files_update_instance_on_file_request import MetadataInstancesFilesUpdateInstanceOnFileRequest as MetadataInstancesFilesUpdateInstanceOnFileRequestPydantic
from box_python_sdk.pydantic.metadata_full import MetadataFull as MetadataFullPydantic

# Path params
FileIdSchema = schemas.StrSchema


class ScopeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def GLOBAL(cls):
        return cls("global")
    
    @schemas.classproperty
    def ENTERPRISE(cls):
        return cls("enterprise")
TemplateKeySchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'file_id': typing.Union[FileIdSchema, str, ],
        'scope': typing.Union[ScopeSchema, str, ],
        'template_key': typing.Union[TemplateKeySchema, str, ],
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


request_path_file_id = api_client.PathParameter(
    name="file_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FileIdSchema,
    required=True,
)
request_path_scope = api_client.PathParameter(
    name="scope",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ScopeSchema,
    required=True,
)
request_path_template_key = api_client.PathParameter(
    name="template_key",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TemplateKeySchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJsonPatchjson = MetadataInstancesFilesUpdateInstanceOnFileRequestSchema


request_body_metadata_instances_files_update_instance_on_file_request = api_client.RequestBody(
    content={
        'application/json-patch+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonPatchjson),
    },
)
SchemaFor200ResponseBodyApplicationJson = MetadataFullSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: MetadataFull


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: MetadataFull


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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

    def _update_instance_on_file_mapped_args(
        self,
        file_id: str,
        scope: str,
        template_key: str,
        body: typing.Optional[MetadataInstancesFilesUpdateInstanceOnFileRequest] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        args.body = body if body is not None else _body
        if file_id is not None:
            _path_params["file_id"] = file_id
        if scope is not None:
            _path_params["scope"] = scope
        if template_key is not None:
            _path_params["template_key"] = template_key
        args.path = _path_params
        return args

    async def _aupdate_instance_on_file_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update metadata instance on file
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_file_id,
            request_path_scope,
            request_path_template_key,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
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
            path_template='/files/{file_id}/metadata/{scope}/{template_key}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_metadata_instances_files_update_instance_on_file_request.serialize(body, content_type)
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


    def _update_instance_on_file_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json-patch+json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update metadata instance on file
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_file_id,
            request_path_scope,
            request_path_template_key,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
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
            path_template='/files/{file_id}/metadata/{scope}/{template_key}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_metadata_instances_files_update_instance_on_file_request.serialize(body, content_type)
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


class UpdateInstanceOnFileRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_instance_on_file(
        self,
        file_id: str,
        scope: str,
        template_key: str,
        body: typing.Optional[MetadataInstancesFilesUpdateInstanceOnFileRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_instance_on_file_mapped_args(
            body=body,
            file_id=file_id,
            scope=scope,
            template_key=template_key,
        )
        return await self._aupdate_instance_on_file_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_instance_on_file(
        self,
        file_id: str,
        scope: str,
        template_key: str,
        body: typing.Optional[MetadataInstancesFilesUpdateInstanceOnFileRequest] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_instance_on_file_mapped_args(
            body=body,
            file_id=file_id,
            scope=scope,
            template_key=template_key,
        )
        return self._update_instance_on_file_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateInstanceOnFile(BaseApi):

    async def aupdate_instance_on_file(
        self,
        file_id: str,
        scope: str,
        template_key: str,
        body: typing.Optional[MetadataInstancesFilesUpdateInstanceOnFileRequest] = None,
        validate: bool = False,
        **kwargs,
    ) -> MetadataFullPydantic:
        raw_response = await self.raw.aupdate_instance_on_file(
            body=body,
            file_id=file_id,
            scope=scope,
            template_key=template_key,
            **kwargs,
        )
        if validate:
            return RootModel[MetadataFullPydantic](raw_response.body).root
        return api_client.construct_model_instance(MetadataFullPydantic, raw_response.body)
    
    
    def update_instance_on_file(
        self,
        file_id: str,
        scope: str,
        template_key: str,
        body: typing.Optional[MetadataInstancesFilesUpdateInstanceOnFileRequest] = None,
        validate: bool = False,
    ) -> MetadataFullPydantic:
        raw_response = self.raw.update_instance_on_file(
            body=body,
            file_id=file_id,
            scope=scope,
            template_key=template_key,
        )
        if validate:
            return RootModel[MetadataFullPydantic](raw_response.body).root
        return api_client.construct_model_instance(MetadataFullPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        file_id: str,
        scope: str,
        template_key: str,
        body: typing.Optional[MetadataInstancesFilesUpdateInstanceOnFileRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_instance_on_file_mapped_args(
            body=body,
            file_id=file_id,
            scope=scope,
            template_key=template_key,
        )
        return await self._aupdate_instance_on_file_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        file_id: str,
        scope: str,
        template_key: str,
        body: typing.Optional[MetadataInstancesFilesUpdateInstanceOnFileRequest] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_instance_on_file_mapped_args(
            body=body,
            file_id=file_id,
            scope=scope,
            template_key=template_key,
        )
        return self._update_instance_on_file_oapg(
            body=args.body,
            path_params=args.path,
        )

