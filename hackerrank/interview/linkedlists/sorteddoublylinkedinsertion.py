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
    if (head is None):
        head = DoublyLinkedListNode(data)
        return head

    current = head
    # check end of the list
    while (current.data < data):
        current = current.next
    newnode = DoublyLinkedListNode(data)
    newnode.next = current
    newnode.prev = current.prev
    current.prev = newnode

    if (newnode.prev is not None):
        newnode.prev.next = newnode

    return head
