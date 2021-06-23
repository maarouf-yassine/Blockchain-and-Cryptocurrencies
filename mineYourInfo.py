# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:55:24 2021

@author: maarouf
"""
from hashlib import sha256
import json, time

#references to convert to hex (decimal to hex & string to hex)
# hex(x)
# '0x'+x.encode("utf-8").hex()
# obtaining the unix epoch time reference 
# int(time.time())

class Block: 
    def __init__(self, university_id, email, name, timestamp, previousHash, nonce=0):
        self.university_id = university_id
        self.email = email
        self.name = name
        self.timestamp=timestamp
        self.previousHash = previousHash
        self.nonce = nonce

    # def update_nonce (self,number): 
    #     self.nonce+=number
    #     return self.nonce

    def block_to_hex(self): 
        block={
            'previous-hash': '0x'+self.previousHash, 
            'nonce' : hex(self.nonce),
            'timestamp': hex(self.timestamp),
            'aub-id': hex(self.university_id),
            'email': '0x'+self.email.encode("utf-8").hex(),
            'full-name': '0x'+self.name.encode("utf-8").hex()
        }
        
        return block
        
    def compute_hash(self,block): 
        block_string = json.dumps(block, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
    
    def mine(self,difficulty):
        computedHash = self.compute_hash(self.block_to_hex())
        while int(computedHash,16)>2**(256-difficulty)-1 and self.nonce<= 2**32-1:
            self.nonce += 1
            #
            print("Updated Nonce")
            computedHash = self.compute_hash(self.block_to_hex())
            #
            print(self.nonce)
            #
            print(computedHash)
        return computedHash, hex(self.nonce)
    #another way but check left most zeros when we want them in hexadecimal instead of binary
    '''
    def mine(self,difficulty):
        computedHash = self.compute_hash(self.block_to_hex())
        while not computedHash.startswith('0' * difficulty) and self.nonce<= 2**32-1:
            self.nonce += 1
            #
            print("Updated Nonce")
            computedHash = self.compute_hash(self.block_to_hex())
            #
            print(self.nonce)
            #
            print(computedHash)
        return computedHash, hex(self.nonce)
      '''  

#Use a previous block hash value from the actual Bitcoin blockchain at https://www.blockchain.com/btc/block/{block number}
curr_time = int(time.time())
myBlock = Block(201906074, 'example@hotmail.com', "My Name", curr_time,'0000000000000000000b65037a3b16309a0f60f648f4a6fae22b397dad047a15')
from timeit import default_timer as timer
start = timer()
print(myBlock.mine(4))
end = timer()
print(end - start) 
#to know the timstamp chosen  
print(hex(curr_time))
