"""Implements a sample BlockChain.
"""

import datetime
import hashlib


class Node:
    """A node for the BlockChain Linked List.
    """

    def __init__(self, block):
        self.block = block
        self.prev = None


class Block:
    """A Block that goes onto the BlockChain.
    """

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp).encode('utf-8')
        hash_str += self.data.encode('utf-8')
        hash_str += str(self.previous_hash).encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    """BlockChain implementation.
    """

    def __init__(self):
        self.head = None

    def add_block(self, block: Block):
        """Adds a block to the blockchain.

        Verifies that the data is consistent before adding the block.
        """

        assert block.previous_hash == self.get_latest_hash(), \
            'Hash mismatch at addition; top of Blockchain might have moved'

        new_node = Node(block)

        if not self.head:
            self.head = new_node
        else:
            new_node.prev = self.head
            self.head = new_node

    def get_latest_hash(self):
        if self.head:
            return self.head.block.hash
        else:
            return 0


if __name__ == '__main__':

    blockchain = BlockChain()

    data1 = 'First Block'
    timestamp1 = datetime.datetime.utcnow() - datetime.timedelta(hours=25)
    print(f'\nBlock with data - {data1}, at {timestamp1}')
    block1 = Block(timestamp1, data1, blockchain.get_latest_hash())
    print(f'Block hash = {block1.hash}')

    # insert block1
    blockchain.add_block(block1)

    data2 = 'This is a valid text.'
    timestamp2 = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
    print(f'\nBlock with data - {data2}, at {timestamp2}')
    block2 = Block(timestamp2, data2, blockchain.get_latest_hash())
    print(f'Block hash = {block2.hash}')

    data3 = 'Final Block'
    timestamp3 = datetime.datetime.utcnow() - datetime.timedelta(hours=4)
    print(f'\nBlock with data - {data3}, at {timestamp3}')
    block3 = Block(timestamp3, data3, blockchain.get_latest_hash())
    print(f'Block hash = {block3.hash}')

    # insert block2
    blockchain.add_block(block2)

    # race condition inserting block3
    try:
        blockchain.add_block(block3)
    except AssertionError as e:
        print(f'Assertion Raised - {e}')

    timestamp3 = datetime.datetime.utcnow() - datetime.timedelta(hours=1)
    print(f'\nBlock with data - {data3}, at {timestamp3}')
    block3 = Block(timestamp3, data3, blockchain.get_latest_hash())
    print(f'Block hash = {block3.hash}')

    # insert block3 properly
    blockchain.add_block(block3)

    # Let's tamper with block2
    print('\nTamper data of block2')
    bad_block = Block(block2.timestamp, block2.data, block2.previous_hash)
    bad_block.data = 'This text has been modified'

    # Validate the block using the hash
    try:
        assert bad_block.hash == bad_block.calc_hash(), \
            'Warning! Block has a wrong hash.'
    except AssertionError as e:
        print(f'Assertion Raised - {e}')

    # Let's tamper with hash of block2
    print('\nTamper hash of block2')
    old_hash = bad_block.hash
    bad_block.hash = bad_block.calc_hash()

    # Validate the block by checking against the block chain
    node = blockchain.head
    while node:
        if node.block.hash == bad_block.hash:
            break
        node = node.prev

    try:
        assert node is not None, 'Warning! Block not found on blockchain'
    except AssertionError as e:
        print(f'Assertion Raised - {e}')

    # Tamper with blockchain
    print('\nTamper with Blockchain')
    node = blockchain.head
    newer_block = None
    while node:
        if node.block.hash == old_hash:
            node.block = bad_block
            break
        node = node.prev

    # Validate violation in the chain
    try:
        node = blockchain.head
        while node:
            assert node.block.previous_hash == node.prev.block.hash, \
                'Warning! Violation in the block chain'
    except AssertionError as e:
        print(f'Assertion Raised - {e}')
