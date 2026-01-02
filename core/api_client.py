import requests
from utils.logger import get_logger

class APIClient:
    def __init__(self,base_url,timeout=30):
        self.base_url = base_url
        self.timeout = timeout
        self.logger = get_logger()

    def get(self, endpoint, headers=None, expected_status=200):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"GET {url}")
        response = requests.get(url, headers=headers, timeout=self.timeout)
        if response.status_code != expected_status:
            self.logger.warning(f"Expected {expected_status} but got {response.status_code}")
        return response

    def post(self, endpoint, data=None, headers=None, expected_status=200):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"POST {url} with data {data}")
        response = requests.post(url, json=data, headers=headers, timeout=self.timeout)
        if response.status_code != expected_status:
            self.logger.warning(f"Expected {expected_status} but got {response.status_code}")
        return response
