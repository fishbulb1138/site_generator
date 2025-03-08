from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    ITALIC = "italic"
    BOLD = "bold"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        if url == "":
            self.url = None
        else:
            self.url = url

    def __eq__(self, text_node):
        return self.text_type == text_node.text_type and self.text == text_node.text and self.url == text_node.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"




