

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):

        def to_html(self):
            raise NotImplementedError

        def props_to_html(self):
            props_string = ""
            for key, value in self.props.items():
                new_string = f" {key}=\"{value}\""
                props_string += new_string

            return props_string

        def __repr__(self):
            print(f"tag: {self.tag} value: {self.value} children: {self.children} props: {self.props.items}")




