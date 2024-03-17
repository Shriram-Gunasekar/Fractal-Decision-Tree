def prune_tree(node, max_fractal_dimension):
    if node is None:
        return

    if fractal_dimension(node) > max_fractal_dimension:
        node.left_child = None
        node.right_child = None
        return

    prune_tree(node.left_child, max_fractal_dimension)
    prune_tree(node.right_child, max_fractal_dimension)
