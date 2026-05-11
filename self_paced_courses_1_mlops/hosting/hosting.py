from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))

# Create the Space if it doesn't already exist
api.create_repo(
        repo_id="masaiida/PIMA-Diabetes-Prediction",
        repo_type="space",
        space_sdk="docker",
        exist_ok=True,
)

api.upload_folder(
        folder_path="self_paced_courses_1_mlops/deployment",
        repo_id="masaiida/PIMA-Diabetes-Prediction",
        repo_type="space",
        path_in_repo="",
)
