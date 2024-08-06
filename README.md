# Moralis Python SDK Performance Testing

This repository contains performance tests for the Moralis Python SDK using Locust. The focus of the tests is on the `get_native_balance` function to evaluate its performance and ensure reliability under load conditions.

## Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your machine.
- **Locust**: A load testing tool used to simulate user requests.
- **Moralis Python SDK**: Used to interact with the Moralis API.
- **Moralis API Key**: Required to authenticate requests.

## Setup Instructions

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/ILESKOV/Moralis_Python_SDK_Performance.git
   cd Moralis_Python_SDK_Performance
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a .env file in the root directory and add your Moralis API key and wallet address:

   ```bash
   MORALIS_API_KEY=your_moralis_api_key
   WALLET_ADDRESS=your_wallet_address
   ```

5. **Run Locust**

   Start Locust server and open the web interface to start tests:

```bash
locust -f locust/locustfile.py
```

Open your web browser and navigate to http://localhost:8089 to access the Locust web interface.

Enter the number of simulated users and the spawn rate, then start the test to generate load on the get_native_balance function.

As a host use 'https://deep-index.moralis.io'

**_Test Results_**

- Response Times: Measures the average, median, and percentile response times for the API calls.
- Throughput: Calculates the number of requests handled per second.
- Success Rate: Shows the percentage of successful requests.
  Due to API rate limits, continuous testing may be restricted. Adjust the number of users or test frequency as needed.

**_Notes_**

- Ensure your API key is valid and has the necessary permissions to access the Moralis API.
- Consider adjusting the wait_time in the Locust script to simulate different user behavior patterns.
