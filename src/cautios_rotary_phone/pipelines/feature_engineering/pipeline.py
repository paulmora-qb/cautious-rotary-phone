from kedro.pipeline import Pipeline

from .nodes import test_node


def create_pipeline() -> Pipeline:

    nodes = [test_node]

    return Pipeline(nodes)
