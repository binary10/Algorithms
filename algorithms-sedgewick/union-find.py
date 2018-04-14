import random

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))    # Initialize an array with N elements
        self.size = [1] * n
        self.count = n             # Total number of connected components


    def root(self, element):
        root = element
        while(root != self.parent[root]): root = self.parent[root]    # Find the root

        while (self.parent[element] != element):
            old_root = self.parent[element]
            self.parent[element] = root
            element = old_root

        return root


    def union(self, p, q):
        # The root of p needs to change to be equal to the root of q
        root_p = self.root(p)
        root_q = self.root(q)
        if root_p == root_q: return

        size_p = self.size[root_p]
        size_q = self.size[root_q]

        if size_p > size_q:
            self.parent[root_q] = root_p
            self.size[root_p] += size_q
        else:   # sizes are equal or q > p
            self.parent[root_p] = root_q
            self.size[root_q] += size_p

        self.count -= 1


    def connected(self, p, q):
        return self.root(p) == self.root(q)


# Test
if __name__ == "__main__":
    size = 1000000

    u = UnionFind(size)

    # Create connections between elements
    for i in range(size):
        p, q = random.randint(0, size - 1), random.randint(0, size - 1)
        u.union(p, q)

    # Sample some connections and test for connectivity
    for i in range(100):
        p, q = random.randint(0, size - 1), random.randint(0, size - 1)
        print('Connected:', p,q, u.connected(p, q))

    # How many connected components are there?
    print(u.count)
