import os 
from pathlib import Path

# List of all project files and directories that will be created
list_of_files = [

    "github/workflows/.gitkeep",   # Keeps GitHub Actions workflows folder tracked in git, even if empty

    # ---------------- Source Code ----------------
    "src/__init__.py",   # Marks "src" as a Python package
    "src/components/__init__.py",   # Marks "components" as a Python package
    "src/components/data_ingestion.py",   # Script to handle data ingestion (loading raw data from source)
    "src/components/data_transformation.py",   # Script to clean, preprocess, and transform raw data
    "src/components/model_trainer.py",   # Script for training ML model(s)
    "src/components/model_evaluation.py",   # Script for evaluating trained model performance

    "src/pipeline/__init__.py",   # Marks "pipeline" as a Python package
    "src/pipeline/training_pipeline.py",   # Orchestrates data ingestion, transformation, training, evaluation
    "src/pipeline/prediction_pipeline.py",   # Handles prediction workflow on new/unseen data

    "src/utils/utils.py",   # Utility/helper functions (e.g., file operations, configs, metrics)
    "src/utils/__init__.py",   # Marks "utils" as a Python package

    "src/logger/logging.py",   # Centralized logging configuration
    "src/exception/exception.py",   # Custom exception handling for better debugging

    # ---------------- Testing ----------------
    "tests/unit/__init__.py",   # Marks "unit" test folder as a package (unit tests for individual components)
    "tests/integration/__init__.py",   # Marks "integration" test folder as a package (tests across multiple components)

    # ---------------- Project Setup ----------------
    "init_setup.sh",   # Shell script for environment setup (install dependencies, env vars)
    "requirements.txt",   # List of dependencies for production
    "requirements_dev.txt",   # List of dependencies for development/testing
    "setup.py",   # Package installation script (setuptools)
    "setup.cfg",   # Configuration for linters, formatters, pytest, etc.
    "pyproject.toml",   # Modern build system configuration (PEP 518)
    "tox.ini",   # Config for testing across different Python environments

    # ---------------- Experiments ----------------
    "experiments/experiments.ipynb"   # Jupyter notebook for experiments, prototyping, and EDA
]

# File & folder creation loop
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        print(f"Creating empty file: {filepath}")
    else:
        print(f"File already exists: {filepath}, skipping...")
