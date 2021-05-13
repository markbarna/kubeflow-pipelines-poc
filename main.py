from kfp import components, dsl, compiler

from components.fetch_data import fetch_data

fetch_data_op = components.create_component_from_func(fetch_data)


@dsl.pipeline(name='cancer classifier', description='test classifier pipeline with breast cancer dataset')
def pipeline():
    fetch_data_op()
    # TODO: get dataset & pre-process
    # TODO: train model (with tuning)
    # TODO: batch predictions (move to separate pipeline)
    # TODO: serve model


if __name__ == '__main__':
    compiler.Compiler().compile(pipeline, 'compiled/pipeline.yaml')
