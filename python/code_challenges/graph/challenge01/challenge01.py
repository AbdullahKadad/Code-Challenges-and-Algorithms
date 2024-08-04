class Vertex:
    """
    Class representing a vertex in the graph.
    """
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return self.value


class Graph:
    """
    Class representing an undirected graph using an adjacency list.
    """
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, value):
        """
        Adds a new vertex to the graph.

        Args:
            value (str): The value of the vertex.

        Returns:
            Vertex: The newly created vertex.
        """
        new_vertex = Vertex(value)
        self.adjacency_list[new_vertex] = []
        return new_vertex

    def add_edge(self, vertex1, vertex2):
        """
        Adds an undirected edge between two vertices.

        Args:
            vertex1 (Vertex): The first vertex.
            vertex2 (Vertex): The second vertex.
        """
        if vertex1 not in self.adjacency_list:
            return "Vertex1 does not exist"
        
        if vertex2 not in self.adjacency_list:
            return "Vertex2 does not exist"
        
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def __str__(self):
        """
        Returns a string representation of the graph.
        """
        return '\n'.join(
            f'{vertex} -> {" ".join(str(adj_vertex) for adj_vertex in adj_vertices)}'
            for vertex, adj_vertices in self.adjacency_list.items()
        )

    def breadth_first_search(self, start_value):
        """
        Performs a breadth-first search (BFS) starting from the vertex with the given value.

        Args:
            start_value (str): The value of the starting vertex.

        Returns:
            list: List of values of the visited vertices.
        """
        start_vertex = None
        for vertex in self.adjacency_list.keys():
            if vertex.value == start_value:
                start_vertex = vertex
                break

        if not start_vertex:
            return []

        visited = set()
        queue = [start_vertex]
        bfs_result = []

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                visited.add(current_vertex)
                bfs_result.append(current_vertex.value)
                for neighbor in self.adjacency_list[current_vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return bfs_result



# Create a new graph
graph = Graph()

# Add vertices
v1 = graph.add_vertex("A")
v2 = graph.add_vertex("B")
v3 = graph.add_vertex("C")
v4 = graph.add_vertex("D")
v5 = graph.add_vertex("E")
v6 = graph.add_vertex("F")
v7 = graph.add_vertex("G")
v8 = graph.add_vertex("H")
v9 = graph.add_vertex("I")
v10 = graph.add_vertex("K")

# Add edges
graph.add_edge(v1, v2)
graph.add_edge(v1, v3)
graph.add_edge(v2, v4)
graph.add_edge(v3, v5)
graph.add_edge(v4, v6)
graph.add_edge(v5, v7)
graph.add_edge(v6, v8)
graph.add_edge(v7, v9)
graph.add_edge(v8, v10)

# Print the graph
print(graph)

# Perform BFS starting from vertex "A"
bfs_result = graph.breadth_first_search("A")
print(bfs_result)
