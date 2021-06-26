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

## Simple Smart Contract
The Solidarity Code [simpleSmartContract.sol](https://github.com/maarouf-yassine/Blockchain-and-Cryptocurrencies/blob/main/simpleSmartContract.sol) is a simple smart contract using the Solidity programming language and the [Remix Ethereum IDE](http://remix.ethereum.org/).

The smart contract should store the grades of students in a class. Student information consists of a name, an ID number, and an email address. Assume that there are up to 25 students, and that each student has grades for four assignments and a final exam.Each assignment or exam grade is an integer between 0 and 100.

The smart contract should store all the above information, and should calculate the following weighted sum and the course letter grade:

weighted sum = 0.15×(sum of assignment grades) + 0.4×(final exam grade)

The course letter grade is assigned to each student in accordance with the following table:

| Weighted Sum  | Course Grade  |
| ------------- |:-------------:|
| <60           | F             |
| 60 to 69      | D             |
| 70 to 79      | C             |
| 80 to 89      | B             |
| 90 to 100     | A             |

### Usage
Compile and deploy the smart contract on the Remix Ethereum IDE on the following link: http://remix.ethereum.org

## ERC20 Based Smart Contract
The Solidarity Code [smartContractToken.sol](https://github.com/maarouf-yassine/Blockchain-and-Cryptocurrencies/blob/main/smartContractToken.sol) is based on the ERC20 Template of the OPENZEPPELIN Implementation. The code represents a smart contract that could be deployed on the Ethereum main-net. In this smart contract there is the LEBDON Token. 
Any user with an Ethereum wallet could use this token. Users can transfer LEBDON tokens to NGOs. This transfer is implemented internally by the `transfer` function in the .sol file. Users will be also 
able to transfer tokens on behalf of other users if they were authorized to do so, and this is implemented internally using the `transferFrom` function. 
Every successful transaction or transfer operation is registered on the blockchain, thus allowing full transparency and ability to track the money spent.

### Usage
Compile and deploy the smart contract on the Remix Ethereum IDE on the following link: http://remix.ethereum.org

Follow this [tutorial](https://www.youtube.com/watch?v=GDq7r1n9zIU) to see how you can send and receive tokens from different Metamask accounts.