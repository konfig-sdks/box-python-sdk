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

from box_python_sdk.model.events import Events as EventsSchema
from box_python_sdk.model.client_error import ClientError as ClientErrorSchema

from box_python_sdk.type.events import Events
from box_python_sdk.type.client_error import ClientError

from ...api_client import Dictionary
from box_python_sdk.pydantic.client_error import ClientError as ClientErrorPydantic
from box_python_sdk.pydantic.events import Events as EventsPydantic

# Query params


class StreamTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def ALL(cls):
        return cls("all")
    
    @schemas.classproperty
    def CHANGES(cls):
        return cls("changes")
    
    @schemas.classproperty
    def SYNC(cls):
        return cls("sync")
    
    @schemas.classproperty
    def ADMIN_LOGS(cls):
        return cls("admin_logs")
    
    @schemas.classproperty
    def ADMIN_LOGS_STREAMING(cls):
        return cls("admin_logs_streaming")
StreamPositionSchema = schemas.StrSchema


class LimitSchema(
    schemas.Int64Schema
):
    pass


class EventTypeSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def ACCESS_GRANTED(cls):
                return cls("ACCESS_GRANTED")
            
            @schemas.classproperty
            def ACCESS_REVOKED(cls):
                return cls("ACCESS_REVOKED")
            
            @schemas.classproperty
            def ADD_DEVICE_ASSOCIATION(cls):
                return cls("ADD_DEVICE_ASSOCIATION")
            
            @schemas.classproperty
            def ADD_LOGIN_ACTIVITY_DEVICE(cls):
                return cls("ADD_LOGIN_ACTIVITY_DEVICE")
            
            @schemas.classproperty
            def ADMIN_LOGIN(cls):
                return cls("ADMIN_LOGIN")
            
            @schemas.classproperty
            def APPLICATION_CREATED(cls):
                return cls("APPLICATION_CREATED")
            
            @schemas.classproperty
            def APPLICATION_PUBLIC_KEY_ADDED(cls):
                return cls("APPLICATION_PUBLIC_KEY_ADDED")
            
            @schemas.classproperty
            def APPLICATION_PUBLIC_KEY_DELETED(cls):
                return cls("APPLICATION_PUBLIC_KEY_DELETED")
            
            @schemas.classproperty
            def CHANGE_ADMIN_ROLE(cls):
                return cls("CHANGE_ADMIN_ROLE")
            
            @schemas.classproperty
            def CHANGE_FOLDER_PERMISSION(cls):
                return cls("CHANGE_FOLDER_PERMISSION")
            
            @schemas.classproperty
            def COLLABORATION_ACCEPT(cls):
                return cls("COLLABORATION_ACCEPT")
            
            @schemas.classproperty
            def COLLABORATION_EXPIRATION(cls):
                return cls("COLLABORATION_EXPIRATION")
            
            @schemas.classproperty
            def COLLABORATION_INVITE(cls):
                return cls("COLLABORATION_INVITE")
            
            @schemas.classproperty
            def COLLABORATION_REMOVE(cls):
                return cls("COLLABORATION_REMOVE")
            
            @schemas.classproperty
            def COLLABORATION_ROLE_CHANGE(cls):
                return cls("COLLABORATION_ROLE_CHANGE")
            
            @schemas.classproperty
            def COMMENT_CREATE(cls):
                return cls("COMMENT_CREATE")
            
            @schemas.classproperty
            def COMMENT_DELETE(cls):
                return cls("COMMENT_DELETE")
            
            @schemas.classproperty
            def CONTENT_WORKFLOW_ABNORMAL_DOWNLOAD_ACTIVITY(cls):
                return cls("CONTENT_WORKFLOW_ABNORMAL_DOWNLOAD_ACTIVITY")
            
            @schemas.classproperty
            def CONTENT_WORKFLOW_AUTOMATION_ADD(cls):
                return cls("CONTENT_WORKFLOW_AUTOMATION_ADD")
            
            @schemas.classproperty
            def CONTENT_WORKFLOW_AUTOMATION_DELETE(cls):
                return cls("CONTENT_WORKFLOW_AUTOMATION_DELETE")
            
            @schemas.classproperty
            def CONTENT_WORKFLOW_POLICY_ADD(cls):
                return cls("CONTENT_WORKFLOW_POLICY_ADD")
            
            @schemas.classproperty
            def CONTENT_WORKFLOW_SHARING_POLICY_VIOLATION(cls):
                return cls("CONTENT_WORKFLOW_SHARING_POLICY_VIOLATION")
            
            @schemas.classproperty
            def CONTENT_WORKFLOW_UPLOAD_POLICY_VIOLATION(cls):
                return cls("CONTENT_WORKFLOW_UPLOAD_POLICY_VIOLATION")
            
            @schemas.classproperty
            def COPY(cls):
                return cls("COPY")
            
            @schemas.classproperty
            def DATA_RETENTION_CREATE_RETENTION(cls):
                return cls("DATA_RETENTION_CREATE_RETENTION")
            
            @schemas.classproperty
            def DATA_RETENTION_REMOVE_RETENTION(cls):
                return cls("DATA_RETENTION_REMOVE_RETENTION")
            
            @schemas.classproperty
            def DELETE(cls):
                return cls("DELETE")
            
            @schemas.classproperty
            def DELETE_USER(cls):
                return cls("DELETE_USER")
            
            @schemas.classproperty
            def DEVICE_TRUST_CHECK_FAILED(cls):
                return cls("DEVICE_TRUST_CHECK_FAILED")
            
            @schemas.classproperty
            def DOWNLOAD(cls):
                return cls("DOWNLOAD")
            
            @schemas.classproperty
            def EDIT(cls):
                return cls("EDIT")
            
            @schemas.classproperty
            def EDIT_USER(cls):
                return cls("EDIT_USER")
            
            @schemas.classproperty
            def EMAIL_ALIAS_CONFIRM(cls):
                return cls("EMAIL_ALIAS_CONFIRM")
            
            @schemas.classproperty
            def EMAIL_ALIAS_REMOVE(cls):
                return cls("EMAIL_ALIAS_REMOVE")
            
            @schemas.classproperty
            def ENTERPRISE_APP_AUTHORIZATION_UPDATE(cls):
                return cls("ENTERPRISE_APP_AUTHORIZATION_UPDATE")
            
            @schemas.classproperty
            def EXTERNAL_COLLAB_SECURITY_SETTINGS(cls):
                return cls("EXTERNAL_COLLAB_SECURITY_SETTINGS")
            
            @schemas.classproperty
            def FAILED_LOGIN(cls):
                return cls("FAILED_LOGIN")
            
            @schemas.classproperty
            def FILE_MARKED_MALICIOUS(cls):
                return cls("FILE_MARKED_MALICIOUS")
            
            @schemas.classproperty
            def FILE_WATERMARKED_DOWNLOAD(cls):
                return cls("FILE_WATERMARKED_DOWNLOAD")
            
            @schemas.classproperty
            def GROUP_ADD_ITEM(cls):
                return cls("GROUP_ADD_ITEM")
            
            @schemas.classproperty
            def GROUP_ADD_USER(cls):
                return cls("GROUP_ADD_USER")
            
            @schemas.classproperty
            def GROUP_CREATION(cls):
                return cls("GROUP_CREATION")
            
            @schemas.classproperty
            def GROUP_DELETION(cls):
                return cls("GROUP_DELETION")
            
            @schemas.classproperty
            def GROUP_EDITED(cls):
                return cls("GROUP_EDITED")
            
            @schemas.classproperty
            def GROUP_REMOVE_ITEM(cls):
                return cls("GROUP_REMOVE_ITEM")
            
            @schemas.classproperty
            def GROUP_REMOVE_USER(cls):
                return cls("GROUP_REMOVE_USER")
            
            @schemas.classproperty
            def ITEM_MODIFY(cls):
                return cls("ITEM_MODIFY")
            
            @schemas.classproperty
            def ITEM_OPEN(cls):
                return cls("ITEM_OPEN")
            
            @schemas.classproperty
            def ITEM_SHARED_UPDATE(cls):
                return cls("ITEM_SHARED_UPDATE")
            
            @schemas.classproperty
            def ITEM_SYNC(cls):
                return cls("ITEM_SYNC")
            
            @schemas.classproperty
            def ITEM_UNSYNC(cls):
                return cls("ITEM_UNSYNC")
            
            @schemas.classproperty
            def LEGAL_HOLD_ASSIGNMENT_CREATE(cls):
                return cls("LEGAL_HOLD_ASSIGNMENT_CREATE")
            
            @schemas.classproperty
            def LEGAL_HOLD_ASSIGNMENT_DELETE(cls):
                return cls("LEGAL_HOLD_ASSIGNMENT_DELETE")
            
            @schemas.classproperty
            def LEGAL_HOLD_POLICY_CREATE(cls):
                return cls("LEGAL_HOLD_POLICY_CREATE")
            
            @schemas.classproperty
            def LEGAL_HOLD_POLICY_DELETE(cls):
                return cls("LEGAL_HOLD_POLICY_DELETE")
            
            @schemas.classproperty
            def LEGAL_HOLD_POLICY_UPDATE(cls):
                return cls("LEGAL_HOLD_POLICY_UPDATE")
            
            @schemas.classproperty
            def LOCK(cls):
                return cls("LOCK")
            
            @schemas.classproperty
            def LOGIN(cls):
                return cls("LOGIN")
            
            @schemas.classproperty
            def METADATA_INSTANCE_CREATE(cls):
                return cls("METADATA_INSTANCE_CREATE")
            
            @schemas.classproperty
            def METADATA_INSTANCE_DELETE(cls):
                return cls("METADATA_INSTANCE_DELETE")
            
            @schemas.classproperty
            def METADATA_INSTANCE_UPDATE(cls):
                return cls("METADATA_INSTANCE_UPDATE")
            
            @schemas.classproperty
            def METADATA_TEMPLATE_CREATE(cls):
                return cls("METADATA_TEMPLATE_CREATE")
            
            @schemas.classproperty
            def METADATA_TEMPLATE_DELETE(cls):
                return cls("METADATA_TEMPLATE_DELETE")
            
            @schemas.classproperty
            def METADATA_TEMPLATE_UPDATE(cls):
                return cls("METADATA_TEMPLATE_UPDATE")
            
            @schemas.classproperty
            def MOVE(cls):
                return cls("MOVE")
            
            @schemas.classproperty
            def NEW_USER(cls):
                return cls("NEW_USER")
            
            @schemas.classproperty
            def OAUTH2_ACCESS_TOKEN_REVOKE(cls):
                return cls("OAUTH2_ACCESS_TOKEN_REVOKE")
            
            @schemas.classproperty
            def PREVIEW(cls):
                return cls("PREVIEW")
            
            @schemas.classproperty
            def REMOVE_DEVICE_ASSOCIATION(cls):
                return cls("REMOVE_DEVICE_ASSOCIATION")
            
            @schemas.classproperty
            def REMOVE_LOGIN_ACTIVITY_DEVICE(cls):
                return cls("REMOVE_LOGIN_ACTIVITY_DEVICE")
            
            @schemas.classproperty
            def RENAME(cls):
                return cls("RENAME")
            
            @schemas.classproperty
            def RETENTION_POLICY_ASSIGNMENT_ADD(cls):
                return cls("RETENTION_POLICY_ASSIGNMENT_ADD")
            
            @schemas.classproperty
            def SHARE(cls):
                return cls("SHARE")
            
            @schemas.classproperty
            def SHARE_EXPIRATION(cls):
                return cls("SHARE_EXPIRATION")
            
            @schemas.classproperty
            def SHIELD_ALERT(cls):
                return cls("SHIELD_ALERT")
            
            @schemas.classproperty
            def SHIELD_EXTERNAL_COLLAB_ACCESS_BLOCKED(cls):
                return cls("SHIELD_EXTERNAL_COLLAB_ACCESS_BLOCKED")
            
            @schemas.classproperty
            def SHIELD_EXTERNAL_COLLAB_ACCESS_BLOCKED_MISSING_JUSTIFICATION(cls):
                return cls("SHIELD_EXTERNAL_COLLAB_ACCESS_BLOCKED_MISSING_JUSTIFICATION")
            
            @schemas.classproperty
            def SHIELD_EXTERNAL_COLLAB_INVITE_BLOCKED(cls):
                return cls("SHIELD_EXTERNAL_COLLAB_INVITE_BLOCKED")
            
            @schemas.classproperty
            def SHIELD_EXTERNAL_COLLAB_INVITE_BLOCKED_MISSING_JUSTIFICATION(cls):
                return cls("SHIELD_EXTERNAL_COLLAB_INVITE_BLOCKED_MISSING_JUSTIFICATION")
            
            @schemas.classproperty
            def SHIELD_JUSTIFICATION_APPROVAL(cls):
                return cls("SHIELD_JUSTIFICATION_APPROVAL")
            
            @schemas.classproperty
            def SHIELD_SHARED_LINK_ACCESS_BLOCKED(cls):
                return cls("SHIELD_SHARED_LINK_ACCESS_BLOCKED")
            
            @schemas.classproperty
            def SHIELD_SHARED_LINK_STATUS_RESTRICTED_ON_CREATE(cls):
                return cls("SHIELD_SHARED_LINK_STATUS_RESTRICTED_ON_CREATE")
            
            @schemas.classproperty
            def SHIELD_SHARED_LINK_STATUS_RESTRICTED_ON_UPDATE(cls):
                return cls("SHIELD_SHARED_LINK_STATUS_RESTRICTED_ON_UPDATE")
            
            @schemas.classproperty
            def SIGN_DOCUMENT_ASSIGNED(cls):
                return cls("SIGN_DOCUMENT_ASSIGNED")
            
            @schemas.classproperty
            def SIGN_DOCUMENT_CANCELLED(cls):
                return cls("SIGN_DOCUMENT_CANCELLED")
            
            @schemas.classproperty
            def SIGN_DOCUMENT_COMPLETED(cls):
                return cls("SIGN_DOCUMENT_COMPLETED")
            
            @schemas.classproperty
            def SIGN_DOCUMENT_CONVERTED(cls):
                return cls("SIGN_DOCUMENT_CONVERTED")
            
            @schemas.classproperty
            def SIGN_DOCUMENT_CREATED(cls):
                return cls("SIGN_DOCUMENT_CREATED")
            
            @schemas.classproperty
            def SIGN_DOCUMENT_DECLINED(cls):
                return cls("SIGN_DOCUMENT_DECLINED")
            
            @schemas.classproperty
            def SIGN_DOCUMENT_EXPIRED(cls):
                return cls("SIGN_DOCUMENT_EXPIRED")
            
            @schemas.classproperty
            def SIGN_DOCUMENT_SIGNED(cls):
                return cls("SIGN_DOCUMENT_SIGNED")
            
            @schemas.classproperty
            def SIGN_DOCUMENT_VIEWED_BY_SIGNED(cls):
                return cls("SIGN_DOCUMENT_VIEWED_BY_SIGNED")
            
            @schemas.classproperty
            def SIGNER_DOWNLOADED(cls):
                return cls("SIGNER_DOWNLOADED")
            
            @schemas.classproperty
            def SIGNER_FORWARDED(cls):
                return cls("SIGNER_FORWARDED")
            
            @schemas.classproperty
            def STORAGE_EXPIRATION(cls):
                return cls("STORAGE_EXPIRATION")
            
            @schemas.classproperty
            def TASK_ASSIGNMENT_CREATE(cls):
                return cls("TASK_ASSIGNMENT_CREATE")
            
            @schemas.classproperty
            def TASK_ASSIGNMENT_DELETE(cls):
                return cls("TASK_ASSIGNMENT_DELETE")
            
            @schemas.classproperty
            def TASK_ASSIGNMENT_UPDATE(cls):
                return cls("TASK_ASSIGNMENT_UPDATE")
            
            @schemas.classproperty
            def TASK_CREATE(cls):
                return cls("TASK_CREATE")
            
            @schemas.classproperty
            def TASK_UPDATE(cls):
                return cls("TASK_UPDATE")
            
            @schemas.classproperty
            def TERMS_OF_SERVICE_ACCEPT(cls):
                return cls("TERMS_OF_SERVICE_ACCEPT")
            
            @schemas.classproperty
            def TERMS_OF_SERVICE_REJECT(cls):
                return cls("TERMS_OF_SERVICE_REJECT")
            
            @schemas.classproperty
            def UNDELETE(cls):
                return cls("UNDELETE")
            
            @schemas.classproperty
            def UNLOCK(cls):
                return cls("UNLOCK")
            
            @schemas.classproperty
            def UNSHARE(cls):
                return cls("UNSHARE")
            
            @schemas.classproperty
            def UPDATE_COLLABORATION_EXPIRATION(cls):
                return cls("UPDATE_COLLABORATION_EXPIRATION")
            
            @schemas.classproperty
            def UPDATE_SHARE_EXPIRATION(cls):
                return cls("UPDATE_SHARE_EXPIRATION")
            
            @schemas.classproperty
            def UPLOAD(cls):
                return cls("UPLOAD")
            
            @schemas.classproperty
            def USER_AUTHENTICATE_OAUTH2_ACCESS_TOKEN_CREATE(cls):
                return cls("USER_AUTHENTICATE_OAUTH2_ACCESS_TOKEN_CREATE")
            
            @schemas.classproperty
            def WATERMARK_LABEL_CREATE(cls):
                return cls("WATERMARK_LABEL_CREATE")
            
            @schemas.classproperty
            def WATERMARK_LABEL_DELETE(cls):
                return cls("WATERMARK_LABEL_DELETE")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EventTypeSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
CreatedAfterSchema = schemas.DateTimeSchema
CreatedBeforeSchema = schemas.DateTimeSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'stream_type': typing.Union[StreamTypeSchema, str, ],
        'stream_position': typing.Union[StreamPositionSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'event_type': typing.Union[EventTypeSchema, list, tuple, ],
        'created_after': typing.Union[CreatedAfterSchema, str, datetime, ],
        'created_before': typing.Union[CreatedBeforeSchema, str, datetime, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_stream_type = api_client.QueryParameter(
    name="stream_type",
    style=api_client.ParameterStyle.FORM,
    schema=StreamTypeSchema,
    explode=True,
)
request_query_stream_position = api_client.QueryParameter(
    name="stream_position",
    style=api_client.ParameterStyle.FORM,
    schema=StreamPositionSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_event_type = api_client.QueryParameter(
    name="event_type",
    style=api_client.ParameterStyle.FORM,
    schema=EventTypeSchema,
)
request_query_created_after = api_client.QueryParameter(
    name="created_after",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedAfterSchema,
    explode=True,
)
request_query_created_before = api_client.QueryParameter(
    name="created_before",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedBeforeSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = EventsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Events


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Events


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

    def _events_mapped_args(
        self,
        stream_type: typing.Optional[str] = None,
        stream_position: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        event_type: typing.Optional[typing.List[str]] = None,
        created_after: typing.Optional[datetime] = None,
        created_before: typing.Optional[datetime] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if stream_type is not None:
            _query_params["stream_type"] = stream_type
        if stream_position is not None:
            _query_params["stream_position"] = stream_position
        if limit is not None:
            _query_params["limit"] = limit
        if event_type is not None:
            _query_params["event_type"] = event_type
        if created_after is not None:
            _query_params["created_after"] = created_after
        if created_before is not None:
            _query_params["created_before"] = created_before
        args.query = _query_params
        return args

    async def _aevents_oapg(
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
        List user and enterprise events
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_stream_type,
            request_query_stream_position,
            request_query_limit,
            request_query_event_type,
            request_query_created_after,
            request_query_created_before,
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
            path_template='/events',
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


    def _events_oapg(
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
        List user and enterprise events
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_stream_type,
            request_query_stream_position,
            request_query_limit,
            request_query_event_type,
            request_query_created_after,
            request_query_created_before,
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
            path_template='/events',
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


class EventsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aevents(
        self,
        stream_type: typing.Optional[str] = None,
        stream_position: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        event_type: typing.Optional[typing.List[str]] = None,
        created_after: typing.Optional[datetime] = None,
        created_before: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._events_mapped_args(
            stream_type=stream_type,
            stream_position=stream_position,
            limit=limit,
            event_type=event_type,
            created_after=created_after,
            created_before=created_before,
        )
        return await self._aevents_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def events(
        self,
        stream_type: typing.Optional[str] = None,
        stream_position: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        event_type: typing.Optional[typing.List[str]] = None,
        created_after: typing.Optional[datetime] = None,
        created_before: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._events_mapped_args(
            stream_type=stream_type,
            stream_position=stream_position,
            limit=limit,
            event_type=event_type,
            created_after=created_after,
            created_before=created_before,
        )
        return self._events_oapg(
            query_params=args.query,
        )

class Events(BaseApi):

    async def aevents(
        self,
        stream_type: typing.Optional[str] = None,
        stream_position: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        event_type: typing.Optional[typing.List[str]] = None,
        created_after: typing.Optional[datetime] = None,
        created_before: typing.Optional[datetime] = None,
        validate: bool = False,
        **kwargs,
    ) -> EventsPydantic:
        raw_response = await self.raw.aevents(
            stream_type=stream_type,
            stream_position=stream_position,
            limit=limit,
            event_type=event_type,
            created_after=created_after,
            created_before=created_before,
            **kwargs,
        )
        if validate:
            return EventsPydantic(**raw_response.body)
        return api_client.construct_model_instance(EventsPydantic, raw_response.body)
    
    
    def events(
        self,
        stream_type: typing.Optional[str] = None,
        stream_position: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        event_type: typing.Optional[typing.List[str]] = None,
        created_after: typing.Optional[datetime] = None,
        created_before: typing.Optional[datetime] = None,
        validate: bool = False,
    ) -> EventsPydantic:
        raw_response = self.raw.events(
            stream_type=stream_type,
            stream_position=stream_position,
            limit=limit,
            event_type=event_type,
            created_after=created_after,
            created_before=created_before,
        )
        if validate:
            return EventsPydantic(**raw_response.body)
        return api_client.construct_model_instance(EventsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        stream_type: typing.Optional[str] = None,
        stream_position: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        event_type: typing.Optional[typing.List[str]] = None,
        created_after: typing.Optional[datetime] = None,
        created_before: typing.Optional[datetime] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._events_mapped_args(
            stream_type=stream_type,
            stream_position=stream_position,
            limit=limit,
            event_type=event_type,
            created_after=created_after,
            created_before=created_before,
        )
        return await self._aevents_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        stream_type: typing.Optional[str] = None,
        stream_position: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        event_type: typing.Optional[typing.List[str]] = None,
        created_after: typing.Optional[datetime] = None,
        created_before: typing.Optional[datetime] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._events_mapped_args(
            stream_type=stream_type,
            stream_position=stream_position,
            limit=limit,
            event_type=event_type,
            created_after=created_after,
            created_before=created_before,
        )
        return self._events_oapg(
            query_params=args.query,
        )

