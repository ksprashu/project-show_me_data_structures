"""Program to find the Union and Intersection of 2 linked lists.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur_head = self.head
        out_string = ""
        if not cur_head:
            out_string = "<empty>"
            return out_string

        while cur_head:
            out_string += str(cur_head.value)
            out_string += ' -> ' if cur_head.next else ''
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        self.size += 1

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        return self.size


def union(llist_1, llist_2):
    """Return a new list with the union of the two lists.
    """
    new_list = LinkedList()
    node = llist_1.head
    while node:
        new_list.append(node.value)
        node = node.next

    node = llist_2.head
    while node:
        new_list.append(node.value)
        node = node.next

    return new_list


def intersection(llist_1, llist_2):
    """Returns a new list with the intersection of two lists.
    """
    # put the smaller list first, to reduce space complexity
    if llist_1.size > llist_2.size:
        llist_1, llist_2 = llist_2, llist_1

    items = dict()
    node = llist_1.head
    while node:
        if node.value in items:
            items[node.value] += 1
        else:
            items[node.value] = 1

        node = node.next

    new_list = LinkedList()
    node = llist_2.head
    while node:
        if node.value in items:
            new_list.append(node.value)
            if items[node.value] > 1:
                items[node.value] -= 1
            else:
                del items[node.value]
        node = node.next

    return new_list


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# [3, 2, 4, 35, 6, 65, 6, 4, 3, 21, 6, 32, 4, 9, 6, 1, 11, 21, 1]
print(intersection(linked_list_1, linked_list_2))
# [4, 6, 6, 21]
print()


# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# [3, 2, 4, 35, 6, 65, 6, 4, 3, 23, 1, 7, 8, 9, 11, 21, 1]
print(intersection(linked_list_3, linked_list_4))
# [] == empty
print()


# Test case 3 - single elements
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1]
element_2 = [1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))  # [1, 1]
print(intersection(linked_list_5, linked_list_6))  # [1]
print()

# Test case 4 - element repeating in one list
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1, 1]
element_2 = [1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))  # [1, 1, 1]
print(intersection(linked_list_5, linked_list_6))  # [1]
print()


# Test case 5 - element repeating in both lists
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1, 1]
element_2 = [1, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))  # [1, 1, 1, 1]
print(intersection(linked_list_5, linked_list_6))  # [1, 1]
print()

# Test case 6 - one empty list
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [10]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))  # [10]
print(intersection(linked_list_5, linked_list_6))  # []
print()

# Test case 7 - two empty lists
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))  # []
print(intersection(linked_list_5, linked_list_6))  # []
print()
