import os
import sys


def sum_of_list():
    a = int(input("a: "))
    b = int(input("b: "))
    list1 = list(range(a, b))
    return list1


def main():
    print(sum(sum_of_list()))
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
