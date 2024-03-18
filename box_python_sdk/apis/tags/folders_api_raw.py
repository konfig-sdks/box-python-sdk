# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.folders_folder_id_copy.post import CreateCopyRaw
from box_python_sdk.paths.folders_folder_id.delete import DeleteByIdRaw
from box_python_sdk.paths.folders.post import FoldersRaw
from box_python_sdk.paths.folders_folder_id.get import GetFolderDetailsRaw
from box_python_sdk.paths.folders_folder_id_items.get import ListItemsInFolderRaw
from box_python_sdk.paths.folders_folder_id.put import UpdateFolderRaw


class FoldersApiRaw(
    CreateCopyRaw,
    DeleteByIdRaw,
    FoldersRaw,
    GetFolderDetailsRaw,
    ListItemsInFolderRaw,
    UpdateFolderRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
