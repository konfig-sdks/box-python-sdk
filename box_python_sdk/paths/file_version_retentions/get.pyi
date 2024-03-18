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
from box_python_sdk.model.file_version_retentions import FileVersionRetentions as FileVersionRetentionsSchema

from box_python_sdk.type.client_error import ClientError
from box_python_sdk.type.file_version_retentions import FileVersionRetentions

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.file_version_retentions import FileVersionRetentions as FileVersionRetentionsPydantic

# Query params
FileIdSchema = schemas.StrSchema
FileVersionIdSchema = schemas.StrSchema
PolicyIdSchema = schemas.StrSchema


class DispositionActionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def PERMANENTLY_DELETE(cls):
        return cls("permanently_delete")
    
    @schemas.classproperty
    def REMOVE_RETENTION(cls):
        return cls("remove_retention")
DispositionBeforeSchema = schemas.StrSchema
DispositionAfterSchema = schemas.StrSchema


class LimitSchema(
    schemas.Int64Schema
):
    pass
MarkerSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'file_id': typing.Union[FileIdSchema, str, ],
        'file_version_id': typing.Union[FileVersionIdSchema, str, ],
        'policy_id': typing.Union[PolicyIdSchema, str, ],
        'disposition_action': typing.Union[DispositionActionSchema, str, ],
        'disposition_before': typing.Union[DispositionBeforeSchema, str, ],
        'disposition_after': typing.Union[DispositionAfterSchema, str, ],
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
    explode=True,
)
request_query_file_version_id = api_client.QueryParameter(
    name="file_version_id",
    style=api_client.ParameterStyle.FORM,
    schema=FileVersionIdSchema,
    explode=True,
)
request_query_policy_id = api_client.QueryParameter(
    name="policy_id",
    style=api_client.ParameterStyle.FORM,
    schema=PolicyIdSchema,
    explode=True,
)
request_query_disposition_action = api_client.QueryParameter(
    name="disposition_action",
    style=api_client.ParameterStyle.FORM,
    schema=DispositionActionSchema,
    explode=True,
)
request_query_disposition_before = api_client.QueryParameter(
    name="disposition_before",
    style=api_client.ParameterStyle.FORM,
    schema=DispositionBeforeSchema,
    explode=True,
)
request_query_disposition_after = api_client.QueryParameter(
    name="disposition_after",
    style=api_client.ParameterStyle.FORM,
    schema=DispositionAfterSchema,
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
SchemaFor200ResponseBodyApplicationJson = FileVersionRetentionsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FileVersionRetentions


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FileVersionRetentions


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_retentions_mapped_args(
        self,
        file_id: typing.Optional[str] = None,
        file_version_id: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        disposition_action: typing.Optional[str] = None,
        disposition_before: typing.Optional[str] = None,
        disposition_after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if file_id is not None:
            _query_params["file_id"] = file_id
        if file_version_id is not None:
            _query_params["file_version_id"] = file_version_id
        if policy_id is not None:
            _query_params["policy_id"] = policy_id
        if disposition_action is not None:
            _query_params["disposition_action"] = disposition_action
        if disposition_before is not None:
            _query_params["disposition_before"] = disposition_before
        if disposition_after is not None:
            _query_params["disposition_after"] = disposition_after
        if limit is not None:
            _query_params["limit"] = limit
        if marker is not None:
            _query_params["marker"] = marker
        args.query = _query_params
        return args

    async def _alist_retentions_oapg(
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
        List file version retentions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_file_id,
            request_query_file_version_id,
            request_query_policy_id,
            request_query_disposition_action,
            request_query_disposition_before,
            request_query_disposition_after,
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
            path_template='/file_version_retentions',
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


    def _list_retentions_oapg(
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
        List file version retentions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_file_id,
            request_query_file_version_id,
            request_query_policy_id,
            request_query_disposition_action,
            request_query_disposition_before,
            request_query_disposition_after,
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
            path_template='/file_version_retentions',
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


class ListRetentionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_retentions(
        self,
        file_id: typing.Optional[str] = None,
        file_version_id: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        disposition_action: typing.Optional[str] = None,
        disposition_before: typing.Optional[str] = None,
        disposition_after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_retentions_mapped_args(
            file_id=file_id,
            file_version_id=file_version_id,
            policy_id=policy_id,
            disposition_action=disposition_action,
            disposition_before=disposition_before,
            disposition_after=disposition_after,
            limit=limit,
            marker=marker,
        )
        return await self._alist_retentions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_retentions(
        self,
        file_id: typing.Optional[str] = None,
        file_version_id: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        disposition_action: typing.Optional[str] = None,
        disposition_before: typing.Optional[str] = None,
        disposition_after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_retentions_mapped_args(
            file_id=file_id,
            file_version_id=file_version_id,
            policy_id=policy_id,
            disposition_action=disposition_action,
            disposition_before=disposition_before,
            disposition_after=disposition_after,
            limit=limit,
            marker=marker,
        )
        return self._list_retentions_oapg(
            query_params=args.query,
        )

class ListRetentions(BaseApi):

    async def alist_retentions(
        self,
        file_id: typing.Optional[str] = None,
        file_version_id: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        disposition_action: typing.Optional[str] = None,
        disposition_before: typing.Optional[str] = None,
        disposition_after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FileVersionRetentionsPydantic:
        raw_response = await self.raw.alist_retentions(
            file_id=file_id,
            file_version_id=file_version_id,
            policy_id=policy_id,
            disposition_action=disposition_action,
            disposition_before=disposition_before,
            disposition_after=disposition_after,
            limit=limit,
            marker=marker,
            **kwargs,
        )
        if validate:
            return RootModel[FileVersionRetentionsPydantic](raw_response.body).root
        return api_client.construct_model_instance(FileVersionRetentionsPydantic, raw_response.body)
    
    
    def list_retentions(
        self,
        file_id: typing.Optional[str] = None,
        file_version_id: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        disposition_action: typing.Optional[str] = None,
        disposition_before: typing.Optional[str] = None,
        disposition_after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FileVersionRetentionsPydantic:
        raw_response = self.raw.list_retentions(
            file_id=file_id,
            file_version_id=file_version_id,
            policy_id=policy_id,
            disposition_action=disposition_action,
            disposition_before=disposition_before,
            disposition_after=disposition_after,
            limit=limit,
            marker=marker,
        )
        if validate:
            return RootModel[FileVersionRetentionsPydantic](raw_response.body).root
        return api_client.construct_model_instance(FileVersionRetentionsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        file_id: typing.Optional[str] = None,
        file_version_id: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        disposition_action: typing.Optional[str] = None,
        disposition_before: typing.Optional[str] = None,
        disposition_after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_retentions_mapped_args(
            file_id=file_id,
            file_version_id=file_version_id,
            policy_id=policy_id,
            disposition_action=disposition_action,
            disposition_before=disposition_before,
            disposition_after=disposition_after,
            limit=limit,
            marker=marker,
        )
        return await self._alist_retentions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        file_id: typing.Optional[str] = None,
        file_version_id: typing.Optional[str] = None,
        policy_id: typing.Optional[str] = None,
        disposition_action: typing.Optional[str] = None,
        disposition_before: typing.Optional[str] = None,
        disposition_after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        marker: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_retentions_mapped_args(
            file_id=file_id,
            file_version_id=file_version_id,
            policy_id=policy_id,
            disposition_action=disposition_action,
            disposition_before=disposition_before,
            disposition_after=disposition_after,
            limit=limit,
            marker=marker,
        )
        return self._list_retentions_oapg(
            query_params=args.query,
        )

