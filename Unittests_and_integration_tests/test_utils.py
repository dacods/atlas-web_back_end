#!/usr/bin/env python3
"""

"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from utils import get_json
from unittest.mock import patch, Mock
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test for access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test for expected result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test KeyError handling
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], expected)


class TestGetJson(unittest.TestCase):
    """
    Test for get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns expected payload
        """
        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test for the memoize decorator
    """
    def test_memoize(self):
        """
        Test that memoize chaches the result after the first call
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        with patch.object(test_instance, 'a_method',
                          return_value=42) as mock_method:
            result1 = test_instance.a_property

            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
