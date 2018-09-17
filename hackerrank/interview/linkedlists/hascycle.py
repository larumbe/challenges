class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    visited = []

    current = head
    while (current is not None):
        if (current.data not in visited):
            visited.append(current.data)
            current = current.next
        else:
            return True
    return False

