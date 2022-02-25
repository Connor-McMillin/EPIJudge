import functools
from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def bst_to_doubly_linked_list(tree: BstNode) -> Optional[BstNode]:
    def rec_bst_to_doubly_linked_list(current: BstNode) -> (Optional[BstNode], Optional[BstNode]):
        if current == None or current.data == None:
            return (None, None)

        left_head, left_tail = rec_bst_to_doubly_linked_list(current.left)
        right_head, right_tail = rec_bst_to_doubly_linked_list(current.right)
        
        if left_tail:
            left_tail.right = current
        current.left = left_tail

        current.right = right_head
        if right_head:
            right_head.left = current

        return (left_head or current, right_tail or current)

    lst_head, lst_tail = rec_bst_to_doubly_linked_list(tree)

    return lst_head

def print_list(tree: BstNode) -> None:
    while (tree != None and tree.data != None):
        print("{} -> ".format(tree.data), end="")
        tree = tree.right

    print("None")

@enable_executor_hook
def bst_to_doubly_linked_list_wrapper(executor, tree):
    l = executor.run(functools.partial(bst_to_doubly_linked_list, tree))

    if l is not None and l.left is not None:
        raise TestFailure(
            'Function must return the head of the list. Left link must be None'
        )

    v = []
    while l:
        v.append(l.data)
        if l.right and l.right.left is not l:
            raise TestFailure('List is ill-formed')
        l = l.right

    return v


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_to_sorted_list.py',
                                       'bst_to_sorted_list.tsv',
                                       bst_to_doubly_linked_list_wrapper))
