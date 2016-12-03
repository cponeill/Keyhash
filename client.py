#!/usr/bin/env python3

from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

wallet = Wallet()
requests = BitTransferRequests(wallet)

server_url = 'http://[::]:7987/'

def get_data():

    sel_url = server_url+'get'
    response = requests.get(url=sel_url)
    print(response)

if __name__ == '__main__':
    get_data()
