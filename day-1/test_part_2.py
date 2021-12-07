import unittest

import part_2 as sut


class TestPart2(unittest.TestCase):
    def test_window_at_index(self):
        # Arrange
        expected = [2, 3, 4]
        list_in = [1, 2, 3, 4, 5]
        index = 1
        # Act
        actual = sut.window_at_index(list_in, index)
        # Assert
        self.assertEqual(expected, actual)

    def test_sum_increased(self):
        # Arrange
        expected = True
        window_1 = [1, 2, 3]
        window_2 = [1, 2, 4]
        # Act
        actual = sut.sum_increased(window_1, window_2)
        # Assert
        self.assertEqual(expected, actual)

    def test_sample_test_case(self):
        # Arrange
        expected = 5
        window_1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        # Act
        actual = sut.number_of_increases(window_1)
        # Assert
        self.assertEqual(expected, actual)
