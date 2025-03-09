import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_non_empty(self):

        props = {"href": "https://example.com", "target": "_blank"}
        node = HTMLNode(props=props)
        result = node.props_to_html()
        expected = ' href="https://example.com" target="_blank"'

        self.assertEqual(result, expected)

    def test_props_to_html_empty(self):

        node = HTMLNode(props={})
        result = node.props_to_html()
        expected = ""

        self.assertEqual(result, expected)

    def test_props_to_html_none(self):

        node = HTMLNode()
        with self.assertRaises(AttributeError):
            node.props_to_html()

