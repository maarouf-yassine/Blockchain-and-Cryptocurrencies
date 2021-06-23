# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:26:34 2021

@author: maarouf
"""

#First create a private key, a public key, and a Bitcoin address on the testnet, using this website: https://www.bitaddress.org/
#To generate a testnet address, append ?testnet=true to the browser URL when you access the website address above. You should see “TESTNET EDITION ACTIVATED”
#Use https://testnet-faucet.mempool.co/ to receive 0.005 coins
#Use https://blockstream.info/testnet to see transactions

from bit import PrivateKeyTestnet

key = PrivateKeyTestnet('ENTER PRIVATE KEY HERE')

# Your Bitcoin address on testnet, given your private key
print(key.address)

#Your balance in bitcoin (btc)
print(key.get_balance('btc'))

#Create a transaction and send 1 mBTC to the specific address
print("\nTransaction ID for this new transaction")
print(key.send(outputs=[('ADDRESS TO SEND TO', 1, 'mbtc')]))

#print(key.get_transactions())

# print("EXTRA: Printing balance after sending transaction...")
# print(key.get_balance('mbtc'))
