from typing import Dict

from kedro.pipeline import Pipeline

from cautios_rotary_phone.pipelines.feature_engineering import (
    pipeline as feature_engineering_pipeline,
)


def create_pipeline_registry() -> Dict[str, Pipeline]:
    return {"feature_engineering": feature_engineering_pipeline.create_pipeline()}
