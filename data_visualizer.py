#!venv/bin/python

import sys
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from additional_utils import exit_with_print, get_vars

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        exit_with_print(
            1,
            f"\
Usage: {sys.argv[0]} <path/to/csv/data/file> <path/to/thetas/file>"
        )

    df = None
    theta0, theta1 = 0.0, 0.0
    try:
        df = pd.read_csv(sys.argv[1])
        theta0, theta1 = get_vars(sys.argv[2])
    except Exception:
        exit_with_print(2, "something went wrong")
    x_col, y_col = df.columns[0], df.columns[1]
    plt.scatter(df[x_col], df[y_col], label="data", color="grey")

    line_x = np.linspace(min(df[x_col]), max(df[x_col]), 20)
    line_y = theta0 + theta1 * line_x
    plt.plot(line_x, line_y, label="regression line")

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.show()
