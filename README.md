# Moralis Performance Testing

This project demonstrates the use of Moralis Python SDK for performance testing using Locust.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Moralis_Performance_Testing.git
   cd Moralis_Performance_Testing
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

Create a .env file and add your Moralis API key and wallet address.

5. **Run Locust**

Start Locust server and open the web interface to start tests:

```bash
locust -f locust/locustfile.py
```
