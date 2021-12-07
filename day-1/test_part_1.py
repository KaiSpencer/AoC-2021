import unittest

import part_1 as sut


class TestPart1(unittest.TestCase):
    def test_number_of_increases(self):
        # Arrange
        expected = 2
        input_list = ["1", "2", "1", "1", "3"]
        # Act
        actual = sut.number_of_increased(input_list)
        # Assert
        self.assertEqual(expected, actual)

    def test_number_of_increases(self):
        # Arrange
        expected = 7
        input_list = [
            "199",
            "200",
            "208",
            "210",
            "200",
            "207",
            "240",
            "269",
            "260",
            "263",
        ]
        # Act
        actual = sut.number_of_increased(input_list)
        # Assert
        self.assertEqual(expected, actual)
