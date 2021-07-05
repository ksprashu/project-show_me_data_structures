# Least Recently Used Cache
## Explanation

What we want here are 2 data structures
1. A Data Structure for storing to and fetching from cache. This will be a `HashMap` since we need a worst case time complexity of `O(1)` for `get()` and `set()`
2. The second Data Structure we need is a mechanism to find the least recently used element. This goes with First In First Out principle which is a `Queue`.

### Data Structures
#### HashMap
The HashMap will be used to store the entries of the cache. We will implement this as a python `dict` object. The read and write complexity of this will be `O(1)`. 
An additional case will be to delete an entry from the cache and this will also be done in `O(1)`
#### Queue
The Queue is necessary to determine the order in which the elements were accessed. Specifically we want to know which element was accessed the earliest. We want to be able to find this out without having to parse the entire queue and remove duplicates.

Hence we will create a custom Queue for this requirement with the following design.
1. We will use a Linked List to store the `keys` that have been pushed to the queue. This is to avoid managing the list indexes and in order to have better space compexity. We want this queue to contain only one instance of an element.
1. We will use a Lookup table to be able to access a `Node` with `O(1)` complexity. This will be a `dict` object where the key is the cache key and the value is the Node reference.

The queue should store only one copy of an element. This is because if the elements pushed are for example `1, 2, 3, 1, 2`, then when we pop we should get back 3 as the least recently used element and we want to be able to get that back with minimum time complexity. Hence whenever an element is pushed to the tail of the queue, we should remove it from elsewhere in the queue. This is where the lookup helps. 

### Time Complexity
There are 2 operations that are done here. 
1. Looking for an entry in the cache, and
2. Adding a key-value entry to the cache
#### Lookup `get()`
There are 2 parts to the lookup. 
1. Look for the key in the lookup table.\
Since we are using a hashmap for this, the lookup happens in `O(1)`
2. Update the Least Recently Used queue.\
Updating the queue is again broken into the following operations
    1. Creating a new node on the queue
    2. Updating the lookup with the new reference

Creating a new node does the following
1. Creating a node and setting its value
2. Linked the left node
3. Linking the right node
4. Updating the left and right nodes
5. Updating the head / tail nodes

While this does take about 5 instructions, it is not dependent on the size of the total entries in the cache and hence happens in constant time - `O(1)`

Updating the lookup does the following
1. Remove the previous entry of the key element from the Queue. This happens in constant time `O(1)` to look up the node address. 
2. Then the process to connect its left and right nodes to each other, and create a new node at the tail. Agains while there are a few operations done here, it happens in constant time `O(1)` and is not dependant on the size of the queue.

Hence overall, Lookup happens in constant time, especially relative to a large cache size. There are multiple operations, each taking a worst case time of `O(1)` and\
hence the overall worst case time is `O(1)`.

#### Insert `put()`
Similar to `get()`, this operation consists of 2 parts.
1. Inserting an element into the lookup. This happens in `O(1)`
2. Add a least recently used entry into the Queue\
This is the same as the Lookup operation since all it does is to update the access to the element and as discussed before, this happens in constant time `O(1)`.

However, if the cache is full, since this is a LRU cache, the oldest entry has to be removed if we are at the limit of the cache size. This involves the following operations
1. Pop the element from the head of the queue
2. Update the queue to a new head
3. Remove the element from the lookup

All the above are operations that will happen in constant time since it requires
modifying a single node and happens in `O(1)`.

Hence, since multiple operations are all taking only `O(1)`,
the overall Insert operation will also happen in constant time `O(1)`

### Space Complexity
For each element in the queue, the following entries are created.
1. 1 key-value in the cache lookup dictionary which stores the key + value
2. 1 key-value in the LRU queue lookup dictionary which stores the key + reference 
to node
3. 1 node in the linked list, which contains the value, and 2 pointers to the 
previous and next nodes.

There are also constant references for book keeping such as head, tail, etc.

Hence for each entry there are about 5 memory spaces used across the data structures. The total space used is then 5 * n, which amounts to `O(n)`
