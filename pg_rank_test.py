import unittest
from pg_rank import init_graph, PageRank, PageRank_one_iter


class TestPageRank(unittest.TestCase):

    def test_init_graph(self):
        # change file path
        graph = init_graph("graph_4.txt")
        self.assertIsNotNone(graph, "Graph initialization should succeed")

    def test_PageRank_one_iter(self):
        graph = init_graph("graph_4.txt")
        PageRank_one_iter(graph, 0.15)
        pagerank_list = graph.get_pagerank_list()
        self.assertIsNotNone(pagerank_list, "PageRank list should be generated")

    def test_PageRank(self):
        graph = init_graph("graph_4.txt")
        PageRank(graph, 0.15, 5)
        pagerank_list = graph.get_pagerank_list()
        self.assertIsNotNone(pagerank_list, "PageRank list should be generated")


if __name__ == "__main__":
    unittest.main()
