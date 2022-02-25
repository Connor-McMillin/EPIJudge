from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []
    else:
        left_list = inorder_traversal(tree.left)
        right_list = inorder_traversal(tree.right)

        return left_list + [tree.data] + right_list

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
