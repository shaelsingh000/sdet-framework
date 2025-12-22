import requests
from utils.logger import get_logger

class APIClient:
    def __init__(self,base_url,timeout=30):
        self.base_url = base_url
        self.timeout = timeout
        self.logger = get_logger()

    def get(self,endpoint,headers=None):
        url = f"{self.baseurl}{endpoint}"
        self.logger.info(f"GET {url}")
        response = requests.get(url,headers=headers,timeout=self.timeout)
        return response
    