import os
import sys


def palindrome(word):
    return word == word[::-1]


def main():
    word = input("word: ")
    answer = palindrome(word)
    if answer:
        print('yes')
    else:
        print('no')
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
