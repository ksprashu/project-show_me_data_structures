# Union and Intersection of Two Linked Lists
## Explanation

### Assumptions
1. There could be duplicates in the list and we have to determine how to handle
them. We will treat each occurrance as a separate element. In case of `Union`
we will retain the recurring elements. In case of `Intersection`, an element
will occur twice in the intersection, if it occurred twice in each of the
linked lists.
2. The second assumption is that we don't have to worry about any sorting order
as long as the elements are present in the final list.

### Union
Union is a `O(m+n)` operation in time, since we can go through each linked list
in sequence and append the elements in a new list.

### Intersection
Intersection involved going through each element in one list, and comparing 
with each element of the second list. This is a `O(m+n)` operation.

However, at the cost of increasing space complexity by `O(m)` where `m < n`, 
we can store the elements of list1 in a `set` and use this to lookup while 
parsing through the second list. `set` has a lookup time of `O(1)` in python.

While some additional operations are performed to maintain the data structure, 
this will be constant per element, hence the worst case time complexity will
continue to be linear at `O(n)`.
