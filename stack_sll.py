# Name:Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/8/2023
# Description:

from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
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
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Adds element to top of the stack
        """
        new_node = SLNode(value)  # creates new object
        if self.is_empty():  # makes sure stack is not empty
            self._head = new_node
        else:
            new_node.next = self._head  # assigns the next node to the head
            self._head = new_node

    def pop(self) -> object:
        """
        Removes top element from stack and returns the value
        """
        if self.is_empty():
            raise StackException("Stack is empty")  # raises StackException if the stack is empty
        value = self._head.value  # stores current node
        if self._head.next is None:
            self._head = None  # Sets head to none if there is only one node
        else:
            self._head = self._head.next  # sets head to the next node
        return value

    def top(self) -> object:
        """
        Returns top element in a stack without removing it
        """
        if self.is_empty():
            raise StackException("Stack is empty")
        return self._head.value  # returns value