
import unittest
from converter import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestConverter(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("Plain text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Plain text")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Link text", TextType.LINK, url="https://www.example.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="https://www.example.com">Link text</a>')

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("", TextType.IMAGE, url="https://www.example.com/image.jpg", alt="Example Image")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com/image.jpg" alt="Example Image" />')

    def test_text_node_to_html_node_invalid_type(self):
        text_node = TextNode("Invalid text", "INVALID_TYPE")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_text_node_to_html_node_link_no_url(self):
        text_node = TextNode("Link text", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_text_node_to_html_node_image_no_url(self):
        text_node = TextNode("", TextType.IMAGE, alt="Example Image")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_text_node_to_html_node_image_no_alt(self):
        text_node = TextNode("", TextType.IMAGE, url="https://www.example.com/image.jpg")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()