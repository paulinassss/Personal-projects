# Implementing directed graph using dictionary where key is a vertex,
# and value - neighbourhood list of this vertex
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex in self.graph:
            self.graph[start_vertex].append(end_vertex)

    # Funkcja odwracajaca graf
    def reverse_graph(self):
        reversed_graph = Graph()
        # Add all vertexes to the reversed graph
        for vertex in self.graph:
            reversed_graph.add_vertex(vertex)
        # Reverse the direction of the edges
        for start_vertex in self.graph:
            for end_vertex in self.graph[start_vertex]:
                reversed_graph.add_edge(end_vertex, start_vertex)
        return reversed_graph

    def print_graph(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])