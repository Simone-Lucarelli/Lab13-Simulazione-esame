from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.selected_year = None
        self.selected_shape = None
        self.graph = nx.Graph()

    def get_years(self):
        return DAO.get_years()

    def get_shapes(self, year):
        return DAO.get_shapes(year)

    def build_graph(self):
        print("build graph called")
        if self.selected_year is not None and self.selected_shape is not None:
            connections = DAO.get_connections(self.selected_year, self.selected_shape)
            for c in connections:
                self.graph.add_edge(c.state1, c.state2, weight=c.weight)
            print(f"Graph has {self.graph.number_of_nodes()} nodes and "
                  f"{self.graph.number_of_edges()} edges")
        else:
            print("build graph failed")


    def print_graph(self):
        print(f"Graph has {self.graph.number_of_nodes()} nodes and {self.graph.number_of_edges()} edges")
        result = []
        for node in self.graph.nodes:
            neighbors = []
            for n in self.graph.neighbors(node):
                neighbors.append(str(n))
            result.append((str(node), len(neighbors)))
        result.sort(key=lambda x: x[0])
        for row in result:
            print(row)
