import os
import sys
import math


def equations_of_motion(vo, a, t):
    v = float(vo + a * t)
    print(v)


def equations_of_motion1(vo, a, ro, r):
    v = math.sqrt((vo ** 2) + (2 * a * (r - ro)))
    print(v)


def main():
    functions = {'1': equations_of_motion, '2': equations_of_motion1}
    print(f"which function will you use to solve for v: ")
    for k, v in functions.items():
        print(k, '-->', v)
    selected = input('Enter the function: ')
    vo = float(input("vo: "))
    a = float(input("a: "))
    t = float(input("t: "))
    if selected == 1:
        print(equations_of_motion(vo, a, t))
    else:
        ro = float(input("ro: "))
        r = float(input("r: "))
        print(equations_of_motion1(vo, a, ro, r))
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())