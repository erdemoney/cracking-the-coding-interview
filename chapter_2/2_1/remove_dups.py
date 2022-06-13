import sys
from ..common.linked_list import *


# question:
#   Write code to remove duplicates from an unsorted linked list.
#   FOLLOW UP
#   How would you solve this problem if a temporary buffer is not allowed?

def removeDups(ll: SinglyLinkedList):
    seen = {}
    prev = ll.head
    for node in ll:
        if seen.get(node.data) != None:
            prev.next = node.next   
        prev = node
        seen[node.data] = True
        
def main() -> int:
    ll = SinglyLinkedList()
    for arg in sys.argv:
       ll.insert(arg) 
    print('original list', ll)
    removeDups(ll)
    print('duplicates removed', ll)
    return 0

if __name__ == "__main__":
    sys.exit(main())
