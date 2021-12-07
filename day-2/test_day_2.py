import unittest

import day_2 as sut


class TestPart1(unittest.TestCase):
    def test_follow_command(self):
        expected = (5, 0)
        sub = sut.Submarine()

        sub.follow_command(sut.Command(direction="forward", distance=5))

        actual = sub.get_position()

        self.assertTupleEqual(expected, actual)

    def test_follow_command_part_2(self):
        expected = (13, 40)
        sub = sut.Submarine()

        sub.follow_command_part_2(sut.Command(direction="forward", distance=5))
        sub.follow_command_part_2(sut.Command(direction="down", distance=5))
        sub.follow_command_part_2(sut.Command(direction="forward", distance=8))

        actual = sub.get_position()

        self.assertTupleEqual(expected, actual)
