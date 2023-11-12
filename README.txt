# Project Bianchini Agroclimatology

1. Introduction
1.1 Overview
This project focuses on Agroclimatology data of the state of Paraná, Brazil. It includes tools to download and preprocess the dataset, 
extract relevant information, and visualize the results through a dashboard.

1.2 Project Structure

- **input:** Directory to store input data.
- **output:** Directory to store output data.
- **download_data.py:** Script to check, download, and update the dataset.
- **elaborate_data.py:** Script to extract a subfile with relevant information from the dataset.
- **dash_tot.py:** Script to create a dashboard using Dash.
- **main.py:** Main script to execute the project, including creating directories, checking/downloading the dataset, extracting information, and running the dashboard.
- **sub_data.py:** Script to do additional elaboration on data for visualization. 
- **config.txt:** Configuration file for driver path and binary location.
- **requirements.txt:** file that contain the required dependencies for runniing the script.
- **README.md:** Documentation file.

1.3 Key Features
Feature 1: [Description of Feature 1]
Feature 2: [Description of Feature 2]
...


2. Getting Started
2.1 System Requirements
Before installing [Project Bianchini Agroclimatology], ensure that your system meets the following requirements:
- You must have a computer and have Python 3 installed on it.
- You must have a browser and its driver installed (preferibly Google Chrome)
- You must have a Kaggle account, otherwise it will be required to create one

Dataset dimension: 
    - agroclimatology.csv: 488.625 KB
    - produtividade_soja.csv: 43 KB

    [Operating System]: Python is cross-platform and can run on Windows, macOS, and Linux.  
    [Processor]: Multi-core processor (e.g., dual-core) is recommended, but with this dataset dimension also a single core will work.
    [RAM]: At least 4 GB of RAM is generally sufficient for basic Python scripts and small to medium-sized datasets.

2.2 Installation
Follow these steps to install [Project Bianchini Agroclimatology]:

[Step 1]: Open the terminal 
[Step 2]: Define the directory where you want to save the project {Suggestion: create a dedicated folder on the Desktop called 'Project Bianchini Agroclimatology'}
[Step 3]: Write in the terminal the command:
    
    $ git clone adresse_publique_de_votre_projet

[Step 4]: Assure that all the required dependencies are installed writing in the terminal the command:
    
    pip install -r requirements.txt


2.3 Configuration
Once installed, configure [Project Bianchini Agroclimatology]:

[Configuration Step 1]: Open file config.txt in the dowloaded folder
[Configuration Step 2]: Delete the content of the file 
[Configuration Step 3]: Write in the first line -> the local path for the executive file of driver of the browser you want to use for the automatic dowload of the dataset
                        Write in the second line -> local binary path for the executive file of the same browser
                
                It should look like:
                    /path/to/driver
                    /path/to/binary

                Example:
                    C:/Users/claud/Documents/Chromedriver/chromedriver.exe
                    C:/Program Files/Google/Chrome/Application/chrome.exe


3. Using the Application
3.1 User Interface
The main components of the user interface:

[Terminal]: The terminal is a command-line interface where you interact with the backend of the application. 
            It provides a text-based environment for executing commands and managing various aspects of the application. 
            In [Project Bianchini Agroclimatology], the terminal is used for tasks such as configuration, data processing, and running scripts.

[Dashboard]: The dashboard is the graphical user interface (GUI) of [Project Bianchini Agroclimatology], providing an interactive and visual representation 
            of the data and analysis results. It allows users to explore, analyze, and visualize data in an intuitive way.

            Key Components:
                - Map: Displays a geographical map with markers representing data points. It provides a visual overview of spatial distribution.
                - Histograms: Show the distribution of selected variables over space and time. Users can customize parameters for in-depth analysis.
                - Lineplots: Present the mean values of a variable across different seasons throughout the year.
                - Scatterplot with Linear Regression: Displays a scatterplot of data points with a fitted linear regression line, aiding in understanding trends and correlations.
                - Table: Provides tabular data, including predicted productivity values for the next three years using a Linear Mixed Model.

            The dashboard is designed for an easy and insightful exploration of agroclimatology data, facilitating data-driven decision-making.


3.2 Workflow
Explain the typical workflow for users:

[Step 1]: Initialization
            Open the Terminal
            Launch the terminal on your system.
            Navigate to the directory where [Project Bianchini Agroclimatology] is installed.

                cd /path/to/your/project

[Step 2]: Run the Application
            Execute the Main Script:    

                python main.py


[Step 3]: Kaggle log-in
            It can be required to log in you Kaggle Account to allow the download of the dataset.
            Downlod process can require some minutes.
            The files will be downloaded in a folder on the Desktop called 'Project Bianchini Agroclimatology'. 
            This will avoid issues during the download. 

[Step 4]: Open the Dashboard:
            The dashboard can we visualized using a local link. The default one is:

                http://127.0.0.1:8050/
            
            Operation to run the dashboard can require some minutes. Refresh your page is 
            nothing is show.

[Step 5]: Stop the code:
            Open the terminal 
            Click CTRL + C

            NB: When the code will stop running, it will be impossible to modify data that are shown in the dashboard.


3.3 Customization Options
Detail any options users have for customizing their experience:

Dropdown Menu: Use the dropdown menu to select: 
    [Dropdown year/month/day]:  - Select the date for which the data will be shown on the Map
                                - Select the year for Histograms

    [Dropdown variable]:        - Select the variable to plot in the Map
                                - Select the variable to plot in the Histograms
                                - Select the variable to plot in the Lineplot 

    [Dropdown season]:          - Select the season to plot in the Histograms     


[Map]:  - Click on markers to view detailed information for specific locations
        - Possibility to Zoom and move the Map with the touchpad or the mouse

[Histograms]: Select on the buttons or on the legend population you want to observe

[Lineplot]: Select on the button or on the legend population you want to observe

[Scatterplot]: - Click one time on a specific municipal in the legend: 
                    it will be hide from the plot if it's visible
                    it will be shown in the plot if it's hidden

                - Click two time on a specific municipal in the legend:
                    it will be the only one shown it more than one municiapl is shown
                    it will be plot with all the other municipal it it's the only one plotted
 
[Table]: Scroll the table and choose its different pages


4. Troubleshooting
4.1 Common Issues
List and provide solutions for common issues users may encounter:

[Issue 1]: There is no possibility to dowload the dataset
            This can happen due to modification on the website. Css_selector can change, check on the webpage:ù

            url = https://www.kaggle.com/datasets/hugovallejo/agroclimatology-data-of-the-state-of-paran-br/data

            UDATED VERSION:
                Move the cursor in the higher left part of the page, where is the last update. 
                    Upon the word 'UPDATED' 
                    Right Click
                    Inspect
                    Right Click
                    Copy
                    Copy selector 

                You shoud have something similar:
                    #site-content > div:nth-child(2) > div > div > div.sc-kriKqB.bdptWe > div.sc-jIXSKn.bdYZfJ > span > span:nth-child(2) > span 

                    write it in file 'download_data.py' at line 53 with the followinig syntax:

                    example:
                    css_selector = '#site-content > div:nth-child(2) > div > div > div.sc-kriKqB.bdptWe > div.sc-jIXSKn.bdYZfJ > span > span:nth-child(2) > span'
                    
            SIGN IN BUTTON:
                Move the cursor in the higher left part of the page, where is the last update. 
                    Upon the button 'Sign in' 
                    Right Click
                    Inspect
                    Right Click
                    Copy
                    Copy selector

                You shoud have something similar:
                    #site-content > div:nth-child(2) > div > div > div.sc-kriKqB.bdptWe > div.sc-jIXSKn.bdYZfJ > span > span:nth-child(2) > span  

                    write it in file 'download_data.py' at line 131 with the followinig syntax:
                    
                    example:
                    id_sign_in = '#site-container > div > div.sc-cmtnDe.WXA-DT > div.sc-lfeRdP.lgbEgp > div.sc-gglKJF.eeMhNC > div > div:nth-child(1) > a > button > span'

                    
            DOWNLOAD BUTTON:
                Move the cursor in the higher left part of the page, where is the last update. 
                    Upon the word 'Download ()' 
                    Right Click
                    Inspect
                    Right Click
                    Copy
                    Copy selector

                You shoud have something similar:
                    #site-content > div:nth-child(2) > div > div > div.sc-kriKqB.bdptWe > div.sc-jIXSKn.bdYZfJ > span > span:nth-child(2) > span  
                    
                    write it in file 'download_data.py' at line 130 with the followinig syntax:
                    
                    example:
                    download_button_selector = '#site-content > div:nth-child(2) > div > div > div.sc-kriKqB.bdptWe > div.sc-jIXSKn.bdYZfJ > div > a > button'


[Issue 2]: It can happen that the default local link will not work. 
            If after some minutes and after refreshing the page the dashboard will not be opened:
            Open the terminal 
            Check for the local link

            example:
                Dash is running on http://127.0.0.1:8050/

                * Serving Flask app 'dash_tot'
                * Debug mode: on
            
            Copy the link or click on it to open the dashboard.


4.2 Error Messages
Explain the meanings of common error messages and how to resolve them:

[Error Message 1]
[Error Message 2]


6. Support and Feedback
For support and feedback, contact our [claudia.bianchini@edu.esiee.fr]. We value your input and are here to assist you.


7. Additional Resources
link to the dataset: https://www.kaggle.com/datasets/hugovallejo/agroclimatology-data-of-the-state-of-paran-br/data
link to the default local path: http://127.0.0.1:8050/


*********************************************************************************************

DATA ANALYSIS:
1. Analyzed variables:

    - Earth Skin Temperature TS [°C']
    - Temperature at 2 Meters T2M [°C]
    - Surface Pressure PS[kPa]
    - Root Zone Soil Wetness GWETROOT [%]
    - Precipitation Corrected PRECTOTCORR ['??']
    - All Sky Surface Shortwave Downward Irradiance ALLSKY_SFC_SW_DWN [??]
    - Clear Sky Surface Shortwave Downward Irradiance CLRSKY_SFC_SW_DWN [??]
    - Wind Speed at 2 Meters WS2M [??],
    - Wind Speed at 10 Meters WS10M [??]

2. Dashboard:
In the dashboard there are many plots: 

    1. MAP: allow to visualize the distribution of the analyzed variables in space for every year. The Circle Marker's dimension depend 
        on the productivity of that region in the selected year.

    2. HISTOGRAMS: allows to visualize how the variable is distributed over seasons and over space for the selected year. The data were devided in 
                subdataset to observe variation in latitudes and longitudes. The observation can be done by comparing North-South and East-West. Latitude dataset 
                division can be intrested beaìcasue Sun will different hit the Earth, while longitudes can be interesting  due to the presence of the sea. 
                Different varibales distribution can lead to differnt production.

    3. LINEPLOTS: for the selected variable it is plotted it's mean value for each season along the year. This also to validate the presence of the season: 
        this reagin iss in fact close to Equator.

    4. SCATTERPLOT WITH LINEAR REGRESSION: from data we have informations about variables from 2003 to 2020, while we have data for productivity only from 2004 to 2017.
                                    This scatterplot show the productivity for each year of every municipal and approximate them with linea regression. 

    5. TABLE: value of predictive productivity for the next 3 years each municipal are showed. They are obtained using a 'Linear Mixed Model'.

3. Geospatial Insights:
    It's possible to analyze data in space both observing the Map and the Histograms:

    - Earth Skin Temperature 'TS': Nothing relevant

    - Temperature at 2 Meters 'T2M': Nothing relevant

    - Surface Preassure 'PS': In the eatest region close to the sea the preassure is lower than elsewhere, almost independent on time.

    - Precipitation Corrected PRECTOTCORR: Nothin relevant

    - Wetness of Soil at soja plants' roots GWETROOT: In the eatest region close to the sea the preassure is lower than elsewhere, almost independent on time. 
        Distribution of population devided by latitude seem don't differ, while it's evident a flatter behaviour for East population repsect West one, where data are centered. 
        Wetness of Soil is almost constant in East Region.

    - All Sky Surface Shortwave Downward Irradiance ALLSKY_SFC_SW_DWN: Nothing relevant

    - Clear Sky Surface Shortwave Downward Irradiance CLRSKY_SFC_SW_DWN: East and North region are a little bit more irradiated respect West and South respectivly.

    - Wind Speed at 2 Meters WS2M: Stronger in Norther region instead of Souther

    - Wind Speed at 10 Meters WS10M: Stronger in Norther region insted of Souther
        and in Wester region insted on Easter. 

    - Soja Productivity: Nothing Relevant




4. Highlight Trends Over Time:
    It's possible to analyze data in time observing the Map, the Histograms, the Lineplot and the Scatterplot:

    - Earth Skin Temperature 'TS': change over season. Observing both latitude and longitude histograms it' evident a centered distribution 
        where the majority of data move in a range [10°C : 30°C]. It's not evident a variation of the center of the distribution when comparing in
        the same histogram different groups.
        The difference in temperature in different season is evident from the lineplot: with some exceptions, the higher mean temperature are always in summer
        than spring, autumn and winter. It's not evident a big change of temperature over year.

    - Temperature at 2 Meters 'T2M': temperature range is a little bit lower in this case than for 'TS', but only of few degrees. It's possible to observe the same dependance
        on season.This is evdent also from the Lineplot: mean value doen't really change for the two temperature anlyzed.

    - Surface Preassure 'PS': it's possible to observe that in Summer preassure is generally lower than in the other season.
                Mean value of preassure over one year is usually higher in winter, lower in Autumn and still lower iin Spring and Summer. 
                While for the firsts two seasons the range are quite separated, there are overcrossing in Spring and Summer. 
                But it seem there isn't any correlation with the production of soja.


    - Precipitation Corrected PRECTOTCORR: Precipitation are distributetd quite uniformly during the year. The higher peak are in Spring.

    - Wetness of Soil at soja plants' roots GWETROOT: this variable is strongly depend on season. It grows moving from summer to winter. 
                From histogram it's evident a shift moving in different regions but it's not easy to figure out a centered distribution. 
                Looking at the latitude histogram the two population seem to have approximatly the same distribution, while the comparison between East and West
                poplations highlights that in East region data are more flat. The distribution is more centered for West population.  
                From the lineplot it's hard to find a correlation with season. It's more interesting observing productivity in this case.
                From the graph it seem that when the humidy is always low (2012) or change a lot during the year (2005, 2008), so when season change, the productivity will decrease. 


    - All Sky Surface Shortwave Downward Irradiance ALLSKY_SFC_SW_DWN: There is a big separation during seasoon along the year. During Summer and Spring All Sky Irrandiance
        is a lot higher than in Autumn and Winter. 

    - Clear Sky Surface Shortwave Downward Irradiance CLRSKY_SFC_SW_DWN: Like the All Sky Irradiance there is a big range difference between Summen and Spring values and WInter and Autumn ones.

    - Wind Speed at 2 Meters WS2M: The strongest wind is in Spring and Winter. There are some low peak that mixed with the lower value's population.
    
    - Wind Speed at 10 Meters WS10M: The strongest wind is also in this case in Spring and Winter, but ranges are not well sepered as for WS2M.
    
    - Soja Productivity: Scatterplot highlight a general growing trend for the productivity of soja over year. 

5. Intresting trends

6. Conclusion
1. Summarize Key Findings:
Begin by summarizing the main findings from the dashboard. Highlight any patterns, trends, or outliers that are evident in the visualizations.

7. Future Directions:
    Further analysis on this dataset can be compute to find a stronger relation between the variables and the soja_production. It could take more result using a multivariable approach
    to the problem. Investigating considering more than one measured variables can lead to more intrested results.


Example Conclusion:
"After a comprehensive exploration of the agroclimatology dataset for Paraná, Brazil, the dashboard has provided valuable insights into the spatial and temporal 
dynamics of key variables. The analysis revealed notable trends in temperature and precipitation, with distinct seasonal patterns observed over the years. Geospatial 
visualizations highlighted clusters of high and low productivity regions, suggesting potential correlations with specific climatic conditions. While these findings 
contribute to our understanding of the agroclimatic factors influencing soja production, it's essential to acknowledge the limitations in data granularity and potential 
biases. Moving forward, further investigations into specific climatic events and their impact on productivity could enhance our predictive capabilities. 
The insights derived from this dashboard have significant implications for agricultural decision-making, providing a foundation for informed strategies in soja 
production in the region."











**********************************************************************************************************


DEVELOPER GUIDE:

A more detailed description of the project can be needed to modify and act on [Project Bianchini Agroclimatology].
The script is organized in modules:

- main.py: This Python module serves as the main entry point for the 'Project Bianchini Agroclimatology.' 
    The module orchestrates the entire workflow of the project, which involves creating a project directory, checking and downloading a dataset from a specified URL, 
    extracting relevant information from the dataset, and finally visualizing the results through a dashboard using Dash.
    
    Functionality and main functions:

    1. Creating Project Directory:
    The create_project_directory function is responsible for creating a project directory on the user's desktop. 
    This directory contains subdirectories for input and output data. If the 'Project' directory or its subdirectories already exist, it will use the already existing ones.

    2. Reading Configuration:
    The read_config function attempts to read configuration information from a file named config.txt. 
    It extracts the paths for a driver and binary location, presumably related to web scraping or automated browsing.
    
    3. Main Workflow:
    The main function puts everything together. 
    It defines the project path, input and output folders, and calls the create_project_directory function to set up the directory structure.
    It specifies the URL of the dataset on Kaggle.
    It reads the configuration from config.txt using the read_config function.
    It checks and downloads the dataset using the dataset_check_download function.
    It extracts relevant information from the dataset using the extract_subfile function.
    It creates a Dash dashboard using the create_dash function, visualizing the extracted data.
    
    4. Dashboard Execution:
    The script checks if it's being run as the main module (__name__ == "__main__") and, if so, runs the Dash app using app.run_server.
    In summary, the module automates the setup of a project directory, handles dataset download and extraction, and presents the results through a web-based dashboard 
    using Dash. The configuration details for web scraping are read from a file, and the entire workflow is encapsulated within the main function.


- dowload_data.py: This module is designed to handle the process of checking, downloading, and unzipping a dataset from a specified webpage. 
    It utilizes the Selenium library to automate interactions with a web page, specifically a Kaggle dataset page in this case.

    Functionality of functions

    1. initialize_driver(): 
    - **Input:** 
        String Variable (`local_directory`): Local directory for downloads.
        String Variable (`chrome_driver_path`): Path to the Chrome WebDriver.
        String Variable(`chrome_binary_location`): Path to the Chrome binary.
    - **Output:**
        webdriver.Chrome: Instance of the Chrome WebDriver.
    - **Description:** This function initializes a Chrome WebDriver with custom settings. It configures the download directory for Chrome and sets the paths to the Chrome binary and WebDriver.

    2. find_last_update(): 
    - **Input:**
        String Variable (url): URL of the webpage to scrape.
        webdriver.Chrome (driver): Instance of the Chrome WebDriver.
    - **Output:**
        String Variable (target_element.text): Last update date found on the webpage.
    - **Description:** This function opens the specified URL in the Chrome browser and uses a CSS selector to locate and extract the last update date from the webpage.

    3. check_last_update():
    - **Input:**
        String Variable (update_date): Last update date of the dataset.
        String Variable (url): URL of the webpage to check for the dataset.
        webdriver.Chrome (driver): Instance of the Chrome WebDriver.
        String Variable (input_directory): Local directory for downloads.
        String Variable (output_directory ): Local directory to store the last update file.
    - **Output:**
        String Variable (sip_file_name): Name of the downloaded ZIP file.
    - **Description:** This function checks if the dataset is updated by comparing the last update date obtained from the webpage with the stored last checked date. 
        If the dataset is updated, it triggers the download of the new version.

    4. download_dataset():
    - **Input:**
        String Variable (dataset_url): URL of the webpage to check for the dataset.
        webdriver.Chrome (driver): Instance of the Chrome WebDriver.
         String Variable (local_directory): Local directory for downloads.
    - **Output:**
        String Variable (sip_file_name): Name of the downloaded ZIP file.
    - **Description:** This function initiates the download of the dataset from the specified URL. 
        It interacts with the webpage, clicks on the download button, and waits for the download to complete. 
        If a login form is encountered, it prompts the user to manually log in.

    5. unzip_file():
    - **Input:**
        String Variable (directory): Directory where the .zip file is located.
        String Variable (zip_file_name): Name of the .zip file to be extracted.
    - **Output:**
        None
    - **Description:** This function unzips a specified .zip file in the given directory.

    6. dataset_check_download():
    - **Input:**
        String Variable (url): URL of the webpage to check for the dataset.
        String Variable (input_directory): Local directory for downloads.
        String Variable (output_directory ): Local directory to store the last update file.
        String Variable (chrome_driver_path): Path to the Chrome WebDriver.
        String Variable (chrome_binary_location): Path to the Chrome binary.
    - **Output:**
        None
    - **Description:** This function orchestrates the entire process for this module. 
        It initializes the Chrome WebDriver, finds the last update date, checks and downloads the dataset if it's updated, and then unzips the downloaded dataset.

The module aims to automate the process of dataset retrieval, making it more convenient for users. 
It's designed with considerations for handling potential challenges, such as login prompts and checking for the last update date to determine whether a new download is necessary.


- elaborate_data.py: This module is designed for data processing and extraction from CSV files. 
    It provides several functions to read, filter, and manipulate data, ultimately creating a processed DataFrame that is saved as a CSV file.
    
    Functionality and main functions

    1. **find_and_read_csv():**
    - **Input:**
        String Variable (directory): The directory path where CSV files are located.
    - **Output:**
        DataFrame (df): DataFrame read from the largest CSV file.
        DataFrame (df_soja): DataFrame read from the smallest CSV file.
    - **Description:** Finds all CSV files in the specified directory, sorts them based on size, and reads the largest and smallest files into two DataFrames.

    2. **filter_rows():**
    - **Input:**Args:
        DataFrame (dataframe): The DataFrame to filter.
        List (productivity_years): List of years considered as productivity years.
    - **Output:**
        DataFrame (dataframe): Filtered DataFrame containing rows only with 'year' values present in productivity_years.
    - **Description:** Filters rows in the DataFrame based on a specified list of productivity years, allowing users to focus on a specific time range.

    3. **drop_columns():**
    - **Input:**
        DataFrame (dataframe): The DataFrame to process.
        List (columns_to_keep): List of columns to keep in the DataFrame.
    - **Output:**
        pd.DataFrame: DataFrame after dropping columns not in the columns_to_keep list.
    - **Description:** Drops columns in the DataFrame that are not in the specified list of columns to keep, allowing users to retain only relevant information.

    4. **assign_date():**
    - **Input:**
        DataFrame (dataframe): The DataFrame to process.
    - **Output:**
        pd.DataFrame: DataFrame with 'year', 'month', and 'day' columns added.
    - **Description:** Assigns 'year', 'month', and 'day' columns based on the 'data' column in the DataFrame, facilitating time-based analysis.

    5. **add_name_ibge():**
    - **Input:**
        DataFrame (df): The primary DataFrame.
        DataFrame (df_soja): The secondary DataFrame.
    - **Output:**
        pd.DataFrame: Merged DataFrame with 'name_ibge' column added.
    - **Description:** Merges two DataFrames, adding the 'name_ibge' column to the primary DataFrame based on the 'codigo_ibge' column.

    6. **assign_seasons():**
    - **Input:**
        DataFrame (dataframe): The DataFrame to process.
    - **Output:**
        DataFrame (dataframe): DataFrame with 'season' column added
    - **Description:** Assigns a 'season' column based on the 'year', 'month', and 'day' columns, categorizing each entry into a specific season.
    This function contains another function that lead to the definition of the season: 
        **assign_season():**
        - **Input:**
            Series (row): single row of the input dataframe
        - **Output:**
            String Variable (season): The assigned season based on the specified periods.


    7. **extract_subfile():**
    - **Input:**
        String Variable (input_folder): The directory path containing input CSV files.
        String Variable (output_folder): The directory path to save the processed CSV file.
    - **Output:**
        DataFrame (df): The processed DataFrame.
        DataFrame (df_soja): Secondary DataFrame for additional processing.
    - **Description:** This function orchestrates the entire process for this module.
        Reads and processes CSV files from the specified input folder. 
        It assigns date-related columns, filters rows based on productivity years, drops unnecessary columns, adds the 'name_ibge' column, and assigns a 'season' column. 
        The resulting DataFrame is saved to a CSV file in the specified output folder.

These functions are designed to streamline the data processing workflow, making it easier for users to handle and analyze CSV datasets. 
The modular structure allows users to choose specific processing steps based on their requirements. 
Additionally, error handling is incorporated to provide informative messages in case of unexpected issues.

- dash_tot.py: This Python module appears to be part of a Dash web application designed for visualizing agroclimatology data related to Paranà, Brazil. 

    Below is a summary of the main functions and their behavior:

    1. **`generate_colormaps()`**
    - **Input:** DataFrame (`df`), List of variables (`variables`)
    - **Output:** Dictionary of LinearColormap objects (`colormaps`)
    - **Description:** Generates LinearColormap objects for numeric columns in the DataFrame, based on the specified list of variables.

    2. **`create_map()`**
    - **Input:** DataFrame (`df`), Dictionary (`color_dict`), LinearColormap (`colormap`), Selected variable (`selected_var`), Variable details (`variable_details`)
    - **Output:** HTML representation of the Folium map (`map_html`)
    - **Description:** Creates a Folium map based on the provided DataFrame and color information. The map includes CircleMarker elements representing geographical data.

    3. **`update_map()`**
    - **Input:** DataFrame (`df`), DataFrame (`df_soja`), Selected year (`selected_year`), Selected month (`selected_month`), Selected day (`selected_day`),
     Selected variable (`selected_var`), Variable details (`variable_details`), LinearColormap (`colormap`)
    - **Output:** HTML representation of the updated Folium map (`map_html`)
    - **Description:** Updates the Folium map based on selected options, including filtering data based on the selected date and updating colors.

    4. **`update_histogram()`**
    - **Input:** Selected year (`selected_year`), Selected season (`selected_season`), Selected variable (`selected_var`), Variable details (`variable_details`), 
    Grouped data for North (`north_data_year`), South (`south_data_year`), East (`east_data_year`), West (`west_data_year`)
    - **Output:** Two Plotly figures representing North/South and East/West histograms (`fig_north_south`, `fig_east_west`)
    - **Description:** Updates histograms based on selected options, including options to show North/South and East/West histograms.

    5. **`update_lineplot()`**
    - **Input:** Selected variable (`selected_var`), Variable details (`variable_details`), DataFrame (`df`), DataFrame (`df_soja`)
    - **Output:** Plotly line plot figure (`scatter_fig`)
    - **Description:** Updates the line plot based on selected options, including a dropdown menu for selecting seasons.

    6. **`remove_outlier_indices()`**
    - **Input:** DataFrame (`df`)
    - **Output:** Boolean series (`true_list`)
    - **Description:** Removes outliers from the DataFrame using the interquartile range (IQR) method.

    7. **`productivity_scatter_and_prediction()`**
    - **Input:** DataFrame (`df`), DataFrame (`df_soja`)
    - **Output:** Tuple containing Scatter plot figure (`scatter_fig`) and DataFrame with predictions (`predictions_df`)
    - **Description:** Creates a scatter plot of productivity data and makes predictions using a mixed-effects model.

    8. **`create_dash()`**
    - **Input:** DataFrame (`df`), DataFrame (`df_soja`)
    - **Output:** Dash application (`app`)
    - **Description:** Creates a Dash web application for visualizing agroclimatology data. The application includes various components such as dropdowns, maps, histograms, line plots, scatter plots, and a data table. The layout and behavior are defined based on the provided DataFrames.

This module integrates various functions to create an interactive web application for exploring and visualizing agroclimatology data in the context of Paranà, Brazil. 
The application uses the Dash framework and includes components for filtering data, generating maps, histograms, line plots, scatter plots, and displaying predictions.

- sub_data.py: This module provides functions for data normalization, dataset division based on coordinates, and extracting structured productivity data from given DataFrames. 
Additionally, it includes a function for creating a normalized productivity DataFrame for a selected year.

    Functions:
    1. `find_normalized_productivity()`: 
    - **Input:** DataFrame (`sub_data_unique_coord`) containing unique coordinates and 'name_ibge' columns
        DataFrame (`df_soja`) containing 'name' column and productivity values for various years,
        String Variable (`selected_year`) for which productivity values need to be normalized.
    - **Output:** Dataframe (`merged_df`) containing normalized productivity values for the selected year
    - **Description:** Finds and normalizes productivity values for a selected year.
     
     
    2. `normalize_values()`: 
    - **Input:** Dictionary (`data`) with keys as column names and values as the original data, 
        Float Variable (`new_min`) and  Float Variable(`new_max`) representing the minimum and maximum values of the normalized scale
    - **Output:** Dictionary (`normalized`) containing normalized values within the specified rangeDataframe
    - **Description:** Normalizes values in a dictionary to a specified range. 
    

    3. `divide_dataset()`: 
    - **Input:** Dataframe (`df`) with geographical data
        Float Variable (`new_min`) and  Float Variable(`new_max`) representing the minimum and maximum values of the normalized scale
    - **Output:** list of DataFrames for north, south, east, and west regions
    - **Description:** Divides the dataset into north, south, east, and west regions based on coordinates.


    4. `productivity_to_df()`: 
    - **Input:** Dataframe (`df`) primary DataFrame with geographical data
        Dataframe (`df_soja`) secondary DataFrame with productivity data.
    - **Output:** list of DataFrames for north, south, east, and west regions
    - **Description:** Extracts and structures productivity data from the given DataFrames. 


