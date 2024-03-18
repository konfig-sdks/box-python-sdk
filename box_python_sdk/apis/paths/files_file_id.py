from box_python_sdk.paths.files_file_id.get import ApiForget
from box_python_sdk.paths.files_file_id.put import ApiForput
from box_python_sdk.paths.files_file_id.post import ApiForpost
from box_python_sdk.paths.files_file_id.delete import ApiFordelete


class FilesFileId(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
