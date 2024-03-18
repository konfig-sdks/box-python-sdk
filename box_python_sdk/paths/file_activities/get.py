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

from box_python_sdk.model.activities import Activities as ActivitiesSchema
from box_python_sdk.model.client_error import ClientError as ClientErrorSchema

from box_python_sdk.type.activities import Activities
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.activities import Activities as ActivitiesPydantic

from . import path

# Query params
FileIdSchema = schemas.StrSchema


class ActivityTypesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "annotation": "ANNOTATION",
                    "app_activity": "APP_ACTIVITY",
                    "comment": "COMMENT",
                    "task": "TASK",
                    "versions": "VERSIONS",
                }
            
            @schemas.classproperty
            def ANNOTATION(cls):
                return cls("annotation")
            
            @schemas.classproperty
            def APP_ACTIVITY(cls):
                return cls("app_activity")
            
            @schemas.classproperty
            def COMMENT(cls):
                return cls("comment")
            
            @schemas.classproperty
            def TASK(cls):
                return cls("task")
            
            @schemas.classproperty
            def VERSIONS(cls):
                return cls("versions")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ActivityTypesSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class CommentFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CommentFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class VersionsFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'VersionsFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class AnnotationFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AnnotationFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class TaskFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TaskFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class AppActivityFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AppActivityFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
ReplyLimitSchema = schemas.StrSchema


class StatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "open": "OPEN",
            "resolved": "RESOLVED",
            "deleted": "DELETED",
        }
    
    @schemas.classproperty
    def OPEN(cls):
        return cls("open")
    
    @schemas.classproperty
    def RESOLVED(cls):
        return cls("resolved")
    
    @schemas.classproperty
    def DELETED(cls):
        return cls("deleted")
EnableRepliesSchema = schemas.BoolSchema


class LimitSchema(
    schemas.Int64Schema
):


    class MetaOapg:
        format = 'int64'
        inclusive_maximum = 1000
MarkerSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'file_id': typing.Union[FileIdSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'activity_types': typing.Union[ActivityTypesSchema, list, tuple, ],
        'comment_fields': typing.Union[CommentFieldsSchema, list, tuple, ],
        'versions_fields': typing.Union[VersionsFieldsSchema, list, tuple, ],
        'annotation_fields': typing.Union[AnnotationFieldsSchema, list, tuple, ],
        'task_fields': typing.Union[TaskFieldsSchema, list, tuple, ],
        'app_activity_fields': typing.Union[AppActivityFieldsSchema, list, tuple, ],
        'reply_limit': typing.Union[ReplyLimitSchema, str, ],
        'status': typing.Union[StatusSchema, str, ],
        'enable_replies': typing.Union[EnableRepliesSchema, bool, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'marker': typing.Union[MarkerSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_file_id = api_client.QueryParameter(
    name="file_id",
    style=api_client.ParameterStyle.FORM,
    schema=FileIdSchema,
    required=True,
    explode=True,
)
request_query_activity_types = api_client.QueryParameter(
    name="activity_types",
    style=api_client.ParameterStyle.FORM,
    schema=ActivityTypesSchema,
    explode=True,
)
request_query_comment_fields = api_client.QueryParameter(
    name="comment_fields",
    style=api_client.ParameterStyle.FORM,
    schema=CommentFieldsSchema,
    explode=True,
)
request_query_versions_fields = api_client.QueryParameter(
    name="versions_fields",
    style=api_client.ParameterStyle.FORM,
    schema=VersionsFieldsSchema,
    explode=True,
)
request_query_annotation_fields = api_client.QueryParameter(
    name="annotation_fields",
    style=api_client.ParameterStyle.FORM,
    schema=AnnotationFieldsSchema,
    explode=True,
)
request_query_task_fields = api_client.QueryParameter(
    name="task_fields",
    style=api_client.ParameterStyle.FORM,
    schema=TaskFieldsSchema,
    explode=True,
)
request_query_app_activity_fields = api_client.QueryParameter(
    name="app_activity_fields",
    style=api_client.ParameterStyle.FORM,
    schema=AppActivityFieldsSchema,
    explode=True,
)
request_query_reply_limit = api_client.QueryParameter(
    name="reply_limit",
    style=api_client.ParameterStyle.FORM,
    schema=ReplyLimitSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
request_query_enable_replies = api_client.QueryParameter(
    name="enable_replies",
    style=api_client.ParameterStyle.FORM,
    schema=EnableRepliesSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_marker = api_client.QueryParameter(
    name="marker",
    style=api_client.ParameterStyle.FORM,
    schema=MarkerSchema,
    explode=True,
)
_auth = [
    'OAuth2Security',
]
SchemaFor200ResponseBodyApplicationJson = ActivitiesSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Activities


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Activities


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
    '200': _response_for_200,
    '404': _response_for_404,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_by_file_id_mapped_args(
        self,
        file_id: str,
        activity_types: typing.Optional[typing.List[str]] = None,
        comment_fields: typing.Optional[typing.List[str]] = None,
        versions_fields: typing.Optional[typing.List[str]] = None,
        annotation_fields: typing.Optional[typing.List[str]] = None,
        task_fields: typing.Optional[typing.List[str]] = None,
        app_activity_fields: typing.Optional[typing.List[str]] = None,
        reply_limit: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        enable_replies: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if file_id is not None:
            _query_params["file_id"] = file_id
        if activity_types is not None:
            _query_params["activity_types"] = activity_types
        if comment_fields is not None:
            _query_params["comment_fields"] = comment_fields
        if versions_fields is not None:
            _query_params["versions_fields"] = versions_fields
        if annotation_fields is not None:
            _query_params["annotation_fields"] = annotation_fields
        if task_fields is not None:
            _query_params["task_fields"] = task_fields
        if app_activity_fields is not None:
            _query_params["app_activity_fields"] = app_activity_fields
        if reply_limit is not None:
            _query_params["reply_limit"] = reply_limit
        if status is not None:
            _query_params["status"] = status
        if enable_replies is not None:
            _query_params["enable_replies"] = enable_replies
        if limit is not None:
            _query_params["limit"] = limit
        if marker is not None:
            _query_params["marker"] = marker
        args.query = _query_params
        return args

    async def _alist_by_file_id_oapg(
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
        List file activities
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_file_id,
            request_query_activity_types,
            request_query_comment_fields,
            request_query_versions_fields,
            request_query_annotation_fields,
            request_query_task_fields,
            request_query_app_activity_fields,
            request_query_reply_limit,
            request_query_status,
            request_query_enable_replies,
            request_query_limit,
            request_query_marker,
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
            path_template='/file_activities',
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


    def _list_by_file_id_oapg(
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
        List file activities
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_file_id,
            request_query_activity_types,
            request_query_comment_fields,
            request_query_versions_fields,
            request_query_annotation_fields,
            request_query_task_fields,
            request_query_app_activity_fields,
            request_query_reply_limit,
            request_query_status,
            request_query_enable_replies,
            request_query_limit,
            request_query_marker,
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
            path_template='/file_activities',
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


class ListByFileIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_by_file_id(
        self,
        file_id: str,
        activity_types: typing.Optional[typing.List[str]] = None,
        comment_fields: typing.Optional[typing.List[str]] = None,
        versions_fields: typing.Optional[typing.List[str]] = None,
        annotation_fields: typing.Optional[typing.List[str]] = None,
        task_fields: typing.Optional[typing.List[str]] = None,
        app_activity_fields: typing.Optional[typing.List[str]] = None,
        reply_limit: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        enable_replies: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_by_file_id_mapped_args(
            file_id=file_id,
            activity_types=activity_types,
            comment_fields=comment_fields,
            versions_fields=versions_fields,
            annotation_fields=annotation_fields,
            task_fields=task_fields,
            app_activity_fields=app_activity_fields,
            reply_limit=reply_limit,
            status=status,
            enable_replies=enable_replies,
            limit=limit,
            marker=marker,
        )
        return await self._alist_by_file_id_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_by_file_id(
        self,
        file_id: str,
        activity_types: typing.Optional[typing.List[str]] = None,
        comment_fields: typing.Optional[typing.List[str]] = None,
        versions_fields: typing.Optional[typing.List[str]] = None,
        annotation_fields: typing.Optional[typing.List[str]] = None,
        task_fields: typing.Optional[typing.List[str]] = None,
        app_activity_fields: typing.Optional[typing.List[str]] = None,
        reply_limit: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        enable_replies: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_by_file_id_mapped_args(
            file_id=file_id,
            activity_types=activity_types,
            comment_fields=comment_fields,
            versions_fields=versions_fields,
            annotation_fields=annotation_fields,
            task_fields=task_fields,
            app_activity_fields=app_activity_fields,
            reply_limit=reply_limit,
            status=status,
            enable_replies=enable_replies,
            limit=limit,
            marker=marker,
        )
        return self._list_by_file_id_oapg(
            query_params=args.query,
        )

class ListByFileId(BaseApi):

    async def alist_by_file_id(
        self,
        file_id: str,
        activity_types: typing.Optional[typing.List[str]] = None,
        comment_fields: typing.Optional[typing.List[str]] = None,
        versions_fields: typing.Optional[typing.List[str]] = None,
        annotation_fields: typing.Optional[typing.List[str]] = None,
        task_fields: typing.Optional[typing.List[str]] = None,
        app_activity_fields: typing.Optional[typing.List[str]] = None,
        reply_limit: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        enable_replies: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ActivitiesPydantic:
        raw_response = await self.raw.alist_by_file_id(
            file_id=file_id,
            activity_types=activity_types,
            comment_fields=comment_fields,
            versions_fields=versions_fields,
            annotation_fields=annotation_fields,
            task_fields=task_fields,
            app_activity_fields=app_activity_fields,
            reply_limit=reply_limit,
            status=status,
            enable_replies=enable_replies,
            limit=limit,
            marker=marker,
            **kwargs,
        )
        if validate:
            return RootModel[ActivitiesPydantic](raw_response.body).root
        return api_client.construct_model_instance(ActivitiesPydantic, raw_response.body)
    
    
    def list_by_file_id(
        self,
        file_id: str,
        activity_types: typing.Optional[typing.List[str]] = None,
        comment_fields: typing.Optional[typing.List[str]] = None,
        versions_fields: typing.Optional[typing.List[str]] = None,
        annotation_fields: typing.Optional[typing.List[str]] = None,
        task_fields: typing.Optional[typing.List[str]] = None,
        app_activity_fields: typing.Optional[typing.List[str]] = None,
        reply_limit: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        enable_replies: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ActivitiesPydantic:
        raw_response = self.raw.list_by_file_id(
            file_id=file_id,
            activity_types=activity_types,
            comment_fields=comment_fields,
            versions_fields=versions_fields,
            annotation_fields=annotation_fields,
            task_fields=task_fields,
            app_activity_fields=app_activity_fields,
            reply_limit=reply_limit,
            status=status,
            enable_replies=enable_replies,
            limit=limit,
            marker=marker,
        )
        if validate:
            return RootModel[ActivitiesPydantic](raw_response.body).root
        return api_client.construct_model_instance(ActivitiesPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        file_id: str,
        activity_types: typing.Optional[typing.List[str]] = None,
        comment_fields: typing.Optional[typing.List[str]] = None,
        versions_fields: typing.Optional[typing.List[str]] = None,
        annotation_fields: typing.Optional[typing.List[str]] = None,
        task_fields: typing.Optional[typing.List[str]] = None,
        app_activity_fields: typing.Optional[typing.List[str]] = None,
        reply_limit: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        enable_replies: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_by_file_id_mapped_args(
            file_id=file_id,
            activity_types=activity_types,
            comment_fields=comment_fields,
            versions_fields=versions_fields,
            annotation_fields=annotation_fields,
            task_fields=task_fields,
            app_activity_fields=app_activity_fields,
            reply_limit=reply_limit,
            status=status,
            enable_replies=enable_replies,
            limit=limit,
            marker=marker,
        )
        return await self._alist_by_file_id_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        file_id: str,
        activity_types: typing.Optional[typing.List[str]] = None,
        comment_fields: typing.Optional[typing.List[str]] = None,
        versions_fields: typing.Optional[typing.List[str]] = None,
        annotation_fields: typing.Optional[typing.List[str]] = None,
        task_fields: typing.Optional[typing.List[str]] = None,
        app_activity_fields: typing.Optional[typing.List[str]] = None,
        reply_limit: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        enable_replies: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_by_file_id_mapped_args(
            file_id=file_id,
            activity_types=activity_types,
            comment_fields=comment_fields,
            versions_fields=versions_fields,
            annotation_fields=annotation_fields,
            task_fields=task_fields,
            app_activity_fields=app_activity_fields,
            reply_limit=reply_limit,
            status=status,
            enable_replies=enable_replies,
            limit=limit,
            marker=marker,
        )
        return self._list_by_file_id_oapg(
            query_params=args.query,
        )

