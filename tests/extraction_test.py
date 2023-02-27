import unittest
from pathlib import Path

from extraction import extract_images_from_pdf

BASE_PATH = Path(__file__).resolve().parent
output_directory = BASE_PATH / "output"
input_directory = BASE_PATH / "input"


class MyTestCase(unittest.TestCase):
    def test_something(self):
        extract_images_from_pdf(str(input_directory), str(output_directory))
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
