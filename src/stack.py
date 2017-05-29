"""Our stack for linked list."""


from linked_list import LinkedList


class Stack(object):
    """Class stack."""

    def __init__(self, data=None):
        """Init for stack."""
        self._newLinkedList = LinkedList(data)

    def push(self, val):
        """Push function for stack."""
        return self._newLinkedList.push(val)

    def pop(self):
        """Pop function for stack."""
        return self._newLinkedList.pop()

    def __len__(self):
        """Length function for stack."""
        return len(self._newLinkedList)
