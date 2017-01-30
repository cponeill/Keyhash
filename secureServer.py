#! /usr/bin/env python3

import requests
import json
import os

from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

import fetch_data as get_data


# Configuring app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)


# Adding 402 decorator and charge 1500 satoshi per request
@app.route('/get')
@payment.required(1500)
def password():
    """
    Input: A file or string.
    Output: A sha256 hash of the file or string and a hash of th sha256 hash.
    params = {'keyhash':{'sha256_hash':___, 'blockchain_hash':___,}}
    """
    password = request.args.get('hash')
    get_pwd = get_data.FetchData().generate_password()
    password = get_data.FetchData().hash_password(get_pwd)
    hash = get_data.FetchData().generate_hash(password)
    params = {
        'keyhash': {
            'sha256_hash': password,
            'blockchain-hash': hash,
        }
    }
    return json.dumps(params, indent=2)


if __name__ == '__main__':
    app.run('::', port=9787)
