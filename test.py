import unittest

from new import SpacecraftNavigator


class TestSpacecraftNavigator(unittest.TestCase):

    def test_full(self):
        navigator = SpacecraftNavigator()
        initial_position = (10,15,40)
        initial_direction = "N"
        commands = "frubl"

        final_position, final_direction = navigator.navigate(commands, initial_position, initial_direction)

        self.assertEqual(final_position, (10,16,39))
        self.assertEqual(final_direction, "N")


if __name__ == "__main__":
    unittest.main()
