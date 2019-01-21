from ico.settings import SOLIDITY_DIR
from solc import  compile_files
from web3.contract import ConciseContract
from webapp.py_solc.ERC20 import IcoToken
import time

#Token object
token = IcoToken()

#Web provider object
w3 = token.w3

#Token address
token_address = token.token_contract_address


class CrowdSale:
    contract_files_list = SOLIDITY_DIR + '/Crowdsale.sol'

    token_sell_compile = compile_files([contract_files_list])

    contract_files = []
    for key in token_sell_compile:
        keys = key
        contract_files.append(keys)

    #Compiled crowdsale solidity file
    crowdsale_intrface = token_sell_compile[contract_files[0]]


    # Instantiate and deploy token-sale contract
    token_sale_contract = w3.eth.contract(abi=crowdsale_intrface['abi'], bytecode=crowdsale_intrface['bin'])


    # Get transaction hash from deployed crowd-sale contract
    crowd_sale_tx_hash =  token_sale_contract.constructor(2000,token_address,185000000000000000000).transact({'from': w3.eth.accounts[0]})
    # print(crowd_sale_tx_hash)

    #Get tx receipt to get crowd-sale contract address
    crowdsale_tx_receipt = w3.eth.waitForTransactionReceipt(crowd_sale_tx_hash,timeout=800)

    # Crowd-sale contract address of solidity smart contract
    crowdsale_contract_address = crowdsale_tx_receipt['contractAddress']


    crowdsale_instance = w3.eth.contract(address=crowdsale_contract_address,
                                        abi=crowdsale_intrface['abi'], ContractFactoryClass=ConciseContract)




