class Vertex:
    # stores some data and a dictionary of edges
    def __init__(self, value):
        self.value = value
        self.edges = {}

    # adds egde and also a weight as a default parameter
    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    # function to return the vertices
    def get_edges(self):
        return list(self.edges.keys())


station = Vertex("Cronk")
