from flask import Blueprint, render_template, jsonify
from flask_login import login_required

from app.utils import fetch_nft_transaction_data, calculate_avg_gas_fee_in_usd, fetch_eth_price_data
from config import Config, ElasticsearchConfig

main_bp = Blueprint('main', __name__)
es_client = ElasticsearchConfig()


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@main_bp.route('/average_gas_fees')
@login_required
def get_average_gas_fees():
    # TODO: Create an Addresses list for each user
    addresses = [Config.MUTANTAPE_ADDRESS, Config.CRYPTOPUNKS_ADDRESS]
    avg_gas_fees_data = {}

    for address in addresses:
        transactions = fetch_nft_transaction_data(address)
        eth_price_data = fetch_eth_price_data(90)
        avg_gas_fees_usd = calculate_avg_gas_fee_in_usd(transactions, eth_price_data)
        avg_gas_fees_data[address] = avg_gas_fees_usd
        es_client.es.index(index='gas_fees', body={'address': address, 'data': avg_gas_fees_usd})

    return jsonify(avg_gas_fees_data)
