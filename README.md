
# Ships CLI Application

This is a Command-Line Interface (CLI) application for interacting with ship data. The application supports various commands, such as displaying countries, showing ships by type, generating histograms of ship speeds, and displaying ship locations on a map.

## Features

- Display a list of countries in the dataset.
- Show the top countries based on ship count.
- View ships grouped by their types.
- Search ships by name.
- Generate a histogram of ship speeds.
- Plot a map of ships with their geographical locations.

## Structure

### Files and Directories

- **`README.md`**: This file, which explains the purpose and usage of the project.
- **`ships_data.json`**: JSON file containing ship data used by the application.
- **`constants.py`**: Contains various constants used across the program (e.g., commands, dataset keys).
- **`input_util.py`**: Utility functions to handle user input and command selection.
- **`load_data.py`**: Functions for loading and accessing ship data from `ships_data.json`.
- **`map_util.py`**: Functions for generating a histogram of ship speeds and drawing maps showing ship locations.
- **`print_util.py`**: Utility functions for displaying information and prompts to the user.
- **`main.py`**: The main entry point of the application, which executes the CLI commands.

## Requirements

- Python 3.x
- Required libraries:
  - `matplotlib`
  - `numpy`
  - `mpl_toolkits.basemap`
  
Install the dependencies using the following command:
```bash
pip install matplotlib numpy basemap
```

## Setup and Usage

1. **Clone the repository**:
   ```bash
   git clone git@github.com:masterschool-weiterbildung/weiterbildung-titanic.git
   cd weiterbildung-titanic
   ```

2. **Run the application**:
   Execute the following command to start the application:
   ```bash
   python main.py
   ```

   Once the program starts, you'll be prompted to enter a command. Available commands are:

   - **`help`**: Displays a list of available commands.
   - **`show_countries`**: Displays a list of unique countries present in the dataset.
   - **`top_countries <num_countries>`**: Displays the top `num_countries` countries with the most ships.
   - **`ships_by_types`**: Displays a list of ship types in the dataset.
   - **`search_ship`**: Prompts you to enter a ship name and searches for ships containing that name.
   - **`speed_histogram`**: Generates a histogram of ship speeds.
   - **`draw_map`**: Displays a map showing ship locations.

3. **Example**:
   To see the top 5 countries with the most ships, enter:
   ```bash
   top_countries 5
   ```

   To search for a ship by name, enter:
   ```bash
   search_ship
   ```

4. **Exit the application**:
   Simply close the terminal or use `Ctrl+C` to stop the program.

## File Description

### **constants.py**

Contains string constants that define commands, dataset keys, and other configuration values. These are used throughout the program to avoid hardcoding strings.

### **input_util.py**

Contains utility functions for:
- Getting user input (`get_user_input_command`).
- Splitting user input into commands and parameters.
- Displaying available options (`display_options`).

### **load_data.py**

Contains functions to:
- Load the ship data from the `ships_data.json` file.
- Fetch the relevant ship data, such as countries, ship types, ship names, and geographical coordinates.

### **map_util.py**

Contains functions for:
- Drawing a histogram of ship speeds.
- Plotting a map showing ship locations using latitude and longitude data.

### **print_util.py**

Contains functions to print introduction messages and display the available options to the user.

### **main.py**

The entry point for the application, responsible for calling the necessary functions based on user input. This script utilizes a dispatcher pattern to invoke the correct function.

---
