from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []

    left_list = postorder_traversal(tree.left)
    right_list = postorder_traversal(tree.right)

    return left_list + right_list + [tree.data]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))
