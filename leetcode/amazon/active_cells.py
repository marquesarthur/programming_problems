class Solution():
    """
        Because there are at most 256 possible states for the prison, eventually the
         states repeat into a cycle rather quickly.
         We can keep track of when the states repeat to find the period t of this cycle,
         and skip days in multiples of t
    """

    def activeAfter(self, cells, days):

        days = days % 14 # How did we get into this number?
        if (days == 0):
            days = 14
        previous_day = list(cells)
        current_day = None
        for i in range(days):
            current_day = list(previous_day)

            current_day[0] = 0
            current_day[7] = 0
            for cell in range(1, 7):
                current_day[cell] = 1 if previous_day[cell - 1] == previous_day[cell + 1] else 0

            print(current_day)
            previous_day = list(current_day)

        return current_day


class SolutionOptimal():
    """
        Because there are at most 256 possible states for the prison, eventually the
         states repeat into a cycle rather quickly.
         We can keep track of when the states repeat to find the period t of this cycle,
         and skip days in multiples of t
    """

    def prisonAfterNDays(self, cells, days):


        loop = self.find_loop_in_cell_config(cells, days)

        days = days % loop
        if (days == 0):
            days = 14

        previous_day = list(cells)
        current_day = None
        for i in range(days):
            current_day = list(previous_day)

            current_day[0] = 0
            current_day[7] = 0
            for cell in range(1, 7):
                current_day[cell] = 1 if previous_day[cell - 1] == previous_day[cell + 1] else 0

            previous_day = list(current_day)

        return current_day

    def find_loop_in_cell_config(self, cells, days):
        previous_day = list(cells)
        current_day = None
        seen = set()
        loop_found = False
        while not loop_found:
            for i in range(days):
                current_day = list(previous_day)

                current_day[0] = 0
                current_day[7] = 0
                for cell in range(1, 7):
                    current_day[cell] = 1 if previous_day[cell - 1] == previous_day[cell + 1] else 0

                if tuple(current_day) not in seen:
                    seen.add(tuple(current_day))
                    previous_day = list(current_day)
                else:
                    loop_found = True
                    break
        return len(seen)


# cells = [0, 1, 0, 1, 1, 0, 0, 1]  # turns into [0,0,1,1,0,0,0,0]
# N = 7
# print(Solution().activeAfter(cells, N))
#
cells = [1, 0, 0, 1, 0, 0, 1, 0]  # turns into [0,0,1,1,1,1,1,0]
N = 1000000000
N = 1000
print(SolutionOptimal().prisonAfterNDays(cells, N))



