# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.files_upload_sessions_upload_session_id_commit.post import CommitSessionRaw
from box_python_sdk.paths.files_upload_sessions.post import CreateSessionForUploadRaw
from box_python_sdk.paths.files_file_id_upload_sessions.post import CreateSessionForUpload0Raw
from box_python_sdk.paths.files_upload_sessions_upload_session_id.put import FilePartUpdateRaw
from box_python_sdk.paths.files_upload_sessions_upload_session_id.get import InfoRaw
from box_python_sdk.paths.files_upload_sessions_upload_session_id_parts.get import ListPartsRaw
from box_python_sdk.paths.files_upload_sessions_upload_session_id.delete import RemoveUploadSessionRaw


class UploadsChunkedApiRaw(
    CommitSessionRaw,
    CreateSessionForUploadRaw,
    CreateSessionForUpload0Raw,
    FilePartUpdateRaw,
    InfoRaw,
    ListPartsRaw,
    RemoveUploadSessionRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass