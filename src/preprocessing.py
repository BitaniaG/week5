from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def encode_categoricals(df: pd.DataFrame, categorical_cols: list) -> pd.DataFrame:
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    encoded = encoder.fit_transform(df[categorical_cols])

    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(categorical_cols),
        index=df.index
    )

    df = df.drop(columns=categorical_cols)
    return pd.concat([df, encoded_df], axis=1)
