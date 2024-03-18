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
from box_python_sdk.model.group_full import GroupFull as GroupFullSchema
from box_python_sdk.model.post_groups_request import PostGroupsRequest as PostGroupsRequestSchema

from box_python_sdk.type.group_full import GroupFull
from box_python_sdk.type.post_groups_request import PostGroupsRequest
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.group_full import GroupFull as GroupFullPydantic
from box_python_sdk.pydantic.post_groups_request import PostGroupsRequest as PostGroupsRequestPydantic

from . import path

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
# body param
SchemaForRequestBodyApplicationJson = PostGroupsRequestSchema


request_body_post_groups_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'OAuth2Security',
]
SchemaFor201ResponseBodyApplicationJson = GroupFullSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: GroupFull


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: GroupFull


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
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
    '201': _response_for_201,
    '409': _response_for_409,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _groups_0_mapped_args(
        self,
        name: str,
        description: typing.Optional[str] = None,
        provenance: typing.Optional[str] = None,
        external_sync_identifier: typing.Optional[str] = None,
        invitability_level: typing.Optional[str] = None,
        member_viewability_level: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if provenance is not None:
            _body["provenance"] = provenance
        if external_sync_identifier is not None:
            _body["external_sync_identifier"] = external_sync_identifier
        if invitability_level is not None:
            _body["invitability_level"] = invitability_level
        if member_viewability_level is not None:
            _body["member_viewability_level"] = member_viewability_level
        args.body = _body
        if fields is not None:
            _query_params["fields"] = fields
        args.query = _query_params
        return args

    async def _agroups_0_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create group
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
            path_template='/groups',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_post_groups_request.serialize(body, content_type)
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


    def _groups_0_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create group
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
            path_template='/groups',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_post_groups_request.serialize(body, content_type)
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


class Groups0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agroups_0(
        self,
        name: str,
        description: typing.Optional[str] = None,
        provenance: typing.Optional[str] = None,
        external_sync_identifier: typing.Optional[str] = None,
        invitability_level: typing.Optional[str] = None,
        member_viewability_level: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._groups_0_mapped_args(
            name=name,
            description=description,
            provenance=provenance,
            external_sync_identifier=external_sync_identifier,
            invitability_level=invitability_level,
            member_viewability_level=member_viewability_level,
            fields=fields,
        )
        return await self._agroups_0_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def groups_0(
        self,
        name: str,
        description: typing.Optional[str] = None,
        provenance: typing.Optional[str] = None,
        external_sync_identifier: typing.Optional[str] = None,
        invitability_level: typing.Optional[str] = None,
        member_viewability_level: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._groups_0_mapped_args(
            name=name,
            description=description,
            provenance=provenance,
            external_sync_identifier=external_sync_identifier,
            invitability_level=invitability_level,
            member_viewability_level=member_viewability_level,
            fields=fields,
        )
        return self._groups_0_oapg(
            body=args.body,
            query_params=args.query,
        )

class Groups0(BaseApi):

    async def agroups_0(
        self,
        name: str,
        description: typing.Optional[str] = None,
        provenance: typing.Optional[str] = None,
        external_sync_identifier: typing.Optional[str] = None,
        invitability_level: typing.Optional[str] = None,
        member_viewability_level: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> GroupFullPydantic:
        raw_response = await self.raw.agroups_0(
            name=name,
            description=description,
            provenance=provenance,
            external_sync_identifier=external_sync_identifier,
            invitability_level=invitability_level,
            member_viewability_level=member_viewability_level,
            fields=fields,
            **kwargs,
        )
        if validate:
            return RootModel[GroupFullPydantic](raw_response.body).root
        return api_client.construct_model_instance(GroupFullPydantic, raw_response.body)
    
    
    def groups_0(
        self,
        name: str,
        description: typing.Optional[str] = None,
        provenance: typing.Optional[str] = None,
        external_sync_identifier: typing.Optional[str] = None,
        invitability_level: typing.Optional[str] = None,
        member_viewability_level: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> GroupFullPydantic:
        raw_response = self.raw.groups_0(
            name=name,
            description=description,
            provenance=provenance,
            external_sync_identifier=external_sync_identifier,
            invitability_level=invitability_level,
            member_viewability_level=member_viewability_level,
            fields=fields,
        )
        if validate:
            return RootModel[GroupFullPydantic](raw_response.body).root
        return api_client.construct_model_instance(GroupFullPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        description: typing.Optional[str] = None,
        provenance: typing.Optional[str] = None,
        external_sync_identifier: typing.Optional[str] = None,
        invitability_level: typing.Optional[str] = None,
        member_viewability_level: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._groups_0_mapped_args(
            name=name,
            description=description,
            provenance=provenance,
            external_sync_identifier=external_sync_identifier,
            invitability_level=invitability_level,
            member_viewability_level=member_viewability_level,
            fields=fields,
        )
        return await self._agroups_0_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        description: typing.Optional[str] = None,
        provenance: typing.Optional[str] = None,
        external_sync_identifier: typing.Optional[str] = None,
        invitability_level: typing.Optional[str] = None,
        member_viewability_level: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._groups_0_mapped_args(
            name=name,
            description=description,
            provenance=provenance,
            external_sync_identifier=external_sync_identifier,
            invitability_level=invitability_level,
            member_viewability_level=member_viewability_level,
            fields=fields,
        )
        return self._groups_0_oapg(
            body=args.body,
            query_params=args.query,
        )

