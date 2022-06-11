import sys
from collections import Counter

# question:
#   Given a stirng, write a function to check if it is a permutation of a
#   palindrome. A palindrome is a word or phrase that is the same forwards and
#   backwards. A permutation is a rearrangement of letters. The palindrome does
#   not need to be limited to just dictionary words.
#
# concept:
#   a string is a permutation of a palindrome if it has no more than one character count that is odd
#   a palindrome has the even counts for each letter with the exception of the center character which
#   can be shared


def palindromePermutation(str: str) -> bool:
    # count each character in string
    counts = Counter(str)
    odd = False

    # if the count of a character is odd set odd to True
    # if its already true, then it cannot be a palidrome permutation,
    # so return false
    for k in counts:
        if counts[k] % 2 != 0:
            if odd:
                return False
            odd = True
    return True
           
def main() -> int:
    if(palindromePermutation(sys.argv[1])):
        print(sys.argv[1], "is a palindrome permutation")
    else:
        print(sys.argv[1], "is not a palindrome permutation")
    return 0

sys.exit(main())
