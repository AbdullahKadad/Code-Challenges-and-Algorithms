class DirectedVertex:
    """
    Class representing a vertex in the directed graph.
    """
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, DirectedVertex) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


class DirectedGraph:
    """
    Class representing a directed graph using an adjacency list.
    """
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, value):
        """
        Adds a new vertex to the graph.

        Args:
            value (str): The value of the vertex.

        Returns:
            DirectedVertex: The newly created vertex.
        """
        new_vertex = DirectedVertex(value)
        if new_vertex not in self.adjacency_list:
            self.adjacency_list[new_vertex] = []
        return new_vertex

    def add_edge(self, vertex1, vertex2):
        """
        Adds a directed edge from vertex1 to vertex2.

        Args:
            vertex1 (DirectedVertex): The starting vertex.
            vertex2 (DirectedVertex): The ending vertex.
        """
        if vertex1 not in self.adjacency_list:
            raise ValueError("Vertex1 does not exist")
        
        if vertex2 not in self.adjacency_list:
            raise ValueError("Vertex2 does not exist")
        
        self.adjacency_list[vertex1].append(vertex2)

    def __str__(self):
        """
        Returns a string representation of the graph.
        """
        return '\n'.join(
            f'{vertex} -> {" ".join(str(adj_vertex) for adj_vertex in adj_vertices)}'
            for vertex, adj_vertices in self.adjacency_list.items()
        )

    def _dfs(self, start_vertex, visited):
        """
        Performs a Depth-First Search (DFS) starting from the given vertex.

        Args:
            start_vertex (DirectedVertex): The starting vertex.
            visited (set): The set of visited vertices.
        """
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.adjacency_list.get(vertex, []):
                    if neighbor not in visited:
                        stack.append(neighbor)

    def _reverse_graph(self):
        """
        Reverses the direction of edges in the graph.
        """
        reversed_graph = DirectedGraph()
        for vertex in self.adjacency_list:
            reversed_graph.add_vertex(vertex.value)
        
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                reversed_graph.add_edge(neighbor, vertex)
        
        return reversed_graph

    def is_strongly_connected(self):
        """
        Checks if the directed graph is strongly connected.

        Returns:
            str: 'Strongly connected' or 'Not strongly connected'.
        """
        if not self.adjacency_list:
            return 'Not strongly connected'

        # Start with an arbitrary vertex
        start_vertex = next(iter(self.adjacency_list))
        
        # Step 1: Perform DFS from the starting vertex
        visited = set()
        self._dfs(start_vertex, visited)

        # If all vertices are not reachable, the graph is not strongly connected
        if len(visited) != len(self.adjacency_list):
            return 'Not strongly connected'
        
        # Step 2: Reverse the graph
        reversed_graph = self._reverse_graph()
        
        # Step 3: Perform DFS from the same starting vertex in the reversed graph
        visited_reversed = set()
        reversed_graph._dfs(start_vertex, visited_reversed)

        # If all vertices are not reachable in the reversed graph, it's not strongly connected
        if len(visited_reversed) != len(reversed_graph.adjacency_list):
            return 'Not strongly connected'
        
        return 'Strongly connected'


# Example usage:

# Example 1
numbers1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,4],[1,7],[7,3]]
graph1 = DirectedGraph()
vertex_map1 = {num: graph1.add_vertex(str(num)) for pair in numbers1 for num in pair}
for v1, v2 in numbers1:
    graph1.add_edge(vertex_map1[v1], vertex_map1[v2])

print(graph1.is_strongly_connected())  # Output: Not strongly connected

# Example 2
numbers2 = [[1,2],[1,0],[0,4],[4,3],[3,2],[3,1],[2,1],[2,4]]
graph2 = DirectedGraph()
vertex_map2 = {num: graph2.add_vertex(str(num)) for pair in numbers2 for num in pair}
for v1, v2 in numbers2:
    graph2.add_edge(vertex_map2[v1], vertex_map2[v2])

print(graph2.is_strongly_connected())  # Output: Strongly connected
