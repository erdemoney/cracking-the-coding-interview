import sys
from collections import Counter

# question:
#   Given two strings, write a method to decide if one is a permutation of the
#   other.
#
# concept:
#   Get character counts for both strings, if they're equal, then s1 is a
#   permutation of s2

def checkPermutation(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)

def main() -> int:
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    if(checkPermutation(str1, str2)):
        print(str1, 'is a permutation of', str2)
    else:
        print(str1, 'is not a permutation of', str2)
    return 0

sys.exit(main())
        
