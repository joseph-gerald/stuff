from flask import Flask, request, jsonify
from flask_cors import CORS

from tronpy import Tron
from tronpy.providers import HTTPProvider
import config

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

client = Tron(HTTPProvider(api_key=config.API_KEY))

for wallet in config.WALLETS:
    print(wallet)
@app.route('/transfer', methods=['GET'])
def transfer():
    try:
        to = request.args.get('to')
        amount = float(request.args.get('amount'))
        address = request.args.get('wallet')
        password = request.args.get('password')
    except:
        return jsonify({'error': 'error'}), 400

    if not to or not amount or not password or not address:
        return jsonify({'error': 'missing parameters'}), 400
    
    pub_key = None
    priv_key = None

    for wallet in config.WALLETS:
        if wallet['public_key'] == address:
            if wallet['password'] != password:
                return jsonify({'error': 'invalid password'}), 400

            pub_key = wallet['public_key']
            priv_key = wallet['private_key']
            break

    if not priv_key:
        return jsonify({'error': 'invalid address'}), 400

    print(f"Transferring {amount} TRX to {to}")
    
    txn = (
        client.trx.transfer(pub_key, to, int(amount * 1_000_000))
        .build()
        .inspect()
        .sign(priv_key)
        .broadcast()
    )
    
    return jsonify(txn.wait())

@app.route('/balance', methods=['GET'])
def balance():
    try :
        address = request.args.get('wallet')
    except:
        return jsonify({'error': 'error'}), 400

    if not address:
        return jsonify({'error': 'missing parameters'}), 400

    balance = client.get_account_balance(address)
    return jsonify({'balance': balance})

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT)

