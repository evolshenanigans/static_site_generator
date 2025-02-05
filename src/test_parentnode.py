import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_tag_and_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_tag_children_and_props(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
            props={"class": "container"}
        )
        expected = '<div class="container"><b>Bold text</b>Normal text</div>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_without_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")])

    def test_to_html_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_to_html_nested_parentnodes(self):
        inner_node = ParentNode(
            "span",
            [
                LeafNode("b", "Inner Bold text"),
                LeafNode(None, "Inner Normal text"),
            ]
        )
        outer_node = ParentNode(
            "div",
            [
                inner_node,
                LeafNode("i", "Outer italic text"),
            ],
            props={"id": "outer"}
        )
        expected = '<div id="outer"><span><b>Inner Bold text</b>Inner Normal text</span><i>Outer italic text</i></div>'
        self.assertEqual(outer_node.to_html(), expected)

    def test_repr(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
            props={"class": "container"}
        )
        expected = "HTMLNode(tag=div, value=None, children=[HTMLNode(tag=b, value=Bold text, children=[], props={}), HTMLNode(tag=None, value=Normal text, children=[], props={})], props={'class': 'container'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()