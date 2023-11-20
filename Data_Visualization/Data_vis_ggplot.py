def create_scatter_plot(time_vector, variable_vector, variable_name, time_period):
    """
    Create a scatter plot of a variable vs time using plotnine.

    Parameters:
    - time_vector (list or array): The time values.
    - variable_vector (list or array): The variable values.
    - variable_name (str): The name of the variable.
    - time_period (str): The time period description.

    Returns:
    - p (plotnine.ggplot): The scatter plot.
    """
    
    # Check if lengths of time_vector and variable_vector match
    if len(time_vector) != len(variable_vector):
        raise ValueError("Lengths of time_vector and variable_vector must be the same.")
    
    # Check if time_vector and variable_vector are not empty
    if not time_vector or not variable_vector:
        raise ValueError("Both time_vector and variable_vector must be non-empty.")
    
    # Check if time_vector and variable_vector contain numeric data
    if not all(isinstance(val, (int, float)) for val in time_vector):
        raise ValueError("All elements in time_vector must be numeric.")
    
    if not all(isinstance(val, (int, float)) for val in variable_vector):
        raise ValueError("All elements in variable_vector must be numeric.")
    
    # Check if time_period is a non-empty string
    if not isinstance(time_period, str) or not time_period.strip():
        raise ValueError("time_period must be a non-empty string.")
    
    # Use the global dataset
    global data
    
    # Create DataFrame if it's not already defined
    if data is None:
        data = pd.DataFrame({'Time': time_vector, variable_name: variable_vector})
    
    # Create scatter plot
    p = ggplot(data, aes(x='Time', y=variable_name)) + \
        geom_point() + \
        labs(title=f'{variable_name} from {time_period}',
             x='Time', y=f'{variable_name}') + \
        theme_minimal()

    # Check if the plot was successfully created
    if p is None:
        raise ValueError("Failed to create the scatter plot.")

    return p




######### Function 1b: Create a line plot 
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


######## Function 2a : Create the same plot as above but with a linear regression line 
from plotnine import ggplot, aes, geom_point, geom_smooth, labs, theme

def add_linear_regression(time_vector, variable_vector, variable_name, time_period_start, time_period_end):
    """
    Add a linear regression line to a plotnine plot.

    Parameters:
    - time_vector (list or array): The time values.
    - variable_vector (list or array): The variable values.
    - variable_name (str): The name of the variable.
    - time_period_start (str): The start of the time period.
    - time_period_end (str): The end of the time period.

    Returns:
    - p (plotnine.ggplot): The plot with the linear regression line.
    """

    # Check if time_vector and variable_vector contain numeric data
    if not all(isinstance(val, (int, float)) for val in time_vector):
        raise ValueError("All elements in time_vector must be numeric.")

    if not all(isinstance(val, (int, float)) for val in variable_vector):
        raise ValueError("All elements in variable_vector must be numeric.")

    # Check if time_period_start and time_period_end are non-empty strings
    if not isinstance(time_period_start, str) or not time_period_start.strip():
        raise ValueError("time_period_start must be a non-empty string.")

    if not isinstance(time_period_end, str) or not time_period_end.strip():
        raise ValueError("time_period_end must be a non-empty string.")

    # Create a DataFrame for plotnine
    import pandas as pd
    data = pd.DataFrame({'Time': time_vector, variable_name: variable_vector})

    # Create scatter plot with linear regression line
    p = ggplot(data, aes(x='Time', y=variable_name)) + \
        geom_point() + \
        geom_smooth(method='lm', se=True, color='red') + \
        labs(title=f'{variable_name} from {time_period_start} to {time_period_end}',
             x='Time', y=f'{variable_name}') + \
        theme_minimal()

    # Check if the plot was successfully created
    if p is None:
        raise ValueError("Failed to create the plot with linear regression line.")

    return p




######## Function 2b  Create the same plot as above but with a LOESS curve 

def add_loess_curve(time_vector, variable_vector, variable_name, time_period_start, time_period_end):
    """
    Add a LOESS curve to a plotnine plot.

    Parameters:
    - time_vector (list or array): The time values.
    - variable_vector (list or array): The variable values.
    - variable_name (str): The name of the variable.
    - time_period_start (str): The start of the time period.
    - time_period_end (str): The end of the time period.

    Returns:
    - p (plotnine.ggplot): The plot with the LOESS curve.
    """

    # Check if time_vector and variable_vector contain numeric data
    if not all(isinstance(val, (int, float)) for val in time_vector):
        raise ValueError("All elements in time_vector must be numeric.")

    if not all(isinstance(val, (int, float)) for val in variable_vector):
        raise ValueError("All elements in variable_vector must be numeric.")

    # Check if time_period_start and time_period_end are non-empty strings
    if not isinstance(time_period_start, str) or not time_period_start.strip():
        raise ValueError("time_period_start must be a non-empty string.")

    if not isinstance(time_period_end, str) or not time_period_end.strip():
        raise ValueError("time_period_end must be a non-empty string.")

    # Create a DataFrame for plotnine
    import pandas as pd
    data = pd.DataFrame({'Time': time_vector, variable_name: variable_vector})

    # Create scatter plot with LOESS curve
    p = ggplot(data, aes(x='Time', y=variable_name)) + \
        geom_point() + \
        geom_smooth(method='loess', se=True, color='red') + \
        labs(title=f'{variable_name} from {time_period_start} to {time_period_end}',
             x='Time', y=f'{variable_name}') + \
        theme_minimal()

    # Check if the plot was successfully created
    if p is None:
        raise ValueError("Failed to create the plot with LOESS curve.")

    return p



#### Function 3a : Export to specified directory as .jpg 
def export_plot_to_jpg(directory, p, filename='plot'):
    """
    Export a plotnine plot to a .jpg file in a user-defined directory.

    Parameters:
    - directory (str): The directory location to save the .jpg file.
    - p (plotnine.ggplot): The plotnine plot object.
    - filename (str): The filename for the saved .jpg file (default is 'plot').

    Returns:
    - filepath (str): The full path to the saved .jpg file.
    """
    if not isinstance(p, ggplot):
    raise ValueError("The provided 'p' argument is not a valid ggplot object.")

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the plot as .jpg
    filepath = os.path.join(directory, f'{filename}.jpg')
    p.save(filepath, width=8, height=6, units='in', dpi=300)

    return filepath





#### Function 3b: Export to specified directory ad a .pdf 

def export_plot_to_pdf(directory, p, filename='plot'):
    """
    Export a plotnine plot to a .pdf file in a user-defined directory.

    Parameters:
    - directory (str): The directory location to save the .pdf file.
    - p (plotnine.ggplot): The plotnine plot object.
    - filename (str): The filename for the saved .pdf file (default is 'plot').

    Returns:
    - filepath (str): The full path to the saved .pdf file.
    """

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the plot as .pdf
    filepath = os.path.join(directory, f'{filename}.pdf')
    p.save(filepath, width=8, height=6, units='in', dpi=300, format='pdf')

    return filepath


