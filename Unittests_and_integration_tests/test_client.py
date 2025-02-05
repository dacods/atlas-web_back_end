#!/usr/bin/env python3
"""

"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
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

        def test_public_repos_url(self):
            """
            
            """
            mock_payload = {"repos_url": "https://website.url"}

            with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock
            ) as mock_org:
                mock_org.return_value = mock_payload
                client = GithubOrgClient("org")
                result = client._public_repos_url
                self.assertEqual(result, mock_payload["repos_url"])
                mock_org.assert_called_once()
