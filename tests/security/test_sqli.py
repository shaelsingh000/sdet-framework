from core.security_client import SecurityClient

def test_sqli(load_config):
    client = SecurityClient(load_config.get("api_base_url"))
    client.check_sql_injection("/login")
