#!/usr/bin/python3
def best_score(a_dictionary):
    """
    max function will compare values returned by .get method
    for each key in the dictionary

    """
    return (max(a_dictionary, key=a_dictionary.get) if a_dictionary else None)
