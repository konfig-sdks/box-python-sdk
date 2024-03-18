# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.files_file_id_metadata_scope_template_key.post import ApplyTemplate
from box_python_sdk.paths.files_file_id_metadata_scope_template_key.get import GetInstance
from box_python_sdk.paths.files_file_id_metadata.get import ListFileMetadata
from box_python_sdk.paths.files_file_id_metadata_scope_template_key.delete import RemoveInstance
from box_python_sdk.paths.files_file_id_metadata_scope_template_key.put import UpdateInstanceOnFile
from box_python_sdk.apis.tags.metadata_instances_files_api_raw import MetadataInstancesFilesApiRaw


class MetadataInstancesFilesApi(
    ApplyTemplate,
    GetInstance,
    ListFileMetadata,
    RemoveInstance,
    UpdateInstanceOnFile,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MetadataInstancesFilesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MetadataInstancesFilesApiRaw(api_client)
