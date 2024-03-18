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


class RequiredEmailAliasesCreateNewAliasRequest(TypedDict):
    # The email address to add to the account as an alias.  Note: The domain of the email alias needs to be registered  to your enterprise. See the [domain verification guide](https://support.box.com/hc/en-us/articles/4408619650579-Domain-Verification) for steps to add a new domain.
    email: str

class OptionalEmailAliasesCreateNewAliasRequest(TypedDict, total=False):
    pass

class EmailAliasesCreateNewAliasRequest(RequiredEmailAliasesCreateNewAliasRequest, OptionalEmailAliasesCreateNewAliasRequest):
    pass
