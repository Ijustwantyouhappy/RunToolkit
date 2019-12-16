# -*- coding: utf-8 -*-
# @Time     : 2019/10/7 12:37
# @Author   : Run 
# @File     : __init__.py.py
# @Software : PyCharm

import os, shutil, stat
import pandas as pd
import pickle


def makedirs(file_path: str) -> None:
    """
    `os.makedirs` enhanced
    """
    if os.path.exists(file_path):
        print("{} already exists".format(file_path))
    else:
        os.makedirs(file_path)
        print("{} established".format(file_path))


def delete_path(file_path: str) -> None:
    """
    Force delete file or dir(contains all subdirs and files).
    Ignore file's attributes like 'read-only'.
    """
    if os.path.exists(file_path):
        if os.path.isfile(file_path):  # file
            os.chmod(file_path, stat.S_IWRITE)
            os.remove(file_path)
        else:  # dir
            for path, sub_folders, sub_files in os.walk(file_path):
                for file in sub_files:
                    os.chmod(os.path.join(path, file), stat.S_IWRITE)
                    os.remove(os.path.join(path, file))
            shutil.rmtree(file_path)
        print("{} deleted".format(file_path))
    else:
        print("{} doesn't exist".format(file_path))


def read_file(file_name):
    """
    读取文件
    :param file_name:
    :param file_type:
    :param encoding:
    :return:
    """
    if not os.path.exists(file_name):
        print("{} doesn't exist.".format(file_name))
        return
    file_type = file_name.split('.')[-1]
    if file_type in {'csv', 'xlsx', 'xls'}:
        if file_type == 'csv':
            func = pd.read_csv
        else:
            func = pd.read_excel
        #
        try:
            res = func(file_name)
        except UnicodeDecodeError:
            try:
                res = func(file_name, encoding="gbk")
            except:
                print("unknown encoding. not utf-8 or gbk.")
                return
        except Exception as e:
            print(e)
            return
    elif file_type == 'pkl':
        with open(file_name, 'rb') as file:
            res = pickle.load(file)
    else:  # todo
        res = None

    return res

