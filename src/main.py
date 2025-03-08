from enum import Enum
from textnode import TextType, TextNode

print("Hello World")

def main():
    new_node = TextNode("I'm hungry", TextType.NORMAL, "https://www.w3schools.com/python/python_classes.asp" )
    print(new_node)

main()