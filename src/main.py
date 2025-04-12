from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from htmlnode import split_nodes_delimiter

def main():
    #dummy = HTMLNode(tag="<a>", value="test link", props={"href": "www.boot.dev", "target": "_blank"})
    node = TextNode("This is text with a `code block` word", TextType.NORMAL)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)


main()