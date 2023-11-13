from typing import List
from queue import Queue
import logging

# Assumption Taken: Each node  have children with unique names.

# Each node has a `name` and a dictionary of its children
# Note: Opted for a dictionary instead of a list of nodes for children to enable efficient searches based on the list element.
class Node:
    def __init__(self, name):
        self.name = name
        self.children_by_name = {}

    def print(self):
        visited = set()
        queue = Queue()
        queue.put(self)
        visited.add(self)

        while not queue.empty():
            current_node = queue.get_nowait()

            child_node_values = ', '.join(current_node.children_by_name.keys())

            print(f"{current_node.name} : {child_node_values}")

            for child_name, child in current_node.children_by_name.items():
                if child not in visited:
                    queue.put(child)
                    visited.add(child)

def merge(inp: List[List[str]]) -> Node:
    root_node = None
    parent_node = None

    for elements_list in inp:
        parent_node = None
        for element_name in elements_list:
            if parent_node is None:
                if root_node is None:
                    # Add a new root node if not present
                    root_node = Node(element_name)
                else:
                    # If root node is already present compare it with the current element in list
                    if root_node.name != element_name:
                        raise Exception("Invalid input format")
                parent_node = root_node
            else:
                # Add a new child node if parent doesn't have a child with `element_name`
                if element_name not in parent_node.children_by_name:
                    parent_node.children_by_name[element_name] = Node(element_name)
                parent_node = parent_node.children_by_name[element_name]

    return root_node


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    root = merge([
        ["*", "a", "b", "car"],
        ["*", "a", "b", "e"],
        ["*", "a", "d", "b"],
        ["*", "a", "x"]
    ])

    root.print()