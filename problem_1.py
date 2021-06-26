"""This modules contains a class that can be used for a LRU Cache.
"""


class DoubleNode:
    """Doubly Linked Node object for the linked queue.
    """

    def __init__(self, value):
        self._value = value
        self._left_node = None
        self._right_node = None

    def get_left_node(self):
        """Returns left node.
        """
        return self._left_node

    def set_left_node(self, node):
        """Sets left node.
        """
        self._left_node = node
        if node:
            node._right_node = self

    def get_right_node(self):
        """Returns right node.
        """
        return self._right_node

    def set_right_node(self, node):
        """Sets right node.
        """
        self._right_node = node
        if node:
            node._left_node = self

    def get_value(self):
        """Gets value of node.
        """
        return self._value


class UniqueQueue:
    """This class will implement a queue where each element has a unique entry.

    Whenever an element is pushed that previously exists, it's existing
    entry will be cleared and the element will be added to the tail.

    Implement queue as a linked list to avoid time complexity when resizing.

    Q: head --> elem1 <--> elem2 <--> elem3 <-- tail
    """

    def __init__(self):
        self._elements = dict()  # will hold the index for each element
        self._head = None
        self._tail = None

    def push(self, value):
        """Pushes a value to the tail.
        """
        new_node = DoubleNode(value)
        if not self._head:
            # set head and tail for first element
            self._head = new_node
            self._tail = self._head
        else:
            # add new node to the right of tail element
            self._tail.set_right_node(new_node)
            self._tail = new_node

            # if element already in queue, then pop it and squeeze links
            if value in self._elements:
                # if value found at head, pop it; tail will self adjust
                if self._head.get_value() == value:
                    self.pop()
                else:
                    old_node = self._elements[value]
                    old_node.get_left_node().set_right_node(
                        old_node.get_right_node())

        # update lookup
        self._elements[value] = new_node

    def pop(self):
        """Pops from the head and return the value
        """
        if self._head:
            node = self._head
            # Move head to the next node
            self._head = self._head.get_right_node()
            if self._head:
                self._head.set_left_node(None)

            # Remove value from lookup dict
            val = node.get_value()
            del self._elements[val]
            return node.get_value()

        return None


class LRU_Cache(object):
    """Least Recenty Used Cache implementation.

    This is built using a Dictionary for O(1) retrieval and a
    Unique Queue for maintaining least used element.
    """

    def __init__(self, capacity):
        self._capacity = capacity
        self._contents = dict()
        self._lru_queue = UniqueQueue()

    def get(self, key):
        """Retrieve item from provided key. Return -1 if nonexistent.
        """

        if key in self._contents:
            self._lru_queue.push(key)  # update usage
            return self._contents[key]
        else:
            return -1

    def set(self, key, value):
        """Set the value if the key is not present in the cache.

        If the cache is at capacity remove the oldest item.
        """

        if self._is_full():
            self._flush_lru_key()

        self._contents[key] = value
        self._lru_queue.push(key)  # update usage

    def _is_full(self):
        """Returns True if the cache is up to capacity.
        """

        if len(self._contents) >= self._capacity:
            return True
        else:
            return False

    def _flush_lru_key(self):
        """Removes a single entry which was the least recenty used.
        """

        oldest = self._lru_queue.pop()
        assert oldest in self._contents, \
            f'LRU Queue has {oldest} but not the contents'
        del self._contents[oldest]
