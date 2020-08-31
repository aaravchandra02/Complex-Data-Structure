from vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.graph_dict = {}
        self.directed = directed

    def add_vertex(self, vertex):
        print(f"Adding vertex.value")
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        print(f"Adding edge from {from_vertex.value} to {to_vertex.value}")
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        # if the graph is not directed
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(
                from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        print(f"Searching from {start_vertex} to {end_vertex}")
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            # removing each element else the loop won't end
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print(f"Visiting {current_vertex}\n")
            if current_vertex == end_vertex:
                return True
            else:
                vertices_to_visit = set(
                    self.graph_dict[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]
        return False


grand_central = Vertex("Grand Central Station")

railway = Graph()
print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)
