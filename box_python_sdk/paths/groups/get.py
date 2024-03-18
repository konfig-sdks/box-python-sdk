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

from box_python_sdk.model.groups import Groups as GroupsSchema
from box_python_sdk.model.client_error import ClientError as ClientErrorSchema

from box_python_sdk.type.client_error import ClientError
from box_python_sdk.type.groups import Groups

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.groups import Groups as GroupsPydantic

from . import path

# Query params
FilterTermSchema = schemas.StrSchema


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


class LimitSchema(
    schemas.Int64Schema
):


    class MetaOapg:
        format = 'int64'
        inclusive_maximum = 1000
OffsetSchema = schemas.Int64Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'filter_term': typing.Union[FilterTermSchema, str, ],
        'fields': typing.Union[FieldsSchema, list, tuple, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_filter_term = api_client.QueryParameter(
    name="filter_term",
    style=api_client.ParameterStyle.FORM,
    schema=FilterTermSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
_auth = [
    'OAuth2Security',
]
SchemaFor200ResponseBodyApplicationJson = GroupsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Groups


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Groups


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _groups_mapped_args(
        self,
        filter_term: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if filter_term is not None:
            _query_params["filter_term"] = filter_term
        if fields is not None:
            _query_params["fields"] = fields
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        args.query = _query_params
        return args

    async def _agroups_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        List groups for enterprise
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_filter_term,
            request_query_fields,
            request_query_limit,
            request_query_offset,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/groups',
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


    def _groups_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        List groups for enterprise
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_filter_term,
            request_query_fields,
            request_query_limit,
            request_query_offset,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/groups',
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


class GroupsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agroups(
        self,
        filter_term: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._groups_mapped_args(
            filter_term=filter_term,
            fields=fields,
            limit=limit,
            offset=offset,
        )
        return await self._agroups_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def groups(
        self,
        filter_term: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._groups_mapped_args(
            filter_term=filter_term,
            fields=fields,
            limit=limit,
            offset=offset,
        )
        return self._groups_oapg(
            query_params=args.query,
        )

class Groups(BaseApi):

    async def agroups(
        self,
        filter_term: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> GroupsPydantic:
        raw_response = await self.raw.agroups(
            filter_term=filter_term,
            fields=fields,
            limit=limit,
            offset=offset,
            **kwargs,
        )
        if validate:
            return RootModel[GroupsPydantic](raw_response.body).root
        return api_client.construct_model_instance(GroupsPydantic, raw_response.body)
    
    
    def groups(
        self,
        filter_term: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        validate: bool = False,
    ) -> GroupsPydantic:
        raw_response = self.raw.groups(
            filter_term=filter_term,
            fields=fields,
            limit=limit,
            offset=offset,
        )
        if validate:
            return RootModel[GroupsPydantic](raw_response.body).root
        return api_client.construct_model_instance(GroupsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        filter_term: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._groups_mapped_args(
            filter_term=filter_term,
            fields=fields,
            limit=limit,
            offset=offset,
        )
        return await self._agroups_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        filter_term: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._groups_mapped_args(
            filter_term=filter_term,
            fields=fields,
            limit=limit,
            offset=offset,
        )
        return self._groups_oapg(
            query_params=args.query,
        )

