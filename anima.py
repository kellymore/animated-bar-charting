import pandas as pd
import os
import bar_chart_race as bcr

def load_data(file_path):
    """
    Load the data from the given CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pandas.DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(file_path)

def main():
    # Change directory to the folder containing the data
    data_dir = '/Users/kelly/Downloads/'
    os.chdir(data_dir)

    # Load data from CSV file
    data_cor = load_data("anima_chart.csv")
    
    # Display the first few rows of the data
    print(data_cor.head())

    # Define columns of interest
    columns_of_interest = ['date', 'Italy', 'China', 'Australia', 'Brazil', 'India', 'United Kingdom']

    # Subset the DataFrame
    subset_df = data_cor[columns_of_interest]

    # Set 'date' column as index
    subset_df.set_index("date", inplace=True)

    # Calculate cumulative sum
    cum_sum_df = subset_df.cumsum(axis=0)

    # Display the last 10 rows of the cumulative sum DataFrame
    print(cum_sum_df.tail(10))

    # Generate bar chart race
    bcr.bar_chart_race(df=cum_sum_df, filename=None, figsize=(3, 5), title='Cases by Country')

if __name__ == "__main__":
    main()
