# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.files_file_id_copy.post import CreateCopy
from box_python_sdk.paths.files_file_id.delete import DeleteFile
from box_python_sdk.paths.files_file_id.get import GetDetails
from box_python_sdk.paths.files_file_id_thumbnail_extension.get import GetThumbnail
from box_python_sdk.paths.files_content.options import PreflightCheckBeforeUpload
from box_python_sdk.paths.files_file_id.put import UpdateFile
from box_python_sdk.apis.tags.files_api_raw import FilesApiRaw


class FilesApi(
    CreateCopy,
    DeleteFile,
    GetDetails,
    GetThumbnail,
    PreflightCheckBeforeUpload,
    UpdateFile,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: FilesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = FilesApiRaw(api_client)
