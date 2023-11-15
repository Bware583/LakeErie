from plotnine import ggplot, aes, geom_point, labs, theme
import pandas as pd
    
data = pd.DataFrame({'Time': time_vector, variable_name: variable_vector})


########## Function 1a: Create a scatter plot 

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
    
    # Create scatter plot
    p = ggplot(data, aes(x='Time', y=variable_name)) + \
        geom_point() + \
        labs(title=f'{variable_name} from {time_period}',
             x='Time', y=f'{variable_name}') + \
        theme_minimal()

    return p


######### Function 1b: Create a line plot 

def create_line_plot(time_vector, variable_vector, variable_name, time_period_start, time_period_end):
    """
    Create a line plot of a variable vs time using plotnine.

    Parameters:
    - time_vector (list or array): The time values.
    - variable_vector (list or array): The variable values.
    - variable_name (str): The name of the variable.
    - time_period_start (str): The start of the time period.
    - time_period_end (str): The end of the time period.

    Returns:
    - p (plotnine.ggplot): The line plot.
    """

    # Create a DataFrame 
    import pandas as pd
    data = pd.DataFrame({'Time': time_vector, variable_name: variable_vector})

    # Create line plot
    p = ggplot(data, aes(x='Time', y=variable_name)) + \
        geom_line() + \
        labs(title=f'{variable_name} from {time_period_start} to {time_period_end}',
             x='Time', y=f'{variable_name}') + \
        theme_minimal()

    return p


######## Function 2a : Create the same plot as above but with a linear regression line 

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

    return p



######## Function 2b  Create the same plot as above but with a LOESS curve 

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

    # Create a DataFrame for plotnine
    import pandas as pd
    data = pd.DataFrame({'Time': time_vector, variable_name: variable_vector})

    # Create scatter plot with linear regression line
    p = ggplot(data, aes(x='Time', y=variable_name)) + \
        geom_point() + \
        geom_smooth(method='LOESS', se=True, color='red') + \
        labs(title=f'{variable_name} from {time_period_start} to {time_period_end}',
             x='Time', y=f'{variable_name}') + \
        theme_minimal()

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


