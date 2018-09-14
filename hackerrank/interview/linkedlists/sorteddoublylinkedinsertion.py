import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)
            
def sortedInsert(head, data):
    newnode = DoublyLinkedListNode(data)

    if (head is None):
        head = newnode
        return head

    current = head
    while (True):
        if (current.data < data):
            if (current.next is not None):
                current = current.next
            else:               # last node
                current.next = newnode
                newnode.prev = current
                return head
        else:                   # found the right place
            newnode.next = current
            newnode.prev = current.prev
            if (newnode.prev is not None):
                newnode.prev.next = newnode
            else:
                head = newnode
            current.prev = newnode
            return head
            
