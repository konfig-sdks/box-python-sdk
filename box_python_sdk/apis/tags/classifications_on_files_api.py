# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.files_file_id_metadata_enterprise_security_classification_6_vm_vochw_uwo.post import AddClassification
from box_python_sdk.paths.files_file_id_metadata_enterprise_security_classification_6_vm_vochw_uwo.get import GetClassificationMetadataInstance
from box_python_sdk.paths.files_file_id_metadata_enterprise_security_classification_6_vm_vochw_uwo.delete import RemoveClassification
from box_python_sdk.paths.files_file_id_metadata_enterprise_security_classification_6_vm_vochw_uwo.put import UpdateClassificationMetadataInstance
from box_python_sdk.apis.tags.classifications_on_files_api_raw import ClassificationsOnFilesApiRaw


class ClassificationsOnFilesApi(
    AddClassification,
    GetClassificationMetadataInstance,
    RemoveClassification,
    UpdateClassificationMetadataInstance,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ClassificationsOnFilesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ClassificationsOnFilesApiRaw(api_client)