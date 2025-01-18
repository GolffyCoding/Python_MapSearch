# Location Map Search

This project is a simple Python application that allows users to search for a location and view it on an interactive map using a graphical user interface (GUI) built with `tkinter`. The map is generated with `folium` and uses `geopy` to geocode the location.

## Features
- Input a location name through a user-friendly GUI.
- Display the location on an interactive map.
- Automatically open the map in the default web browser.
- Handles errors for invalid or empty inputs.

## Requirements
- Python 3.6+
- Installed Python packages:
  - `folium`
  - `geopy`

## Installation
1. Clone the repository or download the script file.
2. Install the required Python packages using pip:
   ```bash
   pip install folium geopy
   ```

## Usage
1. Run the script:
   ```bash
   python map.py
   ```
2. Enter a location in the input field of the GUI and click the "Search" button.
3. The map will be generated and opened in your default web browser.

## Code Overview
### Key Libraries
- **`tkinter`**: Provides the graphical user interface.
- **`folium`**: Generates interactive maps and markers.
- **`geopy`**: Geocodes location names to retrieve latitude and longitude.

### Main Workflow
1. **User Input**: The user inputs a location in the GUI.
2. **Geocoding**: The application uses `geopy` to fetch the coordinates of the entered location.
3. **Map Creation**: An interactive map centered on the location is generated using `folium`.
4. **Display Map**: The map is saved as an HTML file and opened in the browser.

### Example
#### Input:
`New York City`

#### Output:
An interactive map centered on New York City will be displayed in the browser.

## Error Handling
- Displays an error message if:
  - The input field is left empty.
  - The location cannot be found.

## License
This project is licensed under the MIT License. Feel free to use and modify it.

## Acknowledgments
- `folium` documentation: [https://python-visualization.github.io/folium/](https://python-visualization.github.io/folium/)
- `geopy` documentation: [https://geopy.readthedocs.io/](https://geopy.readthedocs.io/)


![Screenshot 2025-01-18 095745](https://github.com/user-attachments/assets/3852ef5b-8cb4-4b7d-9d7f-89d7a2c0a059)
![Screenshot 2025-01-18 095809](https://github.com/user-attachments/assets/b0e3ca64-13f7-4bd9-9861-590a0e9758d4)

