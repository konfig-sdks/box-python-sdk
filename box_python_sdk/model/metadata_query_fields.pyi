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


class MetadataQueryFields(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    By default, this endpoint returns only the most basic info about the items for
which the query matches. This attribute can be used to specify a list of
additional attributes to return for any item, including its metadata.

This attribute takes a list of item fields, metadata template identifiers,
or metadata template field identifiers.

For example:

* `created_by` will add the details of the user who created the item to
the response.
* `metadata.<scope>.<templateKey>` will return the mini-representation
of the metadata instance identified by the `scope` and `templateKey`.
* `metadata.<scope>.<templateKey>.<field>` will return all the mini-representation
of the metadata instance identified by the `scope` and `templateKey` plus
the field specified by the `field` name. Multiple fields for the same
`scope` and `templateKey` can be defined.
    """


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MetadataQueryFields':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)