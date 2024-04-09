class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node.data
            curr_node = curr_node.next


class GraphAdjacencyList:
    def __init__(self, v: int):
        self.v: int = v
        self.e: int = 0
        self._adj: list[LinkedList] = [LinkedList() for _ in range(v)]

    def add_edge(self, v: int, w: int):
        if 0 <= v < self.v and 0 <= w < self.v:
            self._adj[v].append(w)
            self.e += 1

    def V(self):
        return self.v

    def E(self):
        return self.e

    def adj(self, v: int) -> list[int]:
        return list(self._adj[v])

    @classmethod
    def from_adj_matrix(cls, graph: "GraphAdjacencyMatrix"):
        v = graph.V()
        adj_list = cls(v)

        for v in range(v):
            for w in graph.adj(v):
                adj_list.add_edge(v, w)

        return adj_list


class GraphAdjacencyMatrix:
    def __init__(self, v: int):
        self.v: int = v
        self.e: int = 0
        self._adj_matrix: list[list[int]] = [[0] * v for _ in range(v)]

    def add_edge(self, v: int, w: int):
        if 0 <= v < self.v and 0 <= w < self.v:
            self._adj_matrix[v][w] = 1
            self.e += 1

    def V(self):
        return self.v

    def E(self):
        return self.e

    def adj(self, v: int) -> list[int]:
        return [i for i, val in enumerate(self._adj_matrix[v]) if val == 1]

    @classmethod
    def from_adj_list(cls, graph: GraphAdjacencyList):
        v = graph.V()
        adj_list = cls(v)

        for v in range(v):
            for w in graph.adj(v):
                adj_list.add_edge(v, w)

        return adj_list


def main():
    # testing adjacency list
    print("testing adjacency list")
    graph0 = GraphAdjacencyList(v=5)

    graph0.add_edge(0, 1)
    graph0.add_edge(0, 4)
    graph0.add_edge(1, 2)
    graph0.add_edge(1, 3)
    graph0.add_edge(2, 3)
    graph0.add_edge(3, 4)
    graph0.add_edge(4, 3)
    graph0.add_edge(4, 1)

    print(f"Number of vertices: {graph0.V()}")
    print(f"Number of edges: {graph0.E()}")
    
    for v in range(graph0.V()):
        print(f"Adjacent vertices of {v}: {graph0.adj(v)}")

    # testing adjacency matrix
    print("testing adjacency matrix")

    graph1 = GraphAdjacencyMatrix(v=5)
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 4)
    graph1.add_edge(1, 2)
    graph1.add_edge(1, 3)
    graph1.add_edge(2, 3)
    graph1.add_edge(3, 4)
    graph1.add_edge(4, 3)
    graph1.add_edge(4, 1)

    print(f"Number of vertices: {graph1.V()}")
    print(f"Number of edges: {graph1.E()}")

    for v in range(graph1.V()):
        print(f"Adjacent vertices of {v}: {graph1.adj(v)}")

    # testing adj list 2 adj matrix
    print("testing adj list 2 adj matrix")
    graph2 = GraphAdjacencyMatrix.from_adj_list(graph0)

    print(f"Number of vertices: {graph2.V()}")
    print(f"Number of edges: {graph2.E()}")

    for v in range(graph2.V()):
        print(f"Adjacent vertices of {v}: {graph2.adj(v)}")

    # testing adj matrix 2 adj list
    print("testing adj matrix 2 adj list")
    graph3 = GraphAdjacencyList.from_adj_matrix(graph1)

    print(f"Number of vertices: {graph3.V()}")
    print(f"Number of edges: {graph3.E()}")

    for v in range(graph3.V()):
        print(f"Adjacent vertices of {v}: {graph3.adj(v)}")


main() if __name__ == "__main__" else None
