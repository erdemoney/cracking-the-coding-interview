import sys
import random
from ..common.linked_list import *

# question:
#   Given two (singly) linked lists, deterimine if the wro lists intersect.
#   Return the intersecting node. Note that the intersection is defined based
#   on reference, not value. That is, the kth node of the first linked list is
#   the exact same node (by reference) as the jth node of the secind linked
#   list then they are intersecting.
#
# concept:
#   maintain map of all seen nodes in the first list, then iterate over the
#   second list and find the first common node
#
# runtime:
#   O(n)

def intersection(ll1: SinglyLinkedList, ll2: SinglyLinkedList) -> int:
    seen = {}
    index = 0
    for node in ll1:
        seen[node] = 1
    for node in ll2:
        if seen.get(node) is not None:
            return index 
        index += 1
    return -1

def main() -> int:
    # select random intersection point
    intersection_idx = random.randrange(11)
    if intersection_idx == 10:
        print('No intersection set')
    else:
        print('Intersection set at index', intersection_idx)

    ll2 = SinglyLinkedList()
    ll1 = SinglyLinkedList()

    # create two random 10 long lists that intersect at intersection_idx
    for i in range(10):
        if i < intersection_idx:
            ll1.insert(Node(random.randrange(10)))
            ll2.insert(Node(random.randrange(10)))
        if i == intersection_idx:
            node = Node(random.randrange(10)) 
            ll1.insert(node) 
            ll2.insert(node) 
        else:
            ll1.insert(Node(random.randrange(10)))

    ret = intersection(ll1, ll2)
    if ret == -1:
        print('No intersection found')
    else:
        print('Intersection found at index', ret)
    return 0

if __name__ == '__main__':
    sys.exit(main())
