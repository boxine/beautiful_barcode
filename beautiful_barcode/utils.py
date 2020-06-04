import re


def module_coords(modules):
    """ Yields tuples of position to left (in modules) and width (in modules) of painted areas. """

    assert re.match(r'^[01]*$', modules)

    width = 0
    for x, c in enumerate(modules):
        if c == '0' and width > 0:
            yield (x - width, width)
            width = 0
        elif c == '1':
            width += 1
    if width > 0:
        yield (len(modules) - width, width)
