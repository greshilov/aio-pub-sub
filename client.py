import secrets
import string
import requests


def generate_token():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(8))


class AioPubSubClient:
    def __init__(self, host, token):
        self.host = host
        self.token = token

    def send_data(self, binary_blob):
        requests.post('{}/client/{}'.format(self.host, self.token), data=binary_blob)

