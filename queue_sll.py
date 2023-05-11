# Name:Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/8/2023
# Description:

from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds new value to the end of the queue
        """
        new_node = SLNode(value)  # creates new object
        if self.is_empty():  # checks to make sure queue is not empty
            self._head = new_node  # if the queue is empty, points to new node
            self._tail = new_node  # if the queue is empty, points to new node
        else:
            self._tail.next = new_node  # sets the end node to the new node value
            self._tail = new_node

    def dequeue(self) -> object:
        """
        Removes the first element from the queue and returns it
        """
        if self.is_empty():  # checks if queue is empty
            raise QueueException("Empty queue")
        value = self._head.value  # stores the node value in the head
        if self._head is self._tail:  # checks if there is only one node in the queue
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next  # removes first node
        return value

    def front(self) -> object:
        """
        Returns front element in the queue without removing it
        """
        if self.is_empty():  # checks to see if the queue is empty
            raise QueueException("Empty Queue")
        return self._head.value  # returns the value of the first element