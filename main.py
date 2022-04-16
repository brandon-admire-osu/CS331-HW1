from classes_and_functions import *

possible_moves = ["1C", "1W", "2C", "2W", "1C1W"]


def treeSearch(initial_state, goal, pop_order, depth_limit=None):
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
    def h(state):
        # Assumes left is always goal bank. If not the case, prof is monster
        num = state.right[0] + state.right[1]
        # Depth is an abstraction of cost by way of moves made
        return state.depth - num

    # States stored as (state,h(n) score)
    priority = [(initial_state, 0)]  # Priority queue
    explored = []
    nodes_expanded = 0
    while 1:
        if len(priority) >= 1:  # Check for no possible path
            priority.sort(key=lambda x: x[1])  # Sort queue by cost
            current = priority.pop(-1)  # Get lowest cost item
            if current[0] == goal:
                output = []
                current = current[0]
                while current.parent != initial_state:
                    output.append(current)
                    current = current.parent
                output.append(initial_state)
                output.reverse()
                for out in output:
                    print(out)
                return nodes_expanded
            else:
                nodes_expanded += 1
                explored.append(current[0])
                cadidates = current[0].expand()
                for state in cadidates:
                    if state:  # Check if valid state
                        if state not in explored:  # Check if explored
                            priority.append(
                                (state, h(state))
                            )  # Add to queue with calculated h(n) value


if __name__ == "__main__":
    import sys

    # < initial state file > < goal state file > < mode > < output file >
    # bfs (for breadth-first search)
    # dfs (for depth-first search)
    # iddfs (for iterative deepening depth-first search)
    # astar (for A-Star search below)

    initial_state = State(injest(sys.argv[1]))
    goal_state = State(injest(sys.argv[2]))

    if sys.argv[3] == "bfs":
        print(f"Number of nodes expanded: {breadthFirst(initial_state,goal_state)[1]}")
        sys.stdout = open(sys.argv[4], "w")
        print(f"Number of nodes expanded: {breadthFirst(initial_state,goal_state)[1]}")
        sys.stdout.close()
    elif sys.argv[3] == "dfs":
        print(f"Number of nodes expanded: {depthFirst(initial_state,goal_state)[1]}")
        sys.stdout = open(sys.argv[4], "w")
        print(f"Number of nodes expanded: {depthFirst(initial_state,goal_state)[1]}")
    elif sys.argv[3] == "iddfs":
        print(f"Number of nodes expanded: {deepDepthFirst(initial_state,goal_state)}")
        sys.stdout = open(sys.argv[4], "w")
        print(f"Number of nodes expanded: {deepDepthFirst(initial_state,goal_state)}")
    elif sys.argv[3] == "astar":
        print(f"Number of nodes expanded: {aStar(initial_state,goal_state)}")
        sys.stdout = open(sys.argv[4], "w")
        print(f"Number of nodes expanded: {aStar(initial_state,goal_state)}")

    # for i in range(1, 4):
    #     initial_state = State(injest(f"{sys.argv[1]}start{i}.txt"))
    #     goal_state = State(injest(f"{sys.argv[2]}goal{i}.txt"))
    #     sys.stdout = open(f"{sys.argv[3]}out{i}bfs.txt", "w")
    #     print(f"Number of nodes expanded: {breadthFirst(initial_state,goal_state)[1]}")
    #     sys.stdout.close()

    #     initial_state = State(injest(f"{sys.argv[1]}start{i}.txt"))
    #     goal_state = State(injest(f"{sys.argv[2]}goal{i}.txt"))
    #     sys.stdout = open(f"{sys.argv[3]}out{i}dfs.txt", "w")
    #     print(f"Number of nodes expanded: {depthFirst(initial_state,goal_state)[1]}")
    #     sys.stdout.close()

    #     initial_state = State(injest(f"{sys.argv[1]}start{i}.txt"))
    #     goal_state = State(injest(f"{sys.argv[2]}goal{i}.txt"))
    #     sys.stdout = open(f"{sys.argv[3]}out{i}iddfs.txt", "w")
    #     print(f"Number of nodes expanded: {deepDepthFirst(initial_state,goal_state)}")
    #     sys.stdout.close()

    #     initial_state = State(injest(f"{sys.argv[1]}start{i}.txt"))
    #     goal_state = State(injest(f"{sys.argv[2]}goal{i}.txt"))
    #     sys.stdout = open(f"{sys.argv[3]}out{i}astar.txt", "w")
    #     print(f"Number of nodes expanded: {aStar(initial_state,goal_state)}")
    #     sys.stdout.close()

