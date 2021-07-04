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
`Time complexity` is `O(1)` for every insertion and fetching the latest hash.\
For validating a node in case the blockchain itself is tampered with,
the complexity is `O(n)`. For validating against the node itseld, the complexity
is `O(1)`.\
`Space complexity` is `O(n)` since as many nodes have to be created for each 
data.
