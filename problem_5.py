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
        assert block and block.data and block.hash is not None, \
            'Block is empty or doesn\'t have a hash.'
        assert block.previous_hash == self.get_latest_hash(), \
            'Hash mismatch at addition; top of Blockchain might have moved.'
        assert block.timestamp > self.get_latest_timestamp(), \
            'Block has to be newer than the last block on the BlockChain.'

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

    def get_latest_timestamp(self):
        if self.head:
            return self.head.block.timestamp
        else:
            return datetime.datetime.fromtimestamp(0, datetime.timezone.utc)

    def validate_block(self, block):
        """Validates the block and throws an exception if not.

        Checks for the block hash validity.
        Checks whether the block has been linked to from a newer block.
        """
        assert block.hash == block.calc_hash(), \
            f'Warning! Block {block.hash} has a bad hash.'

        node = self.head
        while node:
            if node.block.hash == block.hash:
                break
            node = node.prev
        assert node is not None, \
            f'Warning! Block {block.hash} not found on blockchain'

    def validate_blockchain(self):
        node = self.head
        while node.prev:
            assert node.block.previous_hash == node.prev.block.hash, \
                'Warning! Violation in the BlockChain'
            node = node.prev


if __name__ == '__main__':

    blockchain = BlockChain()

    # insert empty block
    try:
        blockchain.add_block(None)
    except AssertionError as e:
        print(f'Assertion Raised - {e}')

    data1 = 'First Block'
    timestamp1 = datetime.datetime.now(datetime.timezone.utc) - \
        datetime.timedelta(hours=25)
    print(f'\nBlock with data - {data1}, at {timestamp1}')
    block1 = Block(timestamp1, data1, blockchain.get_latest_hash())
    print(f'Block hash = {block1.hash}')

    # insert block1
    blockchain.add_block(block1)

    data2 = 'This is a valid text.'
    timestamp2 = datetime.datetime.now(datetime.timezone.utc) - \
        datetime.timedelta(hours=5)
    print(f'\nBlock with data - {data2}, at {timestamp2}')
    block2 = Block(timestamp2, data2, blockchain.get_latest_hash())
    print(f'Block hash = {block2.hash}')

    data3 = 'Final Block'
    print(f'\nBlock with data - {data3}, at {timestamp2}')
    block3 = Block(timestamp2, data3, blockchain.get_latest_hash())
    print(f'Block hash = {block3.hash}')

    # insert block2
    blockchain.add_block(block2)

    # error inserting block3 - hash
    try:
        print('\nShould raise a hash assertion')
        blockchain.add_block(block3)
    except AssertionError as e:
        print(f'Assertion Raised - {e}')

    # error inserting block3 - timestamp
    block3 = Block(timestamp2, data3, blockchain.get_latest_hash())
    try:
        print('\nShould raise a timestamp assertion')
        blockchain.add_block(block3)
    except AssertionError as e:
        print(f'Assertion Raised - {e}')

    # error inserting block3 - data
    block3 = Block(timestamp2, '', blockchain.get_latest_hash())
    try:
        print('\nShould raise a data assertion')
        blockchain.add_block(block3)
    except AssertionError as e:
        print(f'Assertion Raised - {e}')

    timestamp3 = datetime.datetime.now(datetime.timezone.utc) - \
        datetime.timedelta(hours=1)
    print(f'\nBlock with data - {data3}, at {timestamp3}')
    block3 = Block(timestamp3, data3, blockchain.get_latest_hash())
    print(f'Block hash = {block3.hash}')

    # insert block3 properly
    blockchain.add_block(block3)

    # check that everything is good
    blockchain.validate_block(block3)  # no exceptions
    blockchain.validate_block(block2)  # no exceptions
    blockchain.validate_blockchain()  # no exceptions
    print('\nBlockChain is valid')

    # Let's tamper with block2
    print('\nTamper data of block2')
    bad_block = Block(block2.timestamp, block2.data, block2.previous_hash)
    bad_block.data = 'This text has been modified'

    # Validate the block using the hash
    try:
        blockchain.validate_block(bad_block)
    except AssertionError as e:
        print(f'Assertion Raised - {e}')

    # Let's tamper with hash of block2
    print('\nTamper hash of block2')
    old_hash = bad_block.hash
    bad_block.hash = bad_block.calc_hash()

    try:
        blockchain.validate_block(bad_block)
    except AssertionError as e:
        print(f'Assertion Raised - {e}')

    # Tamper with blockchain
    print('\nTamper with Blockchain')
    node = blockchain.head
    while node:
        if node.block.hash == old_hash:
            node.block = bad_block
            break
        node = node.prev

    # Validate violation in the chain
    try:
        blockchain.validate_blockchain()
    except AssertionError as e:
        print(f'Assertion Raised - {e}')
