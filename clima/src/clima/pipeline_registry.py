from __future__ import annotations
from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from clima.pipelines.exploracion import pipeline as exploracion_pipeline
from clima.pipelines.preparacion import pipeline as preparacion_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    pipelines = find_pipelines()
    pipelines["exploracion"] = exploracion_pipeline.create_pipeline()
    pipelines["preparacion"] = preparacion_pipeline.create_pipeline()
    pipelines["__default__"] = sum(pipelines.values())

    return pipelines
