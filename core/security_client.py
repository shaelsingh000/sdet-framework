from core.api_client import APIClient

class SecurityClient(APIClient):
    def check_sql_injection(self, endpoint):
        payloads = ["' OR 1=1 --", "'; DROP TABLE users; --"]
        for payload in payloads:
            response = self.get(f"{endpoint}?input={payload}", expected_status=400)
            if response.status_code != 400:
                self.logger.warning(f"Potential SQLi detected: {payload}")
