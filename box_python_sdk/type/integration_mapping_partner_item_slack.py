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


class RequiredIntegrationMappingPartnerItemSlack(TypedDict):
    # Type of the mapped item referenced in `id`
    type: str

    # ID of the mapped item (of type referenced in `type`)
    id: str

class OptionalIntegrationMappingPartnerItemSlack(TypedDict, total=False):
    # ID of the Slack workspace with which the item is associated. Use this parameter if Box for Slack is installed at a workspace level. Do not use `slack_org_id` at the same time.
    slack_workspace_id: typing.Optional[str]

    # ID of the Slack org with which the item is associated. Use this parameter if Box for Slack is installed at the org level. Do not use `slack_workspace_id` at the same time.
    slack_org_id: typing.Optional[str]

class IntegrationMappingPartnerItemSlack(RequiredIntegrationMappingPartnerItemSlack, OptionalIntegrationMappingPartnerItemSlack):
    pass
