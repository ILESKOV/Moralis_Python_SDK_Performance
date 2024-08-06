from dotenv import load_dotenv
import os
import pytest
from moralis import evm_api

load_dotenv()

MORALIS_API_KEY = os.getenv('MORALIS_API_KEY')
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')

@pytest.fixture
def api_client():
    return evm_api

def test_get_native_balance(api_client):
    params = {
        "address": WALLET_ADDRESS,
        "chain": "eth",
        "to_block": 1.2,
    }

    result = api_client.balance.get_native_balance(
        api_key=MORALIS_API_KEY,
        params=params,
    )
    assert result is not None
    assert isinstance(result, dict) 

def test_invalid_address(api_client):
    params = {
        "address": "invalid_address",
        "chain": "eth",
        "to_block": 1.2,
    }
    with pytest.raises(Exception):
        api_client.balance.get_native_balance(
            api_key=MORALIS_API_KEY,
            params=params
        )
