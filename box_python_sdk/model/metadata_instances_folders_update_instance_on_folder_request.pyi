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


class MetadataInstancesFoldersUpdateInstanceOnFolderRequest(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    A [JSON-Patch](https://tools.ietf.org/html/rfc6902)
specification for the changes to make to the metadata
instance.

The changes are represented as a JSON array of
operation objects.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['MetadataInstancesFoldersUpdateInstanceOnFolderRequestItem']:
            return MetadataInstancesFoldersUpdateInstanceOnFolderRequestItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['MetadataInstancesFoldersUpdateInstanceOnFolderRequestItem'], typing.List['MetadataInstancesFoldersUpdateInstanceOnFolderRequestItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MetadataInstancesFoldersUpdateInstanceOnFolderRequest':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'MetadataInstancesFoldersUpdateInstanceOnFolderRequestItem':
        return super().__getitem__(i)

from box_python_sdk.model.metadata_instances_folders_update_instance_on_folder_request_item import MetadataInstancesFoldersUpdateInstanceOnFolderRequestItem