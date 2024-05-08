from Graph import Graph


def init_graph(fname):
    with open(fname) as f:
        lines = f.readlines()

    graph = Graph()
    # print(type(graph))

    for line in lines:
        [parent, child] = line.strip().split(",")
        graph.add_edge(parent, child)

    graph.sort_nodes()

    return graph


def HITS_one_iter(graph):
    node_list = graph.nodes

    for node in node_list:
        node.update_auth()

    for node in node_list:
        node.update_hub()

    graph.normalize_auth_hub()


def HITS(graph, iteration=100):
    for i in range(iteration):
        HITS_one_iter(graph)


if __name__ == "__main__":

    iteration = 100
    # change the file path here
    graph = init_graph("graph_4.txt")
    HITS(graph, iteration)
    auth_list, hub_list = graph.get_auth_hub_list()
    print(auth_list)
    print(hub_list)
