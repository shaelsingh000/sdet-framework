from core.base_test import BaseTest
from core.api_client import APIClient


class TestSmoke(BaseTest):

    def test_api_client_setup(self, load_config):
        """
        Validate API client initializes correctly using config values
        """
        client = APIClient(
            base_url=load_config.get("api_base_url"),
            timeout=load_config.get("timeout")
        )

        assert client.base_url is not None
        assert client.timeout is not None

    def test_api_invalid_endpoint(self, load_config):
        """
        Validate API handles invalid endpoint gracefully
        """
        client = APIClient(
            base_url=load_config.get("api_base_url"),
            timeout=load_config.get("timeout")
        )

        response = client.get("/invalid-endpoint")

        # Acceptable failure responses for invalid endpoints
        assert response.status_code in [401, 403, 404]
