# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# Topic : BASIC PYTHON
# Exercise Number : 11
# PROBLEM STATEMENT:
# 	 Write a Python code to convert a given string to a tuple.
# 	 Do not include spaces or tabs in the tuple.
# NOTE : Tuple wil contain each character from "string_given".
# Python Version : 3.7
# string_given = 'Hello,this is your Program      . I am  Program'
from __future__ import print_function
def string_list_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace())
    return result
STR1 = 'Hello,this is your Program      . I am  Program'
print("Original string:")
print(STR1)
print("String to a tuple :")
print(string_list_to_tuple(STR1))
