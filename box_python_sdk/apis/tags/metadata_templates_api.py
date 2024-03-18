# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.metadata_templates_schema.post import CreateNewTemplate
from box_python_sdk.paths.metadata_templates_scope_template_key_schema.delete import DeleteSchema
from box_python_sdk.paths.metadata_templates.get import FindByInstanceId
from box_python_sdk.paths.metadata_templates_template_id.get import GetById
from box_python_sdk.paths.metadata_templates_scope_template_key_schema.get import GetByNameSchema
from box_python_sdk.paths.metadata_templates_enterprise.get import ListForEnterprise
from box_python_sdk.paths.metadata_templates_global.get import ListGlobal
from box_python_sdk.paths.metadata_templates_scope_template_key_schema.put import UpdateSchema
from box_python_sdk.apis.tags.metadata_templates_api_raw import MetadataTemplatesApiRaw


class MetadataTemplatesApi(
    CreateNewTemplate,
    DeleteSchema,
    FindByInstanceId,
    GetById,
    GetByNameSchema,
    ListForEnterprise,
    ListGlobal,
    UpdateSchema,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MetadataTemplatesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MetadataTemplatesApiRaw(api_client)
