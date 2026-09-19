def ft_filter(function, iterable):
    """Recode of the built-in filter using a list comprehension.
    Return the items of iterable for which function(item) is true. When
    function is None, keep the items that are truthy.
    """
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
