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

from box_python_sdk.model.o_auth2_error import OAuth2Error as OAuth2ErrorSchema
from box_python_sdk.model.post_o_auth2_token_refresh_access_token import PostOAuth2TokenRefreshAccessToken as PostOAuth2TokenRefreshAccessTokenSchema
from box_python_sdk.model.access_token import AccessToken as AccessTokenSchema

from box_python_sdk.type.o_auth2_error import OAuth2Error
from box_python_sdk.type.post_o_auth2_token_refresh_access_token import PostOAuth2TokenRefreshAccessToken
from box_python_sdk.type.access_token import AccessToken

from ...api_client import Dictionary
from box_python_sdk.pydantic.o_auth2_error import OAuth2Error as OAuth2ErrorPydantic
from box_python_sdk.pydantic.post_o_auth2_token_refresh_access_token import PostOAuth2TokenRefreshAccessToken as PostOAuth2TokenRefreshAccessTokenPydantic
from box_python_sdk.pydantic.access_token import AccessToken as AccessTokenPydantic

from . import path

# body param
SchemaForRequestBodyApplicationXWwwFormUrlencoded = PostOAuth2TokenRefreshAccessTokenSchema


request_body_post_o_auth2_token_refresh_access_token = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
)
_servers = (
    {
        'url': "https://api.box.com",
        'description': "Server for server-side authentication",
    },
)
SchemaFor200ResponseBodyApplicationJson = AccessTokenSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AccessToken


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AccessToken


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = OAuth2ErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: OAuth2Error


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: OAuth2Error


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = OAuth2ErrorSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: OAuth2Error


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: OAuth2Error


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _refresh_access_token_mapped_args(
        self,
        grant_type: str,
        client_id: str,
        client_secret: str,
        refresh_token: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if grant_type is not None:
            _body["grant_type"] = grant_type
        if client_id is not None:
            _body["client_id"] = client_id
        if client_secret is not None:
            _body["client_secret"] = client_secret
        if refresh_token is not None:
            _body["refresh_token"] = refresh_token
        args.body = _body
        return args

    async def _arefresh_access_token_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Refresh access token
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
            path_template='/oauth2/token#refresh',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_post_o_auth2_token_refresh_access_token.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        host = self._get_host_oapg('refresh_access_token', _servers, host_index)
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _refresh_access_token_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Refresh access token
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
            path_template='/oauth2/token#refresh',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_post_o_auth2_token_refresh_access_token.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        host = self._get_host_oapg('refresh_access_token', _servers, host_index)
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class RefreshAccessTokenRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def arefresh_access_token(
        self,
        grant_type: str,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._refresh_access_token_mapped_args(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )
        return await self._arefresh_access_token_oapg(
            body=args.body,
            **kwargs,
        )
    
    def refresh_access_token(
        self,
        grant_type: str,
        client_id: str,
        client_secret: str,
        refresh_token: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._refresh_access_token_mapped_args(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )
        return self._refresh_access_token_oapg(
            body=args.body,
        )

class RefreshAccessToken(BaseApi):

    async def arefresh_access_token(
        self,
        grant_type: str,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        validate: bool = False,
        **kwargs,
    ) -> AccessTokenPydantic:
        raw_response = await self.raw.arefresh_access_token(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
            **kwargs,
        )
        if validate:
            return AccessTokenPydantic(**raw_response.body)
        return api_client.construct_model_instance(AccessTokenPydantic, raw_response.body)
    
    
    def refresh_access_token(
        self,
        grant_type: str,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        validate: bool = False,
    ) -> AccessTokenPydantic:
        raw_response = self.raw.refresh_access_token(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )
        if validate:
            return AccessTokenPydantic(**raw_response.body)
        return api_client.construct_model_instance(AccessTokenPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        grant_type: str,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._refresh_access_token_mapped_args(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )
        return await self._arefresh_access_token_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        grant_type: str,
        client_id: str,
        client_secret: str,
        refresh_token: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._refresh_access_token_mapped_args(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )
        return self._refresh_access_token_oapg(
            body=args.body,
        )

