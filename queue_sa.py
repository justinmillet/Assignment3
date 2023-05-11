# Name:Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 5/8/2023
# Description:


# Note: Changing any part of the pre-implemented methods (besides adding  #
#       default parameters) will cause the Gradescope tests to fail.      #


from static_array import StaticArray


class QueueException(Exception):
    """Custom exception to be used by Queue class."""
    pass


class Queue:
    def __init__(self) -> None:
        """Initialize new queue based on Static Array."""
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """Override string method to provide more readable output."""

        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)

        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        return self._current_size == 0

    def size(self) -> int:
        """Return number of elements currently in the queue."""
        return self._current_size

    def print_underlying_sa(self) -> None:
        """Print underlying StaticArray. Used for testing purposes."""
        print(self._sa)

    def _increment(self, index: int) -> int:
        """Move index to next position."""

        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0

        return index

    # ---------------------------------------------------------------------- #

    def enqueue(self, value: object) -> None:
        """
        Adds value to end of queue
        """
        if self._current_size == self._sa.length():  # resizes the array if it is full
            new_size = self._sa.length() * 2
            new_array = StaticArray(new_size)  # sets a new array
            index = self._front  # copies elements to new array
            for i in range(self._current_size):  # iterates through the array starting from front to the size
                new_array[i] = self._sa[index]
                index = self._increment(index)
            self._front = 0  # sets first element to index 0
            self._back = self._current_size - 1  # sets last element to the current size minus 1
            self._sa = new_array
        self._back = self._increment(self._back)  # adds new value to the back
        self._sa[self._back] = value
        self._current_size += 1

    def dequeue(self) -> object:
        """
        Removes value from end, and returns it to the beginning
        """
        if self._current_size == 0:  # checks if the size is 0
            raise QueueException("Queue is empty")
        value = self._sa[self._front]  # sets value equal to the front, to be dequeued
        self._front = self._increment(self._front)
        self._current_size -= 1  # lowers the size by 1
        return value

    def front(self) -> object:
        """
        Returns the front element without removing it
        """
        if self._current_size == 0:
            raise QueueException("Queue is empty")
        return self._sa[self._front]  # returns the front element

    # The method below is optional, but recommended, to implement. #
    # You may alter it in any way you see fit.                     #

    def _double_queue(self) -> None:
        """
        TODO: Write this implementation
        """
        pass
