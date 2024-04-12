import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(start, goal, neighbors, heuristic):
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor in neighbors(current_node.state):
            if neighbor in closed_set:
                continue

            neighbor_node = Node(
                neighbor,
                current_node,
                current_node.cost + 1,
                heuristic(neighbor, goal)
            )

            if neighbor_node not in open_list:
                heapq.heappush(open_list, neighbor_node)

    return None

def neighbors(state):
    x, y = state
    possible_neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [(x, y) for x, y in possible_neighbors if 0 <= x < 10 and 0 <= y < 10]

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

start = (0, 0)
goal = (9, 9)

path = astar(start, goal, neighbors, manhattan_distance)
if path:
    print("Path found:", path)
else:
    print("No path found")
