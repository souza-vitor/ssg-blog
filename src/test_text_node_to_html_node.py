import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode, text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node_dict = {"href": "www.wawa.com"}
        node = TextNode("This is a text node", TextType.LINK, node_dict)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")   
        self.assertEqual(html_node.props, {"href": "www.wawa.com"})
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node_dict = {"src": "www.wawa.com", "alt": "wawa website"}
        node = TextNode("", TextType.IMAGE, node_dict)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.wawa.com", "alt": "wawa website"})
        

    
if __name__ == "__main__":
    unittest.main()