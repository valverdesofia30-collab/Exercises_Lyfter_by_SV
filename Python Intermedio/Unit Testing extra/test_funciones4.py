import unittest
from unittest.mock import mock_open, patch

from Funciones4_test import read_lines


class TestReadLines(unittest.TestCase):

    def test_read_lines_returns_expected_lines(self):
        # Arrange
        fake_file = "Hola\nMundo\nPython\n"

        # Act
        with patch("builtins.open", mock_open(read_data=fake_file)):
            result = read_lines("archivo.txt")

        # Assert
        self.assertEqual(result, ["Hola\n", "Mundo\n", "Python\n"])

    def test_read_lines_file_not_found(self):
        # Arrange
        # Act & Assert
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                read_lines("archivo_inexistente.txt")


if __name__ == "__main__":
    unittest.main()