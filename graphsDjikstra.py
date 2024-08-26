class Graph:
    def __init__(self, edges):
        self.edges = edges
        # Converting tuple graph into better dictionary graph (from graph1 to graph2)
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict:", self.graph_dict)

    def get_paths(self, start, end): #Shows all possible paths.
        pass


graph1 = [
    ("London", "Paris"),
    ("London", "New York"),
    ("Paris", "London"),
    ("Paris", "New York")
] #This is a graph made using a list of tuples representing edges.

graph1 = Graph(graph1)

# A better implementation of graphs would be this:
graph2 = {
    "London": ["Paris", "New York"], # London has routes to Paris and Dublin
    "Paris": ["London", "New York"],
} # This graph is made up of a set of dictionary items with a list in them.

# We can convert the first implementation of the graph into the second one.
# See added code in graph class.