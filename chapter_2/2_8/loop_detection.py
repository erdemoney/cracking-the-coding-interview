import sys
import random
from ..common.linked_list import *

# question:
#   Given a circular linked list, implement an algorithm that returns the node
#   at the beginning of the loop.
#
# concept:
#   maintain map of all seen nodes, if a node is already in the seen list then
#   the list contains a loop
#
# runtime:
#   O(n)

def loop_detection(ll: SinglyLinkedList):
    seen = {}
    for node in ll:
        if seen.get(node) is not None:
            return node 
        seen[node] = 1
    return None

def main() -> int:
    return 0

if __name__ == '__main__':
    sys.exit(main())
