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
from box_python_sdk.model.metadata_filter import MetadataFilter as MetadataFilterSchema
from box_python_sdk.model.get_search_response import GetSearchResponse as GetSearchResponseSchema

from box_python_sdk.type.metadata_filter import MetadataFilter
from box_python_sdk.type.get_search_response import GetSearchResponse
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.get_search_response import GetSearchResponse as GetSearchResponsePydantic
from box_python_sdk.pydantic.metadata_filter import MetadataFilter as MetadataFilterPydantic

# Query params
QuerySchema = schemas.StrSchema


class ScopeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def USER_CONTENT(cls):
        return cls("user_content")
    
    @schemas.classproperty
    def ENTERPRISE_CONTENT(cls):
        return cls("enterprise_content")


class FileExtensionsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FileExtensionsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class CreatedAtRangeSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CreatedAtRangeSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class UpdatedAtRangeSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UpdatedAtRangeSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class SizeRangeSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.IntSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SizeRangeSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class OwnerUserIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OwnerUserIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class RecentUpdaterUserIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'RecentUpdaterUserIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class AncestorFolderIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AncestorFolderIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class ContentTypesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
            @schemas.classproperty
            def DESCRIPTION(cls):
                return cls("description")
            
            @schemas.classproperty
            def FILE_CONTENT(cls):
                return cls("file_content")
            
            @schemas.classproperty
            def COMMENTS(cls):
                return cls("comments")
            
            @schemas.classproperty
            def TAG(cls):
                return cls("tag")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ContentTypesSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def FILE(cls):
        return cls("file")
    
    @schemas.classproperty
    def FOLDER(cls):
        return cls("folder")
    
    @schemas.classproperty
    def WEB_LINK(cls):
        return cls("web_link")


class TrashContentSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def NON_TRASHED_ONLY(cls):
        return cls("non_trashed_only")
    
    @schemas.classproperty
    def TRASHED_ONLY(cls):
        return cls("trashed_only")
    
    @schemas.classproperty
    def ALL_ITEMS(cls):
        return cls("all_items")


class MdfiltersSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['MetadataFilter']:
            return MetadataFilter

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['MetadataFilter'], typing.List['MetadataFilter']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MdfiltersSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'MetadataFilter':
        return super().__getitem__(i)


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def MODIFIED_AT(cls):
        return cls("modified_at")
    
    @schemas.classproperty
    def RELEVANCE(cls):
        return cls("relevance")


class DirectionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DESC(cls):
        return cls("DESC")
    
    @schemas.classproperty
    def ASC(cls):
        return cls("ASC")


class LimitSchema(
    schemas.Int64Schema
):
    pass
IncludeRecentSharedLinksSchema = schemas.BoolSchema


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
OffsetSchema = schemas.Int64Schema


class DeletedUserIdsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DeletedUserIdsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class DeletedAtRangeSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DeletedAtRangeSchema':
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
        'query': typing.Union[QuerySchema, str, ],
        'scope': typing.Union[ScopeSchema, str, ],
        'file_extensions': typing.Union[FileExtensionsSchema, list, tuple, ],
        'created_at_range': typing.Union[CreatedAtRangeSchema, list, tuple, ],
        'updated_at_range': typing.Union[UpdatedAtRangeSchema, list, tuple, ],
        'size_range': typing.Union[SizeRangeSchema, list, tuple, ],
        'owner_user_ids': typing.Union[OwnerUserIdsSchema, list, tuple, ],
        'recent_updater_user_ids': typing.Union[RecentUpdaterUserIdsSchema, list, tuple, ],
        'ancestor_folder_ids': typing.Union[AncestorFolderIdsSchema, list, tuple, ],
        'content_types': typing.Union[ContentTypesSchema, list, tuple, ],
        'type': typing.Union[TypeSchema, str, ],
        'trash_content': typing.Union[TrashContentSchema, str, ],
        'mdfilters': typing.Union[MdfiltersSchema, list, tuple, ],
        'sort': typing.Union[SortSchema, str, ],
        'direction': typing.Union[DirectionSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'include_recent_shared_links': typing.Union[IncludeRecentSharedLinksSchema, bool, ],
        'fields': typing.Union[FieldsSchema, list, tuple, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
        'deleted_user_ids': typing.Union[DeletedUserIdsSchema, list, tuple, ],
        'deleted_at_range': typing.Union[DeletedAtRangeSchema, list, tuple, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_query = api_client.QueryParameter(
    name="query",
    style=api_client.ParameterStyle.FORM,
    schema=QuerySchema,
    explode=True,
)
request_query_scope = api_client.QueryParameter(
    name="scope",
    style=api_client.ParameterStyle.FORM,
    schema=ScopeSchema,
    explode=True,
)
request_query_file_extensions = api_client.QueryParameter(
    name="file_extensions",
    style=api_client.ParameterStyle.FORM,
    schema=FileExtensionsSchema,
)
request_query_created_at_range = api_client.QueryParameter(
    name="created_at_range",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedAtRangeSchema,
)
request_query_updated_at_range = api_client.QueryParameter(
    name="updated_at_range",
    style=api_client.ParameterStyle.FORM,
    schema=UpdatedAtRangeSchema,
)
request_query_size_range = api_client.QueryParameter(
    name="size_range",
    style=api_client.ParameterStyle.FORM,
    schema=SizeRangeSchema,
)
request_query_owner_user_ids = api_client.QueryParameter(
    name="owner_user_ids",
    style=api_client.ParameterStyle.FORM,
    schema=OwnerUserIdsSchema,
)
request_query_recent_updater_user_ids = api_client.QueryParameter(
    name="recent_updater_user_ids",
    style=api_client.ParameterStyle.FORM,
    schema=RecentUpdaterUserIdsSchema,
)
request_query_ancestor_folder_ids = api_client.QueryParameter(
    name="ancestor_folder_ids",
    style=api_client.ParameterStyle.FORM,
    schema=AncestorFolderIdsSchema,
)
request_query_content_types = api_client.QueryParameter(
    name="content_types",
    style=api_client.ParameterStyle.FORM,
    schema=ContentTypesSchema,
)
request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
request_query_trash_content = api_client.QueryParameter(
    name="trash_content",
    style=api_client.ParameterStyle.FORM,
    schema=TrashContentSchema,
    explode=True,
)
request_query_mdfilters = api_client.QueryParameter(
    name="mdfilters",
    style=api_client.ParameterStyle.FORM,
    schema=MdfiltersSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_direction = api_client.QueryParameter(
    name="direction",
    style=api_client.ParameterStyle.FORM,
    schema=DirectionSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_include_recent_shared_links = api_client.QueryParameter(
    name="include_recent_shared_links",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeRecentSharedLinksSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_deleted_user_ids = api_client.QueryParameter(
    name="deleted_user_ids",
    style=api_client.ParameterStyle.FORM,
    schema=DeletedUserIdsSchema,
    explode=True,
)
request_query_deleted_at_range = api_client.QueryParameter(
    name="deleted_at_range",
    style=api_client.ParameterStyle.FORM,
    schema=DeletedAtRangeSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = GetSearchResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GetSearchResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GetSearchResponse


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

    def _search_mapped_args(
        self,
        query: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        file_extensions: typing.Optional[typing.List[str]] = None,
        created_at_range: typing.Optional[typing.List[str]] = None,
        updated_at_range: typing.Optional[typing.List[str]] = None,
        size_range: typing.Optional[typing.List[int]] = None,
        owner_user_ids: typing.Optional[typing.List[str]] = None,
        recent_updater_user_ids: typing.Optional[typing.List[str]] = None,
        ancestor_folder_ids: typing.Optional[typing.List[str]] = None,
        content_types: typing.Optional[typing.List[str]] = None,
        type: typing.Optional[str] = None,
        trash_content: typing.Optional[str] = None,
        mdfilters: typing.Optional[typing.List[MetadataFilter]] = None,
        sort: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        include_recent_shared_links: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        deleted_user_ids: typing.Optional[typing.List[str]] = None,
        deleted_at_range: typing.Optional[typing.List[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if query is not None:
            _query_params["query"] = query
        if scope is not None:
            _query_params["scope"] = scope
        if file_extensions is not None:
            _query_params["file_extensions"] = file_extensions
        if created_at_range is not None:
            _query_params["created_at_range"] = created_at_range
        if updated_at_range is not None:
            _query_params["updated_at_range"] = updated_at_range
        if size_range is not None:
            _query_params["size_range"] = size_range
        if owner_user_ids is not None:
            _query_params["owner_user_ids"] = owner_user_ids
        if recent_updater_user_ids is not None:
            _query_params["recent_updater_user_ids"] = recent_updater_user_ids
        if ancestor_folder_ids is not None:
            _query_params["ancestor_folder_ids"] = ancestor_folder_ids
        if content_types is not None:
            _query_params["content_types"] = content_types
        if type is not None:
            _query_params["type"] = type
        if trash_content is not None:
            _query_params["trash_content"] = trash_content
        if mdfilters is not None:
            _query_params["mdfilters"] = mdfilters
        if sort is not None:
            _query_params["sort"] = sort
        if direction is not None:
            _query_params["direction"] = direction
        if limit is not None:
            _query_params["limit"] = limit
        if include_recent_shared_links is not None:
            _query_params["include_recent_shared_links"] = include_recent_shared_links
        if fields is not None:
            _query_params["fields"] = fields
        if offset is not None:
            _query_params["offset"] = offset
        if deleted_user_ids is not None:
            _query_params["deleted_user_ids"] = deleted_user_ids
        if deleted_at_range is not None:
            _query_params["deleted_at_range"] = deleted_at_range
        args.query = _query_params
        return args

    async def _asearch_oapg(
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
        Search for content
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_scope,
            request_query_file_extensions,
            request_query_created_at_range,
            request_query_updated_at_range,
            request_query_size_range,
            request_query_owner_user_ids,
            request_query_recent_updater_user_ids,
            request_query_ancestor_folder_ids,
            request_query_content_types,
            request_query_type,
            request_query_trash_content,
            request_query_mdfilters,
            request_query_sort,
            request_query_direction,
            request_query_limit,
            request_query_include_recent_shared_links,
            request_query_fields,
            request_query_offset,
            request_query_deleted_user_ids,
            request_query_deleted_at_range,
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
            path_template='/search',
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


    def _search_oapg(
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
        Search for content
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_scope,
            request_query_file_extensions,
            request_query_created_at_range,
            request_query_updated_at_range,
            request_query_size_range,
            request_query_owner_user_ids,
            request_query_recent_updater_user_ids,
            request_query_ancestor_folder_ids,
            request_query_content_types,
            request_query_type,
            request_query_trash_content,
            request_query_mdfilters,
            request_query_sort,
            request_query_direction,
            request_query_limit,
            request_query_include_recent_shared_links,
            request_query_fields,
            request_query_offset,
            request_query_deleted_user_ids,
            request_query_deleted_at_range,
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
            path_template='/search',
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


class SearchRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asearch(
        self,
        query: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        file_extensions: typing.Optional[typing.List[str]] = None,
        created_at_range: typing.Optional[typing.List[str]] = None,
        updated_at_range: typing.Optional[typing.List[str]] = None,
        size_range: typing.Optional[typing.List[int]] = None,
        owner_user_ids: typing.Optional[typing.List[str]] = None,
        recent_updater_user_ids: typing.Optional[typing.List[str]] = None,
        ancestor_folder_ids: typing.Optional[typing.List[str]] = None,
        content_types: typing.Optional[typing.List[str]] = None,
        type: typing.Optional[str] = None,
        trash_content: typing.Optional[str] = None,
        mdfilters: typing.Optional[typing.List[MetadataFilter]] = None,
        sort: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        include_recent_shared_links: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        deleted_user_ids: typing.Optional[typing.List[str]] = None,
        deleted_at_range: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_mapped_args(
            query=query,
            scope=scope,
            file_extensions=file_extensions,
            created_at_range=created_at_range,
            updated_at_range=updated_at_range,
            size_range=size_range,
            owner_user_ids=owner_user_ids,
            recent_updater_user_ids=recent_updater_user_ids,
            ancestor_folder_ids=ancestor_folder_ids,
            content_types=content_types,
            type=type,
            trash_content=trash_content,
            mdfilters=mdfilters,
            sort=sort,
            direction=direction,
            limit=limit,
            include_recent_shared_links=include_recent_shared_links,
            fields=fields,
            offset=offset,
            deleted_user_ids=deleted_user_ids,
            deleted_at_range=deleted_at_range,
        )
        return await self._asearch_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def search(
        self,
        query: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        file_extensions: typing.Optional[typing.List[str]] = None,
        created_at_range: typing.Optional[typing.List[str]] = None,
        updated_at_range: typing.Optional[typing.List[str]] = None,
        size_range: typing.Optional[typing.List[int]] = None,
        owner_user_ids: typing.Optional[typing.List[str]] = None,
        recent_updater_user_ids: typing.Optional[typing.List[str]] = None,
        ancestor_folder_ids: typing.Optional[typing.List[str]] = None,
        content_types: typing.Optional[typing.List[str]] = None,
        type: typing.Optional[str] = None,
        trash_content: typing.Optional[str] = None,
        mdfilters: typing.Optional[typing.List[MetadataFilter]] = None,
        sort: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        include_recent_shared_links: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        deleted_user_ids: typing.Optional[typing.List[str]] = None,
        deleted_at_range: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_mapped_args(
            query=query,
            scope=scope,
            file_extensions=file_extensions,
            created_at_range=created_at_range,
            updated_at_range=updated_at_range,
            size_range=size_range,
            owner_user_ids=owner_user_ids,
            recent_updater_user_ids=recent_updater_user_ids,
            ancestor_folder_ids=ancestor_folder_ids,
            content_types=content_types,
            type=type,
            trash_content=trash_content,
            mdfilters=mdfilters,
            sort=sort,
            direction=direction,
            limit=limit,
            include_recent_shared_links=include_recent_shared_links,
            fields=fields,
            offset=offset,
            deleted_user_ids=deleted_user_ids,
            deleted_at_range=deleted_at_range,
        )
        return self._search_oapg(
            query_params=args.query,
        )

class Search(BaseApi):

    async def asearch(
        self,
        query: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        file_extensions: typing.Optional[typing.List[str]] = None,
        created_at_range: typing.Optional[typing.List[str]] = None,
        updated_at_range: typing.Optional[typing.List[str]] = None,
        size_range: typing.Optional[typing.List[int]] = None,
        owner_user_ids: typing.Optional[typing.List[str]] = None,
        recent_updater_user_ids: typing.Optional[typing.List[str]] = None,
        ancestor_folder_ids: typing.Optional[typing.List[str]] = None,
        content_types: typing.Optional[typing.List[str]] = None,
        type: typing.Optional[str] = None,
        trash_content: typing.Optional[str] = None,
        mdfilters: typing.Optional[typing.List[MetadataFilter]] = None,
        sort: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        include_recent_shared_links: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        deleted_user_ids: typing.Optional[typing.List[str]] = None,
        deleted_at_range: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> GetSearchResponsePydantic:
        raw_response = await self.raw.asearch(
            query=query,
            scope=scope,
            file_extensions=file_extensions,
            created_at_range=created_at_range,
            updated_at_range=updated_at_range,
            size_range=size_range,
            owner_user_ids=owner_user_ids,
            recent_updater_user_ids=recent_updater_user_ids,
            ancestor_folder_ids=ancestor_folder_ids,
            content_types=content_types,
            type=type,
            trash_content=trash_content,
            mdfilters=mdfilters,
            sort=sort,
            direction=direction,
            limit=limit,
            include_recent_shared_links=include_recent_shared_links,
            fields=fields,
            offset=offset,
            deleted_user_ids=deleted_user_ids,
            deleted_at_range=deleted_at_range,
            **kwargs,
        )
        if validate:
            return RootModel[GetSearchResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(GetSearchResponsePydantic, raw_response.body)
    
    
    def search(
        self,
        query: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        file_extensions: typing.Optional[typing.List[str]] = None,
        created_at_range: typing.Optional[typing.List[str]] = None,
        updated_at_range: typing.Optional[typing.List[str]] = None,
        size_range: typing.Optional[typing.List[int]] = None,
        owner_user_ids: typing.Optional[typing.List[str]] = None,
        recent_updater_user_ids: typing.Optional[typing.List[str]] = None,
        ancestor_folder_ids: typing.Optional[typing.List[str]] = None,
        content_types: typing.Optional[typing.List[str]] = None,
        type: typing.Optional[str] = None,
        trash_content: typing.Optional[str] = None,
        mdfilters: typing.Optional[typing.List[MetadataFilter]] = None,
        sort: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        include_recent_shared_links: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        deleted_user_ids: typing.Optional[typing.List[str]] = None,
        deleted_at_range: typing.Optional[typing.List[str]] = None,
        validate: bool = False,
    ) -> GetSearchResponsePydantic:
        raw_response = self.raw.search(
            query=query,
            scope=scope,
            file_extensions=file_extensions,
            created_at_range=created_at_range,
            updated_at_range=updated_at_range,
            size_range=size_range,
            owner_user_ids=owner_user_ids,
            recent_updater_user_ids=recent_updater_user_ids,
            ancestor_folder_ids=ancestor_folder_ids,
            content_types=content_types,
            type=type,
            trash_content=trash_content,
            mdfilters=mdfilters,
            sort=sort,
            direction=direction,
            limit=limit,
            include_recent_shared_links=include_recent_shared_links,
            fields=fields,
            offset=offset,
            deleted_user_ids=deleted_user_ids,
            deleted_at_range=deleted_at_range,
        )
        if validate:
            return RootModel[GetSearchResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(GetSearchResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        query: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        file_extensions: typing.Optional[typing.List[str]] = None,
        created_at_range: typing.Optional[typing.List[str]] = None,
        updated_at_range: typing.Optional[typing.List[str]] = None,
        size_range: typing.Optional[typing.List[int]] = None,
        owner_user_ids: typing.Optional[typing.List[str]] = None,
        recent_updater_user_ids: typing.Optional[typing.List[str]] = None,
        ancestor_folder_ids: typing.Optional[typing.List[str]] = None,
        content_types: typing.Optional[typing.List[str]] = None,
        type: typing.Optional[str] = None,
        trash_content: typing.Optional[str] = None,
        mdfilters: typing.Optional[typing.List[MetadataFilter]] = None,
        sort: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        include_recent_shared_links: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        deleted_user_ids: typing.Optional[typing.List[str]] = None,
        deleted_at_range: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._search_mapped_args(
            query=query,
            scope=scope,
            file_extensions=file_extensions,
            created_at_range=created_at_range,
            updated_at_range=updated_at_range,
            size_range=size_range,
            owner_user_ids=owner_user_ids,
            recent_updater_user_ids=recent_updater_user_ids,
            ancestor_folder_ids=ancestor_folder_ids,
            content_types=content_types,
            type=type,
            trash_content=trash_content,
            mdfilters=mdfilters,
            sort=sort,
            direction=direction,
            limit=limit,
            include_recent_shared_links=include_recent_shared_links,
            fields=fields,
            offset=offset,
            deleted_user_ids=deleted_user_ids,
            deleted_at_range=deleted_at_range,
        )
        return await self._asearch_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        query: typing.Optional[str] = None,
        scope: typing.Optional[str] = None,
        file_extensions: typing.Optional[typing.List[str]] = None,
        created_at_range: typing.Optional[typing.List[str]] = None,
        updated_at_range: typing.Optional[typing.List[str]] = None,
        size_range: typing.Optional[typing.List[int]] = None,
        owner_user_ids: typing.Optional[typing.List[str]] = None,
        recent_updater_user_ids: typing.Optional[typing.List[str]] = None,
        ancestor_folder_ids: typing.Optional[typing.List[str]] = None,
        content_types: typing.Optional[typing.List[str]] = None,
        type: typing.Optional[str] = None,
        trash_content: typing.Optional[str] = None,
        mdfilters: typing.Optional[typing.List[MetadataFilter]] = None,
        sort: typing.Optional[str] = None,
        direction: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        include_recent_shared_links: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        offset: typing.Optional[int] = None,
        deleted_user_ids: typing.Optional[typing.List[str]] = None,
        deleted_at_range: typing.Optional[typing.List[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._search_mapped_args(
            query=query,
            scope=scope,
            file_extensions=file_extensions,
            created_at_range=created_at_range,
            updated_at_range=updated_at_range,
            size_range=size_range,
            owner_user_ids=owner_user_ids,
            recent_updater_user_ids=recent_updater_user_ids,
            ancestor_folder_ids=ancestor_folder_ids,
            content_types=content_types,
            type=type,
            trash_content=trash_content,
            mdfilters=mdfilters,
            sort=sort,
            direction=direction,
            limit=limit,
            include_recent_shared_links=include_recent_shared_links,
            fields=fields,
            offset=offset,
            deleted_user_ids=deleted_user_ids,
            deleted_at_range=deleted_at_range,
        )
        return self._search_oapg(
            query_params=args.query,
        )

