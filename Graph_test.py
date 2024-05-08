import unittest
import sys
from io import StringIO
from math import isclose
from Graph import Graph, Node


class TestGraph(unittest.TestCase):

    def test_init_empty_graph(self):
        graph = Graph()
        self.assertEqual(graph.nodes, [], "Graph should initially be empty")

    def test_find_existing_node(self):
        graph = Graph()
        node1 = Node("A")
        graph.nodes.append(node1)

        found_node = graph.find("A")
        self.assertEqual(found_node, node1, "Should find existing node")

    def test_find_create_new_node(self):
        graph = Graph()

        new_node = graph.find("B")
        self.assertEqual(len(graph.nodes), 1, "Should create new node")
        self.assertEqual(new_node.name, "B", "New node should have correct name")

    def test_add_edge(self):
        graph = Graph()
        node1 = graph.find("A")
        node2 = graph.find("B")

        graph.add_edge("A", "B")

        self.assertIn(node2, node1.children, "Node A should have B as a child")
        self.assertIn(node1, node2.parents, "Node B should have A as a parent")

    def test_normalize_pagerank(self):
        graph = Graph()
        node1 = graph.find("A")
        node2 = graph.find("B")
        node3 = graph.find("C")
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")

        node1.pagerank = 2.0
        node2.pagerank = 1.0
        node3.pagerank = 3.0

        graph.normalize_pagerank()

        self.assertAlmostEqual(
            node1.pagerank,
            2.0 / 6.0,
            places=6,
            msg="PageRank values should be normalized",
        )
        self.assertAlmostEqual(
            node2.pagerank,
            1.0 / 6.0,
            places=6,
            msg="PageRank values should be normalized",
        )
        self.assertAlmostEqual(
            node3.pagerank,
            3.0 / 6.0,
            places=6,
            msg="PageRank values should be normalized",
        )

    def test_get_auth_hub_list(self):
        graph = Graph()
        node1 = graph.find("A")
        node2 = graph.find("B")
        node3 = graph.find("C")

        node1.auth = 2.0
        node2.auth = 1.0
        node3.auth = 3.0

        node1.hub = 0.5
        node2.hub = 1.0
        node3.hub = 1.5

        auth_list, hub_list = graph.get_auth_hub_list()

        self.assertListEqual(list(auth_list), [2.0, 1.0, 3.0], "Auth list should match")
        self.assertListEqual(list(hub_list), [0.5, 1.0, 1.5], "Hub list should match")

    def test_get_pagerank_list(self):
        graph = Graph()
        node1 = graph.find("A")
        node2 = graph.find("B")
        node3 = graph.find("C")

        node1.pagerank = 2.0
        node2.pagerank = 1.0
        node3.pagerank = 3.0

        pagerank_list = graph.get_pagerank_list()

        self.assertListEqual(
            list(pagerank_list), [2.0, 1.0, 3.0], "PageRank list should match"
        )


if __name__ == "__main__":
    unittest.main()
