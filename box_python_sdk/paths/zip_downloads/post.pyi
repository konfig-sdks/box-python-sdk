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

from box_python_sdk.model.zip_download import ZipDownload as ZipDownloadSchema
from box_python_sdk.model.client_error import ClientError as ClientErrorSchema
from box_python_sdk.model.zip_download_request_items import ZipDownloadRequestItems as ZipDownloadRequestItemsSchema
from box_python_sdk.model.zip_download_request import ZipDownloadRequest as ZipDownloadRequestSchema

from box_python_sdk.type.zip_download_request_items import ZipDownloadRequestItems
from box_python_sdk.type.zip_download_request import ZipDownloadRequest
from box_python_sdk.type.zip_download import ZipDownload
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.zip_download_request import ZipDownloadRequest as ZipDownloadRequestPydantic
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.zip_download import ZipDownload as ZipDownloadPydantic
from box_python_sdk.pydantic.zip_download_request_items import ZipDownloadRequestItems as ZipDownloadRequestItemsPydantic

# body param
SchemaForRequestBodyApplicationJson = ZipDownloadRequestSchema


request_body_zip_download_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor202ResponseBodyApplicationJson = ZipDownloadSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: ZipDownload


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: ZipDownload


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

    def _create_request_mapped_args(
        self,
        items: ZipDownloadRequestItems,
        download_file_name: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if items is not None:
            _body["items"] = items
        if download_file_name is not None:
            _body["download_file_name"] = download_file_name
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
        ApiResponseFor202Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create zip download
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
            path_template='/zip_downloads',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_zip_download_request.serialize(body, content_type)
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
        ApiResponseFor202,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create zip download
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
            path_template='/zip_downloads',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_zip_download_request.serialize(body, content_type)
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
        items: ZipDownloadRequestItems,
        download_file_name: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_request_mapped_args(
            items=items,
            download_file_name=download_file_name,
        )
        return await self._acreate_request_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_request(
        self,
        items: ZipDownloadRequestItems,
        download_file_name: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_request_mapped_args(
            items=items,
            download_file_name=download_file_name,
        )
        return self._create_request_oapg(
            body=args.body,
        )

class CreateRequest(BaseApi):

    async def acreate_request(
        self,
        items: ZipDownloadRequestItems,
        download_file_name: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ZipDownloadPydantic:
        raw_response = await self.raw.acreate_request(
            items=items,
            download_file_name=download_file_name,
            **kwargs,
        )
        if validate:
            return ZipDownloadPydantic(**raw_response.body)
        return api_client.construct_model_instance(ZipDownloadPydantic, raw_response.body)
    
    
    def create_request(
        self,
        items: ZipDownloadRequestItems,
        download_file_name: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ZipDownloadPydantic:
        raw_response = self.raw.create_request(
            items=items,
            download_file_name=download_file_name,
        )
        if validate:
            return ZipDownloadPydantic(**raw_response.body)
        return api_client.construct_model_instance(ZipDownloadPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        items: ZipDownloadRequestItems,
        download_file_name: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_request_mapped_args(
            items=items,
            download_file_name=download_file_name,
        )
        return await self._acreate_request_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        items: ZipDownloadRequestItems,
        download_file_name: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_request_mapped_args(
            items=items,
            download_file_name=download_file_name,
        )
        return self._create_request_oapg(
            body=args.body,
        )

