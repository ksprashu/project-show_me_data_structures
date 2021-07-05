# Overview - Data Compression
## Explanation - Design Decisions

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
##### Encoding
The following stages are executed to __encode__ the data.
1. A frequency map is created for all the characters. This has to go through each
character in the data and takes `O(n)` time.
2. Now each element is converted into a tree representation. Since there are now
`n'` elements where `n' <= n` is the number of unique characters in the string.
This is done in `O(n`)` time.
3. Each element is inserted into a heap. Since in the worst case an insertion into
the heap will require to re-arrange all the elements along the height of a tree,
the time complexity for inserting a single node is `O(log(n))`. However there are
`n' ~= n` nodes to be inserted, and hence the total time taken for building the heap
is `O(n.log(n))`.
4. Two elements are popped at a time from the heap and combined into a single tree.
There are a fixed number of operations to combine the nodes into a tree (add left child
and add right child), however each time a node is removed from the tree, the tree
has to be rebalanced along the height of the tree and the time complexity for this 
is `O(log(n))`. Doing this for all the `n` elements will be done in `O(n.log(n))`.
5. Finally, the tree is parsed recursively to determine the bits for each node. Since
all `n` nodes are visited once, the time taken is of the order `O(n)` and a lookup
table is created post parsing.
6. Now the data is encoded by going through it one character at a time and finding
the corresponding code. The time complexity is `O(n)`.

Total time complexity for encoding the data will be `4.O(n) + 2.O(n.log(n))`. 
We can ignore the lower order terms since the higher order terms will dominate when
the value of `n` is very large.

Hence the final time complexity is of the order of `O(n.log(n))`

##### Decoding
To __decode__ the data, the bits from the coded data is read in order and the tree
is parsed to get to the leaf node. Assuming a balanced and complete tree, we have to 
read the height of the tree on average to get to the leaf, hence there are `O(log(n))`
reads per character that is decoded. For a string of size `n` the complexity is 
`O(n.log(n))` to decode the entire string.

#### Space Complexity

##### Encoding
The following structures are created while encoding.
1. A dictionary of size `n'` where `n'` is the number of unique characters. In the
worst case all characters occur once, and the complexity is `O(n)`.
2. A heap is created where each element of the heap is the character frequency
represented as the node of the tree. While each node is stored using a couple of
variables, and with the book keeping variables like `head`, the total space taken
up is `O(n)`.
3. A Huffmann Tree is then built where every character is saved as the leaf of the
tree. For every two nodes, there is a root which hold the sum of the frequencies.
The space to store all this will be `2.n` and is of the order `O(n)`.
4. The tree is parsed to get the codes for each character. Since there are `n` 
characters, the complexity is `O(n)`.
5. To create the encoded string, each character is temporarily represented by a few
bits. Assuming a worst case length of `x` for each character, a total of `x.n` bytes
will be needed. This is an order of `O(n)`.

Total space needed for all the above elements is `5.n` and is still of the order
`O(n)`.

##### Decoding
For decoding, the decoded string is built as the tree is parsed which comes in
as the input. Since the only space occupied is the final string, the total space
complexity is `O(n)` where `n` is the number of characters in the string.
