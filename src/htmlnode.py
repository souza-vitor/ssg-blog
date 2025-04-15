from textnode import TextNode, TextType
import re

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_str = ""

        for key, value in sorted(self.props.items()):
            props_str += f' {key}="{value}"'
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if self.tag is None:
            return self.value
        else:
            if self.props is None:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
            
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is missing in ParentNode")
        
        
        if self.children is None or len(self.children) == 0:
            raise ValueError("Children cannot be empty or None")
        else:
            html_children = ''.join([child.to_html() for child in self.children])
            return f'<{self.tag}>{html_children}</{self.tag}>'


# functions ?

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, text_node.url)
        case TextType.IMAGE:
            return LeafNode("img", "", text_node.url)
        case _:
            raise ValueError("Invalid TextType")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue

        if old_node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid markdown: missing closing delimiter")
        
        if delimiter not in old_node.text:
            new_nodes.append(old_node)
            continue
        
        parts = old_node.text.split(delimiter)
        is_inside_delimiter = False

        for part in parts:
            if part:
                if is_inside_delimiter:
                    new_nodes.append(TextNode(part, text_type))
                else:
                    new_nodes.append(TextNode(part, TextType.NORMAL))
            
            is_inside_delimiter = not is_inside_delimiter
    return new_nodes


def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return links