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
from box_python_sdk.model.integration_mapping_partner_item_slack import IntegrationMappingPartnerItemSlack as IntegrationMappingPartnerItemSlackSchema
from box_python_sdk.model.integration_mapping_slack_create_request import IntegrationMappingSlackCreateRequest as IntegrationMappingSlackCreateRequestSchema
from box_python_sdk.model.integration_mapping_box_item_slack import IntegrationMappingBoxItemSlack as IntegrationMappingBoxItemSlackSchema
from box_python_sdk.model.integration_mapping_slack_options import IntegrationMappingSlackOptions as IntegrationMappingSlackOptionsSchema
from box_python_sdk.model.integration_mapping import IntegrationMapping as IntegrationMappingSchema

from box_python_sdk.type.integration_mapping_box_item_slack import IntegrationMappingBoxItemSlack
from box_python_sdk.type.integration_mapping import IntegrationMapping
from box_python_sdk.type.integration_mapping_partner_item_slack import IntegrationMappingPartnerItemSlack
from box_python_sdk.type.integration_mapping_slack_options import IntegrationMappingSlackOptions
from box_python_sdk.type.client_error import ClientError
from box_python_sdk.type.integration_mapping_slack_create_request import IntegrationMappingSlackCreateRequest

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.integration_mapping import IntegrationMapping as IntegrationMappingPydantic
from box_python_sdk.pydantic.integration_mapping_partner_item_slack import IntegrationMappingPartnerItemSlack as IntegrationMappingPartnerItemSlackPydantic
from box_python_sdk.pydantic.integration_mapping_slack_options import IntegrationMappingSlackOptions as IntegrationMappingSlackOptionsPydantic
from box_python_sdk.pydantic.integration_mapping_box_item_slack import IntegrationMappingBoxItemSlack as IntegrationMappingBoxItemSlackPydantic
from box_python_sdk.pydantic.integration_mapping_slack_create_request import IntegrationMappingSlackCreateRequest as IntegrationMappingSlackCreateRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = IntegrationMappingSlackCreateRequestSchema


request_body_integration_mapping_slack_create_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'OAuth2Security',
]
SchemaFor201ResponseBodyApplicationJson = IntegrationMappingSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: IntegrationMapping


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: IntegrationMapping


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '404': _response_for_404,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_slack_mapping_mapped_args(
        self,
        partner_item: IntegrationMappingPartnerItemSlack,
        box_item: IntegrationMappingBoxItemSlack,
        options: typing.Optional[IntegrationMappingSlackOptions] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if partner_item is not None:
            _body["partner_item"] = partner_item
        if box_item is not None:
            _body["box_item"] = box_item
        if options is not None:
            _body["options"] = options
        args.body = _body
        return args

    async def _acreate_slack_mapping_oapg(
        self,
        body: typing.Any = None,
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
        Create Slack integration mapping
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
            path_template='/integration_mappings/slack',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_integration_mapping_slack_create_request.serialize(body, content_type)
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


    def _create_slack_mapping_oapg(
        self,
        body: typing.Any = None,
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
        Create Slack integration mapping
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
            path_template='/integration_mappings/slack',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_integration_mapping_slack_create_request.serialize(body, content_type)
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


class CreateSlackMappingRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_slack_mapping(
        self,
        partner_item: IntegrationMappingPartnerItemSlack,
        box_item: IntegrationMappingBoxItemSlack,
        options: typing.Optional[IntegrationMappingSlackOptions] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_slack_mapping_mapped_args(
            partner_item=partner_item,
            box_item=box_item,
            options=options,
        )
        return await self._acreate_slack_mapping_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_slack_mapping(
        self,
        partner_item: IntegrationMappingPartnerItemSlack,
        box_item: IntegrationMappingBoxItemSlack,
        options: typing.Optional[IntegrationMappingSlackOptions] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_slack_mapping_mapped_args(
            partner_item=partner_item,
            box_item=box_item,
            options=options,
        )
        return self._create_slack_mapping_oapg(
            body=args.body,
        )

class CreateSlackMapping(BaseApi):

    async def acreate_slack_mapping(
        self,
        partner_item: IntegrationMappingPartnerItemSlack,
        box_item: IntegrationMappingBoxItemSlack,
        options: typing.Optional[IntegrationMappingSlackOptions] = None,
        validate: bool = False,
        **kwargs,
    ) -> IntegrationMappingPydantic:
        raw_response = await self.raw.acreate_slack_mapping(
            partner_item=partner_item,
            box_item=box_item,
            options=options,
            **kwargs,
        )
        if validate:
            return RootModel[IntegrationMappingPydantic](raw_response.body).root
        return api_client.construct_model_instance(IntegrationMappingPydantic, raw_response.body)
    
    
    def create_slack_mapping(
        self,
        partner_item: IntegrationMappingPartnerItemSlack,
        box_item: IntegrationMappingBoxItemSlack,
        options: typing.Optional[IntegrationMappingSlackOptions] = None,
        validate: bool = False,
    ) -> IntegrationMappingPydantic:
        raw_response = self.raw.create_slack_mapping(
            partner_item=partner_item,
            box_item=box_item,
            options=options,
        )
        if validate:
            return RootModel[IntegrationMappingPydantic](raw_response.body).root
        return api_client.construct_model_instance(IntegrationMappingPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        partner_item: IntegrationMappingPartnerItemSlack,
        box_item: IntegrationMappingBoxItemSlack,
        options: typing.Optional[IntegrationMappingSlackOptions] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_slack_mapping_mapped_args(
            partner_item=partner_item,
            box_item=box_item,
            options=options,
        )
        return await self._acreate_slack_mapping_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        partner_item: IntegrationMappingPartnerItemSlack,
        box_item: IntegrationMappingBoxItemSlack,
        options: typing.Optional[IntegrationMappingSlackOptions] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_slack_mapping_mapped_args(
            partner_item=partner_item,
            box_item=box_item,
            options=options,
        )
        return self._create_slack_mapping_oapg(
            body=args.body,
        )

