from union_find import UnionFind
import random

class PercolationSimulation:
    def __init__(self, N = 100, p = 0.4):

        self.graph = UnionFind(N * N + 2)
        self.N = N
        self.p = p

        self.blocked = False

        # Indices of virtual nodes
        self.top_element = N * N
        self.bottom_element = N * N + 1

        self.matrix = self.new_matrix()

        # Connect top element
        for i in range(N):
            self.graph.union(self.top_element, i)

        # Connect bottom element
        for i in range(N):
            self.graph.union(self.bottom_element, N * N - 1 - i)

    def new_matrix(self):
        matrix = []
        for i in range(self.N):
            row = [self.blocked] * self.N
            matrix.append(row)
        return matrix

    def element(self, i, j):
        return i * self.N + j

    def run(self):
        # Go through each element in the matrix and turn on/off each block at probability `p`
        for i in range(self.N):
            for j in range(self.N):
                empty = random.random() < self.p
                self.matrix[i][j] = empty
                if empty:
                    if i+1 < self.N and self.matrix[i+1][j]: self.graph.union(self.element(i,j), self.element(i+1, j))
                    if i-1 >= 0 and self.matrix[i-1][j]:     self.graph.union(self.element(i,j), self.element(i-1, j))
                    if j+1 < self.N and self.matrix[i][j+1]: self.graph.union(self.element(i,j), self.element(i, j+1))
                    if j-1 >= 0 and self.matrix[i][j-1]:     self.graph.union(self.element(i,j), self.element(i, j-1))

        return self.percolates()

    def percolates(self):
        return self.graph.connected(self.top_element, self.bottom_element)



if __name__ == "__main__":
    scale = 10
    probabilities = range(int(0.5 * scale), int(0.7 * scale), 1)
    N = 1000

    for p in probabilities:
        p =  p / scale
        n_samples = 10
        n_samples_percolate = 0

        for i in range(n_samples):
            ps = PercolationSimulation(N = N, p = p)
            n_samples_percolate += ps.run()

        r = n_samples_percolate / n_samples
        print ('Probability: {}, Percolation Rate: {}'.format(p, r))