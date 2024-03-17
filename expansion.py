def build_tree_fractal_expansion(node, max_fractal_dimension, max_depth, depth):
    if depth == max_depth or len(node.data) == 1:
        return

    if fractal_dimension(node) > max_fractal_dimension:
        return

    split_feature, split_value = find_best_split(node)
    if split_feature is None:
        return

    left_data = node.data[node.data[split_feature] <= split_value]
    right_data = node.data[node.data[split_feature] > split_value]

    node.split_feature = split_feature
    node.split_value = split_value
    node.left_child = Node(left_data)
    node.right_child = Node(right_data)

    build_tree_fractal_expansion(node.left_child, max_fractal_dimension, max_depth, depth + 1)
    build_tree_fractal_expansion(node.right_child, max_fractal_dimension, max_depth, depth + 1)
