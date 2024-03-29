# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.web_links_web_link_idadd_shared_link.put import AddLinkToWebLink
from box_python_sdk.paths.shared_itemsweb_links.get import FindSharedWebLink
from box_python_sdk.paths.web_links_web_link_idget_shared_link.get import GetLinkInfo
from box_python_sdk.paths.web_links_web_link_idremove_shared_link.put import RemoveSharedLink
from box_python_sdk.paths.web_links_web_link_idupdate_shared_link.put import UpdateSharedLink
from box_python_sdk.apis.tags.shared_links_web_links_api_raw import SharedLinksWebLinksApiRaw


class SharedLinksWebLinksApi(
    AddLinkToWebLink,
    FindSharedWebLink,
    GetLinkInfo,
    RemoveSharedLink,
    UpdateSharedLink,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SharedLinksWebLinksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SharedLinksWebLinksApiRaw(api_client)
