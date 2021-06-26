# Blockchain-and-Cryptocurrencies
A repository of experiments to understand more about Cryptocurrencies & Blockchain

## Table of Content
- [Project](#blockchain-and-cryptocurrencies)
- [Table of Content](table-of-content)
- [Languages Used](#languages-used)
- [Mine Your Information](#mine-your-information)
- [Bitcoin Testnet](#bitcoin-testnet)
- [Simple Smart Contract](#simple-smart-contract)
- [ERC20 Based Smart Contract](erc20-based-smart-contract)

## Languages Used
* Python
* Solidity

## Mine Your Information
The python script [mineYourInfo.py](https://github.com/maarouf-yassine/Blockchain-and-Cryptocurrencies/blob/main/mineYourInfo.py) simulates “mining” your personal information (full name, email, 
and ID) using SHA-256 and Bitcoin-style Proof-of-Work.

Use a previous block hash value from the actual Bitcoin blockchain at https://www.blockchain.com/btc/block/{block number of your choice}

Difficulty is in terms of leftmost zero bits

### Usage
Create a new instance of `Block` Class and enter the details of your choice.

Call the function `mine(difficulty)` with difficulty representiung the left-most zero bits

## Bitcoin Testnet
The python script [bitcoinTestNet.py](https://github.com/maarouf-yassine/Blockchain-and-Cryptocurrencies/blob/main/bitcoinTestNet.py) uses the Bitcoin testnet to conduct Bitcoin transactions

First create a private key, a public key, and a Bitcoin address on the testnet, using this website: https://www.bitaddress.org/
To generate a testnet address, append `?testnet=true` to the browser URL when you access the website address above. You should see “TESTNET EDITION ACTIVATED”.

Save your Bitcoin address, and (securely) save your private key.

You can receive coins on the testnet from a “faucet” that can send non-monetary coins to your address. Use https://testnet-faucet.mempool.co/ to receive 0.005 coins.

Use https://blockstream.info/testnet to see transactions on the Blockchain

### Usage
Install the Python Bit Library to perform transactions and other things
```
pip install bit
```

More details of  the Python Bit library can be found here: (https://ofek.dev/bit)

