"""Unit tests for anomaly.py"""

### Tests for CreateTrendline   

class TestCreateTrendline(unittest.TestCase):
    def setUp(self):
        # Create sample data for testing
        data_str = """times,value_mean
        2023-01-01,25
        2023-01-02,26
        2023-01-03,24
        2023-01-04,23
        2023-01-05,22
        """
        self.data = pd.read_csv(StringIO(data_str))
        self.data['times'] = pd.to_datetime(self.data['times'])

    def test_valid_data(self):
        with patch('plotly.io.show') as mock_show:
            create_trendline(self.data)
            mock_show.assert_called()

    def test_missing_times_column(self):
        data_without_times = self.data.drop(columns=['times'])
        with self.assertRaises(ValueError, msg="Expected ValueError for missing 'times' column."):
            create_trendline(data_without_times)

    def test_missing_value_mean_column(self):
        data_without_value_mean = self.data.drop(columns=['value_mean'])
        with self.assertRaises(ValueError, msg="Expected ValueError for missing 'value_mean' column."):
            create_trendline(data_without_value_mean)

    def test_non_datetime_times_column(self):
        data_non_datetime_times = self.data.copy()
        data_non_datetime_times['times'] = data_non_datetime_times['times'].astype(str)
        with self.assertRaises(ValueError, msg="Expected ValueError for non-datetime 'times' column."):
            create_trendline(data_non_datetime_times)

    def test_empty_data(self):
        empty_data = pd.DataFrame()
        with self.assertRaises(ValueError, msg="Expected ValueError for empty data."):
            create_trendline(empty_data)

    def test_non_numeric_value_mean_column(self):
        data_non_numeric_value_mean = self.data.copy()
        data_non_numeric_value_mean['value_mean'] = ['a', 'b', 'c', 'd', 'e']
        with self.assertRaises(ValueError, msg="Expected ValueError for non-numeric 'value_mean' column."):
            create_trendline(data_non_numeric_value_mean)


#### Tests for CreateAnomalyGraph

class TestCreateAnomalyGraph(unittest.TestCase):
    def setUp(self):
        # Create sample data for testing
        data_str = """times,value_mean
        2023-01-01,25
        2023-01-02,26
        2023-01-03,24
        2023-01-04,23
        2023-01-05,22
        """
        self.data = pd.read_csv(StringIO(data_str))
        self.data['times'] = pd.to_datetime(self.data['times'])

    def test_valid_data(self):
        with patch('plotly.io.show') as mock_show, \
             patch('pytimetk.anomalize') as mock_anomalize, \
             patch('pytimetk.plot_anomalies') as mock_plot_anomalies:

            create_anomaly_graph(self.data)

            mock_anomalize.assert_called_once_with(
                data=self.data,
                date_column='times',
                value_column='value_mean',
                period=7,
                iqr_alpha=0.05,
                clean_alpha=0.75,
                clean="min_max"
            )

            mock_plot_anomalies.assert_called_once_with(
                data=mock_anomalize.return_value,
                date_column='times',
                engine='plotly',
                title='Plot Anomaly Bands'
            )

            mock_show.assert_called_once_with(mock_plot_anomalies.return_value)

    def test_missing_times_column(self):
        data_without_times = self.data.drop(columns=['times'])
        with self.assertRaises(ValueError, msg="Expected ValueError for missing 'times' column."):
            create_anomaly_graph(data_without_times)

    def test_missing_value_mean_column(self):
        data_without_value_mean = self.data.drop(columns=['value_mean'])
        with self.assertRaises(ValueError, msg="Expected ValueError for missing 'value_mean' column."):
            create_anomaly_graph(data_without_value_mean)

    def test_non_datetime_times_column(self):
        data_non_datetime_times = self.data.copy()
        data_non_datetime_times['times'] = data_non_datetime_times['times'].astype(str)
        with self.assertRaises(ValueError, msg="Expected ValueError for non-datetime 'times' column."):
            create_anomaly_graph(data_non_datetime_times)

    def test_empty_data(self):
        empty_data = pd.DataFrame()
        with self.assertRaises(ValueError, msg="Expected ValueError for empty data."):
            create_anomaly_graph(empty_data)

    def test_non_numeric_value_mean_column(self):
        data_non_numeric_value_mean = self.data.copy()
        data_non_numeric_value_mean['value_mean'] = ['a', 'b', 'c', 'd', 'e']
        with self.assertRaises(ValueError, msg="Expected ValueError for non-numeric 'value_mean' column."):
            create_anomaly_graph(data_non_numeric_value_mean)


## Tests for PlotAnomaliesDecomp

class TestPlotAnomaliesDecomp(unittest.TestCase):
    def setUp(self):
        # Create sample data for testing
        data_str = """times,value_mean
        2023-01-01,25
        2023-01-02,26
        2023-01-03,24
        2023-01-04,23
        2023-01-05,22
        """
        self.data = pd.read_csv(StringIO(data_str))
        self.data['times'] = pd.to_datetime(self.data['times'])

    def test_valid_data(self):
        with patch('plotly.io.show') as mock_show:
            plot_anomalies_decomp(self.data)

            mock_show.assert_called_once_with(
                pytimetk.plot_anomalies_decomp(
                    data=self.data,
                    date_column='times',
                    engine='plotly',
                    title='Seasonal Decomposition'
                )
            )

    def test_missing_times_column(self):
        data_without_times = self.data.drop(columns=['times'])
        with self.assertRaises(ValueError, msg="Expected ValueError for missing 'times' column."):
            plot_anomalies_decomp(data_without_times)

    def test_missing_value_mean_column(self):
        data_without_value_mean = self.data.drop(columns=['value_mean'])
        with self.assertRaises(ValueError, msg="Expected ValueError for missing 'value_mean' column."):
            plot_anomalies_decomp(data_without_value_mean)

    def test_non_datetime_times_column(self):
        data_non_datetime_times = self.data.copy()
        data_non_datetime_times['times'] = data_non_datetime_times['times'].astype(str)
        with self.assertRaises(ValueError, msg="Expected ValueError for non-datetime 'times' column."):
            plot_anomalies_decomp(data_non_datetime_times)

    def test_empty_data(self):
        empty_data = pd.DataFrame()
        with self.assertRaises(ValueError, msg="Expected ValueError for empty data."):
            plot_anomalies_decomp(empty_data)

    def test_non_numeric_value_mean_column(self):
        data_non_numeric_value_mean = self.data.copy()
        data_non_numeric_value_mean['value_mean'] = ['a', 'b', 'c', 'd', 'e']
        with self.assertRaises(ValueError, msg="Expected ValueError for non-numeric 'value_mean' column."):
            plot_anomalies_decomp(data_non_numeric_value_mean)