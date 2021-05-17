from components.fetch_data import fetch_data, split_data
import os

ROOT_DIR = os.path.dirname(__file__)


def test_fetch_data(tmp_path):
    x_path = tmp_path / 'x'
    y_path = tmp_path / 'y'
    fetch_data(x_path, y_path)
    assert len(list(tmp_path.iterdir())) == 2


def test_split_data(tmp_path):
    input_path = os.path.join(ROOT_DIR, 'mock_data', 'fetch_data')
    x_path = os.path.join(input_path, 'x')
    y_path = os.path.join(input_path, 'y')
    x_train_path = tmp_path / 'x_train'
    y_train_path = tmp_path / 'y_train'
    x_test_path = tmp_path / 'x_test'
    y_test_path = tmp_path / 'y_test'
    split_data(x_path, y_path, x_train_path, y_train_path, x_test_path, y_test_path)
    assert len(list(tmp_path.iterdir())) == 4
