class State:
    def __init__(self, initial):
        # Format: (chicken, wolves, boat)
        self.left = initial[0]
        self.right = initial[1]

    def __repr__(self):
        # Behavior when print is called
        return f"{self.left}~~~~{self.right}"

    def __bool__(self):
        if (self.left[1] > self.left[0]) or (self.right[1] > self.right[0]):
            return False
        else:
            return True

    def move(self, movestring, show="No"):
        """
        Make change to state based on input.
        1C == move 1 chicken
        2W == move 2 wolves
        1C1W == move 1 chicken and 1 wolf
        """
        if movestring == "1C1W":
            if self.left[2] == 1:
                output = State(
                    (
                        [self.left[0] - 1, self.left[1] - 1, 0],
                        [self.right[0] + 1, self.right[1] + 1, 1],
                    )
                )
            else:
                output = State(
                    (
                        [self.left[0] + 1, self.left[1] + 1, 1],
                        [self.right[0] - 1, self.right[1] - 1, 0],
                    )
                )
        else:
            moveset = list(movestring)
            animal = moveset[1]
            num = int(moveset[0])

            if self.left[2] == 1:
                if animal == "C":
                    output = State(
                        (
                            [self.left[0] - num, self.left[1], 0],
                            [self.right[0] + num, self.right[1], 1],
                        )
                    )
                else:
                    output = State(
                        (
                            [self.left[0], self.left[1] - num, 0],
                            [self.right[0], self.right[1] + num, 1],
                        )
                    )
            else:
                if animal == "C":
                    output = State(
                        (
                            [self.left[0] + num, self.left[1], 1],
                            [self.right[0] - num, self.right[1], 0],
                        )
                    )
                else:
                    output = State(
                        (
                            [self.left[0], self.left[1] + num, 1],
                            [self.right[0], self.right[1] - num, 0],
                        )
                    )

        if show == "Yes":
            if self.right[2] == 1:
                print(f"{output.left}~->~{output.right}")
            else:
                print(f"{output.left}~<-~{output.right}")

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
            output.append((current_left, current_right))

    return output


if __name__ == "__main__":
    test1_state = State(injest("./start1.txt")[0])
    print(test1_state)
    print(test1_state.move("2W", show="Yes"))

