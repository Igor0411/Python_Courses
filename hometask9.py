#! usr/bin/env python


from __future__ import division, print_function
import itertools
import random


class Node(object):

    def __init__(self, value=None, parent=None, l_child=None, r_child=None):
        """

        :param value:
        :param parent:
        :param l_child:
        :param r_child:
        :return:
        """
        self._value = value
        self._parent = parent
        self._l_child = l_child if l_child else None
        self._r_child = r_child if r_child else None

    @property
    def value(self):
        return self._value

    @property
    def parent(self):
        return self._parent

    @property
    def l_child(self):
        return self._l_child

    @property
    def r_child(self):
        return self._r_child

    def __str__(self):
        return str((self.value, self.parent, self.l_child, self.r_child))

    def __ne__(self, other):
        """
        :type other: Node
        :return:
        """
        return not self == other

    def __eq__(self, other):
        """
        :type other: Node
        :return:
        """
        return self.priority == other.priority

    def __gt__(self, other):
        """
        :type other: Node
        :return:
        """
        return self.priority > other.priority

    def __ge__(self, other):
        """
        :type other: Node
        :return:
        """
        return self.priority >= other.priority

    def __lt__(self, other):
        """
        :type other: Node
        :return:
        """
        return self.priority < other.priority

    def __le__(self, other):
        """
        :type other: Node
        :return:
        """
        return self.priority <= other.priority


class SearchTree(object):

    def __init__(self):
        self.

    def push(item):

    def pop(value, default=None):

    def find(value):

    def __contains__(self, item):
        """

        :param item:
        :return:
        """






# def bin_tree_search():
#     """
#
#     :return:
#     """
#
#     def bin_search(sequence, target):
#     """
#     :type sequence: collections.Sequense
#     :param sequence:
#     :return:
#     """
#     start = 0
#     stop = len(sequence)
#     while stop - start >= 1:
#         cur_pos = (start + stop)//2
#         if sequence[cur_pos] == target:
#             return True
#         if sequence[cur_pos] > target:
#             stop = cur_pos
#         else:
#             start = cur_pos
#     return target in (start, stop)


def main():
    pass


if __name__ == "__main__":
    main()