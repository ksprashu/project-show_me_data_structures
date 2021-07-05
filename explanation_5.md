# Blockchain
## Explanation
A blockchain is a linked list where the data in each node contains a Block 
object, and the contents of a Block object has information about previous nodes
in the linked list.

The idea behind this is that if any node in the blockchain is tampered with, 
then the hash of the subsequent nodes will be violated since its hash was
based on the information that was in the prior nodes.

### Linked List
We will implement a basic Linked List, where the data of each node will be a
`Block` object, and will link to the previous node. New nodes will be added
to the `head` and we will have to traverse back in order to validate the 
history.

### Operations
+ add_block()\
This method adds the block to the blockchain. Verifications can be done on top
of the most recent block - eg: validate prev_hash, and validate that the 
timestamp is more recent than the last block.

+ get_latest_hash()\
The latest hash can be fetched from the BlockChain when creating a new block.
This is necessary to preserve the right order of insertion into the blockchain.

## Validation
The BlockChain is validated by tampering with a block in the following ways.
1. Change the text of a block and present it.\
This can be validated by generation the hash and checking whether it has changed.
2. Change the hash itself of the modified block.\
In this case, we can look for the hash in the blockchain and it will not be
found since the has has changed.
3. In the final case, the node in the blockchain itself can be tampered with.\
This can be validated by checking the `previous_hash` in the newer node to 
determine whether the current node has been tampered with.

## Complexity
### Time Complexity
#### Insertion
When inserting a block, there are two operations to be performed. 
1. Compute the hash of the block. While this is an intensive operation, this will
take a constant time per block. The order is `O(1)`
2. The block is then inserted into the linked list. This would take 2-3 book-keeping 
operations to adjust the previous reference and update the head. The order for this
is `O(1)`.

Total time complexity for insert is then `O(1)` for each block.

#### Validation
For validating a block against it's hash, only the hash has to be recomputed. 
This is done in `O(1)` time. When validating against the blockchain or when
validating the blockchain itself, we might have to go through the entire linked
list and this will take `O(n)` time.

This could be optimised with a lookup table at the cost of increased space complexity.
However since we don't understand all the use cases of blockchain as yet, we will 
not implement this for now.

### Space Complexity

For each block, 4 values are saved - the data, timestamp, previous hash, and
own hash. In addition, the node itself will store a reference to the previous node
which is an additional space. 

Since there are a fixed number of references and values saved per block and this
doesn't change with the block, the space complexity for each block is of the order
`O(1)`.

Validation doesn't need any additonal space as we will walk through the node
or list in-memory.
