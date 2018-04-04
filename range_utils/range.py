import functools

@functools.total_ordering
class Range(object):
    """This object defines the meaning of None for start and end in a range.

    If start is None it means that the start is the absolute start and
    is always smaller than anything other than None.

    If end is None it means that the end is the absolute end and is always
    bigger than anything other than None.
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return iter((self.start, self.end))

    def __eq__(self, other):
        if self.start == other.start:
            return self.end == other.end
        return False

    def __lt__(self, other):

        if other.start is not None and (self.start is None or self.start <= other.start):
            if other.end is None or self.start is not None or self.end is None or (self.end is not None or self.end < other.end):
                return True

        return False

    def __repr__(self):
        return "<Range: {} to {}>".format(self.start, self.end)

    def __str__(self):
        return "{} to {}".format(self.start, self.end)
