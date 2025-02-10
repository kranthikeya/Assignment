# -*- coding: utf-8 -*-

import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "0", ["Genesis Block"], time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print("Blockchain is invalid: Current block hash is incorrect.")
                return False

            if current_block.previous_hash != previous_block.hash:
                print("Blockchain is invalid: Previous block hash does not match.")
                return False

        print("Blockchain is valid.")
        return True

    def tamper_with_chain(self, block_index, new_transactions):
        if block_index < len(self.chain):
            self.chain[block_index].transactions = new_transactions
            self.chain[block_index].hash = self.chain[block_index].calculate_hash()
            print(f"Block {block_index} tampered with new transactions: {new_transactions}")
        else:
            print("Invalid block index.")

# Example Usage
if __name__ == "__main__":
    blockchain = Blockchain(difficulty=4)

    print("Mining block 1...")
    blockchain.add_block(Block(1, "", ["Transaction 1", "Transaction 2"], time.time()))

    print("Mining block 2...")
    blockchain.add_block(Block(2, "", ["Transaction 3", "Transaction 4"], time.time()))

    # Print blockchain
    print("\nBlockchain:")
    for block in blockchain.chain:
        print(json.dumps(block.__dict__, indent=4))

    # Validate blockchain
    print("\nValidating blockchain...")
    blockchain.is_chain_valid()

    # Tamper with blockchain
    print("\nTampering with block 1...")
    blockchain.tamper_with_chain(1, ["Tampered Transaction"])

    # Validate blockchain after tampering
    print("\nValidating blockchain after tampering...")
    blockchain.is_chain_valid()