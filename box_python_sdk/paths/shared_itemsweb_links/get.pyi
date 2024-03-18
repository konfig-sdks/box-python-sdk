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
from box_python_sdk.model.web_link import WebLink as WebLinkSchema

from box_python_sdk.type.web_link import WebLink
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.web_link import WebLink as WebLinkPydantic

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
# Header params
IfNoneMatchSchema = schemas.StrSchema
BoxapiSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'boxapi': typing.Union[BoxapiSchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'if-none-match': typing.Union[IfNoneMatchSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_if_none_match = api_client.HeaderParameter(
    name="if-none-match",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IfNoneMatchSchema,
)
request_header_boxapi = api_client.HeaderParameter(
    name="boxapi",
    style=api_client.ParameterStyle.SIMPLE,
    schema=BoxapiSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = WebLinkSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: WebLink


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: WebLink


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor304(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor304Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_304 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor304,
    response_cls_async=ApiResponseFor304Async,
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

    def _find_shared_web_link_mapped_args(
        self,
        boxapi: str,
        if_none_match: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        if fields is not None:
            _query_params["fields"] = fields
        if if_none_match is not None:
            _header_params["if-none-match"] = if_none_match
        if boxapi is not None:
            _header_params["boxapi"] = boxapi
        args.query = _query_params
        args.header = _header_params
        return args

    async def _afind_shared_web_link_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Find web link for shared link
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
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
        for parameter in (
            request_header_if_none_match,
            request_header_boxapi,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/shared_items#web_links',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _find_shared_web_link_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Find web link for shared link
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
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
        for parameter in (
            request_header_if_none_match,
            request_header_boxapi,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/shared_items#web_links',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class FindSharedWebLinkRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def afind_shared_web_link(
        self,
        boxapi: str,
        if_none_match: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_shared_web_link_mapped_args(
            boxapi=boxapi,
            if_none_match=if_none_match,
            fields=fields,
        )
        return await self._afind_shared_web_link_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def find_shared_web_link(
        self,
        boxapi: str,
        if_none_match: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_shared_web_link_mapped_args(
            boxapi=boxapi,
            if_none_match=if_none_match,
            fields=fields,
        )
        return self._find_shared_web_link_oapg(
            query_params=args.query,
            header_params=args.header,
        )

class FindSharedWebLink(BaseApi):

    async def afind_shared_web_link(
        self,
        boxapi: str,
        if_none_match: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> WebLinkPydantic:
        raw_response = await self.raw.afind_shared_web_link(
            boxapi=boxapi,
            if_none_match=if_none_match,
            fields=fields,
            **kwargs,
        )
        if validate:
            return RootModel[WebLinkPydantic](raw_response.body).root
        return api_client.construct_model_instance(WebLinkPydantic, raw_response.body)
    
    
    def find_shared_web_link(
        self,
        boxapi: str,
        if_none_match: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> WebLinkPydantic:
        raw_response = self.raw.find_shared_web_link(
            boxapi=boxapi,
            if_none_match=if_none_match,
            fields=fields,
        )
        if validate:
            return RootModel[WebLinkPydantic](raw_response.body).root
        return api_client.construct_model_instance(WebLinkPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        boxapi: str,
        if_none_match: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_shared_web_link_mapped_args(
            boxapi=boxapi,
            if_none_match=if_none_match,
            fields=fields,
        )
        return await self._afind_shared_web_link_oapg(
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def get(
        self,
        boxapi: str,
        if_none_match: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_shared_web_link_mapped_args(
            boxapi=boxapi,
            if_none_match=if_none_match,
            fields=fields,
        )
        return self._find_shared_web_link_oapg(
            query_params=args.query,
            header_params=args.header,
        )

