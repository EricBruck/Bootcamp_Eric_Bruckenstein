import pandas as pd

def get_summary_stats(df: pd.DataFrame, group_col: str, val_col: str) -> pd.DataFrame:
    """
    Groups a DataFrame by group_col and calculates summary statistics for val_col.
    """
    summary = df.groupby(group_col)[val_col].agg(['count', 'mean', 'std', 'min', 'max', 'sum']).reset_index()
    return summary
