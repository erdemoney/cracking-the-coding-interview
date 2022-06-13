from ..common.linked_list import *
import sys

# question:
#   You have two number represented by a linked list wehre each node contains
#   a single digit. The digits are stored in reverse order, such that the 1's
#   digit is at the head of the list. Write a function that adds the two
#   numbers and returns the sum as a linked list.
#
# concept:
#   add each digit from both lists, store sum -/% 10 in result linked list.
#   if sum is greater than 10, set carry flag and add 1 to next partial sum

def sum_lists(num1: SinglyLinkedList, num2: SinglyLinkedList) -> SinglyLinkedList:
    h1 = num1.head 
    h2 = num2.head
    carry = 0
    sumList = SinglyLinkedList()
    while h1 is not None and h2 is not None:
        sum = 0
        # check if either list is exhausted, if not add current value to partial sum
        if h1 is not None:
            sum += h1.data
            h1 = h1.next
        if h2 is not None:
            sum += h2.data
            h2 = h2.next
        # if carry flag is set add 1 to partial sum
        sum += carry
        # if partial sum is greater than 10, set carry flag else unset
        if sum >= 10:
            carry = 1
        else:
            carry = 0
        # insert value into result list
        sumList.insert(sum % 10)
    return sumList

def main() -> int:
    input = " ".join(sys.argv[1::]).split('+')

    num1List = SinglyLinkedList()
    num2List = SinglyLinkedList()

    num1 = input[0].split()
    num2 = input[1].split()

    for digit in reversed(num1):
       num1List.insert(int(digit)) 
    for digit in reversed(num2):
       num2List.insert(int(digit)) 

    print(sum_lists(num1List, num2List))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
