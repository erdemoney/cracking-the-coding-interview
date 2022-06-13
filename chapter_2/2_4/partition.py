from ..common.linked_list import *
import sys

# question:
#   Write code to partition a linked list around a value x, such that all nodes
#   less than x come before all nodes greater than or equal to x. if x is
#   contained within the list, the values of x only need to be after the
#   elements less than x, (see below). The partition element x can appear
#   anywhere in  the "right partition"; it does not need to appear between the
#   left and right partitions

def parition(ll: SinglyLinkedList, x):
    tail = ll.head
    head = ll.head
    for node in ll:
        tmp = node
        if int(node.data) < x:
            tmp.next = head
            head = tmp
        else:
            tail.next = node
            tail = node

    tail.next = None

def main() -> int:
    ll = SinglyLinkedList()
    for arg in sys.argv[1::]:
       ll.insert(arg) 
    print('original list\n', ll, '\n')
    print('partitioned list')
    print(parition(ll, 5))
    return 0

if __name__ == "__main__":
    sys.exit(main())
