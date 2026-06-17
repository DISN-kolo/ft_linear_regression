import sys

def exit_with_print(code: int = 1, message: str = ""):
    sys.stderr.write(message + "\n")
    exit(code)
