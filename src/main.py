from enum import Enum
from textnode import TextType, TextNode
from htmlnode import HTMLNode

print("Hello World")

def main():
    new_node = TextNode("I'm hungry", TextType.NORMAL, "https://www.w3schools.com/python/python_classes.asp" )
    print(new_node)
    new_htmlnode = HTMLNode("<h1>", "Hamburger Time", None)
    print(new_htmlnode)



main()