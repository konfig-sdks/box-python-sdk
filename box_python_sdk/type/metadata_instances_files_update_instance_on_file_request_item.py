# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


RequiredMetadataInstancesFilesUpdateInstanceOnFileRequestItem = TypedDict("RequiredMetadataInstancesFilesUpdateInstanceOnFileRequestItem", {
    })

OptionalMetadataInstancesFilesUpdateInstanceOnFileRequestItem = TypedDict("OptionalMetadataInstancesFilesUpdateInstanceOnFileRequestItem", {
    # The type of change to perform on the template. Some of these are hazardous as they will change existing templates.
    "op": str,

    # The location in the metadata JSON object to apply the changes to, in the format of a [JSON-Pointer](https://tools.ietf.org/html/rfc6901).  The path must always be prefixed with a `/` to represent the root of the template. The characters `~` and `/` are reserved characters and must be escaped in the key.
    "path": str,

    # The value to be set or tested.  Required for `add`, `replace`, and `test` operations. For `add`, if the value exists already the previous value will be overwritten by the new value. For `replace`, the value must exist before replacing.  For `test`, the existing value at the `path` location must match the specified value.
    "value": str,

    # The location in the metadata JSON object to move or copy a value from. Required for `move` or `copy` operations and must be in the format of a [JSON-Pointer](https://tools.ietf.org/html/rfc6901).
    "from": str,
    }, total=False)

class MetadataInstancesFilesUpdateInstanceOnFileRequestItem(RequiredMetadataInstancesFilesUpdateInstanceOnFileRequestItem, OptionalMetadataInstancesFilesUpdateInstanceOnFileRequestItem):
    pass
