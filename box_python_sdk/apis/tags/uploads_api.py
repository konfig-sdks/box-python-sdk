# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.files_file_id_content.post import FileContentUpdate
from box_python_sdk.paths.files_content.post import SmallFile
from box_python_sdk.apis.tags.uploads_api_raw import UploadsApiRaw


class UploadsApi(
    FileContentUpdate,
    SmallFile,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UploadsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UploadsApiRaw(api_client)