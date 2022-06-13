from collections import Counter
import sys

# question:
#   There are three type of edits that can be performed on strings, insert a
#   character, remove a character, or replace a character. Given two strings,
#   write a function to check if they are one edit (or zero edits) away.
#
# concept:
#   if two string are of different lengths
#   remove the first non matching character from the longer string
#   if strings are identical after removal, return true
#   if string are of same length, iterate over both
#   if there is only one differing character return true

def oneAway(str1: str, str2: str) -> bool:
    if len(str1) > len(str2):
        # loop over length of shorter string
        offset = 0
        for i in range(len(str2)):
            if(str1[i + offset] != str2[i]):
                if offset > 0:
                    return False
                offset += 1
    elif len(str1) < len(str2):
        offset = 0
        for i in range(len(str1)):
            if(str1[i] != str2[i + offset]):
                    if offset > 0:
                        return False
                    offset += 1
    else:
        num_nonmatching_chars = 0
        for c1, c2 in zip(str1, str2):
            if c1 != c2:
                if num_nonmatching_chars > 0:
                    return False
                num_nonmatching_chars += 1 
    return True
        
def main() -> int:
    if(oneAway(sys.argv[1], sys.argv[2])):
        print(sys.argv[1], "is one edit away from", sys.argv[2]) 
    else:
        print(sys.argv[1], "is not one edit away from", sys.argv[2]) 
    return 0;

sys.exit(main())
