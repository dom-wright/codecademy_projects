class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, adjacent_value, weight=0):
        self.edges[adjacent_value] = weight

    def get_edges(self):
        return self.edges.keys()


class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, node):
        self.graph_dict[node.value] = node

    def add_edge(self, from_node, to_node, weight=0):
        self.graph_dict[from_node.value].add_edge(to_node.value, weight)
        self.graph_dict[to_node.value].add_edge(from_node.value, weight)

    def explore(self):
        print("Exploring the graph....\n")
        current_room = 'entrance'
        path_total = 0
        print(f"\nStarting off at the {current_room}\n")

        while current_room != 'treasure room':
            # list next room options
            node = self.graph_dict[current_room]
            for connected_room, weight in node.edges.items():
                key = connected_room[0]
                print(f"Enter '{key}' for {connected_room}: {weight} cost")

            # get the user's choice of next room to explore
            valid_choices = [room[0] for room in node.get_edges()]
            print(f"\nYou have accumulated: {path_total} cost")
            choice = input("\nWhich room do you move to? ")

            # check choice is valid
            if choice not in valid_choices:
                print(
                    f"Invalid choice. Please select from these letters: {valid_choices}")
            else:
                # move to new room
                for room in node.get_edges():
                    if room.startswith(choice):
                        current_room = room
                        path_total += node.edges[room]
                print(f"\n*** You have chosen: {current_room} ***\n")
        print(f"Made it to the treasure room with {path_total} cost")

    def print_map(self):
        print("\nMAZE LAYOUT\n")
        for node_key in self.graph_dict:
            print(f"{node_key} connected to...")
            node = self.graph_dict[node_key]
            for adjacent_node, weight in node.edges.items():
                print(f"=> {adjacent_node}: cost is {weight}")
            print("")
        print("")


def build_graph():
    # create graph
    graph = Graph()

    # create vertices and add to graph
    entrance = Vertex('entrance')
    graph.add_vertex(entrance)

    ante_chamber = Vertex('ante_chamber')
    graph.add_vertex(ante_chamber)

    kings_room = Vertex("king's room")
    graph.add_vertex(kings_room)

    grand_gallery = Vertex("grand gallery")
    graph.add_vertex(grand_gallery)

    treasure_room = Vertex("treasure room")
    graph.add_vertex(treasure_room)

    # add edges
    graph.add_edge(entrance, ante_chamber, 7)
    graph.add_edge(entrance, kings_room, 3)
    graph.add_edge(ante_chamber, kings_room, 1)
    graph.add_edge(grand_gallery, ante_chamber, 2)
    graph.add_edge(grand_gallery, kings_room, 2)
    graph.add_edge(treasure_room, ante_chamber, 6)
    graph.add_edge(treasure_room, grand_gallery, 4)

    graph.print_map()
    return graph
