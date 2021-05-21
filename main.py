from kfp import components, dsl, compiler, Client
import os

from components.fetch_data import fetch_data, split_data
from utils.git import create_version_name
from utils.git import PROJECT_ROOT

BASE_IMAGE = 'dabarnyarddawg/kf-pipelines-base-images:latest'
CLIENT = 'http://127.0.0.1:8080'
PIPELINE_NAME = 'cancer-classifier'

fetch_data_op = components.create_component_from_func(fetch_data, base_image=BASE_IMAGE)
split_data_op = components.create_component_from_func(split_data, base_image=BASE_IMAGE)


@dsl.pipeline(name=PIPELINE_NAME, description='test classifier pipeline with breast cancer dataset')
def pipeline(test_size: float = 0.2):
    fetch_data_task = fetch_data_op()
    split_data_op(x=fetch_data_task.outputs['x'], y=fetch_data_task.outputs['y'], test_size=test_size)
    # TODO: train model(s) (with tuning) in parallel?
    # TODO: batch predictions (move to separate pipeline)
    # TODO: serve model


if __name__ == '__main__':
    compiler.Compiler().compile(pipeline, os.path.join(PROJECT_ROOT, 'compiled', f'{PIPELINE_NAME}.yaml'))
    client = Client(host=CLIENT)
    client.upload_pipeline_version(
        pipeline_package_path=os.path.join(PROJECT_ROOT, 'compiled', f'{PIPELINE_NAME}.yaml'),
        pipeline_name=PIPELINE_NAME,
        # TODO: version name needs some work (include pipeline name?) commit hash would be off by 1
        pipeline_version_name=create_version_name()
    )
