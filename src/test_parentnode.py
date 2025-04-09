import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode("div", None)
            parent_node.to_html()
            self.assertEqual(str(context.exception), "Children cannot be empty or None")

        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode("div", [])
            parent_node.to_html()
            self.assertEqual(str(context.exception), "Children cannot be empty or None")

    def test_parent_node_without_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("span", "child")]).to_html()
        
        self.assertEqual(str(context.exception), "Tag is missing in ParentNode")


    
if __name__ == "__main__":
    unittest.main()