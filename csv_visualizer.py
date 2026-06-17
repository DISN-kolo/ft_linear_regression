#!venv/bin/python
"""
Displays the graph of two csv columns, assuming line 1 is the names of the
axes.

No error handling - sorry, it's a dirty script to preview simple data
visually.
"""

import sys
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv(sys.argv[1])
    x_col, y_col = df.columns[0], df.columns[1]
    plt.scatter(df[x_col], df[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()
