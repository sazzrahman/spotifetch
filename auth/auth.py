import base64
import requests
from dotenv import load_dotenv
import unittest
import os


class Auth:
    def __init__(self, client_id=None, client_secret=None) -> None:

        # credentials are not provided then fetch it from env
        if not client_id or not client_secret:
            load_dotenv()
            client_id = os.getenv("CLIENT_ID")
            client_secret = os.getenv("CLIENT_SECRET")
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token(self):
        TOKEN_URL = 'https://accounts.spotify.com/api/token'
        auth_header = base64.urlsafe_b64encode(
            (self.client_id + ':' + self.client_secret).encode())
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic %s' % auth_header.decode()
        }
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        access_token_request = requests.post(url=TOKEN_URL, data=payload, headers=headers)

        return access_token_request.json()



class TestAuth(unittest.TestCase):
    def test_credentials(self):
        auth = Auth()
        self.assertTrue(auth.client_secret)

    def test_token(self):
        auth = Auth()
        self.assertTrue(auth.get_token().get("access_token"))


if __name__ == "__main__":
    unittest.main()
