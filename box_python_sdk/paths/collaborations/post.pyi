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
from box_python_sdk.model.post_collaborations_request_item import PostCollaborationsRequestItem as PostCollaborationsRequestItemSchema
from box_python_sdk.model.collaboration import Collaboration as CollaborationSchema
from box_python_sdk.model.post_collaborations_request_accessible_by import PostCollaborationsRequestAccessibleBy as PostCollaborationsRequestAccessibleBySchema
from box_python_sdk.model.post_collaborations_request import PostCollaborationsRequest as PostCollaborationsRequestSchema

from box_python_sdk.type.post_collaborations_request import PostCollaborationsRequest
from box_python_sdk.type.post_collaborations_request_accessible_by import PostCollaborationsRequestAccessibleBy
from box_python_sdk.type.collaboration import Collaboration
from box_python_sdk.type.post_collaborations_request_item import PostCollaborationsRequestItem
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.post_collaborations_request_item import PostCollaborationsRequestItem as PostCollaborationsRequestItemPydantic
from box_python_sdk.pydantic.post_collaborations_request_accessible_by import PostCollaborationsRequestAccessibleBy as PostCollaborationsRequestAccessibleByPydantic
from box_python_sdk.pydantic.collaboration import Collaboration as CollaborationPydantic
from box_python_sdk.pydantic.post_collaborations_request import PostCollaborationsRequest as PostCollaborationsRequestPydantic

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
NotifySchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'fields': typing.Union[FieldsSchema, list, tuple, ],
        'notify': typing.Union[NotifySchema, bool, ],
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
request_query_notify = api_client.QueryParameter(
    name="notify",
    style=api_client.ParameterStyle.FORM,
    schema=NotifySchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = PostCollaborationsRequestSchema


request_body_post_collaborations_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = CollaborationSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Collaboration


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Collaboration


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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

    def _collaborations_mapped_args(
        self,
        item: PostCollaborationsRequestItem,
        accessible_by: PostCollaborationsRequestAccessibleBy,
        role: str,
        is_access_only: typing.Optional[bool] = None,
        can_view_path: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        fields: typing.Optional[typing.List[str]] = None,
        notify: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if item is not None:
            _body["item"] = item
        if accessible_by is not None:
            _body["accessible_by"] = accessible_by
        if role is not None:
            _body["role"] = role
        if is_access_only is not None:
            _body["is_access_only"] = is_access_only
        if can_view_path is not None:
            _body["can_view_path"] = can_view_path
        if expires_at is not None:
            _body["expires_at"] = expires_at
        args.body = _body
        if fields is not None:
            _query_params["fields"] = fields
        if notify is not None:
            _query_params["notify"] = notify
        args.query = _query_params
        return args

    async def _acollaborations_oapg(
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
        Create collaboration
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_fields,
            request_query_notify,
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
            path_template='/collaborations',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_post_collaborations_request.serialize(body, content_type)
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


    def _collaborations_oapg(
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
        Create collaboration
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_fields,
            request_query_notify,
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
            path_template='/collaborations',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_post_collaborations_request.serialize(body, content_type)
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


class CollaborationsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acollaborations(
        self,
        item: PostCollaborationsRequestItem,
        accessible_by: PostCollaborationsRequestAccessibleBy,
        role: str,
        is_access_only: typing.Optional[bool] = None,
        can_view_path: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        fields: typing.Optional[typing.List[str]] = None,
        notify: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._collaborations_mapped_args(
            item=item,
            accessible_by=accessible_by,
            role=role,
            is_access_only=is_access_only,
            can_view_path=can_view_path,
            expires_at=expires_at,
            fields=fields,
            notify=notify,
        )
        return await self._acollaborations_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def collaborations(
        self,
        item: PostCollaborationsRequestItem,
        accessible_by: PostCollaborationsRequestAccessibleBy,
        role: str,
        is_access_only: typing.Optional[bool] = None,
        can_view_path: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        fields: typing.Optional[typing.List[str]] = None,
        notify: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._collaborations_mapped_args(
            item=item,
            accessible_by=accessible_by,
            role=role,
            is_access_only=is_access_only,
            can_view_path=can_view_path,
            expires_at=expires_at,
            fields=fields,
            notify=notify,
        )
        return self._collaborations_oapg(
            body=args.body,
            query_params=args.query,
        )

class Collaborations(BaseApi):

    async def acollaborations(
        self,
        item: PostCollaborationsRequestItem,
        accessible_by: PostCollaborationsRequestAccessibleBy,
        role: str,
        is_access_only: typing.Optional[bool] = None,
        can_view_path: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        fields: typing.Optional[typing.List[str]] = None,
        notify: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> CollaborationPydantic:
        raw_response = await self.raw.acollaborations(
            item=item,
            accessible_by=accessible_by,
            role=role,
            is_access_only=is_access_only,
            can_view_path=can_view_path,
            expires_at=expires_at,
            fields=fields,
            notify=notify,
            **kwargs,
        )
        if validate:
            return CollaborationPydantic(**raw_response.body)
        return api_client.construct_model_instance(CollaborationPydantic, raw_response.body)
    
    
    def collaborations(
        self,
        item: PostCollaborationsRequestItem,
        accessible_by: PostCollaborationsRequestAccessibleBy,
        role: str,
        is_access_only: typing.Optional[bool] = None,
        can_view_path: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        fields: typing.Optional[typing.List[str]] = None,
        notify: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> CollaborationPydantic:
        raw_response = self.raw.collaborations(
            item=item,
            accessible_by=accessible_by,
            role=role,
            is_access_only=is_access_only,
            can_view_path=can_view_path,
            expires_at=expires_at,
            fields=fields,
            notify=notify,
        )
        if validate:
            return CollaborationPydantic(**raw_response.body)
        return api_client.construct_model_instance(CollaborationPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        item: PostCollaborationsRequestItem,
        accessible_by: PostCollaborationsRequestAccessibleBy,
        role: str,
        is_access_only: typing.Optional[bool] = None,
        can_view_path: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        fields: typing.Optional[typing.List[str]] = None,
        notify: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._collaborations_mapped_args(
            item=item,
            accessible_by=accessible_by,
            role=role,
            is_access_only=is_access_only,
            can_view_path=can_view_path,
            expires_at=expires_at,
            fields=fields,
            notify=notify,
        )
        return await self._acollaborations_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        item: PostCollaborationsRequestItem,
        accessible_by: PostCollaborationsRequestAccessibleBy,
        role: str,
        is_access_only: typing.Optional[bool] = None,
        can_view_path: typing.Optional[bool] = None,
        expires_at: typing.Optional[datetime] = None,
        fields: typing.Optional[typing.List[str]] = None,
        notify: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._collaborations_mapped_args(
            item=item,
            accessible_by=accessible_by,
            role=role,
            is_access_only=is_access_only,
            can_view_path=can_view_path,
            expires_at=expires_at,
            fields=fields,
            notify=notify,
        )
        return self._collaborations_oapg(
            body=args.body,
            query_params=args.query,
        )

