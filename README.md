# NFT Gas Calculator

The NFT Gas Calculator is a web application built using Flask that helps crypto traders analyze the best time of day to buy NFTs with minimum gas fees. The application fetches transaction data from specific NFT contracts, calculates average gas fees per hour, and presents the data in an interactive chart.

## Features

- User authentication for secure access to the application.
- Fetches transaction data from NFT contracts to calculate average gas fees.
- Converts gas fees from ETH to USD using historical price data.
- Presents gas fee data in an interactive chart.
- Supports multiple NFT contracts and user preferences.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/nft-gas-calculator.git

2. Navigate to the project directory:

```bash
cd nft-gas-calculator
```
3. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt 
```
#Configuration
Create an .env file like the example below:
```bash
SYSTEM_USERNAME=
SYSTEM_PASSWORD=
CRYPTOPUNKS_ADDRESS=0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB
MUTANTAPE_ADDRESS=0x60e4d786628fea6478f785a6d7e704777c86a7c6
COINGECKO_URL='https://api.coingecko.com/api/v3/coins/ethereum/market_chart'
ETHERSCAN_URL=https://docs.etherscan.io/
ETHERSCAN_KEY=
ES_USERNAME=
ES_PASSWORD=
ES_CLOUD_ID=
```
#Usage
Run the Flask development server:
```bash
flask run
```

## API Endpoints

### Authentication Routes

#### Login
- Route: `/login`
- Methods: `GET`, `POST`
- Description: Handles user login. Validates credentials and redirects to the dashboard upon successful login.
- Request Body (POST):
  - `username`: User's username
  - `password`: User's password

#### Logout
- Route: `/logout`
- Method: `GET`
- Description: Logs out the authenticated user and redirects to the login page.

### Main Routes

#### Index
- Route: `/`
- Method: `GET`
- Description: Displays the index page with basic information.

#### Dashboard
- Route: `/dashboard`
- Method: `GET`
- Description: Displays the user's dashboard, which includes the NFT gas fee chart.
- Authentication Required: Yes

#### Average Gas Fees
- Route: `/average_gas_fees`
- Method: `GET`
- Description: Retrieves and returns the average gas fees data for specific NFT contracts.
- Authentication Required: Yes

### Data Processing and Visualization

The application fetches transaction data for specified NFT contracts, calculates average gas fees, and presents the data in an interactive chart.

The following processes are involved:

1. User logs in and accesses the dashboard.
2. The `GET /average_gas_fees` endpoint fetches NFT transaction data and calculates average gas fees for specific contracts.
3. The data is processed and stored in Elasticsearch using the `es.index` method.
4. The dashboard page renders an interactive chart using Highcharts to visualize the average gas fees per hour for each NFT contract.

This project was developed by [Nitay Caspi](https://github.com/nitay12).