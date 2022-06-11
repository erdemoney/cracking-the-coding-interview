import sys

# question:
#   Assume you have a method "isSubstring" which checks if one word is a
#   substring of another. Given two strings, s1 and s2, write code to check if
#   s2 is a rotation of s1 using only one call to "isSubstring"
#   (e.g., "waterbottle" is a rotation of "erbottlewa").
#
# concept:
#   if we concatenate the rotated string 3 times
#   if it is in fact a rotated version of the orignal string
#   it will contain the original string as a substring
#   "waterbottle" "erbottlewat"
#   "erbottlewat""erbottlewat""erbottlewat"
#            ^           ^

def stringRotation(s1: str, s2: str) -> bool:
    expanded = s2 * 3
    return isSubstring(s1, expanded)
    
def isSubstring(s1: str, s2: str) -> bool:
    return s1 in s2

def main() -> int:
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    if stringRotation(s1, s2):
        print(s2, "is a rotation of", s1)
    else:
        print(s2, "is not a rotation of", s1)
    return 0

sys.exit(main())
