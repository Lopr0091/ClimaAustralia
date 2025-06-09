from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preparar_dataset

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preparar_dataset,
                inputs="datos_climaticos",
                outputs="datos_limpios",
                name="preparar_dataset_node",
            ),
        ]
    )
