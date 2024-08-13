import pytest
from challenge03 import DirectedGraph  # Replace with the actual import path

@pytest.fixture
def empty_graph():
    """Fixture for an empty graph."""
    return DirectedGraph()

@pytest.fixture
def single_vertex_graph():
    """Fixture for a graph with a single vertex."""
    g = DirectedGraph()
    g.add_vertex("1")
    return g

@pytest.fixture
def disconnected_graph():
    """Fixture for a graph with multiple disconnected components."""
    g = DirectedGraph()
    # Component 1
    v1 = g.add_vertex("1")
    v2 = g.add_vertex("2")
    g.add_edge(v1, v2)
    
    # Component 2
    v3 = g.add_vertex("3")
    v4 = g.add_vertex("4")
    g.add_edge(v3, v4)
    
    return g

@pytest.fixture
def graph_with_self_loops():
    """Fixture for a graph with self-loops."""
    g = DirectedGraph()
    v1 = g.add_vertex("1")
    v2 = g.add_vertex("2")
    v3 = g.add_vertex("3")
    
    g.add_edge(v1, v1)  # Self-loop
    g.add_edge(v2, v2)  # Self-loop
    g.add_edge(v1, v2)
    g.add_edge(v2, v3)
    g.add_edge(v3, v1)
    
    return g

@pytest.fixture
def complete_graph():
    """Fixture for a complete graph where every vertex is connected to every other vertex."""
    g = DirectedGraph()
    vertices = [g.add_vertex(str(i)) for i in range(3)]
    
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i != j:
                g.add_edge(vertices[i], vertices[j])
    
    return g

@pytest.fixture
def complex_strongly_connected_graph():
    """Fixture for a complex strongly connected graph."""
    g = DirectedGraph()
    vertex_map = {num: g.add_vertex(str(num)) for num in range(6)}
    edges = [
        (0, 1), (1, 2), (2, 0),
        (1, 3), (3, 4), (4, 1),
        (4, 5), (5, 3)
    ]
    for v1, v2 in edges:
        g.add_edge(vertex_map[v1], vertex_map[v2])
    
    return g

def test_empty_graph(empty_graph):
    assert empty_graph.is_strongly_connected() == "Not strongly connected"

def test_single_vertex_graph(single_vertex_graph):
    assert single_vertex_graph.is_strongly_connected() == "Strongly connected"

def test_disconnected_graph(disconnected_graph):
    assert disconnected_graph.is_strongly_connected() == "Not strongly connected"

def test_graph_with_self_loops(graph_with_self_loops):
    assert graph_with_self_loops.is_strongly_connected() == "Strongly connected"

def test_complete_graph(complete_graph):
    assert complete_graph.is_strongly_connected() == "Strongly connected"

def test_complex_strongly_connected_graph(complex_strongly_connected_graph):
    assert complex_strongly_connected_graph.is_strongly_connected() == "Strongly connected"
