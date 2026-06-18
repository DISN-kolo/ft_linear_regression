import sys
from additional_exceptions import EmptyFileNameError

def exit_with_print(code: int = 1, message: str = ""):
    sys.stderr.write(message + "\n")
    exit(code)

def get_vars(filepath: str = ""):
    if (filepath == ""):
        raise EmptyFileNameError
    line0, line1 = "", ""
    with open(filepath) as f:
        line0 = f.readline().strip()
        line1 = f.readline().strip()
    if not line0 or not line1:
        raise ValueError
    return float(line0), float(line1)

