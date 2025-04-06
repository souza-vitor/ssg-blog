from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode

def main():
    dummy = HTMLNode(tag="<a>", value="test link", props={"href": "www.boot.dev", "target": "_blank"})
    print(dummy.props_to_html())


main()