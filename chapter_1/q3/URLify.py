import sys

# question:
#   Write a method to replace all space ina string with '%20'. You may assume
#   that the string has sufficient space at the end to hold the additional
#   characters and that you are given the "true" length of the string.
#   (Note: if implementing in Java, please use a character array so that you can
#   perform this operation in place.)
# concept:
#   use pythons built-in string functions to modify string

# remove extra padding in string using slicing
# use python string replace function to urlify string
def urlify(str, len) -> str:
    return str[:len:].replace(' ', '%20')

# parse input and urlify
def main() -> int:
    print(urlify(sys.argv[1], int(sys.argv[2])))
    return 0

sys.exit(main())
