import os

import supervisely as sly
from dataset_tools.convert.mvtecd2s.main import to_supervisely
from dotenv import load_dotenv

# if sly.is_development():
#   load_dotenv(os.path.expanduser("~/ninja.env"))
#    load_dotenv("local.env")


# api = sly.Api.from_env()
# workspace_id = sly.env.workspace_id()

# project_id = to_supervisely(api, workspace_id)

# print("Project id is", project_id)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # * dataset_path = "Path to the local dir with dataset"

    # Function should read local dataset and upload it to Supervisely project, then return project info.

    raise NotImplementedError("The converter should be implemented manually.")

    # * return project
