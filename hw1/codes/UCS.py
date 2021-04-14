import queue as Q


class UCS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.put((root.step, root, int(root.UID)))

    def run(self, target):
        """ YOUR CODE HERE """
        while self.queue:
            node = self.queue.get()
            self.counter += 1
            if (node[1]).is_equal(target):
                self.counter += 1
                return True, self.counter, node[0]
            for neighbor in self.graph.reveal_neighbors(node[1]):
                if neighbor.UID not in self.visited:
                    self.visited[neighbor.UID] = 1
                    neighbor.distance = node[0] + 1
                    self.queue.put((neighbor.distance, neighbor, int(neighbor.UID)))

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0