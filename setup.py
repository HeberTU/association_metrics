# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 06:38:18 2021

@author: HTRUJILLO
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="association-metrics", # Replace with your own username
    version="0.0.1",
    author="Heber Trujillo",
    author_email="heber.trj.urt@gmail.com",
    description="Python module for measure the degree of association between variables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HeberTU/association_metrics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
