"""
This is the array implementation of trees. Check other repositories for Linkedlist implementation.
"""


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print(f"Removing {child_node.value} from {self.value}")
        # new_children = []
        # for i in self.children:
        #     if (i != child_node):
        #         new_children.append(i)
        # self.children = new_children
        self.children = [i for i in self.children if i != child_node]

    def traverse(self):
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            # pop() will ensure we’re reducing the length of nodes_to_visit
            # and adding current_node.children is necessary to iterate through all nodes in a tree.
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("CTO")
third_child = TreeNode("SWE")
root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)
root.traverse()
