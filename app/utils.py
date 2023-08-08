from datetime import datetime

import requests

from config import Config


def fetch_nft_transaction_data(contract_address):
    url = f'https://api.etherscan.io/api'
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': contract_address,
        'sort': 'asc',
        'apikey': Config.ETHERSCAN_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data['result'] if data['status'] == '1' else []


def convert_gas_to_usd(gas_fee, timestamp, eth_price_data):
    closest_price = None
    min_timestamp_difference = float('inf')

    for price_entry in eth_price_data:
        price_timestamp, price_value = price_entry
        timestamp_difference = abs(price_timestamp - timestamp)

        if timestamp_difference < min_timestamp_difference:
            closest_price = price_entry
            min_timestamp_difference = timestamp_difference

    if closest_price:
        eth_to_usd_price = closest_price[1]
        gwei_to_eth = 1 / 10 ** 9
        gas_fee_eth = gas_fee * gwei_to_eth
        gas_fee_usd = gas_fee_eth * eth_to_usd_price
        return gas_fee_usd

    return None  # No suitable historical price found


def calculate_avg_gas_fee_in_usd(transactions, eth_price_data):
    gas_fee_by_hour = {hour: [] for hour in range(24)}

    for transaction in transactions:
        timestamp = int(transaction['timeStamp'])
        gas_price = int(transaction['gasPrice']) / 10 ** 9
        hour = datetime.utcfromtimestamp(timestamp).hour
        gas_fee_by_hour[hour].append(gas_price)

    average_gas_fees = {
        hour: sum(gas_fee_by_hour[hour]) / len(gas_fee_by_hour[hour])
        if gas_fee_by_hour[hour]
        else 0
        for hour in gas_fee_by_hour
    }

    avg_gas_fees_usd = {
        hour: convert_gas_to_usd(gas_fee, timestamp, eth_price_data)
        for hour, gas_fee in average_gas_fees.items()
    }

    return avg_gas_fees_usd


def fetch_eth_price_data(days_back):
    # today = datetime.now()
    # from_date = today - timedelta(days=days_back)

    params = {
        'vs_currency': 'usd',
        'days': days_back
    }

    response = requests.get(Config.COINGECKO_URL, params=params)
    data = response.json()
    return data['prices']
