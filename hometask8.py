#! usr/bin/env python


from __future__ import division, print_function
import itertools
import random


def mergesort_recursive(lst):
    """
    :type:
    :param lst:
    :return:
    """
    halflist1 = lst[:len(lst) // 2]
    halflist2 = lst[len(lst) // 2:]

    def merge(a, b):
        """
        :type a: list
        :param a: srt list
        :type b: list
        :param b: str list
        :return:
        """
        united_list = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                united_list.append(a[i])
                i += 1
            else:
                united_list.append(b[j])
                j += 1
        if i == len(a):
            united_list.extend(itertools.islice(b, j, len(b)))
        else:
            united_list.extend(itertools.islice(a, i, len(a)))
        return united_list

    if len(halflist1) <= 1 and len(halflist2) <= 1:
        return merge(halflist1, halflist2)
    return merge(mergesort_recursive(halflist1), mergesort_recursive(halflist2))


def test_mergesort_recursive():
    unsorted_list = [random.randint(1, 1000) for _ in xrange(5)]
    return mergesort_recursive(unsorted_list) == sorted(unsorted_list)


def main():
    if not test_mergesort_recursive():
        raise RuntimeError


if __name__ == "__main__":
    main()