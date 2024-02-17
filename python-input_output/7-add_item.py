#!/usr/bin/python3
"""This module adds all arguments to a Python list and saves them to a file."""

import sys


def main():
    # Dynamically import save_to_json_file function from the module '5-save_to_json_file'
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    # Try loading existing items from the file, or initialize an empty list if the file is not found
    try:
        existing_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_items = []

    # Extract new items from command-line arguments
    new_items = sys.argv[1:]

    # Combine existing and new items into a single list
    all_items = existing_items + new_items

    # Save the updated list of items back to the file
    save_to_json_file(all_items, "add_item.json")


if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
