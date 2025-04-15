from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode
from htmlnode import split_nodes_delimiter
from htmlnode import extract_markdown_images
from htmlnode import extract_markdown_links

def main():
    #dummy = HTMLNode(tag="<a>", value="test link", props={"href": "www.boot.dev", "target": "_blank"})
    #node = TextNode("This is text with a `code block` word", TextType.NORMAL)
    #new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))


main()