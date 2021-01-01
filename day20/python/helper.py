import math
from itertools import chain, combinations, zip_longest
from typing import List, NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def read(fname: str) -> str:
    with open(fname) as f:
        return f.read()


def read_lines(fname: str) -> List[str]:
    with open(fname) as f:
        return f.read().strip().splitlines()


def read_lines_as_ints(fname: str) -> List[int]:
    return [int(s) for s in read_lines(fname)]


def angle(a: Point, b: Point, c: Point) -> float:
    """
    from https://medium.com/@manivannan_data/find-the-angle-between-three-points-from-2d-using-python-348c513e2cd
    """
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang


def grouper(iterable, n, fillvalue=None):
    """
    Collect data into fixed-length chunks:
    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx

    (from Peter Norvig's pytudes)
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

    from https://docs.python.org/3/library/itertools.html
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def rotate90(matrix):
    """
    Rotate a matrix by 90 degrees clockwise.
    Returns an immutable matrix.

    Example:

    1 2  -->  3 1
    3 4       4 2
    """
    rotated = list(zip(*matrix[::-1]))
    return tuple(rotated)


def flip(matrix):
    """
    Flip a matrix vertically.
    Returns an immutable matrix.

    Example:

    1 2  -->  2 1
    3 4       4 3
    """
    return tuple([row[::-1] for row in matrix])


def top_row(matrix):
    """
    Return the first (top) row of a matrix.
    Returns a tuple (immutable).
    """
    return tuple(matrix[0])


def bottom_row(matrix):
    """
    Return the last (bottom) row of a matrix.
    Returns a tuple (immutable).
    """
    return tuple(matrix[-1])


def left_column(matrix):
    """
    Return the first (leftmost) column of a matrix.
    Returns a tuple (immutable).
    """
    result = []
    for row in matrix:
        result.append(row[0])
    #
    return tuple(result)


def right_column(matrix):
    """
    Return the last (rightmost) column of a matrix.
    Returns a tuple (immutable).
    """
    result = []
    for row in matrix:
        result.append(row[-1])
    #
    return tuple(result)
