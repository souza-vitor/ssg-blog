

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
