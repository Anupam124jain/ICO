from web3 import Web3
from solc import  compile_files
from web3.contract import ConciseContract
from users.common.ERC20 import contract_files_list

pre_sell_compile = compile_files(contract_files_list)

#Compiled crowdsale solidity file
pre_sale_interface = pre_sell_compile['PreSale.sol:PreSale']

# web3.py instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Instantiate and deploy pre-sale contract
pre_sale_contract = w3.eth.contract(abi=pre_sale_interface['abi'], bytecode=pre_sale_interface['bin'])

# Get transaction hash from deployed pre_sale contract
presale_tx_hash =  pre_sale_contract.constructor(1000000).transact({'from': w3.eth.accounts[0]})
# print(presale_tx_hash)

# Get tx receipt to get token contract address
presale_tx_receipt = w3.eth.getTransactionReceipt(presale_tx_hash)

# Token contract address of solidity smart contract
pre_sale_contract_address = presale_tx_receipt['contractAddress']

pre_sale_abi = pre_sale_interface['abi']
crowdsale_instance = w3.eth.contract(address=pre_sale_contract_address,
                                     abi=pre_sale_abi,
                                     ContractFactoryClass=ConciseContract)