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

from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic

from . import path

# Path params
CollaborationWhitelistEntryIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'collaboration_whitelist_entry_id': typing.Union[CollaborationWhitelistEntryIdSchema, str, ],
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


request_path_collaboration_whitelist_entry_id = api_client.PathParameter(
    name="collaboration_whitelist_entry_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CollaborationWhitelistEntryIdSchema,
    required=True,
)
_auth = [
    'OAuth2Security',
]


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
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
    '204': _response_for_204,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _remove_allowed_domain_entry_mapped_args(
        self,
        collaboration_whitelist_entry_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if collaboration_whitelist_entry_id is not None:
            _path_params["collaboration_whitelist_entry_id"] = collaboration_whitelist_entry_id
        args.path = _path_params
        return args

    async def _aremove_allowed_domain_entry_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Remove domain from list of allowed collaboration domains
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_collaboration_whitelist_entry_id,
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
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _remove_allowed_domain_entry_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Remove domain from list of allowed collaboration domains
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_collaboration_whitelist_entry_id,
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
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class RemoveAllowedDomainEntryRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aremove_allowed_domain_entry(
        self,
        collaboration_whitelist_entry_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_allowed_domain_entry_mapped_args(
            collaboration_whitelist_entry_id=collaboration_whitelist_entry_id,
        )
        return await self._aremove_allowed_domain_entry_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def remove_allowed_domain_entry(
        self,
        collaboration_whitelist_entry_id: str,
    ) -> typing.Union[
        ApiResponseFor204,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_allowed_domain_entry_mapped_args(
            collaboration_whitelist_entry_id=collaboration_whitelist_entry_id,
        )
        return self._remove_allowed_domain_entry_oapg(
            path_params=args.path,
        )

class RemoveAllowedDomainEntry(BaseApi):

    async def aremove_allowed_domain_entry(
        self,
        collaboration_whitelist_entry_id: str,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aremove_allowed_domain_entry(
            collaboration_whitelist_entry_id=collaboration_whitelist_entry_id,
            **kwargs,
        )
    
    
    def remove_allowed_domain_entry(
        self,
        collaboration_whitelist_entry_id: str,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.remove_allowed_domain_entry(
            collaboration_whitelist_entry_id=collaboration_whitelist_entry_id,
        )


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        collaboration_whitelist_entry_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_allowed_domain_entry_mapped_args(
            collaboration_whitelist_entry_id=collaboration_whitelist_entry_id,
        )
        return await self._aremove_allowed_domain_entry_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        collaboration_whitelist_entry_id: str,
    ) -> typing.Union[
        ApiResponseFor204,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_allowed_domain_entry_mapped_args(
            collaboration_whitelist_entry_id=collaboration_whitelist_entry_id,
        )
        return self._remove_allowed_domain_entry_oapg(
            path_params=args.path,
        )

