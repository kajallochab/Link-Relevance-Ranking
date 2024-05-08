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


def PageRank_one_iter(graph, d):
    node_list = graph.nodes
    for node in node_list:
        node.update_pagerank(d, len(graph.nodes))
    graph.normalize_pagerank()
    print(graph.get_pagerank_list())
    print()


def PageRank(graph, d, iteration=10):
    for i in range(iteration):
        PageRank_one_iter(graph, d)


if __name__ == "__main__":

    iteration = 5
    damping_factor = 0.15
    # change file path
    graph = init_graph("graph_4.txt")

    PageRank(graph, damping_factor, iteration)
    print(graph.get_pagerank_list())
