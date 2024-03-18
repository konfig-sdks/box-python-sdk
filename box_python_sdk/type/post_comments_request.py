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

from box_python_sdk.type.post_comments_request_item import PostCommentsRequestItem

class RequiredPostCommentsRequest(TypedDict):
    # The text of the comment.  To mention a user, use the `tagged_message` parameter instead.
    message: str

    item: PostCommentsRequestItem

class OptionalPostCommentsRequest(TypedDict, total=False):
    # The text of the comment, including `@[user_id:name]` somewhere in the message to mention another user, which will send them an email notification, letting them know they have been mentioned.  The `user_id` is the target user's ID, where the `name` can be any custom phrase. In the Box UI this name will link to the user's profile.  If you are not mentioning another user, use `message` instead.
    tagged_message: str

class PostCommentsRequest(RequiredPostCommentsRequest, OptionalPostCommentsRequest):
    pass
