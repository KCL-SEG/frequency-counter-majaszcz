"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    items = [str(x) for x in items]

    for item in items:
        frequencies.update({item : items.count(item)})

    return frequencies
