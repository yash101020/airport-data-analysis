# airport-data-analysis
A Python project for analysing airport flight data from CSV files
# Airport Data Analysis

A Python project created as part of my university coursework to analyse airport flight data from CSV files.

Users enter an airport code and a year to select the dataset they want to analyse.

## Technologies Used

- Python 3
- CSV data files
- graphics.py

## Project Files

| File | Description |
|---|---|
| `airport_analysis.py` | Main Python program |
| `graphics.py` | Supporting graphics library |
| `CDG2021.csv` | Dataset for Charles de Gaulle Airport, 2021 |
| `LHR2025.csv` | Dataset for London Heathrow Airport, 2025 |

## Getting Started

1. Install Python 3.
2. Download the repository using **Code → Download ZIP**.
3. Extract the ZIP and keep the Python files and CSV files together.
4. Open a terminal in the project folder.
5. Run:

   ```bash
   python airport_analysis.py
   ```

Alternatively, open `airport_analysis.py` in Python IDLE and select **Run → Run Module**.

## Selecting a Dataset

Enter an airport code and year that match one of the included files:

| Airport code | Year | Dataset |
|---|---|---|
| `CDG` | `2021` | `CDG2021.csv` |
| `LHR` | `2025` | `LHR2025.csv` |

For example, enter `LHR`, followed by `2025`, to analyse the Heathrow dataset.

Run the program from the project folder so it can find the CSV files. Selecting a dataset that is unavailable will cause a `FileNotFoundError`.

## About the Project

I developed this project to practise working with user input, CSV files, and data processing in Python.

## Acknowledgements

The project uses the supporting `graphics.py` library. Credit for that library belongs to its original author.
