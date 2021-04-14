class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """

        while self.stack:
            node = self.stack.pop()
            for neighbor in self.graph.reveal_neighbors(node):
                self.visited[node.UID] = node.UID
                if neighbor.is_equal(target):
                    self.counter += 1
                    return True, self.counter, neighbor.step
                if neighbor.UID not in self.visited:
                    self.visited[node.UID] = neighbor.UID
                    self.stack.append(neighbor)
                    self.counter += 1


        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0