import unittest

from htmlnode import extract_markdown_images


class TestHTMLNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images2(self):
        matches = extract_markdown_images("This is text with another ![image](https://i.imgur.com/236LP.png)")
        self.assertListEqual([("image", "https://i.imgur.com/236LP.png")], matches)
        
        
if __name__ == "__main__":
    unittest.main()