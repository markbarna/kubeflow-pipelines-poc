from kfp.components import InputPath, OutputPath


def train(x_path: InputPath(str), y_path: InputPath(str), model_path: OutputPath(str)):
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    import joblib

    x = pd.read_parquet(x_path)
    y = pd.read_parquet(y_path)

    model = LogisticRegression()
    model.fit(x, y)
    joblib.dump(model, model_path)

    # TODO: output artifact of model stats
    coefs = {feature: round(value, 2) for feature, value in zip(x.columns, model.coef_.flatten())}
    coefs['intercept'] = round(model.intercept_[0], 2)

    return coefs
