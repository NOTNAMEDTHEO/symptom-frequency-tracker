# Symptom Frequency Tracker

A small Python project to record reported symptoms and see which ones happen the most. I made this to practice working with files, data analysis, and charts.

## What It Does

- Checks for (or creates) a file called `symptoms_log.csv`.
- Lets you type in symptoms one at a time.
- Saves each entry with the current date and time.
- Counts how often each symptom appears.
- Shows a bar chart of the top 5 symptoms.

## How to Run

1. Make sure you have Python 3 installed.
2. Install the required packages:
   ```bash
   pip install pandas matplotlib
   ```
3. Download or copy `symptom_tracker.py` into a folder.
4. Open a terminal in that folder and run:
   ```bash
   python symptom_tracker.py
   ```
5. Follow the prompt to enter symptoms. When you’re done, press Enter on an empty line.

## File Details

- `symptom_tracker.py` — the main script that does everything.
- `symptoms_log.csv` — automatically created to store your entries.

## Notes

- You can open the CSV in Excel or Google Sheets to see all the raw data.
- If you want to change how many top symptoms show, edit the `N` value in the code.
- This is my first project, so any suggestions or improvements are welcome!

