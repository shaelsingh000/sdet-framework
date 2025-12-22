from core.base_test import BaseTest
from core.api_client import APIClient

class TestSmoke(BaseTest):
    def test_api_client_setup(self,load_config):
        client = APIClient(
            base_url=load_config.get("api_base_url"),
            timeout=load_config.get("timeout")
        )
        assert client.base_url is not None