import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
project_name="BHP"
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingetion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/loggers.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "Dockerfile"
    
]
for file_path in list_of_files:
    file_path=Path(file_path)
    filedir, filename=os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating the directory : {filedir} for the file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
        logging.info(f"creating empty file {file_path}") 
    else:
        logging.info(f" {filename} is already exists")           