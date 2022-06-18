from kedro.pipeline import Pipeline

from .nodes import loading_node


def create_pipeline() -> Pipeline:

    nodes = [loading_node]

    return Pipeline(nodes)
