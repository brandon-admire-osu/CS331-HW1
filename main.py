from classes_and_functions import *

possible_moves = ["1C", "1W", "2C", "2W", "1C1W"]


def treeSearch(initial_state, goal, pop_order, depth_limit=None):
    current_depth = 0
    nodes_expanded = 0
    if initial_state == goal:
        return True, nodes_expanded
    else:
        frontier = [initial_state]
        explored = []
        while 1:
            if len(frontier) >= 1:
                current = frontier.pop(pop_order)  # Pop specified item off frontier
                if current == goal:
                    output = []
                    while current.parent != initial_state:
                        output.append(current)
                        current = current.parent
                    output.append(initial_state)
                    output.reverse()
                    for out in output:
                        print(out)
                    return True, nodes_expanded
                else:
                    nodes_expanded += 1
                    candidates = current.expand()
                    explored.append(current)
                    for state in candidates:
                        # print(state, bool(state))
                        if state:  # Check if valid
                            if state not in explored:
                                if state not in frontier:
                                    if depth_limit is not None:
                                        if state.depth > depth_limit:
                                            frontier.append(state)
                                    else:
                                        frontier.append(state)
            else:
                if depth_limit is not None:
                    return False, nodes_expanded
                else:
                    return -1


# Breadth-First Search
def breadthFirst(initial_state, goal):
    # FIFO
    return treeSearch(initial_state, goal, 0)


# Depth-First Search
def depthFirst(initial_state, goal, depth_limit=None):
    # LIFO
    return treeSearch(initial_state, goal, -1, depth_limit)


# Iterative-Deepening Depth First Search
def deepDepthFirst(initial_state, goal):
    depth_count = 0
    counter = 0
    while 1:
        result, count = depthFirst(initial_state, goal, depth_limit=depth_count)
        counter += count
        if result == True:
            return counter
        depth_count += 1


# A Star Search
def aStar(initial_state, goal):
    pass


if __name__ == "__main__":
    initial_state = State(injest("./goalsAndStates/tests/start1.txt"))
    goal = State(injest("./goalsAndStates/goals/goal1.txt"))
    print(
        f"Number of nodes expanded for depth first: {depthFirst(initial_state, goal)}"
    )
    print(
        f"Number of nodes expanded for breadth first: {breadthFirst(initial_state, goal)}"
    )
    print(
        f"Number of nodes expanded for deep depth first: {deepDepthFirst(initial_state, goal)}"
    )

