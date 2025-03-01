
# ECG Heart Rate Analyzer

This project is an ECG Heart Rate Analyzer that allows users to load ECG data from a CSV file, calculate heart rates, and visualize the ECG signal with R-peaks. The application is built using Python and Tkinter for the GUI, and it uses libraries such as NumPy, Pandas, Matplotlib, and SciPy for data processing and visualization.

## Features

- Load ECG data from a CSV file
- Calculate heart rates from the ECG data
- Display the average heart rate and individual heart rates
- Visualize the ECG signal with R-peaks
- User-friendly GUI with Tkinter
- Help information for users

## Requirements

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- SciPy
- Tkinter

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ecg-heart-rate-analyzer.git
    cd ecg-heart-rate-analyzer
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python ecg.py
    ```

2. Click the "Import ECG Data" button to load a CSV file containing ECG data. The CSV file should have a column named 'ECG' with the ECG signal values.

3. The application will calculate the heart rates and display the average heart rate and individual heart rates in the text box.

4. The ECG signal with R-peaks will be visualized in the plot area.

5. Click the "Help" button to display help information.

## File Structure

 
