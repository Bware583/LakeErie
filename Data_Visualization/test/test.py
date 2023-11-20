
import unittest
import pandas as pd
from your_script import create_scatter_plot  # Replace 'your_script' with the actual name of your script

class TestCreateScatterPlot(unittest.TestCase):

    def test_successful_plot_creation(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]
        variable_name = "Variable"
        time_period = "Test Period"

        # Ensure no errors are raised
        try:
            plot = create_scatter_plot(time_vector, variable_vector, variable_name, time_period)
        except Exception as e:
            self.fail(f"create_scatter_plot raised an unexpected exception: {str(e)}")

        # Ensure the plot is not None
        self.assertIsNotNone(plot)

    def test_mismatched_vector_lengths(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25]  # Mismatched length

        with self.assertRaises(ValueError):
            create_scatter_plot(time_vector, variable_vector, "Variable", "Test Period")

    def test_empty_vectors(self):
        time_vector = []
        variable_vector = []

        with self.assertRaises(ValueError):
            create_scatter_plot(time_vector, variable_vector, "Variable", "Test Period")

    def test_non_numeric_data(self):
        time_vector = [1, 2, 3, "four", 5]  # Non-numeric element
        variable_vector = [10, 20, 15, 25, 30]

        with self.assertRaises(ValueError):
            create_scatter_plot(time_vector, variable_vector, "Variable", "Test Period")

    def test_empty_time_period(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]

        with self.assertRaises(ValueError):
            create_scatter_plot(time_vector, variable_vector, "Variable", "")

    def test_successful_plot_creation_with_existing_data(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]
        variable_name = "Variable"
        time_period = "Test Period"

        # Create a DataFrame to be used as existing data
        existing_data = pd.DataFrame({'Time': time_vector, variable_name: variable_vector})

        # Set the global data variable
        global data
        data = existing_data.copy()

        # Ensure no errors are raised
        try:
            plot = create_scatter_plot(time_vector, variable_vector, variable_name, time_period)
        except Exception as e:
            self.fail(f"create_scatter_plot raised an unexpected exception: {str(e)}")

        # Ensure the plot is not None
        self.assertIsNotNone(plot)

###################################################################################################

class TestCreateLinePlot(unittest.TestCase):

    def test_successful_plot_creation(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]
        variable_name = "Variable"
        time_period_start = "Start Period"
        time_period_end = "End Period"

        # Ensure no errors are raised
        try:
            plot = create_line_plot(time_vector, variable_vector, variable_name, time_period_start, time_period_end)
        except Exception as e:
            self.fail(f"create_line_plot raised an unexpected exception: {str(e)}")

        # Ensure the plot is not None
        self.assertIsNotNone(plot)

    def test_mismatched_vector_lengths(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25]  # Mismatched length

        with self.assertRaises(ValueError):
            create_line_plot(time_vector, variable_vector, "Variable", "Start Period", "End Period")

    def test_empty_vectors(self):
        time_vector = []
        variable_vector = []

        with self.assertRaises(ValueError):
            create_line_plot(time_vector, variable_vector, "Variable", "Start Period", "End Period")

    def test_non_numeric_data(self):
        time_vector = [1, 2, 3, "four", 5]  # Non-numeric element
        variable_vector = [10, 20, 15, 25, 30]

        with self.assertRaises(ValueError):
            create_line_plot(time_vector, variable_vector, "Variable", "Start Period", "End Period")

    def test_empty_time_periods(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]

        with self.assertRaises(ValueError):
            create_line_plot(time_vector, variable_vector, "Variable", "", "")

    def test_successful_plot_creation_with_existing_data(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]
        variable_name = "Variable"
        time_period_start = "Start Period"
        time_period_end = "End Period"

        # Create a DataFrame to be used as existing data
        existing_data = pd.DataFrame({'Time': time_vector, variable_name: variable_vector})

        # Set the global data variable
        global data
        data = existing_data.copy()

        # Ensure no errors are raised
        try:
            plot = create_line_plot(time_vector, variable_vector, variable_name, time_period_start, time_period_end)
        except Exception as e:
            self.fail(f"create_line_plot raised an unexpected exception: {str(e)}")

        # Ensure the plot is not None
        self.assertIsNotNone(plot)

############################################################################################################

import unittest
import pandas as pd
from plot_functions import create_scatter_plot, create_line_plot, add_linear_regression  # Replace 'plot_functions' with the actual name of your script

class TestAddLinearRegression(unittest.TestCase):

    def test_successful_plot_creation(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]
        variable_name = "Variable"
        time_period_start = "Start Period"
        time_period_end = "End Period"

        # Create a scatter plot to add linear regression to
        scatter_plot = create_scatter_plot(time_vector, variable_vector, variable_name, "Test Period")

        # Ensure no errors are raised
        try:
            plot = add_linear_regression(time_vector, variable_vector, variable_name, time_period_start, time_period_end)
        except Exception as e:
            self.fail(f"add_linear_regression raised an unexpected exception: {str(e)}")

        # Ensure the plot is not None
        self.assertIsNotNone(plot)

    def test_mismatched_vector_lengths(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25]  # Mismatched length

        with self.assertRaises(ValueError):
            add_linear_regression(time_vector, variable_vector, "Variable", "Start Period", "End Period")

    def test_empty_vectors(self):
        time_vector = []
        variable_vector = []

        with self.assertRaises(ValueError):
            add_linear_regression(time_vector, variable_vector, "Variable", "Start Period", "End Period")

    def test_non_numeric_data(self):
        time_vector = [1, 2, 3, "four", 5]  # Non-numeric element
        variable_vector = [10, 20, 15, 25, 30]

        with self.assertRaises(ValueError):
            add_linear_regression(time_vector, variable_vector, "Variable", "Start Period", "End Period")

    def test_empty_time_periods(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]

        with self.assertRaises(ValueError):
            add_linear_regression(time_vector, variable_vector, "Variable", "", "")

    def test_successful_plot_creation_with_existing_data(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]
        variable_name = "Variable"
        time_period_start = "Start Period"
        time_period_end = "End Period"

        # Create a line plot to add linear regression to
        line_plot = create_line_plot(time_vector, variable_vector, variable_name, time_period_start, time_period_end)

        # Ensure no errors are raised
        try:
            plot = add_linear_regression(time_vector, variable_vector, variable_name, time_period_start, time_period_end)
        except Exception as e:
            self.fail(f"add_linear_regression raised an unexpected exception: {str(e)}")

        # Ensure the plot is not None
        self.assertIsNotNone(plot)


################################################################################################################################

class TestAddLoessCurve(unittest.TestCase):

    def test_successful_plot_creation(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]
        variable_name = "Variable"
        time_period_start = "Start Period"
        time_period_end = "End Period"

        # Create a scatter plot to add LOESS curve to
        scatter_plot = create_scatter_plot(time_vector, variable_vector, variable_name, "Test Period")

        # Ensure no errors are raised
        try:
            plot = add_loess_curve(time_vector, variable_vector, variable_name, time_period_start, time_period_end)
        except Exception as e:
            self.fail(f"add_loess_curve raised an unexpected exception: {str(e)}")

        # Ensure the plot is not None
        self.assertIsNotNone(plot)

    def test_mismatched_vector_lengths(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25]  # Mismatched length

        with self.assertRaises(ValueError):
            add_loess_curve(time_vector, variable_vector, "Variable", "Start Period", "End Period")

    def test_empty_vectors(self):
        time_vector = []
        variable_vector = []

        with self.assertRaises(ValueError):
            add_loess_curve(time_vector, variable_vector, "Variable", "Start Period", "End Period")

    def test_non_numeric_data(self):
        time_vector = [1, 2, 3, "four", 5]  # Non-numeric element
        variable_vector = [10, 20, 15, 25, 30]

        with self.assertRaises(ValueError):
            add_loess_curve(time_vector, variable_vector, "Variable", "Start Period", "End Period")

    def test_empty_time_periods(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]

        with self.assertRaises(ValueError):
            add_loess_curve(time_vector, variable_vector, "Variable", "", "")

    def test_successful_plot_creation_with_existing_data(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]
        variable_name = "Variable"
        time_period_start = "Start Period"
        time_period_end = "End Period"

        # Create a line plot to add LOESS curve to
        line_plot = create_line_plot(time_vector, variable_vector, variable_name, time_period_start, time_period_end)

        # Ensure no errors are raised
        try:
            plot = add_loess_curve(time_vector, variable_vector, variable_name, time_period_start, time_period_end)
        except Exception as e:
            self.fail(f"add_loess_curve raised an unexpected exception: {str(e)}")

        # Ensure the plot is not None
        self.assertIsNotNone(plot)



##############################################################


class TestExportPlotToJpg(unittest.TestCase):

    def test_successful_export(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]
        variable_name = "Variable"
        time_period = "Test Period"

        # Create a scatter plot to export
        scatter_plot = create_scatter_plot(time_vector, variable_vector, variable_name, time_period)

        # Ensure no errors are raised during export
        try:
            filepath = export_plot_to_jpg('test_output', scatter_plot, 'scatter_plot')
        except Exception as e:
            self.fail(f"export_plot_to_jpg raised an unexpected exception: {str(e)}")

        # Ensure the file exists
        self.assertTrue(os.path.exists(filepath))

        # Clean up: Remove the created file
        os.remove(filepath)

    def test_invalid_ggplot_object(self):
        # Create an invalid ggplot object
        invalid_plot = "This is not a ggplot object"

        # Ensure a ValueError is raised for an invalid ggplot object
        with self.assertRaises(ValueError):
            export_plot_to_jpg('test_output', invalid_plot, 'invalid_plot')

    def test_nonexistent_directory(self):
        time_vector = [1, 2, 3, 4, 5]
        variable_vector = [10, 20, 15, 25, 30]
        variable_name = "Variable"
        time_period = "Test Period"

        # Create a scatter plot to export
        scatter_plot = create_scatter_plot(time_vector, variable_vector, variable_name, time_period)

        # Attempt to export to a nonexistent directory
        with self.assertRaises(FileNotFoundError):
            export_plot_to_jpg('nonexistent_directory', scatter_plot, 'scatter_plot')