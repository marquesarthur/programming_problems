
class Schedule(object):

    def __init__(self, start, end, employee_id="NaN"):
        self.start = start
        self.end = end
        self.employee_id = employee_id

    def __str__(self):
        return "[%d, %d): %s" % (self.start, self.end, self.employee_id)

    def __repr__(self):
        return "[%d, %d): %s" % (self.start, self.end, self.employee_id)

    def overlap(self, other):
        if self.start < other.start: # left interval
            return self.start <= other.start <= self.end
        else: # right interval
            return other.start <= self.start <= other.end


class Solution(object):


    def freeTimeIntervals(self, schedule):
        # create tupple with interval start, end, and employee
        # sort by tupple start and end
        # add interval to stack
        # iterate from 1 to n
        # if i - 1 and i overlap with top of stack:
        #   update stack
        # else add new interval to stack
        # pop from stack finding gaps

        work_schedule = []
        for employee in xrange(len(schedule)):
            for work_time in schedule[employee]:
                work_schedule.append(Schedule(work_time[0], work_time[1], str(employee)))

        work_schedule = sorted(work_schedule, key=lambda k: (k.start, k.end))


        stack = []
        stack.append(work_schedule[0])

        for schedule in work_schedule[1:]:
            if schedule.overlap(stack[-1]):
                stack[-1] = self.update_working_interval(schedule, stack[-1])
            else:
                stack.append(schedule)

        result = []

        for i in xrange(1, len(stack)):
            a = stack[i - 1]
            b = stack[i]
            free = Schedule(a.end, b.start)
            if free.end - free.start != 0: # avoid zero length intervals
                result.append(free)

        return [[a.start, a.end] for a in result]


    def update_working_interval(self, a, b):
        return Schedule(min(a.start, b.start), max(a.end, b.end))






schedule = [
    [[1,2],[5,6]],
    [[1,3]],[[4,10]]
]
# Output: [[3,4]]
# Explanation:
# There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
print(Solution().freeTimeIntervals(schedule))


schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
# Output: [[5, 6], [7, 9]]
print(Solution().freeTimeIntervals(schedule))
