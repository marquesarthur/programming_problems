


class Robot:

    def __init__(self):
        self.current_position = (0, 0)
        self.facing = 'north'
        self.instructions = []


    def set_instructions(self, instructions):
        self.instructions = instructions


    def has_circle(self, max_loops=20):
        current_loop = 0

        has_loop = False
        while current_loop < max_loops:
            for i in self.instructions:
                self.do_instruction(i)

            if self.current_position == (0, 0):
                has_loop = True
                break
            current_loop += 1

        return has_loop


    def do_instruction(self, i):
        movements = ['north', 'east', 'south', 'west']

        if i == 'G':
            if self.facing == 'north':
                x, y = self.current_position
                y += 1
                self.current_position = x, y
            if self.facing == 'south':
                x, y = self.current_position
                y -= 1
                self.current_position = x, y
            if self.facing == 'west':
                x, y = self.current_position
                x -= 1
                self.current_position = x, y
            if self.facing == 'east':
                x, y = self.current_position
                x += 1
                self.current_position = x, y
        elif i == 'L':
            current = movements.index(self.facing)
            counter_clocwise = current - 1
            self.facing = movements[counter_clocwise]
        elif i == 'R':
            current = movements.index(self.facing)
            clocwise = current + 1
            if clocwise == len(movements):
                clocwise = 0
            self.facing = movements[clocwise]






class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        robot = Robot()
        robot.set_instructions(instructions)
        result = robot.has_circle()
        return result








# The robot performs the instructions given in order, and repeats them forever.


instructions = "GGLLGG"
print(Solution().isRobotBounded(instructions))
# Output: true


instructions = "GG"
print(Solution().isRobotBounded(instructions))
# Output: false



instructions = "GL"
print(Solution().isRobotBounded(instructions))
# Output: true