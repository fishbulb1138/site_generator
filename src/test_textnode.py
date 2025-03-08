import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("Hamburger Time", TextType.NORMAL)
        node2 = TextNode("Hamburger Time", TextType.BOLD)
        self.assertNotEqual(node2, node)

    def test_url(self):
        node = TextNode("No URL", TextType.NORMAL, url=None)
        self.assertIs(node.url == None, True)





if __name__ == "__main__":
    unittest.main()