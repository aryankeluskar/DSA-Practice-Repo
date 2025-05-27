import unittest
from typing import Dict, List, Set

class TestInterstellarWaterExpedition(unittest.TestCase):
    def test_basic_valid_path(self):
        # Test a simple valid path with proper water collection order
        graph = {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3],
            3: [2]
        }
        water_types = {0: 'F', 1: 'N', 2: 'S', 3: 'N'}
        start = 0
        end = 3
        # Expected path: 0(F) -> 2(S) -> 3(N)
        # Length should be 2
        self.assertEqual(find_shortest_path(graph, water_types, start, end), 2)

    def test_no_valid_path(self):
        # Test when no valid path exists due to water collection rules
        graph = {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        }
        water_types = {0: 'S', 1: 'N', 2: 'N', 3: 'S'}
        start = 0
        end = 3
        # No fresh water available
        self.assertEqual(find_shortest_path(graph, water_types, start, end), -1)

    def test_consecutive_opposing_transitions(self):
        # Test path with invalid consecutive opposing transitions
        graph = {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
        water_types = {0: 'F', 1: 'S', 2: 'F', 3: 'S'}
        start = 0
        end = 3
        # Path would require F->S->F->S which is invalid
        self.assertEqual(find_shortest_path(graph, water_types, start, end), -1)

    def test_salt_before_fresh(self):
        # Test attempting to collect salt water before fresh water
        graph = {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
        water_types = {0: 'N', 1: 'S', 2: 'F', 3: 'N'}
        start = 0
        end = 3
        # Must collect fresh water before salt water
        self.assertEqual(find_shortest_path(graph, water_types, start, end), -1)

    def test_complex_valid_path(self):
        # Test a more complex graph with multiple possible paths
        graph = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0, 4],
            3: [1, 5],
            4: [1, 2, 5],
            5: [3, 4]
        }
        water_types = {0: 'F', 1: 'N', 2: 'N', 3: 'S', 4: 'N', 5: 'N'}
        start = 0
        end = 5
        # Expected shortest valid path: 0(F) -> 1(N) -> 3(S) -> 5(N)
        # Length should be 3
        self.assertEqual(find_shortest_path(graph, water_types, start, end), 3)

    def test_minimum_water_collection(self):
        # Test path that must include both water types
        graph = {
            0: [1, 2],
            1: [0, 3],
            2: [0, 3],
            3: [1, 2]
        }
        water_types = {0: 'N', 1: 'F', 2: 'S', 3: 'N'}
        start = 0
        end = 3
        # Must collect both F and S water
        self.assertEqual(find_shortest_path(graph, water_types, start, end), 3)

    def test_large_graph(self):
        # Test with a larger graph to verify performance
        graph = {i: [] for i in range(10)}
        for i in range(9):
            graph[i].append(i + 1)
            graph[i + 1].append(i)
        water_types = {0: 'F', 1: 'N', 2: 'N', 3: 'S', 4: 'N',
                      5: 'N', 6: 'N', 7: 'N', 8: 'N', 9: 'N'}
        start = 0
        end = 9
        # Valid path exists: 0(F) -> 1 -> 2 -> 3(S) -> ... -> 9
        self.assertEqual(find_shortest_path(graph, water_types, start, end), 9)

    def test_only_neutral_path(self):
        # Test when path exists but doesn't satisfy water collection rules
        graph = {
            0: [1],
            1: [0, 2],
            2: [1]
        }
        water_types = {0: 'N', 1: 'N', 2: 'N'}
        start = 0
        end = 2
        # Path exists but no water collection possible
        self.assertEqual(find_shortest_path(graph, water_types, start, end), -1)

    def test_start_end_water_types(self):
        # Test various start/end water type combinations
        graph = {
            0: [1],
            1: [0, 2],
            2: [1, 3],
            3: [2]
        }
        water_types = {0: 'F', 1: 'N', 2: 'S', 3: 'F'}
        start = 0
        end = 3
        # Valid path: 0(F) -> 1(N) -> 2(S) -> 3(F)
        self.assertEqual(find_shortest_path(graph, water_types, start, end), 3)

if __name__ == '__main__':
    unittest.main()