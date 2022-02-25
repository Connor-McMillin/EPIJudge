from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []

    left_list = preorder_traversal(tree.left)
    right_list = preorder_traversal(tree.right)

    return [tree.data] + left_list + right_list


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
