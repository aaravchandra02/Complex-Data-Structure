class Vertex:
    # stores some data and a dictionary of edges
    def __init__(self, value):
        self.value = value
        self.edges = {}

    # adds egde and also a weight as a default parameter
    def add_edge(self, vertex, weight=0):
        print(f"Adding edge to {vertex}")
        print(f"Adding edge to {vertex}")
        self.value = vertex
        self.edges[vertex] = weight

    # define .add_edge() here
    def add_edges(self, vertex):

        self.value = vertex

    # function to return the vertices
    def get_edges(self):
        return list(self.edges.keys())


station = Vertex("Cronk")
grand_central = Vertex('Grand Central Station')
forty_second_street = Vertex('42nd Street Station')

print(grand_central.get_edges())

grand_central.add_edge(forty_second_street.value)

print(grand_central.get_edges())
