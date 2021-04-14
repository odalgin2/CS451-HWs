import queue as Q


class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        self.queue.put((self.root.step, self.root, int(self.root.UID)))
        while self.queue is not None:
            node = self.queue.get()
            self.counter += 1
            if node[1].is_equal(target):
                self.counter += 1
                return True, self.counter, node[1].distance_top
            for neighbor in self.graph.reveal_neighbors(node[1]):
                if neighbor.UID not in self.visited:
                    neighbor.distance_top = node[1].distance_top + 1
                    self.visited[neighbor.UID] = 1
                    neighbor.step = self.manhattan_distance(neighbor, target)
                    self.queue.put((neighbor.step, neighbor, int(neighbor.UID)))

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def manhattan_distance(self, node, end):
        arr = [0] * (self.graph.size + 1)
        brr = [0] * (self.graph.size + 1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist
