from webapp.py_solc.ERC20 import IcoToken
from webapp.py_solc.crowd_sale import CrowdSale
import binascii

class BuyTokens:
    crowdsale = CrowdSale()

    token = IcoToken()


    crowd_sale_address = crowdsale.crowdsale_contract_address

    token_address = token.token_contract_address
    w3 = token.w3

    #Set crowdsale address

    set_crowdsale_address = token.token_instance.setCrowdsale(crowd_sale_address)
    print(set_crowdsale_address)

    transfer = token.token_instance.transfer(w3.eth.accounts[1], 200000000000000000000, transact = {'from':w3.eth.accounts[0], 'to':token_address, 'gas':500000})
    print(binascii.hexlify(transfer))

    #Transfer token to crowdsale address
    tokens = 8000000000000000000000

    transfer_token = token.token_instance.buyTokens(
    crowd_sale_address, tokens, transact = {'from':w3.eth.accounts[0], 'to':token_address, 'gas':500000})

    print(binascii.hexlify(transfer_token))







