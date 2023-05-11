# Name:Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/8/2023
# Description:


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        Adds new node at the beginning of the list
        """
        new_node = SLNode(value)  # creates new object "SLNode"
        new_node.next = self._head.next
        self._head.next = new_node  # updates the new node object

    def insert_back(self, value: object) -> None:
        """
        Adds new node at the end of a list
        """
        new_node = SLNode(value)  # creates a new object "SLNode"
        node = self._head
        while node.next:  # iterates through list until the last node is reached
            node = node.next
        node.next = new_node  # inserts the new node at the back

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a value at a specific position in a list
        """
        if index < 0 or index > self.length():
            raise SLLException("Invalid index")  # raises the exception if the index is less than 0 or greater than
            # the length
        new_node = SLNode(value)  # creates new object
        current_node = self._head
        current_index = 0  # indexs the list at 0
        while current_index < index:  # iterates through until the object is reached
            current_node = current_node.next
            current_index += 1  # adds 1 to the index
        new_node.next = current_node.next
        current_node.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        Removes a value at a specified index
        """
        if index < 0 or index >= self.length():
            raise SLLException("Invalid index")
        current_node = self._head
        current_index = 0
        while current_index < index:
            current_node = current_node.next
            current_index += 1
        node_to_remove = current_node.next
        current_node.next = node_to_remove.next
        node_to_remove.next = None

    def remove(self, value: object) -> bool:
        """
        Removes the first value that matches the given value target
        """
        current_node = self._head
        while current_node.next is not None:
            if current_node.next.value == value:
                node_to_remove = current_node.next
                current_node.next = node_to_remove.next
                node_to_remove.next = None
                return True
            current_node = current_node.next
        return False

    def count(self, value: object) -> int:
        """
        Counts the number of objects that match the determined value
        """
        count = 0  # sets the count to 0
        current_node = self._head.next
        while current_node:
            if current_node.value == value:
                count += 1
            current_node = current_node.next
        return count

    def find(self, value: object) -> bool:
        """
        Returns a Boolean value based on whether the determined value is in the list
        """
        current_node = self._head.next
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        Returns a new linked list the contains the requested number of nodes from the original list, starting at the
        requested index
        """
        if start_index < 0 or start_index >= self.length():
            raise SLLException("Invalid start index")
        if size < 0:
            raise SLLException("Invalid size")
        if start_index + size > self.length():
            raise SLLException("Not enough nodes for the requested slice size")
        node = self._head.next
        count = 0  # creates the count
        while count < start_index:  # starting node
            node = node.next
            count += 1
        new_list = LinkedList()  # creates new list
        while count < start_index + size:  # copies contents of original list to the new list
            new_list.insert_back(node.value)
            node = node.next
            count += 1
        return new_list