import unittest
from hits import init_graph, HITS, HITS_one_iter


class TestHITS(unittest.TestCase):

    def test_init_graph(self):
        graph = init_graph("graph_4.txt")
        self.assertIsNotNone(graph, "Graph initialization should succeed")

    def test_HITS_one_iter(self):
        graph = init_graph("graph_4.txt")
        HITS_one_iter(graph)
        auth_list, hub_list = graph.get_auth_hub_list()
        self.assertIsNotNone(auth_list, "Auth list should be generated")
        self.assertIsNotNone(hub_list, "Hub list should be generated")

    def test_HITS(self):
        graph = init_graph("graph_4.txt")
        HITS(graph)
        auth_list, hub_list = graph.get_auth_hub_list()
        self.assertIsNotNone(auth_list, "Auth list should be generated")
        self.assertIsNotNone(hub_list, "Hub list should be generated")


if __name__ == "__main__":
    unittest.main()
