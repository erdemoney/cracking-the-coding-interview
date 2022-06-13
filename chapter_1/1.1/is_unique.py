import sys

# question:
#   Implement an algorithm to determine if a string has all unique characters
#   What if you cannot use additonal data structures?
#
# concept:
#   use a map to record each seen character
#   if a character has already been seen,
#   return False

def isUnique(s: str) -> bool:
    char_set = {}
    for c in s:
        if char_set.get(c) != None:
            return False
        char_set[c] = 1 
    return True

def main() -> int:
    args = sys.argv[1::]
    for arg in args:
        if isUnique(arg):
            print(arg, 'has all unique characters')
        else:
            print(arg, 'does not have all unique characters')
    return 0

sys.exit(main())
