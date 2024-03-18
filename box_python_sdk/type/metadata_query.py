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

from box_python_sdk.type.metadata_query_fields import MetadataQueryFields
from box_python_sdk.type.metadata_query_order_by import MetadataQueryOrderBy
from box_python_sdk.type.metadata_query_query_params import MetadataQueryQueryParams

RequiredMetadataQuery = TypedDict("RequiredMetadataQuery", {
    # Specifies the template used in the query. Must be in the form `scope.templateKey`. Not all templates can be used in this field, most notably the built-in, Box-provided classification templates can not be used in a query.
    "from": str,

    # The ID of the folder that you are restricting the query to. A value of zero will return results from all folders you have access to. A non-zero value will only return results found in the folder corresponding to the ID or in any of its subfolders.
    "ancestor_folder_id": str,
    })

OptionalMetadataQuery = TypedDict("OptionalMetadataQuery", {
    # The query to perform. A query is a logical expression that is very similar to a SQL `SELECT` statement. Values in the search query can be turned into parameters specified in the `query_param` arguments list to prevent having to manually insert search values into the query string.  For example, a value of `:amount` would represent the `amount` value in `query_params` object.
    "query": str,

    "query_params": MetadataQueryQueryParams,

    "order_by": MetadataQueryOrderBy,

    # A value between 0 and 100 that indicates the maximum number of results to return for a single request. This only specifies a maximum boundary and will not guarantee the minimum number of results returned.
    "limit": int,

    # Marker to use for requesting the next page.
    "marker": str,

    "fields": MetadataQueryFields,
    }, total=False)

class MetadataQuery(RequiredMetadataQuery, OptionalMetadataQuery):
    pass
