import pytest
from web3 import Web3

from engine.evm import btoken, dtfactory

from web3tools import web3util, account, wallet

@pytest.fixture
def dtfactory_address():
    return _dtfactory_address()

@pytest.fixture
def bfactory_address():
    return _bfactory_address()

@pytest.fixture
def OCEAN_address():
    return _OCEAN_address()

@pytest.fixture
def alice_private_key():
    return alice_info().private_key

@pytest.fixture
def alice_address():
    return alice_info().address

@pytest.fixture
def alice_wallet():
    return alice_info().wallet

@pytest.fixture
def alice_account():
    return alice_info().account

# @pytest.fixture
# def alice_ocean():
#     return alice_info().ocean

@pytest.fixture
def bob_private_key():
    return bob_info().private_key

@pytest.fixture
def bob_address():
    return bob_info().address

@pytest.fixture
def bob_wallet():
    return bob_info().wallet

@pytest.fixture
def bob_account():
    return bob_info().account

# @pytest.fixture
# def bob_ocean():
#     return bob_info().ocean

# @pytest.fixture
# def T1():  #'TOK1' with 1000.0 held by Alice
#     return alice_info().T1

# @pytest.fixture
# def T2():  #'TOK2' with 1000.0 held by Alice
#     return alice_info().T2

def alice_info():
    return make_info('Alice', 'TEST_PRIVATE_KEY1')

def bob_info():
    return make_info('Bob', 'TEST_PRIVATE_KEY2')

def make_info(name, private_key_name):
    # assume that this account has ETH with gas.
    class _Info:
        pass
    info = _Info()
    network =  web3util.get_network()
    _web3 = web3util.get_web3()
    info.private_key = web3util.confFileValue(network, private_key_name)
    info.address = account.privateKeyToAddress(info.private_key)
    info.account = account.Account(private_key=info.private_key)
    info.wallet = wallet.Wallet(web3=_web3, private_key=info.private_key)
    # config = {'network': _NETWORK,
    #           'privateKey': info.private_key,
    #           'dtfactory.address': _dtfactory_address(),
    #           'bfactory.address': _sfactory_address(),
    #           'OCEAN.address': _OCEAN_address(),
    # }
    # info.ocean = Ocean(config)
    # info.T1 = _deployAndMintToken('TOK1', info.address)
    # info.T2 = _deployAndMintToken('TOK2', info.address)    

    return info

# def _deployAndMintToken(symbol: str, to_address: str) -> btoken.BToken:
#     private_key = web3util.confFileValue(network, 'FACTORY_DEPLOYER_PRIVATE_KEY')
#     from_wallet = wallet.Wallet(private_key=private_key)
#     token_address = dtfactory.DTFactory().createToken(blob='foo', from_wallet=alice_wallet)
#     token = BToken(token_address)
#     token.mint(to_address, util.toBase18(1000.0), from_wallet=from_wallet)
    
#     return token

def _dtfactory_address():
    return web3util.contractAddress('DTFactory')

def _bfactory_address():
    return web3util.contractAddress('BFactory')

def _OCEAN_address():
    return web3util.contractAddress('Ocean')
