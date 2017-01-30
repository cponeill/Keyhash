#!/usr/bin/env python3
# Adding in unittests in Keyhash microservice.
# TO-DO: Add tests for invalid data.
import os
import unittest
import secureServer
import json

from unittest import mock


class KeyhashTestCase(unittest.TestCase):

    def get(self, url):
        # Ensure the app is retrieving a url.
        self.app = secureServer.app.test_client()
        return self.app.get(url)

    def test_success(self):
        # Asserting 'get' is requesting 402 endpoint.
        response = self.get('/get')
        self.assertEqual(response.status_code, 402)

    # Adding patch to 'mock' 402 endpoint purchase using a test case.
    @mock.patch('two1.bitserv.flask.decorator.Payment.contains_payment',
                return_value=True)
    def test_buy_success(self, *args):
        # Ensuring 402 request retrieves 200 status.
        response = self.get('/get?hash="keyhash"')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
