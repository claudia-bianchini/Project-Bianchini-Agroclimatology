***********************************************************************************************************************


# Project Bianchini Agroclimatology
# Author: Bianchini Claudia


***********************************************************************************************************************


## USER GUIDE

### 1. Introduction
### 1.1 Overview
This project focuses on Agroclimatology data of the state of Paraná, Brazil. It includes tools to download and preprocess the dataset, extract relevant information, and visualize the results through a dashboard.

#### 1.2 Project Structure
- **input:** Directory to store input data.
- **output:** Directory to store output data.
- **download_data.py:** Script to check, download, and update the dataset.
- **elaborate_data.py:** Script to extract a subfile with relevant information from the dataset.
- **dash_tot.py:** Script to create a dashboard using Dash.
- **main.py:** Main script to execute the project, including creating directories, checking/downloading the dataset, extracting information, and running the dashboard.
- **sub_data.py:** Script to do additional elaboration on data for visualization. 
- **config.txt:** Configuration file for driver path and binary location.
- **requirements.txt:** File that contains the required dependencies for running the script.
- **README.md:** Documentation file.

### 2. Getting Started
#### 2.1 System Requirements
Before installing *Project-Bianchini-Agroclimatology*, ensure that your system meets the following requirements:
- You must have a computer with Python 3 installed on it.
- You must have internet connection on your computer.
- You must have a browser and its driver installed (preferably Google Chrome).
- You must have a Kaggle account; otherwise, it will be required to create one.

Dataset dimension: 
- agroclimatology.csv: 488.625 KB
- produtividade_soja.csv: 43 KB

[Operating System]: Windows is needed to run the scrip.  
[Processor]: Multi-core processor (e.g., dual-core) is recommended, but with this dataset dimension, also a single core will work.
[RAM]: At least 4 GB of RAM is generally sufficient for basic Python scripts and small to medium-sized datasets.

#### 2.2 Browser Driver Installation
To automate the dataset download process, you need to have the appropriate browser driver installed. Follow the steps below based on your preferred browser:

##### Google Chrome:
1. Download the ChromeDriver executable from [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/).
2. Specify the path to the ChromeDriver executable in the `config.txt` file under the 'Driver Path' configuration.
3. Additionally, provide the path to the Google Chrome binary in the 'Binary Path' configuration in the same `config.txt` file.

Example:
/path/to/chromedriver
/path/to/chrome/binary


##### Other Browsers:
- For browsers other than Chrome, download the appropriate driver and update the configuration accordingly.

#### 2.3 Installation
Follow these steps to install *Project-Bianchini-Agroclimatology*:

1. Open the terminal.
2. Navigate to the directory where you want to save the project (create a dedicated folder for it).
3. Run the following command to clone the project repository:
    ```
    git clone https://github.com/claudia-bianchini/Project-Bianchini-Agroclimatology.git
    ```
4. A Folder called *Project-Bianchini-Agroclimatology* will be downloaded in the selected directory. Enter in the folder.
5. Ensure all required dependencies are installed by running the following command:
    ```
    pip install -r requirements.txt
    ```

#### 2.4 Configuration
Once installed, configure *Project-Bianchini-Agroclimatology*:

1. Open the `config.txt` file in the downloaded folder.
2. Delete the existing content.
3. Provide the local paths for the browser driver and binary as described in Section 2.2.

#### 2.5 Usage
Follow these steps to use *Project-Bianchini-Agroclimatology*:

##### Step 1: Initialization
- Open the Terminal.
- Launch the terminal on your system.
- Navigate to the directory where *Project-Bianchini-Agroclimatology* is installed:


##### Step 2: Run the Application
- Execute the Main Script:
    ```
    python main.py
    ```

##### Step 3: Kaggle log-in
- It may be required to log in to your Kaggle Account to allow the download of the dataset.
- The download process may take some minutes.
- The files will be downloaded in a folder on the Desktop called 'Project-Bianchini-Agroclimatology' to avoid issues during the download.

##### Step 4: Open the Dashboard
- The dashboard can be visualized using a local link. The default one is:
    ```
    http://127.0.0.1:8050/
    ```
- Operation to run the dashboard can take some minutes. Refresh your page if nothing is shown.

##### Step 5: Stop the code
- Open the terminal.
- Click `CTRL + C`.
- Note: When the code stops running, it will be impossible to modify data that are shown in the dashboard.


### 3. Customization Options

**Dropdown Menu:** Use the dropdown menu to select: 
- [Dropdown year/month/day]: Select the date for which the data will be shown on the Map or the year for Histograms.
- [Dropdown variable]: Select the variable to plot in the Map, Histograms, or Lineplot.
- [Dropdown season]: Select the season to plot in the Histograms.

**Map:**
- Click on markers to view detailed information for specific locations.
- Possibility to Zoom and move the Map with the touchpad or the mouse.

**Histograms:** Select on the buttons or on the legend population you want to observe.

**Lineplot:** Select on the button or on the legend population you want to observe.

**Scatterplot:**
- Click once on a specific municipal in the legend: 
    - It will be hidden from the plot if it's visible.
    - It will be shown in the plot if it's hidden.
- Click twice on a specific municipal in the legend:
    - It will be the only one shown if more than one municipal is shown.
    - It will be plotted with all the other municipals if it's the only one plotted.

**Table:** Scroll the table and choose its different pages.

### 4. Troubleshooting

#### 4.1 Common Issues

**[Issue 1]: Unable to Download the Dataset**

This can happen due to modifications on the website. Css_selector may change. Check on the webpage:

- URL: [https://www.kaggle.com/datasets/hugovallejo/agroclimatology-data-of-the-state-of-paran-br/data](https://www.kaggle.com/datasets/hugovallejo/agroclimatology-data-of-the-state-of-paran-br/data)

**Updated Version:**

1. Move the cursor to the higher left part of the page, where the last update is.
2. Right-click on the word 'UPDATED'.
3. Inspect, then right-click and copy the selector.

Write it in the 'download_data.py' file at line 72 with the following syntax:

css_selector = '#site-content > div:nth-child(2) > div > div > div.sc-kriKqB.bdptWe > div.sc-jIXSKn.bdYZfJ > span > span:nth-child(2) > span'

**Sign in Button:**

1. Move the cursor to the higher left part of the page, where the last update is.
2. Right-click on the 'Sign in' button.
3. Inspect, then right-click and copy the selector.

Write it in the 'download_data.py' file at line 160 with the following syntax:

id_sign_in = '#site-container > div > div.sc-cmtnDe.WXA-DT > div.sc-lfeRdP.lgbEgp > div.sc-gglKJF.eeMhNC > div > div:nth-child(1) > a > button > span'

**Download Button:**

1. Move the cursor to the higher left part of the page, where the last update is.
2. Right-click on the word 'Download ()'.
3. Inspect, then right-click and copy the selector.

Write it in the 'download_data.py' file at line 159 with the following syntax:

download_button_selector = '#site-content > div:nth-child(2) > div > div > div.sc-kriKqB.bdptWe > div.sc-jIXSKn.bdYZfJ > div > a > button'

**[Issue 2]: Default Local Link Not Working**

If, after some minutes and refreshing the page, the dashboard fails to open, follow these steps:

1. Open the terminal.
2. Check for the local link.

   Example:
   Dash is running on http://127.0.0.1:8050/
   * Serving Flask app 'dash_tot'
   * Debug mode: on


**[Issue 2]: Default Local Link Not Working**

If for some reason the running is interrupted before the creation of the dashboard, check on the Desktop, in the folder *Project-Bianchini-Agroclimatology* if there are the unzipped file in the subfolder [input]. If yes, the script will work. If there isn't the folder, or there is nothing in the subfolder, or just a .zip file, you must go in subfolder [output] and delete the file [last_update.txt].

### 5. Common Errors

**[Error 1]: Registration response error message: PHONE_REGISTRATION_ERROR**

This error is linked to the connection. Can be showed because if the connection is not perfectly stable and strong it can take some time to move fromo a url to another during the dowloading phase. Attending few seconds everything will be automatically fixed.

### 5. Support and Feedback
For support and feedback, contact our claudia.bianchini@edu.esiee.fr. We value your input and are here to assist you.

### 6. Additional Resources:
-Dataset Link: [https://www.kaggle.com/datasets/hugovallejo/agroclimatology-data-of-the-state-of-paran-br/data]

-Local Dashboard Default Link: [http://127.0.0.1:8050/]

***********************************************************************************************************************


## DATA ANALYSIS

### 1. Analyzed Variables:

- Earth Skin Temperature TS [°C']
- Temperature at 2 Meters T2M [°C]
- Surface Pressure PS[kPa]
- Root Zone Soil Wetness GWETROOT [%]
- Precipitation Corrected PRECTOTCORR ['-']
- All Sky Surface Shortwave Downward Irradiance ALLSKY_SFC_SW_DWN [Wm^2]
- Clear Sky Surface Shortwave Downward Irradiance CLRSKY_SFC_SW_DWN [Wm^2]
- Wind Speed at 2 Meters WS2M [m/s],
- Wind Speed at 10 Meters WS10M [m/s]

### 2. Dashboard:

#### 1. MAP:
Allows visualization of the distribution of analyzed variables in space for every year. The Circle Marker's dimension depends on the productivity of that region in the selected year.

#### 2. HISTOGRAMS:
Allows visualization of how the variable is distributed over seasons and over space for the selected year. The data are divided into subdatasets to observe variations in latitudes and longitudes.

#### 3. LINEPLOTS:
For the selected variable, it is plotted as its mean value for each season along the year. This helps validate the presence of the season.

#### 4. SCATTERPLOT WITH LINEAR REGRESSION:
Shows productivity for each year of every municipal and approximates them with linear regression.

#### 5. TABLE:
Shows the value of predictive productivity for the next 3 years for each municipal, obtained using a 'Linear Mixed Model'.

### 3. Geospatial Insights:

#### Earth Skin Temperature 'TS':
Nothing relevant.

#### Temperature at 2 Meters 'T2M':
Nothing relevant.

#### Surface Pressure 'PS':
In the east region close to the sea, the pressure is lower than elsewhere, almost independent of time.

#### Precipitation Corrected PRECTOTCORR:
Nothing relevant.

#### Wetness of Soil at soja plants' roots GWETROOT:
In the east region close to the sea, the pressure is lower than elsewhere, almost independent of time. Distribution of population divided by latitude seems not to differ, while it's evident a 
flatter behavior for East population compared to West, where data are centered. Wetness of Soil is almost constant in the East Region.

#### All Sky Surface Shortwave Downward Irradiance ALLSKY_SFC_SW_DWN:
Nothing relevant.

#### Clear Sky Surface Shortwave Downward Irradiance CLRSKY_SFC_SW_DWN:
East and North regions are a little bit more irradiated than West and South, respectively.

#### Wind Speed at 2 Meters WS2M:
Stronger in Northern region than in Southern.

#### Wind Speed at 10 Meters WS10M:
Stronger in Northern region than in Southern and in Western region than in Eastern.

#### Soja Productivity:
Nothing relevant.

### 4. Highlight Trends Over Time:

#### Earth Skin Temperature 'TS':
Change over seasons. Observing both latitude and longitude histograms, it's evident a centered distribution where the majority of data move in a range [10°C : 30°C]. 
It's not evident a variation of the center of the distribution when comparing different groups. The difference in temperature in different seasons is evident from the line plot: 
with some exceptions, the higher mean temperatures are always in summer than in spring, autumn, and winter. It's not evident a big change of temperature over the year.

#### Temperature at 2 Meters 'T2M':
Temperature range is a little bit lower in this case than for 'TS', but only of a few degrees. It's possible to observe the same dependence on season. 
This is evident also from the Lineplot: mean value doesn't really change for the two temperatures analyzed.

#### Surface Pressure 'PS':
It's possible to observe that in summer pressure is generally lower than in the other seasons. Mean value of pressure over one year is usually higher in winter,
lower in autumn, and still lower in spring and summer. While for the first two seasons, the ranges are quite separated, there are overlapping in spring and summer. 
But it seems there isn't any correlation with the production of soja.

#### Precipitation Corrected PRECTOTCORR:
Precipitation is distributed quite uniformly during the year. The higher peaks are in spring.

#### Wetness of Soil at soja plants' roots GWETROOT:
This variable is strongly dependent on the season. It grows moving from summer to winter. From the histogram, it's evident a shift moving in different regions, 
but it's not easy to figure out a centered distribution. Looking at the latitude histogram, the two populations seem to have approximately the same distribution, 
while the comparison between East and West populations highlights that in the East region data are more flat. The distribution is more centered for West population. 
From the line plot, it's hard to find a correlation with the season. It's more interesting observing productivity in this case. From the graph, it seems that when the humidity is always low (2012)
or changes a lot during the year (2005, 2008), so when seasons change, the productivity will decrease.

#### All Sky Surface Shortwave Downward Irradiance ALLSKY_SFC_SW_DWN:
There is a big separation during the season along the year. During Summer and Spring All Sky Irradiance is a lot higher than in Autumn and Winter.

#### Clear Sky Surface Shortwave Downward Irradiance CLRSKY_SFC_SW_DWN:
Like the All Sky Irradiance, there is a big range difference between Summer and Spring values and Winter and Autumn ones.

#### Wind Speed at 2 Meters WS2M:
The strongest wind is in Spring and Winter. There are some low peaks that mix with the lower value's population.

#### Wind Speed at 10 Meters WS10M:
The strongest wind is also in this case in Spring and Winter, but ranges are not well separated as for WS2M.

#### Soja Productivity:
Scatterplot highlights a general growing trend for the productivity of soja over the years.

### 6. Conclusion

#### 1. Summarize Key Findings:

After a comprehensive exploration of the agroclimatology dataset for Paraná, Brazil, the dashboard has provided valuable insights into the spatial and temporal dynamics of key variables. The stronger finded dependece for soja production is time. It's evidet from scatterplot a linear dependance between these two variables and the fact that for the majority of the municipals there is a growing trend. This is the unique strong relation highlighted by data, and it's the only one that we can use to estimate the produtivity for next years. 
Finding relation with the other variables it's harder. Lineplot give information about the effective presence of the season, which wasn't obvious at that latitude. It also highlight the independence between the local productivity and the mean value of parameter in the region, even if the region is not that big. Also the presence of the sea in the east is significant only for some variables (Wetness of Soil at soja plants' and Surface Preassure). 
From this conclusion it's possible to assume that there are other factors that are not in the dataset (like the increasing of coltivated field area or introduction of new agricultural techniques) that are responsable for the increasing of the productivity over years.


#### 2. Future Directions:

Further analysis on this dataset can be computed to find a stronger relation between the variables and the soja_production.
It can be good implementing plots that shows dependance between the measured variables.
More detailed studies for singolar municipal can lead to better estimation to relation between parameter.
Another interesting step can be dynamically observing, with an automatic sweep along days, the Map.
Looking for additional data of different types can give better results.


***********************************************************************************************************************


## DEVELOPER GUIDE

A more detailed description of the project may be needed for modifying and acting on *Project-Bianchini-Agroclimatology*. 
The script is organized in modules. The developer can have a live description on what a module is doing by setting to True the global variable [debug]:

DEBUG = True

Moduls are:
### main.py

This Python module serves as the main entry point for 'Project Bianchini Agroclimatology.' The module orchestrates the entire workflow of the project, including creating a project directory, checking and downloading a dataset from a specified URL, extracting relevant information, and visualizing results through a dashboard using Dash.

#### Functions:

1. **Creating Project Directory:**
   - `create_project_directory`: Creates a project directory on the user's desktop, containing subdirectories for input and output data.

2. **Reading Configuration:**
   - `read_config`: Reads configuration information from a file named config.txt, extracting paths for a driver and binary location.

3. **Main Workflow:**
   - `main`: Orchestrates the entire workflow, defining the project path, input and output folders, and calling functions to set up the directory structure, download the dataset, extract relevant information, and create a Dash dashboard.

4. **Dashboard Execution:**
   - Checks if being run as the main module and, if so, runs the Dash app using app.run_server.

### download_data.py

This module handles checking, downloading, and unzipping a dataset from a specified webpage. It utilizes the Selenium library for web automation.

#### Functions:

1. `initialize_driver`: Initializes a Chrome WebDriver with custom settings.
2. `find_last_update`: Finds the last update date on the webpage using a CSS selector.
3. `check_last_update`: Checks if the dataset is updated based on the last update date.
4. `download_dataset`: Initiates the download of the dataset from the specified URL.
5. `unzip_file`: Unzips a specified .zip file in the given directory.
6. `dataset_check_download`: Orchestrates the entire process, including checking the last update date, downloading, and unzipping.

### elaborate_data.py

This module processes and extracts data from CSV files. It provides functions to read, filter, and manipulate data, creating a processed DataFrame saved as a CSV file.

#### Functions:

1. `find_and_read_csv`: Finds all CSV files, sorts them, and reads the largest and smallest into two DataFrames.
2. `filter_rows`: Filters rows based on specified productivity years.
3. `drop_columns`: Drops unnecessary columns.
4. `assign_date`: Assigns 'year', 'month', and 'day' columns based on the 'date' column.
5. `add_name_ibge`: Merges two DataFrames, adding the 'name_ibge' column.
6. `assign_seasons`: Assigns a 'season' column based on 'year', 'month', and 'day'.
7. `extract_subfile`: Orchestrates the entire process of reading and processing CSV files, assigning date-related columns, filtering rows, dropping unnecessary columns, adding the 'name_ibge' column, and assigning a 'season' column.

### dash_tot.py

This module is part of a Dash web application for visualizing agroclimatology data. It integrates various functions to create an interactive web application.

#### Functions:

1. `generate_colormaps`: Generates LinearColormap objects for numeric columns in the DataFrame.
2. `create_map`: Creates a Folium map based on the provided DataFrame and color information.
3. `update_map`: Updates the Folium map based on selected options.
4. `update_histogram`: Updates histograms based on selected options.
5. `update_lineplot`: Updates the line plot based on selected options.
6. `remove_outlier_indices`: Removes outliers from the DataFrame using the interquartile range (IQR) method.
7. `productivity_scatter_and_prediction`: Creates a scatter plot of productivity data and makes predictions using a mixed-effects model.
8. `create_dash`: Creates a Dash web application for visualizing agroclimatology data.

### sub_data.py

This module provides functions for data normalization, dataset division based on coordinates, and extracting structured productivity data from given DataFrames.

#### Functions:

1. `find_normalized_productivity`: Finds and normalizes productivity values for a selected year.
2. `normalize_values`: Normalizes values in a dictionary to a specified range.
3. `divide_dataset`: Divides the dataset into north, south, east, and west regions based on coordinates.
4. `productivity_to_df`: Extracts and structures productivity data from given DataFrames.

These modules collectively form the backbone of the project, providing functionalities for data processing, visualization, and interaction through the Dash web application.
