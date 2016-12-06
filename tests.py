#!/usr/bin/env python3
import os
import unittest
import secureServer
import json

from unittest import mock

class KeyhashTestCase(unittest.TestCase):

    def get(self, url):
        self.app = secureServer.app.test_client()
        return self.app.get(url)

    def test_success(self):
        response = self.get('/get')
        self.assertEqual(response.status_code, 402)

    @mock.patch('two1.bitserv.flask.decorator.Payment.contains_payment',
                return_value=True)
    def test_buy_success(self, *args):
        response = self.get('/get')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
