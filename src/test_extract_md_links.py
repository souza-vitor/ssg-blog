import unittest

from htmlnode import extract_markdown_links

class TestHTMLNode(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_markdown_links2(self):
        matches = extract_markdown_links("This is text with a link [to google](https://www.google.com)")
        self.assertListEqual([("to google", "https://www.google.com")], matches)
    
if __name__ == "__main__":
    unittest.main()