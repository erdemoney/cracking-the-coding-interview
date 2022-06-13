from ..common.linked_list import *
import sys

# question:
#   implement a function to check if a linked list is a palindrome.
#
# concept:
#   stringify linked list and check if its identical forward and reversed

def palindrome(ll: SinglyLinkedList) -> bool:
    s = []
    for node in ll:
       s.append(node.data) 
    s_reversed = s.copy()
    s_reversed.reverse()
    return s == s_reversed

def main() -> int:
    ll = SinglyLinkedList()
    for c in sys.argv[1]:
       ll.insert(c) 
    if palindrome(ll):
       print(sys.argv[1], 'is a palindrome') 
    else:
       print(sys.argv[1], 'is not a palindrome') 
    return 0

if __name__ == "__main__":
    sys.exit(main())
