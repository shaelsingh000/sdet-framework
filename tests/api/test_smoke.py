from core.base_test import BaseTest
from core.api_client import APIClient

class TestSmoke(BaseTest):
    def test_api_client_setup(self,load_config):
        
        client = APIClient(
            base_url=load_config.get("api_base_url"),
            timeout=load_config.get("timeout")
        )
        assert client.base_url is not None

    def test_api_invalid_endpoint(load_config):
        client = APIClient(load_config.get("api_base_url"))
        response = client.get("/invalid-endpoint", expected_status=404)
        assert response.status_code == 404