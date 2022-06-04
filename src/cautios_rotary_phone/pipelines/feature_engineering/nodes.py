from kedro.pipeline import node

from .test_node import test_func

test_node = node(
    func=test_func, inputs="params:test", outputs="test1", name="test", tags=["test"]
)
