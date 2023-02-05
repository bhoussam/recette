from typing import List

import numpy as np
import pandas as pd


def distinct_values(col: pd.Series) -> List:
    return [x for x in col.unique() if x is not np.NaN]
