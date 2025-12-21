import pandas as pd


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if 'signup_time' not in df.columns or 'purchase_time' not in df.columns:
        raise ValueError("Required timestamp columns missing")

    df['time_since_signup'] = (
        df['purchase_time'] - df['signup_time']
    ).dt.total_seconds() / 3600

    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek

    return df


def add_transaction_behavior(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    tx_counts = df.groupby('user_id')['purchase_time'].count()
    df['num_transactions'] = df['user_id'].map(tx_counts)

    return df
