# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.tasks_task_id.get import GetInfoRaw
from box_python_sdk.paths.files_file_id_tasks.get import ListOnFileRaw
from box_python_sdk.paths.tasks_task_id.delete import RemoveFileRaw
from box_python_sdk.paths.tasks.post import TasksRaw
from box_python_sdk.paths.tasks_task_id.put import UpdateTaskConfigurationRaw


class TasksApiRaw(
    GetInfoRaw,
    ListOnFileRaw,
    RemoveFileRaw,
    TasksRaw,
    UpdateTaskConfigurationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass