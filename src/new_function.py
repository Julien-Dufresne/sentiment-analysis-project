import pandas as pd

def print_dataset_summary(df: pd.DataFrame) -> None:
    """
    Prints a concise summary of the dataset, including its dimensions, 
    column data types, and missing value counts.

    Parameters:
    -----------
    df : pd.DataFrame
        The pandas DataFrame to summarize.

    Returns:
    --------
    None
    """
    print("=" * 40)
    print("DATASET SUMMARY")
    print("=" * 40)
    print(f"Total rows: {df.shape[0]}")
    print(f"Total columns: {df.shape[1]}")
    print("\nMissing values per column:")
    print(df.isnull().sum())
    print("-" * 40)