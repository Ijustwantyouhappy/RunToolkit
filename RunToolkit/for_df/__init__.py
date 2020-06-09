# -*- coding: utf-8 -*-
# @Time     : 2019/10/5 10:57
# @Author   : Run 
# @File     : __init__.py.py
# @Software : PyCharm

"""
Notes:
    1. move Cube to package `df_helper`
"""

import numpy as np
import pandas as pd
from string import ascii_lowercase


def gen_df(row_num: int, col_num: int, lb: int=0, ub: int=100):
    """
    generate dataframe consist of int data and lowercase headers
    :param row_num:
    :param col_num:
    :param lb: lower bound
    :param ub: upper bound
    :return:
    """
    shape = (row_num, col_num)
    data = np.random.randint(lb, ub, shape)
    cols = list(ascii_lowercase[:col_num])
    df = pd.DataFrame(data, columns=cols)
    print("shape:", df.shape)
    print(df.head(2))
    return df


def compare_df(df1: pd.DataFrame, df2: pd.DataFrame, delta=1e-6) -> bool:
    """
    Check if two DataFrames are the same.
    Notes:
        1. todo `type(1.0) != type(1)`, but `1.0 == 1`
        2. todo speed up
    :param df1:
    :param df2:
    :param delta: precision of float
    :return:
    """
    if df1.shape != df2.shape:
        print("different shape")
        print("df1: {}".format(df1.shape))
        print("df2: {}".format(df2.shape))
        return False
    if df1.dtypes.tolist() != df2.dtypes.tolist():
        print("different dtypes")
        print("df1: {}".format(df1.dtypes))
        print("df2: {}".format(df2.dtypes))
        return False
    if df1.columns.names != df2.columns.names:
        print("different header names")
        print("df1: {}".format(df1.columns.names))
        print("df2: {}".format(df2.columns.names))
        return False
    if df1.columns.tolist() != df2.columns.tolist():
        print("different header")
        print("df1: {}".format(df1.columns))
        print("df2: {}".format(df2.columns))
        return False
    if df1.index.names != df2.index.names:
        print("different index names")
        print("df1: {}".format(df1.index.names))
        print("df2: {}".format(df2.index.names))
        return False
    if df1.index.tolist() != df2.index.tolist():
        print("different index")
        return False
    #
    m, n = df1.shape
    for i in range(m):
        for j in range(n):
            x1, x2 = df1.iloc[i, j], df2.iloc[i, j]
            type1, type2 = type(x1), type(x2)
            if type1 != type2:
                print("different type")
                print("type(df1[{}, {}]): {}".format(i, j, type1))
                print("type(df2[{}, {}]): {}".format(i, j, type2))
                return False
            if isinstance(x1, float) or isinstance(x1, np.floating):
                if abs(x1 - x2) > delta:
                    print("different float value")
                    print("df1[{}, {}]: {}".format(i, j, x1))
                    print("df2[{}, {}]: {}".format(i, j, x2))
                    return False
            else:
                if str(x1) != str(x2):
                    print("different value")
                    print("df1[{}, {}]: {}".format(i, j, x1))
                    print("df2[{}, {}]: {}".format(i, j, x2))
                    return False
    print("df1 and df2 are the same.")
    return True


def merge_by(df1: pd.DataFrame, df2: pd.DataFrame, condition):
    """
    similar to conditional join in sql
    :param df1:
    :param df2:
    :param condition:
    :return:
    """
    pass  # todo


# def conditional_merge(df_left, df_right, start_col='start_date', end_col='end_date', date='event_date'):
#     """
#     Left join in conditional
#
#     Parameters
#     ------------------------
#     :param df_left: by evnet
#     :param df_right: by day
#     :param start_col: start_date【by event】
#     :param end_col: end_date【by event】
#     :param date: date【by day】
#
#     examples
#     -------------------------
#     >>> df_A = pd.DataFrame({'start_date':['2017-03-27','2017-01-10'],'end_date':['2017-04-20','2017-02-01']})
#     >>> df_B = pd.DataFrame({'event_date':['2017-01-20','2017-01-27'],'price':[100,200]})
#     >>> conditional_merge(df_A,df_B)
#     """
#     # convert to timestamp
#     df_left[end_col] = pd.to_datetime(df_left[end_col])
#     df_left[start_col] = pd.to_datetime(df_left[start_col])
#     df_right[date] = pd.to_datetime(df_right[date])
#
#     # left join
#     df_left = df_left.assign(key=1)
#     df_right = df_right.assign(key=1)
#     df_merge = pd.merge(df_left, df_right, on='key').drop('key', axis=1)
#     df_merge = df_merge.query('{0} >= {1} and {2} <= {3}'.format(date, start_col, date, end_col))
#     df_out = df_left.merge(df_merge, on=[start_col, end_col], how='left').fillna('').drop('key', axis=1)
#     return df_out