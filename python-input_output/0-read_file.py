#!/usr/bin/python3
def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")  # Using end="" to avoid extra newlines when printindef read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its contents to stdout.
    
    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    
    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")  # Using end="" to avoid extra newlines when printing
