
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
        yield self.start
        yield self.end

    def __cmp__(self, other):
        start_cmp = self._cmp_start(other)
        if start_cmp == 0:
            return self._cmp_end(other)
        return start_cmp

    def _cmp_start(self, other):
        if self.start is None and other.start is None:
            return 0
        elif self.start is None and other.start is not None:
            return -1
        elif self.start is not None and other.start is None:
            return 1
        elif self.start > other.start:
            return 1
        elif self.start < other.start:
            return -1
        else:
            return 0

    def _cmp_end(self, other):
        if self.end is None and other.end is None:
            return 0
        elif self.end is None and other.end is not None:
            return 1
        elif self.end is not None and other.end is None:
            return -1
        elif self.end > other.end:
            return 1
        elif self.end < other.end:
            return -1
        else:
            return 0

    def __repr__(self):
        return "<Range: {} to {}>".format(self.start, self.end)

    def __str__(self):
        return "{} to {}".format(self.start, self.end)


def merge_ranges(list_of_ranges):
    merged_ranges = []

    list_of_ranges = [Range(start, end) for start, end in list_of_ranges]

    if len(list_of_ranges) > 0:
        sorted_list = sorted(list_of_ranges)
        range_start, range_end = sorted_list[0]
        for start, end in sorted_list:
            if start is None or start <= range_end:
                if end is None:
                    range_end = None
                    break
                elif range_end is not None:
                    range_end = max(range_end, end)
            else:
                merged_ranges.append((range_start, range_end))
                range_start, range_end = start, end
        merged_ranges.append((range_start, range_end))

    return merged_ranges
