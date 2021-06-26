# Blockchain-and-Cryptocurrencies
A repository of experiments to understand more about Cryptocurrencies & Blockchain

## Table of contents
- [Project](#blockchain-and-cryptocurrencies)
- [Languages Used](#languages-used)
- [Mine Your Information](#mine-your-info)
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
