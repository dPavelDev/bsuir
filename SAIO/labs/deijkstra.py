class Deijkstra(object):
    INF = 100000000

    def __init__(self, vertecies_count, edges):
        self.vertecies_count = vertecies_count
        self.graph = [[] for i in xrange(vertecies_count)]
        self.distances = [[] for i in xrange(vertecies_count)]
        for x, y, d in edges:
            self.graph[x - 1].append(y - 1)
            self.distances[x - 1].append(d)
            self.graph[y - 1].append(x - 1)
            self.distances[y - 1].append(d)

    def solve(self, start_vertex):
        d = [self.INF for i in xrange(self.vertecies_count)]
        visited = [False for i in xrange(self.vertecies_count)]
        d[start_vertex - 1] = 0
        for i in xrange(self.vertecies_count):
            min = self.INF
            index = -1
            for j in xrange(self.vertecies_count):
                if d[j] < min and not visited[j]:
                    min = d[j]
                    index = j
            visited[index] = True
            for j in xrange(len(self.distances[index])):
                if d[index] + self.distances[index][j] < d[self.graph[index][j]]:
                    d[self.graph[index][j]] = d[index] + self.distances[index][j]

        return d


if __name__ == "__main__":
    n = 4
    input = [
        [1, 2, 3],
        [2, 3, 1],
        [3, 4, 5],
        [1, 4, 6]
    ]

    solver = Deijkstra(n, input)

    print solver.solve(4)
    print solver.solve(1)
