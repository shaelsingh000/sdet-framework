from core.base_test import BaseTest

class TestSmoke(BaseTest):
    def test_framework_bootstrap(self):
        self.logger.info("Framework Bootstrap Test Running")
        assert True
        