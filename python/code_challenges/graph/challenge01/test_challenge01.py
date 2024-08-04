import pytest
from challenge01 import Graph, Vertex  

@pytest.fixture
def setup_graph():
    """
    Fixture to set up a sample graph with two disconnected components and one single vertex.
    
    Returns:
        tuple: A tuple containing:
            - Graph instance
            - Vertex objects for group 1 (A, B, C, D)
            - Vertex objects for group 2 (E, F, G)
            - Vertex object with no neighbors (H)
    """
    graph = Graph()
    
    # Group 1
    v1 = graph.add_vertex("A")
    v2 = graph.add_vertex("B")
    v3 = graph.add_vertex("C")
    v4 = graph.add_vertex("D")
    
    graph.add_edge(v1, v2)
    graph.add_edge(v2, v3)
    graph.add_edge(v3, v4)
    
    # Group 2 (Disconnected from Group 1)
    v5 = graph.add_vertex("E")
    v6 = graph.add_vertex("F")
    v7 = graph.add_vertex("G")
    
    graph.add_edge(v5, v6)
    graph.add_edge(v6, v7)
    
    # Single vertex with no neighbors
    v8 = graph.add_vertex("H")
    
    return graph, v1, v2, v3, v4, v5, v6, v7, v8

def test_bfs_existing_vertex(setup_graph):
    """
    Test BFS traversal starting from an existing vertex.
    
    Args:
        setup_graph (tuple): Contains the graph and vertices setup.
    """
    graph, v1, _, _, _, _, _, _, _ = setup_graph
    assert graph.breadth_first_search("A") == ["A", "B", "C", "D"]

def test_bfs_non_existing_vertex(setup_graph):
    """
    Test BFS traversal starting from a vertex that does not exist in the graph.
    
    Args:
        setup_graph (tuple): Contains the graph and vertices setup.
    """
    graph, _, _, _, _, _, _, _, _ = setup_graph
    assert graph.breadth_first_search("X") == []

def test_bfs_disconnected_graph(setup_graph):
    """
    Test BFS traversal starting from a vertex in a disconnected group of vertices.
    
    Args:
        setup_graph (tuple): Contains the graph and vertices setup.
    """
    graph, _, _, _, _, v5, v6, v7, _ = setup_graph
    assert graph.breadth_first_search("E") == ["E", "F", "G"]

def test_bfs_single_vertex(setup_graph):
    """
    Test BFS traversal starting from a single vertex with no neighbors.
    
    Args:
        setup_graph (tuple): Contains the graph and vertices setup.
    """
    graph, _, _, _, _, _, _, _, v8 = setup_graph
    assert graph.breadth_first_search("H") == ["H"]

def test_bfs_vertex_with_no_neighbors(setup_graph):
    """
    Test BFS traversal starting from a vertex that has no neighbors.
    
    Args:
        setup_graph (tuple): Contains the graph and vertices setup.
    """
    graph, _, _, _, _, _, _, _, v8 = setup_graph
    assert graph.breadth_first_search("H") == ["H"]
