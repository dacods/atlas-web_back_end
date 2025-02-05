#!/usr/bin/env python3
"""

"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        
        """
        test_client = GithubOrgClient(org_name)
        mock_get_json.return_value = {"org": org_name}

        result = test_client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"org": org_name})
