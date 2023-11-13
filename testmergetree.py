import unittest
from mergetree import merge

class TestMergeFunction(unittest.TestCase):
    def test_merge_valid_input(self):
        input_data = [
            ["*", "a", "b", "car"],
            ["*", "a", "b", "e"],
            ["*", "a", "d", "b"],
            ["*", "a", "x"]
        ]
        root = merge(input_data)
        # Validate root node
        self.assertEqual(root.name, "*")
        self.assertEqual(root.children_by_name["a"].name, "a")
        self.assertEqual(root.children_by_name["a"].children_by_name["b"].name, "b")
        self.assertEqual(root.children_by_name["a"].children_by_name["b"].children_by_name["car"].name, "car")
        self.assertEqual(root.children_by_name["a"].children_by_name["b"].children_by_name["e"].name, "e")
        self.assertEqual(root.children_by_name["a"].children_by_name["d"].name, "d")
        self.assertEqual(root.children_by_name["a"].children_by_name["d"].children_by_name["b"].name, "b")
        self.assertEqual(root.children_by_name["a"].children_by_name["x"].name, "x")

    def test_merge_invalid_input(self):
        input_data = [
            ["*", "a", "b", "car"],
            ["t", "a", "c", "e"],  # Different child name at the root level
            ["*", "a", "d", "b"],
            ["*", "a", "x"]
        ]
        with self.assertRaises(Exception):
            merge(input_data)

    def test_merge_empty_input(self):
        input_data = []
        root = merge(input_data)
        self.assertIsNone(root)

if __name__ == "__main__":
    unittest.main()
