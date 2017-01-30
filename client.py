#! /usr/bin/env python3
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests


wallet = Wallet()
requests = BitTransferRequests(wallet)
server_url = 'http://[::]:9787/'


def get_data():
    """
    Getting data from server and outputing JSON.
    """
    password = input()
    sel_url = server_url+'get?password={0}'
    response = requests.get(url=sel_url.format(password))
    print(response)


if __name__ == '__main__':
    get_data()
