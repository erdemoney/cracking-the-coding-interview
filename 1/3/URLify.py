import sys

# challenges:
#   isolating string input
#   accounting for a possible comma "," in input string

# remove extra padding in string using slicing
# use native string replace function to urlify string
def urlify(str, len) -> str:
    return str[:len:].replace(' ', '%20')

# parse input and urlify
def main() -> int:
    print(urlify(sys.argv[1], int(sys.argv[2])))
    return 0

if __name__ == '__main__':
   sys.exit(main())
