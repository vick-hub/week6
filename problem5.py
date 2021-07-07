import os
import sys


def double(text, a=2):
    return ''.join([x * a for x in text])


def main():
    a = 3
    text = input("enter a sentence: ")
    print(double(text, a))
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
