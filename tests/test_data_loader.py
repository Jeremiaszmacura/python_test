import unittest
from unittest.mock import patch, Mock

from lab_app.data_loader import DataLoader


class DataLoaderTestCase(unittest.TestCase):
    """This class represents the DataLoader test cases"""

    def setUp(self):
        """Define test variables and initialize data loader."""
        self.data_loader = DataLoader()

    def test_data_loader(self):
        """Test data loader loads data from file"""
        file_name = "./input_test.csv"

        expected_data = [("John", "Smith"), ("John", "Doe")]
        data = self.data_loader.read_data(file_name)

        self.assertEqual(expected_data, data)

    @patch("lab_app.data_loader.open")
    def test_data_loader_empty_file(self, open_mock):
        """Test data loader raises VauleError when file is empty"""
        # Mock jako Stub
        file_handler_mock = Mock()
        file_handler_mock.readlines = Mock(return_value="")
        open_mock.return_value = file_handler_mock

        file_name = "some_nonexisting_file.csv"
        with self.assertRaises(ValueError):
            self.data_loader.read_data(file_name)
        # Mock jako Mock
        file_handler_mock.readlines.assert_called_once_with()
        open_mock.assert_called_once_with("some_nonexisting_file.csv", "r")

    @patch("lab_app.data_loader.open")
    def test_data_loader_wrong_separator(self, open_mock):
        """Test data loader raises VauleError when used wrong separator"""
        # Mock jako Stub
        file_handler_mock = Mock()
        file_handler_mock.readlines = Mock(return_value=["a;b"])
        open_mock.return_value = file_handler_mock

        file_name = "some_nonexisting_file.csv"
        with self.assertRaises(ValueError):
            self.data_loader.read_data(file_name)
        # Mock jako Mock
        file_handler_mock.readlines.assert_called_once_with()
        open_mock.assert_called_once_with("some_nonexisting_file.csv", "r")

    @patch("lab_app.data_loader.open")
    def test_data_loader_duplicate_email(self, open_mock):
        """Test data loader raises VauleError when file contains duplicate name and surname pairs"""
        # Mock jako Stub
        file_handler_mock = Mock()
        file_handler_mock.readlines = Mock(return_value=["John,Doe", "John,Doe"])
        open_mock.return_value = file_handler_mock

        file_name = "some_nonexisting_file.csv"
        with self.assertRaises(ValueError):
            self.data_loader.read_data(file_name)
        # Mock jako Mock
        file_handler_mock.readlines.assert_called_once_with()
        open_mock.assert_called_once_with("some_nonexisting_file.csv", "r")

    @patch("lab_app.data_loader.open")
    def test_data_loader_forbidden_words(self, open_mock):
        """Test data loader raises VauleError when file contains forbidden words"""
        # Mock jako Stub
        file_handler_mock = Mock()
        file_handler_mock.readlines = Mock(return_value=["John,Doe", "Fuck,That"])
        open_mock.return_value = file_handler_mock

        file_name = "some_nonexisting_file.csv"
        with self.assertRaises(ValueError):
            self.data_loader.read_data(file_name)
        # Mock jako Mock
        file_handler_mock.readlines.assert_called_once_with()
        open_mock.assert_called_once_with("some_nonexisting_file.csv", "r")

    def tearDown(self):
        """Teardown all initialized variables and close data loader."""
        pass
