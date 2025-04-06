import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_italic_eq(self):
        node = TextNode("this is a italic text node", TextType.ITALIC)
        node2 = TextNode("this is also a italic text node", TextType.ITALIC)
        self.assertEqual(node.text_type, node2.text_type)

    def test_url_eq(self):
        node = TextNode("this is a italic text node", TextType.ITALIC)
        node2 = TextNode("this is also a italic text node", TextType.ITALIC)
        self.assertEqual(node.url, node2.url)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    
if __name__ == "__main__":
    unittest.main()