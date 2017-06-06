import requests
from decimal import Decimal


class PaylikeApiClient:
    api_key = None
    merchant_id = None
    api_base_url = "https://api.paylike.io"

    def __init__(self, api_key="", merchant_id=""):
        self.api_key = api_key
        self.merchant_id = merchant_id

    def cancel_transaction(self, transaction_id, amount):
        return self._call_api('/transaction/%s/voids' % transaction_id,
                              method='POST',
                              data={
                                  "amount": self.convert_to_paylike_amount(amount),
                              })

    def capture_transaction(self, transaction_id, amount, descriptor='', currency=None):
        data = {
            "amount": self.convert_to_paylike_amount(amount),
            "descriptor": descriptor
        }
        if currency is not None:
            data["currency"] = currency

        return self._call_api('/transaction/%s/captures' % transaction_id,
                              method='POST',
                              data=data)

    def create_payment_from_transaction(self, transaction_id, currency, amount, descriptior=''):
        return self._call_api('/merchants/%s/transactions/', method='POST', data={
            "transactionId": transaction_id,
            "descriptor": descriptior,
            "currency": currency,
            "amount": self.convert_to_paylike_amount(amount)
        })

    def create_payment_from_saved_card(self, card_id, currency, amount, descriptor=''):
        return self._call_api('/merchants/%s/transactions/', method='POST', data={
            "cardId": card_id,
            "descriptor": descriptor,
            "currency": currency,
            "amount": self.convert_to_paylike_amount(amount)
        })

    def get_transaction(self, transaction_id):
        return self._call_api('/transactions/%s' % transaction_id)["transaction"]

    def get_transactions(self, limit=100):
        return self._call_api('/merchants/%s/transactions/?limit=%i' % (self.merchant_id, limit))

    def refund_transaction(self, transaction_id, amount, descriptor=""):
        return self._call_api('/transactions/%s/refunds' % transaction_id,
                              method='POST',
                              data={
                                  "amount": self.convert_to_paylike_amount(amount),
                                  "descriptor": descriptor
                              })

    def _call_api(self, uri, method='GET', data={}, headers={}):

        url = "%s%s" % (self.api_base_url, uri)
        auth = ("",self.api_key) if self.api_key is not None else None

        r = requests.request(method, url, json=data, headers=headers, params=data, auth=auth)
        if r.status_code == 200:
            return r.json()
        else:
            return None


    def convert_to_paylike_amount(self, amount):
        assert isinstance(amount, Decimal)
        return int(round(amount * 100))