# Assignment
Simple Blockchain
Explanation of the Code
Block Class:

Represents a single block in the blockchain.

Contains attributes like index, previous_hash, transactions, timestamp, nonce, and hash.

The calculate_hash method computes the SHA-256 hash of the block's data.

The mine_block method implements a simple proof-of-work mechanism by finding a hash with a specified number of leading zeros (based on the difficulty).

Blockchain Class:

Manages the chain of blocks.

The create_genesis_block method creates the first block (genesis block) in the chain.

The add_block method adds a new block to the chain after mining it.

The is_chain_valid method checks the integrity of the blockchain by verifying the hashes and links between blocks.

The tamper_with_chain method demonstrates tampering with a block's data.

Proof-of-Work:

The mine_block method ensures that block creation is computationally intensive by requiring the hash to have a certain number of leading zeros.

Tampering Detection:

The is_chain_valid method detects any tampering by recalculating and comparing hashes
