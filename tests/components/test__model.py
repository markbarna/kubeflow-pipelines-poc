import os

from components.model import train

ROOT_DIR = os.path.dirname(__file__)


def test_train(tmp_path):
    input_path = os.path.join(ROOT_DIR, 'mock_data', 'model')
    x_path = os.path.join(input_path, 'x_train')
    y_path = os.path.join(input_path, 'y_train')
    model_path = os.path.join(tmp_path, 'model')
    stats = train(x_path, y_path, model_path)
    assert 'model' in os.listdir(tmp_path)
    assert isinstance(stats, dict)
