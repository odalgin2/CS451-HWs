class BFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = list()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.append(root)

    def run(self, target):
        """ YOUR CODE HERE """
        while self.queue is not None:
            node = self.queue.pop(0)
            for neighbor in self.graph.reveal_neighbors(node):
                if neighbor.UID not in self.visited:
                    self.queue.append(neighbor)
                    self.visited[neighbor.UID] = node.UID
                    self.counter += 1
            if neighbor.is_equal(target):
                self.counter += 1
                return True, self.counter, neighbor.step

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0


