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



from ...api_client import Dictionary

from . import path

# Query params


class ResponseTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        format = 'token'
        enum_value_to_name = {
            "code": "CODE",
        }
    
    @schemas.classproperty
    def CODE(cls):
        return cls("code")
ClientIdSchema = schemas.StrSchema
RedirectUriSchema = schemas.StrSchema
StateSchema = schemas.StrSchema
ScopeSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'response_type': typing.Union[ResponseTypeSchema, str, ],
        'client_id': typing.Union[ClientIdSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'redirect_uri': typing.Union[RedirectUriSchema, str, ],
        'state': typing.Union[StateSchema, str, ],
        'scope': typing.Union[ScopeSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_response_type = api_client.QueryParameter(
    name="response_type",
    style=api_client.ParameterStyle.FORM,
    schema=ResponseTypeSchema,
    required=True,
    explode=True,
)
request_query_client_id = api_client.QueryParameter(
    name="client_id",
    style=api_client.ParameterStyle.FORM,
    schema=ClientIdSchema,
    required=True,
    explode=True,
)
request_query_redirect_uri = api_client.QueryParameter(
    name="redirect_uri",
    style=api_client.ParameterStyle.FORM,
    schema=RedirectUriSchema,
    explode=True,
)
request_query_state = api_client.QueryParameter(
    name="state",
    style=api_client.ParameterStyle.FORM,
    schema=StateSchema,
    explode=True,
)
request_query_scope = api_client.QueryParameter(
    name="scope",
    style=api_client.ParameterStyle.FORM,
    schema=ScopeSchema,
    explode=True,
)
_servers = (
    {
        'url': "https://account.box.com/api/oauth2",
        'description': "Server for client-side authentication",
    },
)
SchemaFor200ResponseBodyTextHtml = schemas.StrSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: str


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'text/html': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextHtml),
    },
)
SchemaFor0ResponseBodyTextHtml = schemas.StrSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: str


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'text/html': api_client.MediaType(
            schema=SchemaFor0ResponseBodyTextHtml),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'text/html',
)


class BaseApi(api_client.Api):

    def _authorize_mapped_args(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if response_type is not None:
            _query_params["response_type"] = response_type
        if client_id is not None:
            _query_params["client_id"] = client_id
        if redirect_uri is not None:
            _query_params["redirect_uri"] = redirect_uri
        if state is not None:
            _query_params["state"] = state
        if scope is not None:
            _query_params["scope"] = scope
        args.query = _query_params
        return args

    async def _aauthorize_oapg(
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
        Authorize user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_response_type,
            request_query_client_id,
            request_query_redirect_uri,
            request_query_state,
            request_query_scope,
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
            path_template='/authorize',
            headers=_headers,
        )
    
        host = self._get_host_oapg('authorize', _servers, host_index)
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            host=host,
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


    def _authorize_oapg(
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
        Authorize user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_response_type,
            request_query_client_id,
            request_query_redirect_uri,
            request_query_state,
            request_query_scope,
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
            path_template='/authorize',
            headers=_headers,
        )
    
        host = self._get_host_oapg('authorize', _servers, host_index)
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            host=host,
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


class AuthorizeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aauthorize(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._authorize_mapped_args(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            state=state,
            scope=scope,
        )
        return await self._aauthorize_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def authorize(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._authorize_mapped_args(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            state=state,
            scope=scope,
        )
        return self._authorize_oapg(
            query_params=args.query,
        )

class Authorize(BaseApi):

    async def aauthorize(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> str:
        raw_response = await self.raw.aauthorize(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            state=state,
            scope=scope,
            **kwargs,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body
    
    
    def authorize(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        validate: bool = False,
    ) -> str:
        raw_response = self.raw.authorize(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            state=state,
            scope=scope,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._authorize_mapped_args(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            state=state,
            scope=scope,
        )
        return await self._aauthorize_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        response_type: str,
        client_id: str,
        redirect_uri: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._authorize_mapped_args(
            response_type=response_type,
            client_id=client_id,
            redirect_uri=redirect_uri,
            state=state,
            scope=scope,
        )
        return self._authorize_oapg(
            query_params=args.query,
        )

