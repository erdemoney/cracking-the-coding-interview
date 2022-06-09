import sys
from collections import defaultdict

def checkPermutation(str1, str2):
    def def_value():
        return 0
    char_count = defaultdict(def_value)

    for c in str1:
        char_count[c] += 1
    for c in str2:
        char_count[c] -= 1
    for k in char_count:
        if char_count[k] != 0:
            return False
    return True

def main() -> int:
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    if(checkPermutation(str1, str2)):
        print(str1, 'is a permutation of', str2)
    else:
        print(str1, 'is not a permutation of', str2)
    return 0

if __name__ == '__main__':
    sys.exit(main())
        
