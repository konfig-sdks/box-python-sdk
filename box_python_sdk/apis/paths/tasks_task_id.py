from box_python_sdk.paths.tasks_task_id.get import ApiForget
from box_python_sdk.paths.tasks_task_id.put import ApiForput
from box_python_sdk.paths.tasks_task_id.delete import ApiFordelete


class TasksTaskId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
