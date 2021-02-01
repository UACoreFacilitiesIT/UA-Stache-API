import os
from unittest import TestCase
from ua_stache_api import ua_stache_api


class TestUAStacheApi(TestCase):
    def setUp(self):
        self.get_key = {
            "X-STACHE-KEY": "ef418df86cfe8a0b214c4138f99e4532126fdb67f8470cfad1f6823a849e6763"}
        self.post_key = {"X-STACHE-KEY": "27d776c2a9046a37733f19837ba90137e4be764f2e04680987765a569ec70e56"}
        self.get_url = "https://stache.arizona.edu/api/v2/entry/fcea4e830511f64312d8fcb8a18b31e9/data/read"
        self.post_url = "https://stache.arizona.edu/api/v2/entry/fcea4e830511f64312d8fcb8a18b31e9/data/edit"
        self.base_content = {
            "Nested": {
                "Test": "Passed"
            },
            "Un-Nested": ["Silly", "Rabbit", "Tricks", "Are", "4", "Kids"]
        }
        self.updated_content = {
            "Nested": {
                "Test": "Passed"
            },
            "Un-Nested": ["Silly", "Rabbit", "Tricks", "Are", "4", "Adults"]
        }
        self.base_all_content = {
            'nickname': 'Test Stache API', 
            'purpose': '', 
            'secret': {
                'Nested': {'Test': 'Passed'}, 
                'Un-Nested': ['Silly', 'Rabbit', 'Tricks', 'Are', '4', 'Kids']
            }, 
            'memo': ''
        }
        self.updated_all_content = {
            'nickname': 'Test Stache API', 
            'purpose': '', 
            'secret': {
                'Nested': {'Test': 'Passed'}, 
                'Un-Nested': ['Silly', 'Rabbit', 'Tricks', 'Are', '4', 'Adults']
            }, 
            'memo': ''
        }

    def test_get_entry(self):
        template_path = (os.path.join(
            os.path.split(__file__)[0], "test_get.json"))
        with open(template_path, 'r') as file:
            contents = file.read()
        key, url = ua_stache_api.get_entry(contents)
        assert key == self.get_key
        assert url == self.get_url

        template_path = (os.path.join(
            os.path.split(__file__)[0], "test_post.json"))
        with open(template_path, 'r') as file:
            contents = file.read()
        key, url = ua_stache_api.get_entry(contents)
        assert key == self.post_key
        assert url == self.post_url

    def test_unnested_get(self):
        data = ua_stache_api.auth(self.get_key, self.get_url)
        assert data["Nested"]["Test"] == "Passed"

    def test_nested_get(self):
        cred_type_test = ua_stache_api.auth(
            self.get_key, self.get_url, cred_type="Nested/Test")
        assert cred_type_test == "Passed"

    def test_get_all(self):
        data = ua_stache_api.auth(self.get_key, self.get_url, get_all=True)
        assert data == self.base_all_content
    
    def test_post(self):
        ua_stache_api.post(self.post_key, self.post_url, self.updated_all_content)
        current_data = ua_stache_api.auth(self.get_key, self.get_url, get_all=True)
        assert current_data == self.updated_all_content

        ua_stache_api.post(self.post_key, self.post_url, self.base_all_content)
        current_data = ua_stache_api.auth(self.get_key, self.get_url, get_all=True)
        assert current_data == self.base_all_content

