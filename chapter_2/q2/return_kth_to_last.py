import sys
from ..common.linked_list import *

# question:
#   Implement an algorithm to find the kth to last element of a singly linked
#   list.
#
# concept:
#   advance fast pointer k elements forward
#   start slow pointer and advance both until fast pointer hits the end
#   slow pointer will be k elements from end

def return_kth_to_last(ll: SinglyLinkedList, k: int):
    fast = ll.head
    for _ in range(k):
       fast = fast.next
    slow = ll.head
    while fast is not None:
        fast = fast.next
        slow = slow.next
    return slow.data

def main() -> int:
    ll = SinglyLinkedList()
    for arg in sys.argv[1::]:
       ll.insert(arg) 
    print(ll,'\n')
    print(return_kth_to_last(ll, int(sys.argv[1])), 'is the', sys.argv[1], 'th element')
    return 0

if __name__ == "__main__":
    sys.exit(main())
