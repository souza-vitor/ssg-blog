import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="test link", props={"href": "www.boot.dev", "target": "_blank"})
        self.assertEqual(' href="www.boot.dev" target="_blank"', node.props_to_html())
    
    def test_eq(self):
        node = HTMLNode(tag="a", value="test link", props={"href": "www.boot.dev", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="test link", props={"href": "www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_not_eq(self):
        node = HTMLNode(tag="a", value="test link", props={"href": "www.boot.dev", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="test link", props={"href": "www.google.com", "target": "_blank"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())
    
    
if __name__ == "__main__":
    unittest.main()