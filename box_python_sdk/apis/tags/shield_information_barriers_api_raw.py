# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.shield_information_barriers_change_status.post import AddChangedStatusRaw
from box_python_sdk.paths.shield_information_barriers.post import CreateBarrierRaw
from box_python_sdk.paths.shield_information_barriers_shield_information_barrier_id.get import GetByIdRaw
from box_python_sdk.paths.shield_information_barriers.get import ListInformationObjectsRaw


class ShieldInformationBarriersApiRaw(
    AddChangedStatusRaw,
    CreateBarrierRaw,
    GetByIdRaw,
    ListInformationObjectsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
