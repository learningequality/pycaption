from __future__ import unicode_literals
import numbers


def classic_div(a, b):
    """
    Divide the way Python 2's ``/`` does: floor division when both operands
    are integers, true division otherwise. Caption timings and sizes can be
    either ints or floats, and each keeps its result.
    """
    if isinstance(a, numbers.Integral) and isinstance(b, numbers.Integral):
        return a // b
    return a / b


def is_leaf(element):
    """
    Return True if the element is a leaf, False otherwise. The element is
    considered a leaf if it is either NavigableString or the "br" tag
    :param element: A BeautifulSoup tag or NavigableString
    """
    name = getattr(element, 'name', None)
    if not name or name == 'br':
        return True
    return False
