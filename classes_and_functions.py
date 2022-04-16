class State:
    def __init__(self, initial, depth=0, parent=None):
        # Format: (chicken, wolves, boat)
        self.left = initial[0]
        self.right = initial[1]
        self.parent = parent
        try:
            self.depth = parent.depth + 1
        except:
            self.depth = 0

    def __repr__(self):
        # Behavior when print is called
        return f"{self.left}~~~~{self.right}"

    def __bool__(self):
        # Behavior when "if <state object>" is called (checks validity of state against rules of game)
        if self.left[1] > self.left[0]:
            if self.left[0] == 0:
                return True
            else:
                return False
        elif self.right[1] > self.right[0]:
            if self.right[0] == 0:
                return True
            else:
                return False
        else:
            return True

    def __eq__(self, other):
        if self.left == other.left and self.right == other.right:
            return True
        else:
            return False

    def move(self, movestring, show="No"):
        """
        Make change to state based on input.
        - Format
            1C == move 1 chicken
            2W == move 2 wolves
            1C1W == move 1 chicken and 1 wolf
        - Assumes boat direction, i.e. If boat is on left, assume movement to the right.
        - Does not accept movement w/o animal
        - Returns new state as a State class object
        - Does NOT alter state of current object
        """
        if movestring == "1C1W":
            if self.left[2] == 1:  # Left to right
                output_tuple = (
                    [self.left[0] - 1, self.left[1] - 1, 0],
                    [self.right[0] + 1, self.right[1] + 1, 1],
                )

            else:  # Right to left
                output_tuple = (
                    [self.left[0] + 1, self.left[1] + 1, 1],
                    [self.right[0] - 1, self.right[1] - 1, 0],
                )

        else:
            moveset = list(movestring)
            animal = moveset[1]
            num = int(moveset[0])

            if self.left[2] == 1:  # left to right
                if animal == "C":  # [c h i c k e n s]
                    output_tuple = (
                        [self.left[0] - num, self.left[1], 0],
                        [self.right[0] + num, self.right[1], 1],
                    )

                else:  # wolves
                    output_tuple = (
                        [self.left[0], self.left[1] - num, 0],
                        [self.right[0], self.right[1] + num, 1],
                    )

            else:  # Right to left
                if animal == "C":  # [c h i c k e n s]
                    output_tuple = (
                        [self.left[0] + num, self.left[1], 1],
                        [self.right[0] - num, self.right[1], 0],
                    )

                else:  # Wolves
                    output_tuple = (
                        [self.left[0], self.left[1] + num, 1],
                        [self.right[0], self.right[1] - num, 0],
                    )

        output = State(output_tuple, parent=self)

        # Handle for displaying movement
        if show == "Yes":
            if self.right[2] == 1:
                print(f"{output.left}~->~{output.right}")
            else:
                print(f"{output.left}~<-~{output.right}")

        return output

    def expand(self):
        output = []
        if self.left[2] == 1:  # boat on left shore
            if self.left[0] >= 2:  # 2 chickens
                output.append(self.move("2C"))
            if self.left[0] >= 1:  # 1 chicken
                output.append(self.move("1C"))
            if self.left[1] >= 2:  # 2 wolf
                output.append(self.move("2W"))
            if self.left[1] >= 1:
                output.append(self.move("1W"))
            if (self.left[0] >= 1) and (self.left[1 >= 1]):
                output.append(self.move("1C1W"))
        else:  # boat on right shore
            if self.right[0] >= 1:  # 1 chicken
                output.append(self.move("1C"))
            if self.right[0] >= 2:  # 2 chickens
                output.append(self.move("2C"))
            if self.right[1] >= 1:
                output.append(self.move("1W"))
            if (self.right[0] >= 1) and (self.right[1] >= 1):
                output.append(self.move("1C1W"))
            if self.right[1] >= 2:  # 2 wolf
                output.append(self.move("2W"))
        return output


def pathFind(node, initial):
    output = []
    current = node
    while current.parent != initial:
        output.append(current)
        current = current.parent
    output.append(initial)
    output.reverse()
    return output


def injest(path):
    """
    Take target state file and return an array of tuples, each tuple representing a starting state.
    """
    output = []
    with open(path, "r") as target:
        for leftbank, rightbank in zip(target, target):
            current_left = list(map(int, leftbank.strip("\n").split(",")))
            current_right = list(map(int, rightbank.strip("\n").split(",")))
            output = (current_left, current_right)

    return output


if __name__ == "__main__":
    a = [2, 3, 6, 1, 2, 0, 9]
    a.sort(key=lambda x: x)
    print(a)

    # test1_state = State(injest("./goalsAndStates/tests/start1.txt"))
    # test1_state2 = State(injest("./goalsAndStates/tests/start1.txt"))
    # test2 = State(injest("./goalsAndStates/tests/start2.txt"))
    # print(test1_state == test1_state2)
    # print(test1_state == test2)

