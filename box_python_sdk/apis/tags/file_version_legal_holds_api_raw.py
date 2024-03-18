# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.file_version_legal_holds_file_version_legal_hold_id.get import GetFileVersionLegalHoldInfoRaw
from box_python_sdk.paths.file_version_legal_holds.get import ListFileVersionLegalHoldsRaw


class FileVersionLegalHoldsApiRaw(
    GetFileVersionLegalHoldInfoRaw,
    ListFileVersionLegalHoldsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
