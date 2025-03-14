#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a UTF-8 encoded text file.
It follows PEP8 guidelines for formatting and readability.
"""

def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
        None

    Example:
        If the file 'example.txt' contains:
        Hello, World!

        Calling read_file('example.txt') will output:
        Hello, World!
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")  # Using end="" to avoid extra newlines when printing

