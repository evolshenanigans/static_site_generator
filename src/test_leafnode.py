import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_value(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)
    
    def test_to_html_with_tag_value_and_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_without_tag(self):
        node = LeafNode(value="Raw text")
        expected = "Raw text"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value=None)

    def test_repr(self):
        node = LeafNode(tag="a", value="Click here", props={"href": "https://www.google.com"})
        expected = "HTMLNode(tag=a, value=Click here, children=[], props={'href': 'https://www.google.com'})"
        self.assertEqual(repr(node), expected)
    


if __name__ == "__main__":
    unittest.main()