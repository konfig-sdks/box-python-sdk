# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.files_file_id_metadata_global_box_skills_cards.post import ApplyBoxSkillCards
from box_python_sdk.paths.files_file_id_metadata_global_box_skills_cards.get import ListBoxSkillCards
from box_python_sdk.paths.files_file_id_metadata_global_box_skills_cards.delete import RemoveBoxSkillCards
from box_python_sdk.paths.skill_invocations_skill_id.put import UpdateAllBoxSkillCards
from box_python_sdk.paths.files_file_id_metadata_global_box_skills_cards.put import UpdateBoxSkillCardsOnFile
from box_python_sdk.apis.tags.skills_api_raw import SkillsApiRaw


class SkillsApi(
    ApplyBoxSkillCards,
    ListBoxSkillCards,
    RemoveBoxSkillCards,
    UpdateAllBoxSkillCards,
    UpdateBoxSkillCardsOnFile,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SkillsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SkillsApiRaw(api_client)
