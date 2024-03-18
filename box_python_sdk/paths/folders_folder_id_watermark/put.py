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

from box_python_sdk.model.watermarks_folders_apply_to_folder_request_watermark import WatermarksFoldersApplyToFolderRequestWatermark as WatermarksFoldersApplyToFolderRequestWatermarkSchema
from box_python_sdk.model.client_error import ClientError as ClientErrorSchema
from box_python_sdk.model.watermark import Watermark as WatermarkSchema
from box_python_sdk.model.watermarks_folders_apply_to_folder_request import WatermarksFoldersApplyToFolderRequest as WatermarksFoldersApplyToFolderRequestSchema

from box_python_sdk.type.watermarks_folders_apply_to_folder_request_watermark import WatermarksFoldersApplyToFolderRequestWatermark
from box_python_sdk.type.watermark import Watermark
from box_python_sdk.type.watermarks_folders_apply_to_folder_request import WatermarksFoldersApplyToFolderRequest
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.watermarks_folders_apply_to_folder_request import WatermarksFoldersApplyToFolderRequest as WatermarksFoldersApplyToFolderRequestPydantic
from box_python_sdk.pydantic.watermark import Watermark as WatermarkPydantic
from box_python_sdk.pydantic.watermarks_folders_apply_to_folder_request_watermark import WatermarksFoldersApplyToFolderRequestWatermark as WatermarksFoldersApplyToFolderRequestWatermarkPydantic

from . import path

# Path params
FolderIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'folder_id': typing.Union[FolderIdSchema, str, ],
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


request_path_folder_id = api_client.PathParameter(
    name="folder_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FolderIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = WatermarksFoldersApplyToFolderRequestSchema


request_body_watermarks_folders_apply_to_folder_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'OAuth2Security',
]
SchemaFor200ResponseBodyApplicationJson = WatermarkSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Watermark


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Watermark


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = WatermarkSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Watermark


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Watermark


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
    '200': _response_for_200,
    '201': _response_for_201,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _apply_to_folder_mapped_args(
        self,
        watermark: WatermarksFoldersApplyToFolderRequestWatermark,
        folder_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if watermark is not None:
            _body["watermark"] = watermark
        args.body = _body
        if folder_id is not None:
            _path_params["folder_id"] = folder_id
        args.path = _path_params
        return args

    async def _aapply_to_folder_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Apply watermark to folder
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_folder_id,
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
            path_template='/folders/{folder_id}/watermark',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_watermarks_folders_apply_to_folder_request.serialize(body, content_type)
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


    def _apply_to_folder_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Apply watermark to folder
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_folder_id,
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
            path_template='/folders/{folder_id}/watermark',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_watermarks_folders_apply_to_folder_request.serialize(body, content_type)
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


class ApplyToFolderRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aapply_to_folder(
        self,
        watermark: WatermarksFoldersApplyToFolderRequestWatermark,
        folder_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._apply_to_folder_mapped_args(
            watermark=watermark,
            folder_id=folder_id,
        )
        return await self._aapply_to_folder_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def apply_to_folder(
        self,
        watermark: WatermarksFoldersApplyToFolderRequestWatermark,
        folder_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._apply_to_folder_mapped_args(
            watermark=watermark,
            folder_id=folder_id,
        )
        return self._apply_to_folder_oapg(
            body=args.body,
            path_params=args.path,
        )

class ApplyToFolder(BaseApi):

    async def aapply_to_folder(
        self,
        watermark: WatermarksFoldersApplyToFolderRequestWatermark,
        folder_id: str,
        validate: bool = False,
        **kwargs,
    ) -> WatermarkPydantic:
        raw_response = await self.raw.aapply_to_folder(
            watermark=watermark,
            folder_id=folder_id,
            **kwargs,
        )
        if validate:
            return WatermarkPydantic(**raw_response.body)
        return api_client.construct_model_instance(WatermarkPydantic, raw_response.body)
    
    
    def apply_to_folder(
        self,
        watermark: WatermarksFoldersApplyToFolderRequestWatermark,
        folder_id: str,
        validate: bool = False,
    ) -> WatermarkPydantic:
        raw_response = self.raw.apply_to_folder(
            watermark=watermark,
            folder_id=folder_id,
        )
        if validate:
            return WatermarkPydantic(**raw_response.body)
        return api_client.construct_model_instance(WatermarkPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        watermark: WatermarksFoldersApplyToFolderRequestWatermark,
        folder_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._apply_to_folder_mapped_args(
            watermark=watermark,
            folder_id=folder_id,
        )
        return await self._aapply_to_folder_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        watermark: WatermarksFoldersApplyToFolderRequestWatermark,
        folder_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._apply_to_folder_mapped_args(
            watermark=watermark,
            folder_id=folder_id,
        )
        return self._apply_to_folder_oapg(
            body=args.body,
            path_params=args.path,
        )

