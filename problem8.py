import os
import sys


def gravitational_law(m1, m2, r, g=10):
    f = float(g * ((m1 * m2) / r ** 2))
    return f


def main():
    try:
        m1 = float(input("m1: "))
        m2 = float(input("m2: "))
        r = float(input("r : "))
        print(f"Force = {gravitational_law(m1, m2, r)}N")
    except ZeroDivisionError as err:
        print(f"Handling runtime error:", err)
    except ValueError as val:
        print("Oops! is not valid number: ", val)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
