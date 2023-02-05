import pandas as pd


def get_data() -> pd.DataFrame:
    return pd.read_csv(
        "data/site.csv",
        header=0,
        delimiter=','
    )

