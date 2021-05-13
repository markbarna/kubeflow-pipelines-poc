from components.fetch_data import fetch_data


def test_fetch_data(tmp_path):
    x_path = tmp_path / 'x'
    y_path = tmp_path / 'y'
    fetch_data(x_path, y_path)
    assert len(list(tmp_path.iterdir())) == 2