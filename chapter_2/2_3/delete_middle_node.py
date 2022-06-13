import sys
import random
from ..common.linked_list import *

# question:
#   Implement an algorithm to delete a node in the middle (i.e., any node but
#   the first or last node, not necessarily the exact middle) of a singly
#   linked list, given only acess to that node.

def delete_middle_node(ll: SinglyLinkedList, node: Node) -> SinglyLinkedList:
    prev = node
    while node.next is not None:
        node.data = node.next.data
        prev = node
        node = node.next
    prev.next = None
    return ll


def random_middle_node(ll: SinglyLinkedList) -> Node:
    n = len(ll)
    assert n > 3

    r = random.randrange(1, n-1)
    cur = ll.head
    for _ in range(r):
       cur = cur.next 
    return cur

def main() -> int:
    ll = SinglyLinkedList()
    for arg in sys.argv:
       ll.insert(arg) 
    print('original list\n', ll, '\n')
    node = random_middle_node(ll)
    print(node.data, 'deleted')
    print(delete_middle_node(ll, node))
    return 0

if __name__ == "__main__":
    sys.exit(main())
