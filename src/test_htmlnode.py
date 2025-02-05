import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
    
    def test_repr(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com"})
        expected = "HTMLNode(tag=a, value=Click here, children=None, props={'href': 'https://www.google.com'})"
        self.assertEqual(repr(node), expected)

    def test_optional_properties(self):
        node = HTMLNode(value="Raw text")
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)
        self.assertEqual(node.value, "Raw text")

if __name__ == "__main__":
    unittest.main()