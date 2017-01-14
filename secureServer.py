"""
Copyright (c) 2016-2017 Blockshare Technologies, LLC.
  ____  _            _     ____  _                      ___ ___  
 | __ )| | ___   ___| | __/ ___|| |__   __ _ _ __ ___  |_ _/ _ \ 
 |  _ \| |/ _ \ / __| |/ /\___ \| '_ \ / _` | '__/ _ \  | | | | |
 | |_) | | (_) | (__|   <  ___) | | | | (_| | | |  __/_ | | |_| |
 |____/|_|\___/ \___|_|\_\|____/|_| |_|\__,_|_|  \___(_)___\___/ 
"""

__author__ = "cponeill"
__version__ = "0.01"
__maintainer__ = "cponeill"
__email__ = "cponeill@blockshare.io"

#!/usr/bin/env python3

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

    password = request.args.get('password')
    get_pwd = get_data.FetchData().generate_password	()
    password = get_data.FetchData().hash_password(get_pwd)
    hash = get_data.FetchData().generate_hash(password)
    params = {
        'keyhash': {
            'random-hash': password,
            'blockchain-hash': hash,
        }
    }
    return json.dumps(params, indent=2)


if __name__ == '__main__':
    app.run('::', port=9787)
