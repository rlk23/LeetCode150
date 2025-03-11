'''
Question: Construct a Binary Tree from HTML Syntax
Context
Parsing and understanding HTML structure is an essential skill for web scraping, browser engines, and HTML parsers. HTML documents follow a hierarchical structure, making them a great candidate for representation as a binary tree.

Problem Statement
Given an HTML snippet as a string, construct a binary tree where:

Each HTML tag is a node.
The first child tag is the left child.
The next sibling tag (at the same level) is the right child.
Your task is to parse the given HTML string and construct the corresponding binary tree representation.


'''

from html.parser import HTMLParser

class TreeNode:
    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = dict(attrs) if attrs else {}  # Store attributes as a dictionary
        self.left = None  # First child
        self.right = None  # Next sibling

    def __repr__(self):
        return f"{self.tag} {self.attrs}"  # Display tag with attributes


class HTMLParserTree(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []  # Stack to maintain hierarchy
        self.root = None  # Root of the tree

    def handle_starttag(self, tag, attrs):
        new_node = TreeNode(tag, attrs)  # Create a new TreeNode with attributes

        if self.stack: 
            parent = self.stack[-1]
            if not parent.left:
                parent.left = new_node  # Assign as left child
            else:
                sibling = parent.left
                while sibling.right:
                    sibling = sibling.right
                sibling.right = new_node  # Assign as right sibling

        else:
            self.root = new_node  # First node is the root

        self.stack.append(new_node)  # Push onto stack

    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()  # Close the current tag

    def get_tree(self):
        return self.root


def print_tree(node, level=0):
    if node:
        print("    " * level + f"- {node.tag} {node.attrs}")
        print_tree(node.left, level + 1)  # Traverse children
        print_tree(node.right, level)  # Traverse siblings


# Sample HTML input
html_string = """
<div>
    <h1 id="title"></h1>
    <p class="text">
        <span></span>
    </p>
</div>
"""

# Parsing the HTML and constructing the tree
parser = HTMLParserTree()
parser.feed(html_string)
root = parser.get_tree()

# Print the constructed binary tree
print_tree(root)
