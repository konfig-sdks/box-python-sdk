# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

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


class WorkflowsStartBasedOnRequestRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "folder",
            "files",
            "flow",
        }
        
        class properties:
        
            @staticmethod
            def flow() -> typing.Type['WorkflowsStartBasedOnRequestRequestFlow']:
                return WorkflowsStartBasedOnRequestRequestFlow
        
            @staticmethod
            def files() -> typing.Type['WorkflowsStartBasedOnRequestRequestFiles']:
                return WorkflowsStartBasedOnRequestRequestFiles
        
            @staticmethod
            def folder() -> typing.Type['WorkflowsStartBasedOnRequestRequestFolder']:
                return WorkflowsStartBasedOnRequestRequestFolder
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def WORKFLOW_PARAMETERS(cls):
                    return cls("workflow_parameters")
            
            
            class outcomes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Outcome']:
                        return Outcome
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Outcome'], typing.List['Outcome']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'outcomes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Outcome':
                    return super().__getitem__(i)
            __annotations__ = {
                "flow": flow,
                "files": files,
                "folder": folder,
                "type": type,
                "outcomes": outcomes,
            }
    
    folder: 'WorkflowsStartBasedOnRequestRequestFolder'
    files: 'WorkflowsStartBasedOnRequestRequestFiles'
    flow: 'WorkflowsStartBasedOnRequestRequestFlow'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flow"]) -> 'WorkflowsStartBasedOnRequestRequestFlow': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> 'WorkflowsStartBasedOnRequestRequestFiles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder"]) -> 'WorkflowsStartBasedOnRequestRequestFolder': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outcomes"]) -> MetaOapg.properties.outcomes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["flow", "files", "folder", "type", "outcomes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flow"]) -> 'WorkflowsStartBasedOnRequestRequestFlow': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> 'WorkflowsStartBasedOnRequestRequestFiles': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder"]) -> 'WorkflowsStartBasedOnRequestRequestFolder': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outcomes"]) -> typing.Union[MetaOapg.properties.outcomes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["flow", "files", "folder", "type", "outcomes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        folder: 'WorkflowsStartBasedOnRequestRequestFolder',
        files: 'WorkflowsStartBasedOnRequestRequestFiles',
        flow: 'WorkflowsStartBasedOnRequestRequestFlow',
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        outcomes: typing.Union[MetaOapg.properties.outcomes, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowsStartBasedOnRequestRequest':
        return super().__new__(
            cls,
            *args,
            folder=folder,
            files=files,
            flow=flow,
            type=type,
            outcomes=outcomes,
            _configuration=_configuration,
            **kwargs,
        )

from box_python_sdk.model.outcome import Outcome
from box_python_sdk.model.workflows_start_based_on_request_request_files import WorkflowsStartBasedOnRequestRequestFiles
from box_python_sdk.model.workflows_start_based_on_request_request_flow import WorkflowsStartBasedOnRequestRequestFlow
from box_python_sdk.model.workflows_start_based_on_request_request_folder import WorkflowsStartBasedOnRequestRequestFolder