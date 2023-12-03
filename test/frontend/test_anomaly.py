import unittest

import pandas as pd
from datetime import datetime

from anomaly.py import create_trendline  
from anomaly.py import create_anomaly_graph
from anomaly.py import create_anomaly_decomp_graph


class TestCreateTrendline(unittest.TestCase):
    """
    Test cases for the create_trendline function.
    """

    def test_valid_data(self):
        """
        Test create_trendline with valid data.
        """
        data = pd.DataFrame({
            'times': [datetime(2023, 1, 1), datetime(2023, 1, 2)],
            'value_mean': [1, 2]
        })
        # This test should not raise any exceptions
        create_trendline(data)

    def test_missing_columns(self):
        """
        Test create_trendline with missing columns.
        """
        data = pd.DataFrame({'invalid_column': [1, 2]})
        # Expecting a ValueError to be raised since required columns are missing
        with self.assertRaises(ValueError):
            create_trendline(data)

    def test_invalid_datetime_column(self):
        """
        Test create_trendline with an invalid datetime column.
        """
        data = pd.DataFrame({
            'times': ['2023-01-01', '2023-01-02'],
            'value_mean': [1, 2]
        })
        # Expecting a ValueError to be raised since 'times' column is not a datetime object
        with self.assertRaises(ValueError):
            create_trendline(data)

    def test_empty_columns(self):
        """
        Test create_trendline with empty columns.
        """
        data = pd.DataFrame({'times': [], 'value_mean': []})
        # Expecting a ValueError to be raised since either 'times' or 'value_mean' column is empty
        with self.assertRaises(ValueError):
            create_trendline(data)

    def test_non_numeric_values(self):
        """
        Test create_trendline with non-numeric values.
        """
        data = pd.DataFrame({
            'times': [datetime(2023, 1, 1), datetime(2023, 1, 2)],
            'value_mean': [1, 'invalid']
        })
        # Expecting a ValueError to be raised since 'value_mean' column contains non-numeric values
        with self.assertRaises(ValueError):
            create_trendline(data)


class TestCreateAnomalyGraph(unittest.TestCase):
    """
    Test cases for the create_anomaly_graph function.
    """

    def test_valid_data(self):
        """
        Test create_anomaly_graph with valid data.
        """
        data = pd.DataFrame({
            'times': [datetime(2023, 1, 1), datetime(2023, 1, 2)],
            'value_mean': [1, 2]
        })
        # This test should not raise any exceptions
        create_anomaly_graph(data)

    def test_missing_columns(self):
        """
        Test create_anomaly_graph with missing columns.
        """
        data = pd.DataFrame({'invalid_column': [1, 2]})
        # Expecting a ValueError to be raised since required columns are missing
        with self.assertRaises(ValueError):
            create_anomaly_graph(data)

    def test_invalid_datetime_column(self):
        """
        Test create_anomaly_graph with an invalid datetime column.
        """
        data = pd.DataFrame({
            'times': ['2023-01-01', '2023-01-02'],
            'value_mean': [1, 2]
        })
        # Expecting a ValueError to be raised since 'times' column is not a datetime object
        with self.assertRaises(ValueError):
            create_anomaly_graph(data)

    def test_empty_columns(self):
        """
        Test create_anomaly_graph with empty columns.
        """
        data = pd.DataFrame({'times': [], 'value_mean': []})
        # Expecting a ValueError to be raised since either 'times' or 'value_mean' column is empty
        with self.assertRaises(ValueError):
            create_anomaly_graph(data)

    def test_non_numeric_values(self):
        """
        Test create_anomaly_graph with non-numeric values.
        """
        data = pd.DataFrame({
            'times': [datetime(2023, 1, 1), datetime(2023, 1, 2)],
            'value_mean': [1, 'invalid']
        })
        # Expecting a ValueError to be raised since 'value_mean' column contains non-numeric values
        with self.assertRaises(ValueError):
            create_anomaly_graph(data)


class TestCreateAnomalyDecompGraph(unittest.TestCase):
    """
    Test cases for the create_anomaly_decomp_graph function.
    """

    def test_valid_data(self):
        """
        Test create_anomaly_decomp_graph with valid data.
        """
        data = pd.DataFrame({
            'times': [datetime(2023, 1, 1), datetime(2023, 1, 2)],
            'value_mean': [1, 2]
        })
        # This test should not raise any exceptions
        create_anomaly_decomp_graph(data)

    def test_missing_columns(self):
        """
        Test create_anomaly_decomp_graph with missing columns.
        """
        data = pd.DataFrame({'invalid_column': [1, 2]})
        # Expecting a ValueError to be raised since required columns are missing
        with self.assertRaises(ValueError):
            create_anomaly_decomp_graph(data)

    def test_invalid_datetime_column(self):
        """
        Test create_anomaly_decomp_graph with an invalid datetime column.
        """
        data = pd.DataFrame({
            'times': ['2023-01-01', '2023-01-02'],
            'value_mean': [1, 2]
        })
        # Expecting a ValueError to be raised since 'times' column is not a datetime object
        with self.assertRaises(ValueError):
            create_anomaly_decomp_graph(data)

    def test_empty_columns(self):
        """
        Test create_anomaly_decomp_graph with empty columns.
        """
        data = pd.DataFrame({'times': [], 'value_mean': []})
        # Expecting a ValueError to be raised since either 'times' or 'value_mean' column is empty
        with self.assertRaises(ValueError):
            create_anomaly_decomp_graph(data)

    def test_non_numeric_values(self):
        """
        Test create_anomaly_decomp_graph with non-numeric values.
        """
        data = pd.DataFrame({
            'times': [datetime(2023, 1, 1), datetime(2023, 1, 2)],
            'value_mean': [1, 'invalid']
        })
        # Expecting a ValueError to be raised since 'value_mean' column contains non-numeric values
        with self.assertRaises(ValueError):
            create_anomaly_decomp_graph(data)
