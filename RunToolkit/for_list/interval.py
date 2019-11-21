# -*- coding: utf-8 -*-
# @Time     : 2019/10/11 16:02
# @Author   : Run 
# @File     : interval.py
# @Software : PyCharm

from typing import List
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def continuous_int_to_ranges(nums: List[int]):
    """
    LeetCode 228: Summary Ranges
    Given a sorted integer array without duplicates, return the summary of its ranges(continuous int).
    Examples:
        1. [1] -> [[1, 1]]
        2. [0, 1, 2, 4, 5, 7] -> [[0, 2], [4, 5], [7, 7]]
        3. [0, 2, 3, 4, 6, 8, 9, 10, 11] -> [[0, 0], [2, 4], [6, 6], [8, 11]]
    :param nums: sorted int list without duplicates
    :return:
    """
    l = len(nums)
    if l == 0:
        return []
    res = []
    start = nums[0]
    for i in range(l - 1):
        if nums[i] + 1 < nums[i + 1]:
            res.append([start, nums[i]])
            start = nums[i + 1]
    res.append([start, nums[-1]])
    return res


def find_missing_ranges(nums: List[int], lower: int, upper: int):
    """
    LeetCode 163: Missing Ranges
    Given a sorted integer array where the range of elements are [lower, upper] inclusive,
        return its missing ranges.
    Examples:
        1. [0, 1, 3, 50, 75], lower: 0 and upper: 99, return: [[2, 2], [4, 49], [51, 74], [76, 99]]
    Notes:
        the same as `continuous_int_to_intervals([x for x in range(lower, upper + 1) if x not in nums])`
    """
    res = []
    for x in nums:
        if x > lower:
            res.append([lower, x - 1])
        lower = x + 1
    if upper > lower:
        res.append([lower, upper])

    return res


def merge_intervals(intervals: List[List]) -> List[List]:
    """
    LeetCode 59: Merge Intervals
    Given a collection of intervals, merge all overlapping intervals.
    Examples:
        1. [[1, 3], [8, 10], [2, 6], [15, 18]] -> [[1, 6], [8, 10], [15, 18]]
        2. [[1, 4], [4, 5]] -> [[1, 5]]
    """
    if len(intervals) <= 1:
        return intervals
    res = []
    intervals = sorted(intervals)
    first = intervals[0]
    for second in intervals[1:]:
        if first[1] < second[0]:
            res.append(first)
            first = second
        elif first[1] <= second[1]:
            first[1] = second[1]

    res.append(first)
    return res


def interval_list_intersection(A: List[List], B: List[List], visualization: bool = True) -> List[List]:
    """
    LeteCode 986: Interval List Intersections
    Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
        Return the intersection of these two interval lists.
    Examples:
        1. A: [[0, 2], [5, 10], [13, 23], [24, 25]], B: [[1, 5], [8, 12], [15, 24], [25, 26]]
           return: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    """
    res = []
    i = j = 0
    while i < len(A) and j < len(B):
        s = max(A[i][0], B[j][0])
        e = min(A[i][1], B[j][1])
        if s <= e:
            res.append([s, e])

        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    if visualization:
        interval_list_intersection_visualization(A, B, res)

    return res


def interval_list_intersection_visualization(A, B, res, figure_size=(20, 2)):
    """
    visualization for LeetCode 986 by matplotlib
    :param A: List[List]
    :param B: List[List]
    :param res: List[List]
    :return:
    """
    y0 = 0.2
    gap = 0.2
    height = 0.2
    font_size = 15
    #
    fig = plt.figure(figsize=figure_size)
    ax = fig.add_subplot(111)
    #
    xmin = min(A[0][0], B[0][0]) - 1
    xmax = max(A[-1][1], B[-1][1]) + 1
    ymin = 0
    ymax = y0 + 3 * height + 3 * gap
    plt.axis([xmin, xmax, ymin, ymax])
    plt.axis('off')
    # plt.yticks([])  # 设置y轴刻度不可见
    # frame = plt.gca()
    # frame.axes.get_yaxis().set_visible(False)  # y 轴不可见
    # frame.axes.get_xaxis().set_visible(False)  # x 轴不可见
    #
    plt.text(xmin, y0 + 2 * height + 2 * gap, 'A', color='black', ha='center', fontsize=font_size)
    for left, right in A:
        ax.add_patch(
            patches.Rectangle(
                (left, y0 + 2 * height + 2 * gap),  # (x, y)
                right - left,  # width
                height,  # height
            )
        )
    #
    plt.text(xmin, y0 + height + gap, 'B', color='black', ha='center', fontsize=font_size)
    for left, right in B:
        ax.add_patch(
            patches.Rectangle(
                (left, y0 + height + gap),  # (x, y)
                right - left,  # width
                height,  # height
                color='yellow'
            )
        )
    #
    plt.text(xmin, y0, 'res', color='black', ha='center', fontsize=font_size)
    for left, right in res:
        ax.add_patch(
            patches.Rectangle(
                (left, y0),  # (x, y)
                right - left,  # width
                height,  # height
                color='pink'
            )
        )
    # 以文本的形式展示x轴刻度
    for tick in set(sum(A, []) + sum(B, [])):
        plt.text(tick, 0, str(tick), color='black', ha='center')

    plt.show()


def insert_interval(intervals: List[List], new_interval: '[s, e]') -> List[List]:
    """
    LeetCode 57: Insert Interval
    Given a set of non-overlapping and sorted intervals, insert a new interval into the intervals (merge if necessary),
        and make sure these intervals keep non-overlapping and sorted.
    Examples:
        1. intervals: [[1, 3],[6, 9]], new_interval: [2, 5], res: [[1, 5], [6, 9]]
        2. intervals: [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], new_interval: [4, 8],
           res: [[1, 2], [3, 10], [12, 16]]
    """
    l = len(intervals)
    s, e = new_interval
    left = [x for x in intervals if x[1] < s]
    right = [x for x in intervals if x[0] > e]
    l1, l2 = len(left), len(right)
    if l1 + l2 != l:
        s = min(s, intervals[l1][0])
        e = max(e, intervals[~l2][1])
    return left + [[s, e]] + right


def erase_overlap_intervals_count(intervals: List[List[int]]) -> int:
    """
    LeteCode 435: Non-overlapping Intervals
    Given a list of intervals, find the minimum number of intervals you need to remove
        to make the rest of the intervals non-overlapping.
    Examples:
        1. intervals: [[1, 2], [2, 3], [3, 4], [1, 3]], return: 1
        2. intervals: [1, 2], [1, 2], [1, 2]], return 2
    """
    l = len(intervals)
    if l <= 1:
        return 0
    intervals = sorted(intervals, key=lambda x: x[1])

    res = 0
    end = intervals[0][1]
    for x in intervals[1:]:
        if x[0] >= end:
            end = x[1]
        else:
            res += 1

    return res


def erase_overlap_intervals(intervals: List[List[int]]):
    """
    a variant for LeetCode 435
    Given a list of intervals, remove minimal intervals to make the rest of the intervals non-overlapping.
    注意：剩余列表中允许打乱原列表的顺序。如果要求保持原顺序，则需要在排序前先记录index。
    Examples:
        1. intervals: [[1, 2], [2, 3], [3, 4], [1, 3]], return: [[1, 2], [2, 3], [3, 4]], [[1, 3]]
        2. intervals: [1, 2], [1, 2], [1, 2]], return: [[1, 2]], [[1, 2], [1, 2]]
    :param intervals:
    :return:
        left_intervals: List[List[int]]
        remove_intervals: List[List[int]]
    """
    l = len(intervals)
    if l <= 1:
        return l, []
    intervals = sorted(intervals, key=lambda x: x[1])

    left, remove = [], []
    interval = intervals[0]
    end = interval[1]
    for x in intervals[1:]:
        if x[0] >= end:
            left.append(interval)
            interval = x
            end = x[1]
        else:
            remove.append(x)
    left.append(interval)

    return left, remove


def range_addition(n, updates):
    """

    LeetCode 370: Range Addition
    Assume you have a list `[0] * n` and are given k update operations.
    Each operation is represented as a triplet `[start_index, end_index, increment]`,
    which adds increment to each element of subarray A[start_index ... end_index] (start_index and end_index inclusive).
    Return the modified array after all k operations were executed.
    Examples:
        1. n = 5, updates = [(1,  3,  2), (2,  4,  3), (0,  2, -2)]. return: [-2, 0, 3, 5, 3]
    :param n: length of list
    :param updates: [(start_index, end_index, increment), ...]
    :return:
    """
    res = [0] * (n + 1)
    for si, ei, inc in updates:
        res[si] += inc
        res[ei + 1] -= inc
    for i in range(1, n + 1):
        res[i] += res[i - 1]
    return res[:-1]


if __name__ == '__main__':
    print(continuous_int_to_ranges([1]))
    print(continuous_int_to_ranges([0, 1, 2, 4, 5, 7]))
    print(continuous_int_to_ranges([0, 2, 3, 4, 6, 8, 9, 10, 11]))
    print()

    print(find_missing_ranges([0, 1, 3, 50, 75], 0, 99))
    print()

    print(merge_intervals([[1, 3], [8, 10], [2, 6], [15, 18]]))
    print(merge_intervals([[1, 4], [4, 5]]))
    print()

    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(interval_list_intersection(A, B, False))
    print(interval_list_intersection(A, B))
    print()

    print(insert_interval([[1, 3],[6, 9]], [2, 5]))
    print(insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print()

    print(range_addition(5, [(1, 3, 2), (2, 4, 3), (0, 2, -2)]))
    print()

    print(erase_overlap_intervals_count([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(erase_overlap_intervals_count([[1, 2], [1, 2], [1, 2]]))
    print(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))
    print()