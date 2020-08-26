 # linked_list.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================


'''
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
**********************************************************************************
'''

class SLNode:
    def __init__(self):
        self.next = None
        self.data = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"[Node: {self.data}] --> Next: {self.next.data})"


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        cur = self.head # cur = front sentinal
        for i in range(index): # loops the linked list to get node at index - 1 for insertion.
            if cur.next != self.tail:
                cur = cur.next
            else:
                raise Exception("Index out of bounds.")
        if index > -1:
            new_link.next = cur.next # records the next node of the linked list.
            cur.next = new_link # inserts new_link into the linked list.
        else:
            raise Exception("Index out of bounds.")

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """
        cur = self.head.next # cur = front sentinal
        prev = self.head
        if self.head.next != self.tail: # Ensures the list is not empty.
            for i in range(index): # loops the linked list to get node at index - 1 for insertion.
                if cur.next != self.tail: # Ensures cur and prev don't progress past the last link
                    cur = cur.next
                    prev = prev.next
                else:
                    raise Exception("Index out of bounds.")

            if index > -1:
                prev.next = cur.next
            else:
                raise Exception("Index out of bounds.")
        else:
            raise Exception("Index out of bounds.")

    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        new_link.next = self.head.next  # Sets new_link.next to previous head.next value.
        self.head.next = new_link  # Re-sets self.head.next to new_link. Done second to avoid losing all references to later data.


    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        cur = self.head
        while cur.next != self.tail: # Loops list until cur just before tail. Works on empty list.
            cur = cur.next

        new_link.next = cur.next  # records the end of the linked list.
        cur.next = new_link  # inserts new_link into the linked list.

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        if self.head.next != self.tail: # Ensures the list is not empty.
            return self.head.next.data
        else:
            return None

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """
        cur = self.head
        while cur.next != self.tail: # Loops list until cur is equal to the final link.
            cur = cur.next

        if cur != self.head: # Ensures the list is not empty.
            return cur.data
        else:
            return None

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        if self.head.next != self.tail: # Ensures the list is not empty.
            cur = self.head.next
            self.head.next = cur.next


    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        cur = self.head.next
        prev = self.head
        while cur != self.tail and cur.next != self.tail: # Ensures cur doesn't = self.tail in case of empty list. Loops list until cur is at the final link.
            cur = cur.next
            prev = prev.next

        if cur != self.tail:
            prev.next = cur.next

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """
        if self.head.next == self.tail:
            return True
        else:
            return False



    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        cur = self.head
        while cur.next != self.tail: # Loops list looking for match
            cur = cur.next
            if cur.data == value: # If match, return true
                return True

        return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """
        found = None
        cur = self.head.next
        prev = self.head
        while self.head.next != self.tail and found == None: # Loops is list is not empty and item has not been confirmed found or not found.
            if cur.data == value: # Since cur stars at self.head.next, checks this link first
                prev.next = cur.next  # Remove cur from list
                found = True  # Ensures only first instance of item is removed.

            if cur.next == self.tail:
                found = False

            if cur.next != self.tail: # Ensures cur doesn't pass last item in list.
                cur = cur.next
                prev = prev.next

'''
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List
**********************************************************************************
'''

class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None

class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        cur = self.sentinel # cur = sentinel
        for i in range(index): # loops the linked list to get node at index - 1 for insertion.
            if cur.next != self.sentinel:
                cur = cur.next
            else:
                raise Exception("Index out of bounds.")
        if index > -1:
            new_link.next = cur.next # records new_links next node
            new_link.prev = cur  # records cur as new_links previous node
            cur.next.prev = new_link # records prev of next link to new_link
            cur.next = new_link # records next of cur to new_link.
        else:
            raise Exception("Index out of bounds.")


    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        cur = self.sentinel.next # cur = sentinal
        if self.sentinel.next != self.sentinel: # Ensures the list is not empty.
            for i in range(index): # loops the linked list to get node at index - 1 for insertion.
                if cur.next != self.sentinel: # Ensures cur doesn't progress past the last link
                    cur = cur.next
                else:
                    raise Exception("Index out of bounds.")

            if index > -1:
                cur.prev.next = cur.next # Cur is no longer called by .next
                cur.next.prev = cur.prev # Cur is no longer called by .prev, removing all references to it.
            else:
                raise Exception("Index out of bounds.")
        else:
            raise Exception("Index out of bounds.")

    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        new_link.next = self.sentinel.next # Records next for insertion
        new_link.prev = self.sentinel # Records prev for insertion
        self.sentinel.next = new_link # Replaces sentinels next with new link
        new_link.next.prev = new_link # Replaces the next nodes previous with new link, fully inserting it.

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        new_link.next = self.sentinel # Records next for insertion
        new_link.prev = self.sentinel.prev # Records prev for insertion
        new_link.prev.next = new_link # Replaces previous nodes next with new link
        self.sentinel.prev = new_link # Replaces sentinels prev with new link, fully inserting it.

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """
        if self.sentinel.next != self.sentinel:
            return self.sentinel.next.data
        else:
            return None

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """
        if self.sentinel.prev != self.sentinel:
            return self.sentinel.prev.data
        else:
            return None

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        if self.sentinel.next != self.sentinel: # Ensures list is not empty.
            self.sentinel.next.next.prev = self.sentinel # Removes sentinel.next from being called by .prev
            self.sentinel.next = self.sentinel.next.next # Removes sentinel.next from being called by .next. Removes all reference to it.


    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """
        if self.sentinel.prev != self.sentinel: # Ensures list is not empty.
            self.sentinel.prev.prev.next = self.sentinel # Removes sentinel.prev from being called by .next
            self.sentinel.prev = self.sentinel.prev.prev # Removes sentinel. prev from being called by .prev, removing all references to the node

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """
        if self.sentinel.next == self.sentinel:
            return True
        else:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """
        cur = self.sentinel
        while cur.next != self.sentinel:
            cur = cur.next
            if cur.data == value:
                return True
        return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """
        found = None
        cur = self.sentinel.next
        while self.sentinel.next != self.sentinel and found == None:  # Loops is list is not empty and item has not been confirmed found or not found.
            if cur.data == value:  # Checks if value matches cur.data
                cur.prev.next = cur.next  # Removes cur from being called by next.
                cur.next.prev = cur.prev # Removes cur from being called by prev. No references to cur, it's removed.
                found = True  # Ensures only first instance of item is removed.

            if cur.next == self.sentinel:
                found = False

            if cur.next != self.sentinel:  # Iterates cur and prev forward. Ensures cur doesn't pass last item in list.
                cur = cur.next

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0
        """
        endFound = False
        cur = self.sentinel
        oldNext = self.sentinel.next # Keeps track of the old .next value
        while endFound == False: # Re-verses the traversal order of .next
            cur.next = cur.prev
            cur.prev = oldNext
            oldNext = cur
            cur = cur.next
            if cur == self.sentinel: # Once the list has been fully traversed, return endFound = True
                endFound = True

