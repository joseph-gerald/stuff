from flask import Flask, request, jsonify
from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider
import config

app = Flask(__name__)
client = Tron(HTTPProvider(api_key=config.API_KEY))
priv_key = PrivateKey(bytes.fromhex(config.PRIVATE_KEY))

@app.route('/transfer', methods=['GET'])
def transfer():
    try:
        to = request.args.get('to')
        amount = float(request.args.get('amount'))
        password = request.args.get('password')
    except ValueError:
        return jsonify({'error': 'invalid amount'}), 400

    if not to or not amount or not password:
        return jsonify({'error': 'missing parameters'}), 400
    
    if password != config.PASSWORD:
        return jsonify({'error': 'invalid password'}), 401

    print(f"Transferring {amount} TRX to {to}")
    
    txn = (
        client.trx.transfer(config.PUBLIC_KEY, to, int(amount * 1_000_000))
        .build()
        .inspect()
        .sign(priv_key)
        .broadcast()
    )
    
    return jsonify(txn.wait())

@app.route('/balance', methods=['GET'])
def balance():
    balance = client.get_account_balance(config.PUBLIC_KEY)
    return jsonify({'balance': balance})

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT)

