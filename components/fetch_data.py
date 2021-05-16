from kfp.components import OutputPath


def fetch_data(x_path: OutputPath(str), y_path: OutputPath(str)):
    from sklearn import datasets

    x, y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)
    x.to_parquet(x_path)
    y.to_frame().to_parquet(y_path)
