from kfp import components, dsl, compiler

from components.fetch_data import fetch_data, split_data

BASE_IMAGE = 'dabarnyarddawg/kf-pipelines-base-images:latest'

fetch_data_op = components.create_component_from_func(
    fetch_data, base_image=BASE_IMAGE
)
split_data_op = components.create_component_from_func(
    split_data, base_image=BASE_IMAGE
)


@dsl.pipeline(name='cancer classifier', description='test classifier pipeline with breast cancer dataset')
def pipeline(test_size: float = 0.2):
    fetch_data_task = fetch_data_op()
    split_data_op(x=fetch_data_task.outputs['x'], y=fetch_data_task.outputs['y'], test_size=test_size)
    # TODO: train model(s) (with tuning) in parallel?
    # TODO: batch predictions (move to separate pipeline)
    # TODO: serve model


if __name__ == '__main__':
    # TODO: switch to using client connection
    compiler.Compiler().compile(pipeline, 'compiled/pipeline.yaml')
    # TODO: compile on release job in github
