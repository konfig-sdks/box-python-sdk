# coding: utf-8

"""
    Box Platform API

    [Box Platform](https://box.dev) provides functionality to provide access to content stored within [Box](https://box.com). It provides endpoints for basic manipulation of files and folders, management of users within an enterprise, as well as more complex topics such as legal holds and retention policies.

    The version of the OpenAPI document: 2.0.0
    Contact: devrel@box.com
    Created by: https://box.dev
"""

from box_python_sdk.paths.task_assignments.post import AssignMultipleUsersRaw
from box_python_sdk.paths.task_assignments_task_assignment_id.delete import DeleteSpecificAssignmentRaw
from box_python_sdk.paths.task_assignments_task_assignment_id.get import GetTaskAssignmentInfoRaw
from box_python_sdk.paths.tasks_task_id_assignments.get import ListForTaskRaw
from box_python_sdk.paths.task_assignments_task_assignment_id.put import UpdateStateAssignedToUserRaw


class TaskAssignmentsApiRaw(
    AssignMultipleUsersRaw,
    DeleteSpecificAssignmentRaw,
    GetTaskAssignmentInfoRaw,
    ListForTaskRaw,
    UpdateStateAssignedToUserRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
