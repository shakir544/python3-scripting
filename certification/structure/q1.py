# Example questions on Document structure

"""
print the elements seperated by separator
"""

def print_them(*elements, sep=","):
    """
    :param elements: list of elements
    :param sep: seperator
    :return: List of elements
    """
    return sep.join(elements)


print(print_them.__doc__)
