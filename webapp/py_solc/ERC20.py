from ico.settings import SOLIDITY_DIR
from web3 import Web3, HTTPProvider, IPCProvider
from solc import compile_files
from web3.contract import ConciseContract
from web3.middleware import geth_poa_middleware
import binascii

class IcoToken:

    contract_files_list = SOLIDITY_DIR + '/ICOToken.sol'
    token_compile = compile_files([contract_files_list])
    contract_files = []
    for key in token_compile:
        keys = key
        contract_files.append(keys)


    # Compiled token solidi
    token_interface = token_compile[contract_files[0]]

    # web3.py instance
    # my_provider = Web3.IPCProvider("/home/anupam/.ethereum/geth.ipc")
    my_provider = Web3.HTTPProvider("HTTP://127.0.0.1:7545")

    w3 = Web3(my_provider)
    poa = w3.middleware_stack.inject(geth_poa_middleware, layer=0)
    balance = w3.eth.getBalance(w3.eth.accounts[0])

    # Instantiate and deploy token contract
    token_contract = w3.eth.contract(
    abi=token_interface['abi'], bytecode=token_interface['bin'])

    # Get transaction hash from deployed ERC20 contract
    token_tx_hash = token_contract.constructor(
    94500000000000000000000000).transact({'from': w3.eth.accounts[0]})

    # Get tx receipt to get token contract address
    token_tx_receipt = w3.eth.waitForTransactionReceipt(token_tx_hash,timeout=5000)

    # print(token_contract.functions.transfer(w3.eth.accounts[1],10).call({'from': w3.eth.accounts[0]}))

    # Token contract address of solidity smart contract
    token_contract_address = token_tx_receipt['contractAddress']


    # token instance in concise mode
    token_instance = w3.eth.contract(address=token_contract_address,
                 abi=token_interface['abi'], ContractFactoryClass=ConciseContract)


