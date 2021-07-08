import os
import sys


def gravitational_law(m1, m2, r, g=10):
    f = float(g * ((m1 * m2) / r ** 2))
    return f


def main():
    m1 = float(input("m1: "))
    m2 = float(input("m2: "))
    r = float(input("r : "))
    try:
        print(f"Force = {gravitational_law(m1, m2, r)}N")
    except ZeroDivisionError as error:
        print("Handling runtime error:", error)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
