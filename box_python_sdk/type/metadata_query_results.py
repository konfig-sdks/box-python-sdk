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

from box_python_sdk.type.metadata_query_results_entries import MetadataQueryResultsEntries

class RequiredMetadataQueryResults(TypedDict):
    pass

class OptionalMetadataQueryResults(TypedDict, total=False):
    entries: MetadataQueryResultsEntries

    # The limit that was used for this search. This will be the same as the `limit` query parameter unless that value exceeded the maximum value allowed.
    limit: int

    # The marker for the start of the next page of results.
    next_marker: str

class MetadataQueryResults(RequiredMetadataQueryResults, OptionalMetadataQueryResults):
    pass
