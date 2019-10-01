from unittest import TestCase
from ua_stache_api import ua_stache_api


class TestUAStacheApi(TestCase):
    def setUp(self):
        api_code = (
            "207a930c586487bc5d05551852ecd2a16f99111f5a3af8404e6a522a453d4ad5"
        )
        self.api_key = {"X-STACHE-READ-KEY": api_code}
        self.url = (
            "https://stache.arizona.edu/"
            "api/v1/item/read/fa4004d4dd816e72fbed07ca330ecfc7")

    def test_get_entry(self):
        key, url = ua_stache_api.get_entry("test_stache_token.json")
        assert key == self.api_key
        assert url == self.url

    def test_auth_with_and_without_cred_type(self):
        data = ua_stache_api.auth(self.api_key, self.url)
        assert data["Nested"]["Test"] == "Passed"

        cred_type_test = ua_stache_api.auth(
            self.api_key, self.url, "Nested/Test")
        assert cred_type_test == "Passed"
