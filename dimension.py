class Node:
    def __init__(self, data, split_feature=None, split_value=None, left_child=None, right_child=None):
        self.data = data
        self.split_feature = split_feature
        self.split_value = split_value
        self.left_child = left_child
        self.right_child = right_child

def calculate_complexity(node):
    # Calculate the complexity of the tree using a simple measure (e.g., number of nodes and depth)
    if node is None:
        return 0, 0
    left_depth, left_nodes = calculate_complexity(node.left_child)
    right_depth, right_nodes = calculate_complexity(node.right_child)
    depth = max(left_depth, right_depth) + 1
    nodes = left_nodes + right_nodes + 1
    return depth, nodes

def fractal_dimension(node):
    depth, nodes = calculate_complexity(node)
    return nodes / (2 ** depth)
