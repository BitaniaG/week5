import pandas as pd

def ip_to_country(transactions_df: pd.DataFrame,
                  ip_df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps IP addresses to countries using range-based matching.
    """

    required_cols = {'ip_address'}
    if not required_cols.issubset(transactions_df.columns):
        raise ValueError("transactions_df must contain 'ip_address'")

    # Convert to int
    transactions_df = transactions_df.copy()
    transactions_df['ip_address'] = transactions_df['ip_address'].astype('int64')

    ip_df = ip_df.copy()
    ip_df['lower_bound_ip_address'] = ip_df['lower_bound_ip_address'].astype('int64')
    ip_df['upper_bound_ip_address'] = ip_df['upper_bound_ip_address'].astype('int64')

    # Sort for merge_asof
    transactions_df = transactions_df.sort_values('ip_address')
    ip_df = ip_df.sort_values('lower_bound_ip_address')

    # Merge
    merged = pd.merge_asof(
        transactions_df,
        ip_df,
        left_on='ip_address',
        right_on='lower_bound_ip_address',
        direction='backward'
    )

    # Validate range
    merged = merged[merged['ip_address'] <= merged['upper_bound_ip_address']]

    return merged
