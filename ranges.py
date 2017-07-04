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
        return (self.start, self.end)

    def __eq__(self, other):
        if self.start == other.start:
            return self.end == other.end
        return False

    def __lt__(self, other):
        if self.start is not None and self.end is None:
            return False

        if other.start is not None and (self.start <= other.start or self.start is None):
            if other.end is None or (self.end < other.end or self.end is not None):
                return True

        return False

    def __repr__(self):
        return "<Range: {} to {}>".format(self.start, self.end)

    def __str__(self):
        return "{} to {}".format(self.start, self.end)


def merge_ranges(list_of_ranges):
    merged_ranges = []
    if len(list_of_ranges) > 0:
        sorted_list = sorted(list_of_ranges, key=lambda x: Range(x[0], x[1]))
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


def check_overlap(list_of_ranges):
    if len(list_of_ranges) > 0:
        sorted_list = sorted(list_of_ranges, key=lambda x: Range(x[0], x[1]))
        while len(sorted_list):
            cur_start, cur_end = sorted_list.pop(0)
            for other_start, other_end in sorted_list:
                if cur_end > other_start or cur_end is None:
                    return True
        return False
