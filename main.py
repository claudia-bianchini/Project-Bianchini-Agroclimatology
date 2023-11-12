"""
    Main module for the 'Project Bianchini Agroclimatology.'

    This module orchestrates the entire project workflow, including creating the project directory,
    checking and downloading the dataset, extracting relevant information, and visualizing 
    the results through a dashboard.

    Args:
        None

    Returns:
        None
"""

import os
from download_data import dataset_check_download
from elaborate_data import extract_subfile
from dash_tot import create_dash

DEBUG = False

def create_project_directory(project_path, input_folder, output_folder, DEBUG=False):
    """
    Create the project directory structure with input and output subdirectories.

    Parameters:
    - project_path (str): Path to the main project directory.
    - input_folder (str): Name of the input subdirectory.
    - output_folder (str): Name of the output subdirectory.
    - DEBUG (bool, optional): If True, print DEBUG messages. Default is False.

    Returns:
    Tuple[str, str]: Paths to the input and output subdirectories.
    """
    # Create the 'Project' directory on the Desktop if it doesn't exist
    if not os.path.exists(project_path):
        os.makedirs(project_path)
        if DEBUG:
            print("Project directory created on the Desktop.")
    elif DEBUG:
        print("Project directory already exists on the Desktop.")

    # Create 'input' and 'output' subdirectories inside 'Project'
    input_path = os.path.join(project_path, input_folder)
    output_path = os.path.join(project_path, output_folder)

    for folder_path, folder_name in zip([input_path, output_path], ['input', 'output']):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            if DEBUG:
                print(f"'{folder_name}' subdirectory created.")
        elif DEBUG:
            print(f"'{folder_name}' subdirectory already exists.")

    return input_path, output_path



def read_config():
    """
    Read configuration values from the 'config.txt' file.

    Parameters:
    - None

    Returns:
    Tuple[str, str]: Driver path and binary location.
                    Returns (None, None) if the file is not found.
    """
    driver_path, binary_location = None, None

    try:
        # Try to read from the config file
        with open("config.txt", "r") as file:
            lines = file.readlines()

        # Parse the values from the file
        driver_path = lines[0].strip()
        binary_location = lines[1].strip()

    except FileNotFoundError:
        if DEBUG:
            print("Config file 'config.txt' not found.")

    return driver_path, binary_location


def main():
    """
    Main function to execute the Agroclimatology project.

    Parameters:
    - None
    """
    if DEBUG:
        print("You're in DEBUGGING mode.")
        print("Let's start.")

    # Create the workspace
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    project_path = os.path.join(desktop, 'Project-Bianchini-Agroclimatology')

    input_folder = "input"
    output_folder = "output"

    input_folder_path, output_folder_path = create_project_directory(
        project_path, input_folder, output_folder
    )
    if DEBUG:
        print('Project directory created.')

    # URL of the dataset
    url = ('https://www.kaggle.com/datasets/hugovallejo/'
        'agroclimatology-data-of-the-state-of-paran-br/data')

    # Read user configuration from the file 'config.txt'
    driver_path, binary_location = read_config()
    if DEBUG:
        print('Configuration file read.')

    # Check and download the dataset
    dataset_check_download(url, input_folder_path, output_folder_path, driver_path, binary_location)
    if DEBUG:
        print('Dataset checked and downloaded.')

    # Adjust the dataset by extracting a subfile with interested information
    df, df_soja = extract_subfile(input_folder_path, output_folder_path)
    if DEBUG:
        print(f'Dataframes extracted: {df}, {df_soja}')

    # Create a dashboard to visualize the result
    app = create_dash(df, df_soja)

    if __name__ == '__main__':
        app.run_server(debug=True, use_reloader=False)

if __name__ == "__main__":
    main()

