# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from box_python_sdk import schemas  # noqa: F401


class TimelineSkillCardEntriesItemAppears(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Defines a list of timestamps for when this item should appear on the
timeline.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TimelineSkillCardEntriesItemAppearsItem']:
            return TimelineSkillCardEntriesItemAppearsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TimelineSkillCardEntriesItemAppearsItem'], typing.List['TimelineSkillCardEntriesItemAppearsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TimelineSkillCardEntriesItemAppears':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TimelineSkillCardEntriesItemAppearsItem':
        return super().__getitem__(i)

from box_python_sdk.model.timeline_skill_card_entries_item_appears_item import TimelineSkillCardEntriesItemAppearsItem