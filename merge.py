# Helper function to check if the two intervals overlap
def is_overlapping(a, b):
    if b[0] > a[0] and b[0] < a[1]:
        return True
    else:
        return False

class Merge:

    def merge(intervals):
        """ Merging a list of intervals into overlapping intervals"""
        
        # sort the intervals by its first value
        intervals.sort(key = lambda x: x[0])
        
        # stores the resulting list
        result = []

        # put the first interval into the resulting list
        result.append(intervals[0])

        # iterate over the remaining intervals
        for i in range(1, len(intervals)):
            
            # get the last interval of the result list
            pop_element = result.pop()

            # get the current interval from the intervals list
            current_interval = intervals[i]

            # check if it overlaps
            if is_overlapping(pop_element, current_interval):
                # if yes: extend the interval and add it to the result list
                new_element = [pop_element[0], max(pop_element[1], current_interval[1])]
                result.append(new_element)
            else:
                # if no: put the last interval and the current interval to the result list
                result.append(pop_element)
                result.append(current_interval)

        return result
