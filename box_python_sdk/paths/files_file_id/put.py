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
from box_python_sdk.model.files_update_file_request_collections import FilesUpdateFileRequestCollections as FilesUpdateFileRequestCollectionsSchema
from box_python_sdk.model.files_update_file_request_permissions import FilesUpdateFileRequestPermissions as FilesUpdateFileRequestPermissionsSchema
from box_python_sdk.model.files_update_file_request_tags import FilesUpdateFileRequestTags as FilesUpdateFileRequestTagsSchema
from box_python_sdk.model.files_update_file_request import FilesUpdateFileRequest as FilesUpdateFileRequestSchema
from box_python_sdk.model.files_update_file_request_lock import FilesUpdateFileRequestLock as FilesUpdateFileRequestLockSchema
from box_python_sdk.model.file_full import FileFull as FileFullSchema

from box_python_sdk.type.files_update_file_request import FilesUpdateFileRequest
from box_python_sdk.type.files_update_file_request_collections import FilesUpdateFileRequestCollections
from box_python_sdk.type.files_update_file_request_permissions import FilesUpdateFileRequestPermissions
from box_python_sdk.type.file_full import FileFull
from box_python_sdk.type.files_update_file_request_lock import FilesUpdateFileRequestLock
from box_python_sdk.type.files_update_file_request_tags import FilesUpdateFileRequestTags
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.files_update_file_request import FilesUpdateFileRequest as FilesUpdateFileRequestPydantic
from box_python_sdk.pydantic.files_update_file_request_lock import FilesUpdateFileRequestLock as FilesUpdateFileRequestLockPydantic
from box_python_sdk.pydantic.files_update_file_request_collections import FilesUpdateFileRequestCollections as FilesUpdateFileRequestCollectionsPydantic
from box_python_sdk.pydantic.files_update_file_request_permissions import FilesUpdateFileRequestPermissions as FilesUpdateFileRequestPermissionsPydantic
from box_python_sdk.pydantic.files_update_file_request_tags import FilesUpdateFileRequestTags as FilesUpdateFileRequestTagsPydantic
from box_python_sdk.pydantic.file_full import FileFull as FileFullPydantic

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
# Header params
IfMatchSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'if-match': typing.Union[IfMatchSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_if_match = api_client.HeaderParameter(
    name="if-match",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IfMatchSchema,
)
# Path params
FileIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'file_id': typing.Union[FileIdSchema, str, ],
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


request_path_file_id = api_client.PathParameter(
    name="file_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FileIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = FilesUpdateFileRequestSchema


request_body_files_update_file_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'OAuth2Security',
]
SchemaFor200ResponseBodyApplicationJson = FileFullSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FileFull


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FileFull


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
SchemaFor401ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
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
SchemaFor405ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor405(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor405Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
    response_cls_async=ApiResponseFor405Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor405ResponseBodyApplicationJson),
    },
)
SchemaFor412ResponseBodyApplicationJson = ClientErrorSchema


@dataclass
class ApiResponseFor412(api_client.ApiResponse):
    body: ClientError


@dataclass
class ApiResponseFor412Async(api_client.AsyncApiResponse):
    body: ClientError


_response_for_412 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor412,
    response_cls_async=ApiResponseFor412Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor412ResponseBodyApplicationJson),
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
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '405': _response_for_405,
    '412': _response_for_412,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_file_mapped_args(
        self,
        file_id: str,
        tags: typing.Optional[FilesUpdateFileRequestTags] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        shared_link: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        lock: typing.Optional[FilesUpdateFileRequestLock] = None,
        disposition_at: typing.Optional[datetime] = None,
        permissions: typing.Optional[FilesUpdateFileRequestPermissions] = None,
        collections: typing.Optional[FilesUpdateFileRequestCollections] = None,
        fields: typing.Optional[typing.List[str]] = None,
        if_match: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        _body = {}
        if tags is not None:
            _body["tags"] = tags
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if parent is not None:
            _body["parent"] = parent
        if shared_link is not None:
            _body["shared_link"] = shared_link
        if lock is not None:
            _body["lock"] = lock
        if disposition_at is not None:
            _body["disposition_at"] = disposition_at
        if permissions is not None:
            _body["permissions"] = permissions
        if collections is not None:
            _body["collections"] = collections
        args.body = _body
        if fields is not None:
            _query_params["fields"] = fields
        if if_match is not None:
            _header_params["if-match"] = if_match
        if file_id is not None:
            _path_params["file_id"] = file_id
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aupdate_file_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Update file
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_file_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
        for parameter in (
            request_header_if_match,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/files/{file_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_files_update_file_request.serialize(body, content_type)
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


    def _update_file_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        Update file
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_file_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
        for parameter in (
            request_header_if_match,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/files/{file_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_files_update_file_request.serialize(body, content_type)
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


class UpdateFileRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_file(
        self,
        file_id: str,
        tags: typing.Optional[FilesUpdateFileRequestTags] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        shared_link: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        lock: typing.Optional[FilesUpdateFileRequestLock] = None,
        disposition_at: typing.Optional[datetime] = None,
        permissions: typing.Optional[FilesUpdateFileRequestPermissions] = None,
        collections: typing.Optional[FilesUpdateFileRequestCollections] = None,
        fields: typing.Optional[typing.List[str]] = None,
        if_match: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_file_mapped_args(
            file_id=file_id,
            tags=tags,
            description=description,
            name=name,
            parent=parent,
            shared_link=shared_link,
            lock=lock,
            disposition_at=disposition_at,
            permissions=permissions,
            collections=collections,
            fields=fields,
            if_match=if_match,
        )
        return await self._aupdate_file_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def update_file(
        self,
        file_id: str,
        tags: typing.Optional[FilesUpdateFileRequestTags] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        shared_link: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        lock: typing.Optional[FilesUpdateFileRequestLock] = None,
        disposition_at: typing.Optional[datetime] = None,
        permissions: typing.Optional[FilesUpdateFileRequestPermissions] = None,
        collections: typing.Optional[FilesUpdateFileRequestCollections] = None,
        fields: typing.Optional[typing.List[str]] = None,
        if_match: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_file_mapped_args(
            file_id=file_id,
            tags=tags,
            description=description,
            name=name,
            parent=parent,
            shared_link=shared_link,
            lock=lock,
            disposition_at=disposition_at,
            permissions=permissions,
            collections=collections,
            fields=fields,
            if_match=if_match,
        )
        return self._update_file_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class UpdateFile(BaseApi):

    async def aupdate_file(
        self,
        file_id: str,
        tags: typing.Optional[FilesUpdateFileRequestTags] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        shared_link: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        lock: typing.Optional[FilesUpdateFileRequestLock] = None,
        disposition_at: typing.Optional[datetime] = None,
        permissions: typing.Optional[FilesUpdateFileRequestPermissions] = None,
        collections: typing.Optional[FilesUpdateFileRequestCollections] = None,
        fields: typing.Optional[typing.List[str]] = None,
        if_match: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FileFullPydantic:
        raw_response = await self.raw.aupdate_file(
            file_id=file_id,
            tags=tags,
            description=description,
            name=name,
            parent=parent,
            shared_link=shared_link,
            lock=lock,
            disposition_at=disposition_at,
            permissions=permissions,
            collections=collections,
            fields=fields,
            if_match=if_match,
            **kwargs,
        )
        if validate:
            return RootModel[FileFullPydantic](raw_response.body).root
        return api_client.construct_model_instance(FileFullPydantic, raw_response.body)
    
    
    def update_file(
        self,
        file_id: str,
        tags: typing.Optional[FilesUpdateFileRequestTags] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        shared_link: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        lock: typing.Optional[FilesUpdateFileRequestLock] = None,
        disposition_at: typing.Optional[datetime] = None,
        permissions: typing.Optional[FilesUpdateFileRequestPermissions] = None,
        collections: typing.Optional[FilesUpdateFileRequestCollections] = None,
        fields: typing.Optional[typing.List[str]] = None,
        if_match: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FileFullPydantic:
        raw_response = self.raw.update_file(
            file_id=file_id,
            tags=tags,
            description=description,
            name=name,
            parent=parent,
            shared_link=shared_link,
            lock=lock,
            disposition_at=disposition_at,
            permissions=permissions,
            collections=collections,
            fields=fields,
            if_match=if_match,
        )
        if validate:
            return RootModel[FileFullPydantic](raw_response.body).root
        return api_client.construct_model_instance(FileFullPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        file_id: str,
        tags: typing.Optional[FilesUpdateFileRequestTags] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        shared_link: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        lock: typing.Optional[FilesUpdateFileRequestLock] = None,
        disposition_at: typing.Optional[datetime] = None,
        permissions: typing.Optional[FilesUpdateFileRequestPermissions] = None,
        collections: typing.Optional[FilesUpdateFileRequestCollections] = None,
        fields: typing.Optional[typing.List[str]] = None,
        if_match: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_file_mapped_args(
            file_id=file_id,
            tags=tags,
            description=description,
            name=name,
            parent=parent,
            shared_link=shared_link,
            lock=lock,
            disposition_at=disposition_at,
            permissions=permissions,
            collections=collections,
            fields=fields,
            if_match=if_match,
        )
        return await self._aupdate_file_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        file_id: str,
        tags: typing.Optional[FilesUpdateFileRequestTags] = None,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        parent: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        shared_link: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        lock: typing.Optional[FilesUpdateFileRequestLock] = None,
        disposition_at: typing.Optional[datetime] = None,
        permissions: typing.Optional[FilesUpdateFileRequestPermissions] = None,
        collections: typing.Optional[FilesUpdateFileRequestCollections] = None,
        fields: typing.Optional[typing.List[str]] = None,
        if_match: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_file_mapped_args(
            file_id=file_id,
            tags=tags,
            description=description,
            name=name,
            parent=parent,
            shared_link=shared_link,
            lock=lock,
            disposition_at=disposition_at,
            permissions=permissions,
            collections=collections,
            fields=fields,
            if_match=if_match,
        )
        return self._update_file_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

