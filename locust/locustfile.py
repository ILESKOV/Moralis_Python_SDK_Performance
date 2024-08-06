from locust import HttpUser, task, between
from moralis import evm_api
import os
from dotenv import load_dotenv

load_dotenv()

MORALIS_API_KEY = os.getenv('MORALIS_API_KEY')
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')

class MoralisUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_native_balance(self):
        params = {
            "address": WALLET_ADDRESS,
            "chain": "eth"
        }
        try:
            with self.client.get(
                url="/api/v2/{address}/balance".format(address=WALLET_ADDRESS),
                params=params,
                headers={"X-API-Key": MORALIS_API_KEY},
                catch_response=True
            ) as response:
                sdk_result = evm_api.balance.get_native_balance(
                    api_key=MORALIS_API_KEY,
                    params=params
                )
                if 'balance' in sdk_result:
                    print("Balance result:", sdk_result)
                    response.success()
                else:
                    response.failure("Failed to retrieve balance")
        except Exception as e:
            print(f"Error retrieving balance: {str(e)}")
