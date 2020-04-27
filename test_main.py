import unittest
from main import distance_between_stops, number_of_stops

class TestShortestPath(unittest.TestCase):
    def test_distance_a_b_c(self):
        self.assertEqual(distance_between_stops('A-B-C'), 9)

    def test_distance_a_d(self):
        self.assertEqual(distance_between_stops('A-D'), 5)

    def test_distance_a_d_c(self):
        self.assertEqual(distance_between_stops('A-D-C'), 13)

    def test_distance_a_e_b_c_d(self):
        self.assertEqual(distance_between_stops('A-E-B-C-D'), 22)

    def test_distance_a_e_d(self):
        self.assertEqual(distance_between_stops('A-E-D'), 'NO SUCH ROUTE')

    def test_distance_all_routes(self):
        self.assertEqual(number_of_stops('C', 'C', 3), 2)

    def test_distance_all_routes(self):
        self.assertEqual(number_of_stops('A', 'C', 4), 2)

if __name__ == '__main__':
    unittest.main()
