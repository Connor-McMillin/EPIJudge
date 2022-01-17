from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return solve(float('-inf'), float('inf'), tree)

def solve(left: int, right: int, tree: BinaryTreeNode) -> bool:
    if tree == None:
        return True
    elif left <= tree.data and tree.data <= right:
        return solve(left, tree.data, tree.left) and solve(tree.data, right, tree.right)
    else:
        return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
