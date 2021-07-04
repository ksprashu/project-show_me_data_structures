# Overview - Data Compression
## Explanation

### Frequency Map / Priority Queue
The first thing that we'll need here is a data structure to collect the occurances of each character. We can go through the text once and collect the occurance of each character in a dictionary.

This will require `O(n)` space and will happen in `O(n)` time.\
Once this is done, we can sort the dictionary by values so that we get the frequency of characters in ascending order. Sorting will happen in `O(n.log(n))` time.

### Building the Huffman Tree
Now we will have to build a tree picking the nodes in order of frequency. There
are a few approaches that I am thinking of here. 

#### 1. Sorted Dictionary
We can chose a simple approach of a dictionary + sorting as it will take the same time complexity as inserting into a priority queue, which has to maintain sort order by scanning on every insert.

However while building the tree, once I have combined the first two smallest
elements and got a tree, I have to then each time select the first two elements, 
and compare the second element with the root of the tree to decide whether to use 
the tree + first frequency element, or use the two frequency elements.

This leads to a lot of comparisons, and writing the algorithm will get a
little more complex. Especially if each combination generates another tree - then
we'll have to compare multiple tree with multiple frequency elements and this will
get out of hand very soon.

#### Recursive code
If I had a always sorted data structure, I could simply keep popping the first
two elements off the stack and combining them together in a tree and then pushing
the tree back into the sorted list. This requires far less comparision logic at
the algorithmic level and we could write a simple recursive code.

In order to write a simple algorithm (for maintainability and readability) we
will go with the sorted data structure approach. There is a time complexity involved
here since with each insertion, or each time we pop elements (in fact twice), 
we have to rebalance the tree.

The two options are Priority Queues and Min Heaps.

#### 2a. Priority Queue
This is basically what is needed for holding the nodes of the tree so that we
can pick up the smallest two nodes each time and insert a new node which will find
it's right sorted place in the queue.

However while the fetch is trivial, the overhead is that the entire list will 
auto sort each time an insert is made. Considering sorting is `O(n.log(n))` and 
we have to insert `n` nodes, the complexity will become `O(n.n.log(n))`

#### 2b. Min Heap
When using min heap, only the branch that is modified is heapified and the entire
tree is not re-sorted. This happens each time we pop an element, and again each
time we insert an element. However the complexity is then only `O(2.n.log(n))`
since we do this twice for each of `n` elements.

It probably then makes sense to implement a Min Heap to store the nodes and we 
will hide the complexity to build the entire tree behind a recursion.

### Parsing the Huffmann Tree
To decode the characters based on the code, we have to walk down the tree. 
Access time to walk down the tree for each element is `O(log(n))` and hence to  decode, the time taken for `n` elements will be `O(n.log(n))`.

Space complexity will be only what is necessary to store each element of the Huffmann tree and the transient priority queue which is of the order `O(n)`.

#### Time Complexity

Total time complexity for each encoding and decoding will then be `O(n.log(n))`.
Space complexity will be of the order `O(n)` - the tree being sized for each
character and the code will be a compressed version, but at worst will be of the
order `O(n)`.