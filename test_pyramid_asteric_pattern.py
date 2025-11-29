import unittest

from pyramid_asteric_pattern import build_pyramid


class PyramidTests(unittest.TestCase):

    def test_height_1(self):
        self.assertEqual(build_pyramid(1), ['*'])

    def test_height_3_solid(self):
        expected = [
            '  *  ',
            ' *** ',
            '*****'
        ]
        self.assertEqual(build_pyramid(3), expected)

    def test_height_4_hollow(self):
        expected = [
            '   *   ',
            '  * *  ',
            ' *   * ',
            '*******'
        ]
        self.assertEqual(build_pyramid(4, hollow=True), expected)


if __name__ == '__main__':
    unittest.main()
