# Author: Anantha Perumal
# Date: Oct 1, 2020

from hashlib import sha256

def updateHash(*args):
    hashing_text = ""
    h = sha256()
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

class Block():
    """A Block in BlockChain"""
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self,data,number=0):
        self.data = data
        self.number = number

    def hash(self):
        return updateHash(
            self.previous_hash,
            self.number,
            self.data,
            self.nonce
        )

    def __str__(self):
        return str(
        "Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n" %(
            self.number,
            self.hash(),
            self.previous_hash,
            self.data,
            self.nonce
            )
        )

class BlockChain(object):
    """Chain of Blocks"""
    difficulty = 4

    def __init__(self,chain=[]):
        self.chain = chain

    def add(self,block):
        self.chain.append(block)

    def remove(self, block):
        self.chain.remove(block)

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].hash()
        except IndexError:
            pass

        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block)
                break
            else:
                block.nonce +=1

    def isValid(self):
        for i in range(1, len(self.chain)):
            previous_hash = self.chain[i].previous_hash
            current_hash = self.chain[i-1].hash()
            self_hash = self.chain[i].hash()
            if previous_hash != current_hash or self_hash[:self.difficulty] != "0" * self.difficulty:
                return "Blockchain is not valid: Block "+ str(i+1) +" seems to be changed"
                + " is not valid"
        return "Blockchain is valid"

def main():
    blockchain = BlockChain()
    database = ["data 1", "data 2", "data 3"]

    num = 0
    for data in database:
        num += 1
        blockchain.mine(Block(data,num))

    blockchain.chain[2].data = "New Data"

    for block in blockchain.chain:
        print("Block :")
        print(block)

    print(blockchain.isValid())

if __name__ == '__main__':
    main()
