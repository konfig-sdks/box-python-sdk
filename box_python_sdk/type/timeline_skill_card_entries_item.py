# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from box_python_sdk.type.timeline_skill_card_entries_item_appears import TimelineSkillCardEntriesItemAppears

class RequiredTimelineSkillCardEntriesItem(TypedDict):
    pass

class OptionalTimelineSkillCardEntriesItem(TypedDict, total=False):
    # The text of the entry. This would be the display name for an item being placed on the timeline, for example the name of the person who was detected in a video.
    text: str

    appears: TimelineSkillCardEntriesItemAppears

    # The image to show on a for an entry that appears on a timeline. This image URL is required for every entry.  The image will be shown in a list of items (for example faces), and clicking the image will show the user where that entry appears during the duration of this entry.
    image_url: str

class TimelineSkillCardEntriesItem(RequiredTimelineSkillCardEntriesItem, OptionalTimelineSkillCardEntriesItem):
    pass
