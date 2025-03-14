#!/usr/bin/python3
"""
Module: 0-read_file.py
Function to read a file and print its content to stdout.
"""

def read_file(filename=""):
    """Reads a UTF-8 file and prints its content to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")

