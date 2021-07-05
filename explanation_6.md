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
To get the union of two linked lists, we will go through each element in the first
list while adding it to a new list. We will then go through each element in the second
list while adding it to the end of the previously created new list. 

### Intersection
Normally the intersection operation will require us to take each node in list1
and compare it to every element in list2 to check if it exists. If it exists, we
will add it to the new list. However this is not efficient. At the cost of increased
space complexity, we can introduce a lookup table which is populated while parsing a
single linked list. 

In this case we will use a `set()`. The set is populated as we walk
through the first list. Then for every element part of secnd list, we will check
if it exists in the set and if so, we will add it to the new linked list. To handle
multiple occurrances, we will delete a node once we have made an intersection.

### Time Complexity.
__Union__ is a `O(m+n)` operation in time where `m` is the size of list1 and `n` is
the size of list2. Since we can go through each linked list in sequence and append 
the elements in a new list, the time complexity for union is `O(m+n)`.

__Intersection__ with the improved logic take `O(m+n)` time to go through both
the lists. To create the lookup table, insertion is a `O(1)` operation. To read
from the lookup table is also a `O(1)` operation. 

Hence total time complexity for intersection is `O(m+n)`

### Space Complexity
For __union__, we will store every element in a new list as we read it. There is 
no other space used for creating the union and hence space complexity is `O(n)`.

For __intersection__, since we are prioritising time complexity, there is a
lookup table that is created as a python set. This takes `O(m)` space where `m < n`.
This is a optimization that we can apply to keep the size of the set small. 
In addition the worst case space taken to create the new list will be the size
of the smaller list at most, which is `O(m)`.

