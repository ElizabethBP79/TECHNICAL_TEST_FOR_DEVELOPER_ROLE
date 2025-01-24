import unittest
from tower_of_hanoi import solve_tower_of_hanoi

class TestTowerOfHanoi(unittest.TestCase):

    def test_valid_input(self):
        n = 3
        disks = [(3, "red"), (2, "blue"), (1, "red")]
        result = solve_tower_of_hanoi(n, disks)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_invalid_input(self):
        n = 3
        disks = [(3, "red"), (2, "red"), (1, "blue")]
        result = solve_tower_of_hanoi(n, disks)
        self.assertEqual(result, -1)

    def test_edge_case_single_disk(self):
        n = 1
        disks = [(1, "blue")]
        result = solve_tower_of_hanoi(n, disks)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

 

if __name__ == "__main__":
    unittest.main()