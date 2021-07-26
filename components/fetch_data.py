from kfp.components import OutputPath, InputPath


def fetch_data(x_path: OutputPath(str), y_path: OutputPath(str)):
    # download data locally
    from sklearn import datasets

    import os

    print(os.getcwd())
    print(os.listdir('.'))
    print(os.environ)

    x, y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)
    x.to_parquet(x_path)
    y.to_frame().to_parquet(y_path)

    from src.utils import print_hello_world
    print_hello_world()


def split_data(
        x_path: InputPath(str),
        y_path: InputPath(str),
        x_train_path: OutputPath(str),
        y_train_path: OutputPath(str),
        x_test_path: OutputPath(str),
        y_test_path: OutputPath(str),
        test_size: float = 0.2
):
    # split into training and test sets
    import pandas as pd
    from sklearn.model_selection import train_test_split

    x = pd.read_parquet(x_path)
    y = pd.read_parquet(y_path)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=1)

    x_train.to_parquet(x_train_path)
    x_test.to_parquet(x_test_path)
    y_train.to_parquet(y_train_path)
    y_test.to_parquet(y_test_path)
