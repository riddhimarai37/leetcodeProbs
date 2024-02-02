# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        directions = [(-1,0), (0,1), (1,0), (0,-1)] # HAVE TO go in this order of up down right left
        visited = set()

        def go_back():
            # reversed our direction and reset 
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(x,y, direction):
            visited.add((x,y))
            robot.clean()

            for i in range(4):
                # 0 reps up, 1 reps right, 2 reps down, 3 reps left
                new_direction = (direction + i) % 4
                # new direction goes up, down, right or left by % 4

                new_x = x + directions[new_direction][0]
                new_y = y + directions[new_direction][1]

                if (new_x,new_y) not in visited and robot.move():
                    backtrack(new_x, new_y, new_direction)
                    go_back()

                # turning robot 90 degress each time
                robot.turnRight()

        backtrack(0,0,0)