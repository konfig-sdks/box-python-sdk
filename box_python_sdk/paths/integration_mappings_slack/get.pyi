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
from box_python_sdk.model.integration_mappings import IntegrationMappings as IntegrationMappingsSchema

from box_python_sdk.type.integration_mappings import IntegrationMappings
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.integration_mappings import IntegrationMappings as IntegrationMappingsPydantic

# Query params
MarkerSchema = schemas.StrSchema


class LimitSchema(
    schemas.Int64Schema
):
    pass


class PartnerItemTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CHANNEL(cls):
        return cls("channel")
PartnerItemIdSchema = schemas.StrSchema
BoxItemIdSchema = schemas.StrSchema


class BoxItemTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def FOLDER(cls):
        return cls("folder")
IsManuallyCreatedSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'marker': typing.Union[MarkerSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'partner_item_type': typing.Union[PartnerItemTypeSchema, str, ],
        'partner_item_id': typing.Union[PartnerItemIdSchema, str, ],
        'box_item_id': typing.Union[BoxItemIdSchema, str, ],
        'box_item_type': typing.Union[BoxItemTypeSchema, str, ],
        'is_manually_created': typing.Union[IsManuallyCreatedSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_marker = api_client.QueryParameter(
    name="marker",
    style=api_client.ParameterStyle.FORM,
    schema=MarkerSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_partner_item_type = api_client.QueryParameter(
    name="partner_item_type",
    style=api_client.ParameterStyle.FORM,
    schema=PartnerItemTypeSchema,
    explode=True,
)
request_query_partner_item_id = api_client.QueryParameter(
    name="partner_item_id",
    style=api_client.ParameterStyle.FORM,
    schema=PartnerItemIdSchema,
    explode=True,
)
request_query_box_item_id = api_client.QueryParameter(
    name="box_item_id",
    style=api_client.ParameterStyle.FORM,
    schema=BoxItemIdSchema,
    explode=True,
)
request_query_box_item_type = api_client.QueryParameter(
    name="box_item_type",
    style=api_client.ParameterStyle.FORM,
    schema=BoxItemTypeSchema,
    explode=True,
)
request_query_is_manually_created = api_client.QueryParameter(
    name="is_manually_created",
    style=api_client.ParameterStyle.FORM,
    schema=IsManuallyCreatedSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = IntegrationMappingsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: IntegrationMappings


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: IntegrationMappings


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
SchemaFor404ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
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

    def _list_slack_mappings_mapped_args(
        self,
        marker: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        partner_item_type: typing.Optional[str] = None,
        partner_item_id: typing.Optional[str] = None,
        box_item_id: typing.Optional[str] = None,
        box_item_type: typing.Optional[str] = None,
        is_manually_created: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if marker is not None:
            _query_params["marker"] = marker
        if limit is not None:
            _query_params["limit"] = limit
        if partner_item_type is not None:
            _query_params["partner_item_type"] = partner_item_type
        if partner_item_id is not None:
            _query_params["partner_item_id"] = partner_item_id
        if box_item_id is not None:
            _query_params["box_item_id"] = box_item_id
        if box_item_type is not None:
            _query_params["box_item_type"] = box_item_type
        if is_manually_created is not None:
            _query_params["is_manually_created"] = is_manually_created
        args.query = _query_params
        return args

    async def _alist_slack_mappings_oapg(
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
        List Slack integration mappings
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_marker,
            request_query_limit,
            request_query_partner_item_type,
            request_query_partner_item_id,
            request_query_box_item_id,
            request_query_box_item_type,
            request_query_is_manually_created,
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
            path_template='/integration_mappings/slack',
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


    def _list_slack_mappings_oapg(
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
        List Slack integration mappings
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_marker,
            request_query_limit,
            request_query_partner_item_type,
            request_query_partner_item_id,
            request_query_box_item_id,
            request_query_box_item_type,
            request_query_is_manually_created,
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
            path_template='/integration_mappings/slack',
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


class ListSlackMappingsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_slack_mappings(
        self,
        marker: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        partner_item_type: typing.Optional[str] = None,
        partner_item_id: typing.Optional[str] = None,
        box_item_id: typing.Optional[str] = None,
        box_item_type: typing.Optional[str] = None,
        is_manually_created: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_slack_mappings_mapped_args(
            marker=marker,
            limit=limit,
            partner_item_type=partner_item_type,
            partner_item_id=partner_item_id,
            box_item_id=box_item_id,
            box_item_type=box_item_type,
            is_manually_created=is_manually_created,
        )
        return await self._alist_slack_mappings_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_slack_mappings(
        self,
        marker: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        partner_item_type: typing.Optional[str] = None,
        partner_item_id: typing.Optional[str] = None,
        box_item_id: typing.Optional[str] = None,
        box_item_type: typing.Optional[str] = None,
        is_manually_created: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_slack_mappings_mapped_args(
            marker=marker,
            limit=limit,
            partner_item_type=partner_item_type,
            partner_item_id=partner_item_id,
            box_item_id=box_item_id,
            box_item_type=box_item_type,
            is_manually_created=is_manually_created,
        )
        return self._list_slack_mappings_oapg(
            query_params=args.query,
        )

class ListSlackMappings(BaseApi):

    async def alist_slack_mappings(
        self,
        marker: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        partner_item_type: typing.Optional[str] = None,
        partner_item_id: typing.Optional[str] = None,
        box_item_id: typing.Optional[str] = None,
        box_item_type: typing.Optional[str] = None,
        is_manually_created: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> IntegrationMappingsPydantic:
        raw_response = await self.raw.alist_slack_mappings(
            marker=marker,
            limit=limit,
            partner_item_type=partner_item_type,
            partner_item_id=partner_item_id,
            box_item_id=box_item_id,
            box_item_type=box_item_type,
            is_manually_created=is_manually_created,
            **kwargs,
        )
        if validate:
            return RootModel[IntegrationMappingsPydantic](raw_response.body).root
        return api_client.construct_model_instance(IntegrationMappingsPydantic, raw_response.body)
    
    
    def list_slack_mappings(
        self,
        marker: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        partner_item_type: typing.Optional[str] = None,
        partner_item_id: typing.Optional[str] = None,
        box_item_id: typing.Optional[str] = None,
        box_item_type: typing.Optional[str] = None,
        is_manually_created: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> IntegrationMappingsPydantic:
        raw_response = self.raw.list_slack_mappings(
            marker=marker,
            limit=limit,
            partner_item_type=partner_item_type,
            partner_item_id=partner_item_id,
            box_item_id=box_item_id,
            box_item_type=box_item_type,
            is_manually_created=is_manually_created,
        )
        if validate:
            return RootModel[IntegrationMappingsPydantic](raw_response.body).root
        return api_client.construct_model_instance(IntegrationMappingsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        marker: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        partner_item_type: typing.Optional[str] = None,
        partner_item_id: typing.Optional[str] = None,
        box_item_id: typing.Optional[str] = None,
        box_item_type: typing.Optional[str] = None,
        is_manually_created: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_slack_mappings_mapped_args(
            marker=marker,
            limit=limit,
            partner_item_type=partner_item_type,
            partner_item_id=partner_item_id,
            box_item_id=box_item_id,
            box_item_type=box_item_type,
            is_manually_created=is_manually_created,
        )
        return await self._alist_slack_mappings_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        marker: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        partner_item_type: typing.Optional[str] = None,
        partner_item_id: typing.Optional[str] = None,
        box_item_id: typing.Optional[str] = None,
        box_item_type: typing.Optional[str] = None,
        is_manually_created: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_slack_mappings_mapped_args(
            marker=marker,
            limit=limit,
            partner_item_type=partner_item_type,
            partner_item_id=partner_item_id,
            box_item_id=box_item_id,
            box_item_type=box_item_type,
            is_manually_created=is_manually_created,
        )
        return self._list_slack_mappings_oapg(
            query_params=args.query,
        )

