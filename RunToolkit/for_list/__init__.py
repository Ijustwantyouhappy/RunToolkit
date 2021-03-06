# -*- coding: utf-8 -*-
# @Time     : 2019/10/11 14:47
# @Author   : Run 
# @File     : __init__.py.py
# @Software : PyCharm

from typing import Iterable
from collections import Counter, defaultdict, deque
# from statistics import mode


def flatten_iterable(its: Iterable, deep: bool = False) -> list:
    """
    flatten instance of Iterable to list
    Notes:
        1. except of str, won't flatten 'abc' to 'a', 'b', 'c'
    demo: [[[1], [2], [3]], 4]
        if deep is True: flatten to [1, 2, 3, 4]
        if deep is False, flatten to [[1], [2], [3], 4].
    """
    res = []
    for it in its:
        if isinstance(it, str):
            res.append(it)
        elif isinstance(it, Iterable):
            if deep:
                res += flatten_iterable(it, True)
            else:
                res.extend(it)
        else:
            res.append(it)
    return res


def find_mode(l: list) -> 'item in l':
    """
    Find the most common item in a list.
    If there is not exactly one most common value, this function will return one between them.
    todo compare speeds between different methods
    Notes:
        1. `statistics.mode`: If there is not exactly one most common value, ``mode`` will raise StatisticsError.
    """
    # method1
    # d = Counter(l)
    # return max(d, key=d.get)
    #
    # return Counter(l).most_common()[0][0]  # method2
    return max(set(l), key=l.count)  # method3


def group_by(l: list, func, group_format: str = 'set') -> dict:
    """

    Parameters
    ----------
    l
    func
    group_format: 'set'/'list', default = 'set'

    Returns
    -------

    Warnings
    --------
    1. 不能使用itertools.groupby函数，因为那个是把相邻的重复元素放至一起

    """
    if group_format == 'set':
        d = defaultdict(set)
        for x in l:
            d[func(x)].add(x)
    elif group_format == 'list':
        d = defaultdict(list)
        for x in l:
            d[func(x)].append(x)
    else:
        raise Exception("invalid parameter `group_format`: {}".format(group_format))

    return dict(d)


def drop_adjacent_duplicates(l: list) -> list:
    """
    drop adjacent duplicates and keep original order
    Examples:
        1. [0, 0, 1, 1, 1, 2, 3, 4, 4, 5] -> [0, 1, 2, 3, 4, 5]
        2. [] -> []
    """
    if len(l) <= 1:
        return l
    x = l[0]
    res = [x]
    for y in l[1:]:
        if y != x:
            res.append(y)
            x = y
    return res


def rotate(l: list, n: int = 1) -> list:
    """
    Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left.
    Notes:
        1. numpy.roll(a, shift, axis=None)
        2. collections.deque.rotate
    """
    dq = deque(l)
    dq.rotate(n)
    return list(dq)


def argmin(l: list) -> int:
    """
    numpy.argmin()
    """
    return l.index(min(l))


def argmax(l: list) -> int:
    """
    numpy.argmax()
    """
    return l.index(max(l))


if __name__ == "__main__":
    l1 = [[[1], [2], [3]], 4]
    print(flatten_iterable(l1))
    print(flatten_iterable(l1, True))
    #
    l2 = [[1, 2], 3, {4, 5}, 6, (7, 8), [[[[{9}, 10]]]]]
    print(flatten_iterable(l2))
    print(flatten_iterable(l2, True))
    print()
    #
    print(flatten_iterable(['abc', 'de', [1, 2], (3, 4), {5, 6}]))
    print()

    print(find_mode([1, 2, 1, 2, 3, 2, 1, 4, 2]))
    print(find_mode([1, 1, 2, 2]))
    print(find_mode([2, 2, 1, 1]))
    print()

    import math
    print(group_by([6.1, 4.2, 6.3], math.floor))
    print(group_by(['one', 'two', 'three'], len))
    print(group_by([6.1, 4.2, 6.3], math.floor, 'list'))  # {4: [4.2], 6: [6.1, 6.3]}
    print(group_by(['one', 'two', 'three'], len, 'list'))  # {3: ['one', 'two'], 5: ['three']}
    print()

    print(drop_adjacent_duplicates([0, 0, 1, 1, 1, 2, 3, 4, 4, 5]))
    print(drop_adjacent_duplicates([]))
    print()

    print(rotate([1, 2, 3, 4, 5]))
    print(rotate([1, 2, 3, 4, 5], 2))
    print(rotate([1, 2, 3, 4, 5], -2))
    print()

    print(argmin([1, 4, 3, 2, 1]))
    print(argmax([1, 4, 3, 2, 4]))
    print()
