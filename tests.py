#!/usr/bin/env python3
# Adding in unittests in Keyhash microservice.
import os
import unittest
import secureServer
import json

from unittest import mock

class KeyhashTestCase(unittest.TestCase):

    # Getting app to test url.
    def get(self, url):
        self.app = secureServer.app.test_client()
        return self.app.get(url)

    # Testing whethere 402 endpoint is called by the client.
    def test_success(self):
        response = self.get('/get')
        self.assertEqual(response.status_code, 402)

    # Testing whether 200 endpoint is returned after payment received.
    @mock.patch('two1.bitserv.flask.decorator.Payment.contains_payment',
                return_value=True)
    def test_buy_success(self, *args):
        response = self.get('/get?hash="keyhash"')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
