from singleLinkedList import *


def findMergeNode(head1, head2):
    visited = []

    c1 = head1
    c2 = head2

    while(True):
        if (c1 is not None):
            if c1.data in visited:
                return c1.data
            else:
                print(c1.data)
                visited.append(c1.data)
                c1 = c1.next

        if (c2 is not None):
            if c2.data in visited:
                return c2.data
            else:
                print(c2.data)
                visited.append(c2.data)
                c2 = c2.next

        if ((c1 is None) and (c2 is None)):
            return 0


l1 = SinglyLinkedList()
a = SinglyLinkedListNode(1)
l1.insert_node(a)
a = SinglyLinkedListNode(2)
l1.insert_node(a)
a = SinglyLinkedListNode(3)
l1.insert_node(a)

l2 = SinglyLinkedList()
a = SinglyLinkedListNode(1)
l2.insert_node(a)
a = SinglyLinkedListNode(3)
l2.insert_node(a)
