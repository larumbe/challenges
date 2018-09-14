import DoubleLinkList

def reverse(head):
    if (head is None):
        return head

    auxprev = None
    current = head
    while (current is not None):
        new = DoublyLinkedListNode(current.data)
        new.next = auxprev
        if (auxprev is not None):
            auxprev.prev = new
        current = current.next
        auxprev = new

    return auxprev
        
        
        
        

