"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from .usecases.pipeline_registry import create_pipeline_registry


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return create_pipeline_registry()
