# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.shield_information_barrier_reports.post import CreateReport
from box_python_sdk.paths.shield_information_barrier_reports_shield_information_barrier_report_id.get import GetById
from box_python_sdk.paths.shield_information_barrier_reports.get import ListReports
from box_python_sdk.apis.tags.shield_information_barrier_reports_api_raw import ShieldInformationBarrierReportsApiRaw


class ShieldInformationBarrierReportsApi(
    CreateReport,
    GetById,
    ListReports,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ShieldInformationBarrierReportsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ShieldInformationBarrierReportsApiRaw(api_client)
