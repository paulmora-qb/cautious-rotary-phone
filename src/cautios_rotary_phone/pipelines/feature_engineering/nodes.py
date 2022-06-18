from kedro.pipeline import node

from .loading import load_songs_in_kern

loading_node = node(
    func=load_songs_in_kern,
    inputs="params:feature_engineering.loading_raw",
    outputs="test1",
    name="test",
    tags=["test"],
)
