import sys

# question:
#   Implement an algorithm to determine if a string has all unique characters
#   What if you cannot use additonal data structures?
# concept:
#   use a map to record each seen character
#   if a character has already been seen,
#   return False
def isUnique(str):
    char_set = {}
    for c in str:
        if char_set.get(c) != None:
            return False
        char_set[c] = 1 
    return True

def main() -> int:
    for i in range(1, len(sys.argv)):
        str = sys.argv[i]
        if isUnique(str):
            print(str, 'has all unique characters')
            continue
        print(str, 'does not have all unique characters')
    return 0

sys.exit(main())
