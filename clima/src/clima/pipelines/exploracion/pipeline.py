from kedro.pipeline import Pipeline, node, pipeline
from .nodes import explorar_datos

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=explorar_datos,
            inputs="datos_climaticos",
            outputs=None,
            name="nodo_exploracion"
        )
    ])
