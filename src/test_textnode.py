import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        """Test inequality when the 'text' property is different."""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different Text", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_not_eq_differnt_url(self):
        """Test inequality when the 'url' property is different."""
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://example2.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_text_type(self):
        """Test inequality when the text type is differnt"""
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_with_none_url(self):
        """test equality when both objects have none as the url"""
        node = TextNode("This is a text Node", TextType.BOLD)
        node2 = TextNode("This is a text Node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_one_has_url(self):
        """Test inequality when one object has a URL and the other does not"""
        node = TextNode("This is a text Node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text Node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()