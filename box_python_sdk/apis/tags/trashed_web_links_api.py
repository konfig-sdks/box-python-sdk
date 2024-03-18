# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.web_links_web_link_id_trash.get import GetTrashedLink
from box_python_sdk.paths.web_links_web_link_id_trash.delete import PermanentlyRemove
from box_python_sdk.paths.web_links_web_link_id.post import RestoreWebLink
from box_python_sdk.apis.tags.trashed_web_links_api_raw import TrashedWebLinksApiRaw


class TrashedWebLinksApi(
    GetTrashedLink,
    PermanentlyRemove,
    RestoreWebLink,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TrashedWebLinksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TrashedWebLinksApiRaw(api_client)
