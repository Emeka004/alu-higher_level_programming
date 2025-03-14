#!/usr/bin/python3
import json
"""
Module: 4-from_json_string.py
Function to return an object (Python data structure) represented by a JSON string.
"""


def from_json_string(my_str):
    """Returns the object (Python data structure) represented by a JSON string"""
    return json.loads(my_str)

json_str = '[1, 2, 3, "Holberton"]'
my_obj = from_json_string(json_str)
print(my_obj)

