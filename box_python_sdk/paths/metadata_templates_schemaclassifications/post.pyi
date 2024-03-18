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
from box_python_sdk.model.classifications_initialize_template_request import ClassificationsInitializeTemplateRequest as ClassificationsInitializeTemplateRequestSchema
from box_python_sdk.model.classification_template import ClassificationTemplate as ClassificationTemplateSchema
from box_python_sdk.model.classifications_initialize_template_request_fields import ClassificationsInitializeTemplateRequestFields as ClassificationsInitializeTemplateRequestFieldsSchema

from box_python_sdk.type.classifications_initialize_template_request import ClassificationsInitializeTemplateRequest
from box_python_sdk.type.classifications_initialize_template_request_fields import ClassificationsInitializeTemplateRequestFields
from box_python_sdk.type.classification_template import ClassificationTemplate
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.classification_template import ClassificationTemplate as ClassificationTemplatePydantic
from box_python_sdk.pydantic.classifications_initialize_template_request_fields import ClassificationsInitializeTemplateRequestFields as ClassificationsInitializeTemplateRequestFieldsPydantic
from box_python_sdk.pydantic.classifications_initialize_template_request import ClassificationsInitializeTemplateRequest as ClassificationsInitializeTemplateRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = ClassificationsInitializeTemplateRequestSchema


request_body_classifications_initialize_template_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = ClassificationTemplateSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ClassificationTemplate


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ClassificationTemplate


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

    def _initialize_template_mapped_args(
        self,
        scope: str,
        template_key: str,
        display_name: str,
        fields: ClassificationsInitializeTemplateRequestFields,
        hidden: typing.Optional[bool] = None,
        copy_instance_on_item_copy: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if scope is not None:
            _body["scope"] = scope
        if template_key is not None:
            _body["templateKey"] = template_key
        if display_name is not None:
            _body["displayName"] = display_name
        if hidden is not None:
            _body["hidden"] = hidden
        if copy_instance_on_item_copy is not None:
            _body["copyInstanceOnItemCopy"] = copy_instance_on_item_copy
        if fields is not None:
            _body["fields"] = fields
        args.body = _body
        return args

    async def _ainitialize_template_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Add initial classifications
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
            path_template='/metadata_templates/schema#classifications',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_classifications_initialize_template_request.serialize(body, content_type)
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


    def _initialize_template_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Add initial classifications
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
            path_template='/metadata_templates/schema#classifications',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_classifications_initialize_template_request.serialize(body, content_type)
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


class InitializeTemplateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def ainitialize_template(
        self,
        scope: str,
        template_key: str,
        display_name: str,
        fields: ClassificationsInitializeTemplateRequestFields,
        hidden: typing.Optional[bool] = None,
        copy_instance_on_item_copy: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._initialize_template_mapped_args(
            scope=scope,
            template_key=template_key,
            display_name=display_name,
            fields=fields,
            hidden=hidden,
            copy_instance_on_item_copy=copy_instance_on_item_copy,
        )
        return await self._ainitialize_template_oapg(
            body=args.body,
            **kwargs,
        )
    
    def initialize_template(
        self,
        scope: str,
        template_key: str,
        display_name: str,
        fields: ClassificationsInitializeTemplateRequestFields,
        hidden: typing.Optional[bool] = None,
        copy_instance_on_item_copy: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._initialize_template_mapped_args(
            scope=scope,
            template_key=template_key,
            display_name=display_name,
            fields=fields,
            hidden=hidden,
            copy_instance_on_item_copy=copy_instance_on_item_copy,
        )
        return self._initialize_template_oapg(
            body=args.body,
        )

class InitializeTemplate(BaseApi):

    async def ainitialize_template(
        self,
        scope: str,
        template_key: str,
        display_name: str,
        fields: ClassificationsInitializeTemplateRequestFields,
        hidden: typing.Optional[bool] = None,
        copy_instance_on_item_copy: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> ClassificationTemplatePydantic:
        raw_response = await self.raw.ainitialize_template(
            scope=scope,
            template_key=template_key,
            display_name=display_name,
            fields=fields,
            hidden=hidden,
            copy_instance_on_item_copy=copy_instance_on_item_copy,
            **kwargs,
        )
        if validate:
            return ClassificationTemplatePydantic(**raw_response.body)
        return api_client.construct_model_instance(ClassificationTemplatePydantic, raw_response.body)
    
    
    def initialize_template(
        self,
        scope: str,
        template_key: str,
        display_name: str,
        fields: ClassificationsInitializeTemplateRequestFields,
        hidden: typing.Optional[bool] = None,
        copy_instance_on_item_copy: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> ClassificationTemplatePydantic:
        raw_response = self.raw.initialize_template(
            scope=scope,
            template_key=template_key,
            display_name=display_name,
            fields=fields,
            hidden=hidden,
            copy_instance_on_item_copy=copy_instance_on_item_copy,
        )
        if validate:
            return ClassificationTemplatePydantic(**raw_response.body)
        return api_client.construct_model_instance(ClassificationTemplatePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        scope: str,
        template_key: str,
        display_name: str,
        fields: ClassificationsInitializeTemplateRequestFields,
        hidden: typing.Optional[bool] = None,
        copy_instance_on_item_copy: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._initialize_template_mapped_args(
            scope=scope,
            template_key=template_key,
            display_name=display_name,
            fields=fields,
            hidden=hidden,
            copy_instance_on_item_copy=copy_instance_on_item_copy,
        )
        return await self._ainitialize_template_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        scope: str,
        template_key: str,
        display_name: str,
        fields: ClassificationsInitializeTemplateRequestFields,
        hidden: typing.Optional[bool] = None,
        copy_instance_on_item_copy: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._initialize_template_mapped_args(
            scope=scope,
            template_key=template_key,
            display_name=display_name,
            fields=fields,
            hidden=hidden,
            copy_instance_on_item_copy=copy_instance_on_item_copy,
        )
        return self._initialize_template_oapg(
            body=args.body,
        )

