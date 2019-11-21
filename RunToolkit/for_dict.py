# -*- coding: utf-8 -*-
# @Time     : 2019/10/2 23:43
# @Author   : Run 
# @File     : for_dict.py
# @Software : PyCharm


from collections import ChainMap, defaultdict


def merge_dicts(*args):
    """

    :param args: d1, d2, ...
    :return:
    :Notes: dicts: d1, d2
        1. d1.update(d2), d1 changed
        2. {**d1, **d2}
        3. collections.ChainMap(d2, d1), share space with d1 and d2
        4. dict(collections.ChainMap(d2, d1))

        * cost time: 3 << 1 < 2 < 4
        * If d1 >> d2, d1.update(d2) faster than d2.update(d1), but the results might be different.
    """
    # return ChainMap(*args[::-1])
    return dict(ChainMap(*args[::-1]))


def reverse_dict(d: dict, keep: str='all'):
    """
    swap keys and values to get a reverse dict
    without `pd.groupby`
    :param d:
    :param keep:
        'any':  if d[k1]==d[k2]==...==v, res[v] = random choice from {k1, k2, ...}
        'all':  if d[k1]==d[k2]==...==v, res[v] = {k1, k2, ...}
        'sum':  if d[k1]==d[k2]==...==v, res[v] = sum({k1, k2, ...})
        'mean': if d[k1]==d[k2]==...==v, res[v] = mean({k1, k2, ...})
        'max':  if d[k1]==d[k2]==...==v, res[v] = max({k1, k2, ...})
        'min':  if d[k1]==d[k2]==...==v, res[v] = min({k1, k2, ...})
    """
    if keep == 'any':
        res = {v: k for (k, v) in d.items()}
    elif keep == 'all':
        res = defaultdict(set)
        for k, v in d.items():
            res[v].add(k)
        res = dict(res)
    elif keep == 'sum':
        res = {}
        for k, v in d.items():
            if v not in res:
                res[v] = k
            else:
                res[v] += k
    elif keep == 'mean':
        res = {}
        count = {}
        for k, v in d.items():
            if v not in res:
                res[v] = k
                count[v] = 1
            else:
                res[v] += k
                count[v] += 1
        for k, v in res.items():
            res[k] = v / count[k]
        res = dict(res)
    elif keep == 'max':
        res = {}
        for k, v in d.items():
            if v not in res or k > res[v]:
                res[v] = k
    elif keep == 'min':
        res = {}
        for k, v in d.items():
            if v not in res or k < res[v]:
                res[v] = k
    else:
        raise Exception("invalid parameter 'keep': {}".format(keep))

    return res


if __name__ == "__main__":
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 10, 'c': 3}
    print(merge_dicts(d1, d2))
    print(d1, d2)
    print()

    print(reverse_dict({1: 4, 3: 4, 5: 6, 7: 8}, 'all'))
    print(reverse_dict({1: 4, 3: 4, 5: 6, 7: 8}, 'any'))
    print(reverse_dict({1: 4, 3: 4, 5: 6, 7: 8}, 'sum'))
    print(reverse_dict({1: 4, 3: 4, 5: 6, 7: 8}, 'mean'))
    print(reverse_dict({1: 4, 3: 4, 5: 6, 7: 8}, 'max'))
    print(reverse_dict({1: 4, 3: 4, 5: 6, 7: 8}, 'min'))
    print()