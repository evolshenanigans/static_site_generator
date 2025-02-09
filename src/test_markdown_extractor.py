import unittest
from markdown_extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_images_basic(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_extract_images_empty_alt(self):
        text = "![ ](http://example.com)"
        self.assertEqual(extract_markdown_images(text), [(" ", "http://example.com")])

    def test_extract_images_multiple(self):
        text = "![a](b)![c](d)"
        self.assertEqual(extract_markdown_images(text), [("a", "b"), ("c", "d")])

    def test_extract_images_none(self):
        text = "No images here."
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_links_basic(self):
        text = "A [link](https://boot.dev) and [another](https://example.com)"
        self.assertEqual(extract_markdown_links(text), [
            ("link", "https://boot.dev"),
            ("another", "https://example.com")
        ])

    def test_extract_links_with_images(self):
        text = "Link [here](url) and image ![there](img)"
        self.assertEqual(extract_markdown_links(text), [("here", "url")])

    def test_extract_links_empty(self):
        text = "[]()"
        self.assertEqual(extract_markdown_links(text), [("", "")])

    def test_extract_links_none(self):
        text = "No links here."
        self.assertEqual(extract_markdown_links(text), [])

    def test_links_not_images(self):
        text = "![Not a link](image.png) [but this is](link.html)"
        self.assertEqual(extract_markdown_links(text), [("but this is", "link.html")])

if __name__ == "__main__":
    unittest.main()