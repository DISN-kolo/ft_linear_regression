#!venv/bin/python

import sys
from additional_utils import exit_with_print, get_vars
from additional_exceptions import EmptyFileNameError
import pandas as pd
import numpy as np

def est_fun_array(t0: float, t1: float, x: np.ndarray):
    return t0 + t1*x

def mse(df, t0: float, t1: float):
    est_y = est_fun_array(t0, t1, df["km"])
    return sum( (est_y - df["price"]) ** 2 )/len(df)

def get_df(filepath: str = ""):
    if (filepath == ""):
        raise EmptyFileNameError
    return pd.read_csv(filepath)

def partial_d_of_mse_by_theta0(df, t0: float, t1: float):
    est_y = est_fun_array(t0, t1, df["km"])
    return sum(est_y - df["price"])/len(df)

def partial_d_of_mse_by_theta1(df, t0: float, t1: float):
    est_y = est_fun_array(t0, t1, df["km"])
    return sum( (est_y - df["price"]) * df["km"] )/len(df)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        exit_with_print(1, f"Usage: {sys.argv[0]} <path/to/csv/data/file>")

    principal_data = None
    eta = 5e-12
    theta0, theta1 = 0.0, 0.0
    # partial deriviatives of mse by theta0 and theta1.
    # for some reason, multiplied by eta and called "tmptheta0" and
    #"tmptheta1" in the subject.
    dmsedt0, dmsedt1 = 0.0, 0.0
    try:
        principal_data = get_df(sys.argv[1])
    except FileNotFoundError:
        exit_with_print(2, f"{sys.argv[1]} not found")
    except PermissionError:
        exit_with_print(3, f"No access to {sys.argv[1]}")
    except ValueError:
        exit_with_print(4, "Bad values passed into 'read_csv'")
    except EmptyFileNameError:
        exit_with_print(5, "Empty filename")
    except pd.errors.ParserError:
        exit_with_print(6, "pandas' parser error happpened")
    except pd.errors.EmptyDataError:
        exit_with_print(7, "Data turned up empty according to pandas")
    except Exception:
        exit_with_print(8, "Some error occured")

    if principal_data is not None:
        print("Take a look at the data:\n", principal_data)
        print("Starting training...")
        i = 0
        prev_mse = mse(principal_data, theta0, theta1)*10
        cur_mse = mse(principal_data, theta0, theta1)
        while (abs(prev_mse - cur_mse) > 10 and i < 50):
            print(f"\
Iteration {i:3d}, prev mse: {prev_mse:10.2g}, cur mse: {cur_mse:10.2g}"
            )
            dmsedt0 = partial_d_of_mse_by_theta0(
                principal_data, theta0, theta1)
            dmsedt1 = partial_d_of_mse_by_theta1(
                principal_data, theta0, theta1)
            theta0 -= eta * dmsedt0
            theta1 -= eta * dmsedt1
            prev_mse = cur_mse
            cur_mse = mse(principal_data, theta0, theta1)
            i += 1

