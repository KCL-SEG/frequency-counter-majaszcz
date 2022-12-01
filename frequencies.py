"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    items.sort()
    for item in items:
        frequencies.update({item : items.count(item)})
    
    return frequencies
