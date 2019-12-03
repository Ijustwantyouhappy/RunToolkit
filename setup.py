# -*- coding: utf-8 -*-
# @Time     : 2019/5/13 10:15
# @Author   : Run 
# @File     : setup.py
# @Software : PyCharm

from setuptools import setup, find_packages
import re


setup(
    name="RunToolkit",
    version=re.findall('__version__\s*=\s*"(.*?)"', open("RunToolkit/__init__.py", "r", encoding="utf-8").read())[0],
    author='Ijustwantyouhappy',
    author_email='',
    description="A fundamental python library for data scientists and engineers.",
    long_description=open('README.rst').read(),  # todo write README seriously
    # long_description_content_type="text/markdown",
    url='',
    # maintainer='aRun',
    # maintainer_email='',
    license='MIT',
    packages=find_packages(),
    # package_data = {
    #     '': ['*.hdf5', '*.html', '*.ipynb', '*.jpg', '*.npz']
    # },
    include_package_data=True,
    zip_safe=False,
    # platforms=["all"],
    python_requires='>=3.5',
    install_requires=["numpy>=1.16.3",
                      "pandas>=0.23.4",
                      "pyexcelerate"],
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows',
        'Operating System :: MacOS',
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 3.'
    ],
    keywords='Tools'
)
