#!/usr/bin/python3
"""
Module: append_write.py
Function to append a string to a file and return the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)

