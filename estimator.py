#!venv/bin/python

import sys
from additional_exceptions import EmptyFileNameError
from additional_utils import exit_with_print

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

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        exit_with_print(1, f"Usage: {sys.argv[0]} <path/to/thetas/file>")

    theta0, theta1 = 0.0, 0.0
    try:
        theta0, theta1 = get_vars(sys.argv[1])
    except FileNotFoundError:
        exit_with_print(2, f"{sys.argv[1]} not found")
    except PermissionError:
        exit_with_print(3, f"No access to {sys.argv[1]}")
    except ValueError:
        exit_with_print(4, "Bad file contents")
    except EmptyFileNameError:
        exit_with_print(5, "Empty filename")
    except Exception:
        exit_with_print(6, "Some error occured")
    print(f"theta_0 is {theta0}\ntheta_1 is {theta1}")

    while (True):
        x = 0.0
        try:
            x = float(input("Enter the mileage: "))
            y = theta0 + theta1 * x;
            print(f"Calculated price estmation: {y:.2f}")
        except ValueError:
            print("Try entering something in a floating point number format.")
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            exit(0)
