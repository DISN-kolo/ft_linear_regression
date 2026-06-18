#!venv/bin/python

import sys
from additional_utils import exit_with_print, get_vars
from additional_exceptions import EmptyFileNameError
import pandas as pd

def get_df(filepath: str = ""):
    if (filepath == ""):
        raise EmptyFileNameError
    return pd.read_csv(filepath)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        exit_with_print(1, f"Usage: {sys.argv[0]} <path/to/csv/data/file>")

    principal_data = None
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

