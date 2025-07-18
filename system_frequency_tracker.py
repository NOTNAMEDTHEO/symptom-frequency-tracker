# -*- coding: utf-8 -*-
"""System Frequency Tracker.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vAnIZNOuPgenOW5r2AtwJuKA1zjo1TcN
"""

import matplotlib.pyplot as plt

# 1. Define your data

symptom_counts = {
    'fever': 45,
    'cough': 60,
    'fatigue': 30,
    'headache': 20,
    'nausea': 15,
    'shortness of breath': 25,
    'sore  throat': 35
}

# 2. Sort by count (value), highest first
sorted_counts = sorted(
    symptom_counts.items(),    #list of (symptom, count)
    key=lambda x: x[1],         # sort by the count
    reverse=True                # largest counts first
)

# 3. Print both to compare
print("Original dict itmes:")
print(list(symptom_counts.items()))
print('\nSorted List of tuples:')
print(sorted_counts)


# Part 3: take the top N resluts (e.g, N = 5)
N = 5
top_N = sorted_counts[:N]    # slice off the first N tuples
symptoms, counts = zip(*top_N)  # unzip inot two sequences

# ( optional) Print to verify
print('Top', N, 'symptoms:', symptoms)
print('Their counts:      ', counts)

plt.figure(figsize=(8,5))   #1. Set figure size (width, height in inces)
plt.barh(symptoms, counts) #2. Draw horizonatal bars
plt.xlabel('Frequency')    #4a. Label the x-axis
plt.title('Top 5 Most Common Symptoms')         #4b. Add a title
plt.gca().invert_yaxis()   #3. Highest-frequencey at the top
plt.tight_layout()         #5. Adjust Layout
plt.show()                 #6. Display the plot


# ----------------- EXPANDED VERSION WITH CSV + INPUT -----------------
# 0. Imports
import pandas as pd                      # Handle tabular data
import matplotlib.pyplot as plt          # Create visualizations
from pathlib import Path                 # Work with filesystem paths
from datetime import datetime           # Timestamp new entries

# 1. Load or create CSV file
FILE = Path("symptoms_log.csv")          # Define CSV path
if FILE.exists():
    df = pd.read_csv(FILE)               # Read existing data into DataFrame
else:
    df = pd.DataFrame(                   # Create empty DataFrame with two columns
        columns=["timestamp", "symptom"]
    )
    df.to_csv(FILE, index=False)         # Save empty CSV for future runs

# 2. Collect user input
print("\nType a symptom (or press Enter to finish):")
while True:
    symptom = input("> ").strip().lower()   # Read, trim whitespace, normalize case
    if not symptom:                         # Stop if the user enters a blank line
        break
    # ---- replace df.append with df.loc: ----
    df.loc[len(df)] = {                     # Add a new row at index = current length
        "timestamp": datetime.utcnow()      # Capture current UTC time
                         .isoformat(timespec="seconds"),
        "symptom": symptom                  # Store the entered symptom
    }

# 3. Save updated data back to CSV
df.to_csv(FILE, index=False)                # Overwrite CSV with updated DataFrame

# 4. Aggregate and sort symptom counts
symptom_counts = (
    df["symptom"]
      .value_counts()                       # Count how often each symptom appears
      .sort_values(ascending=False)         # Sort counts from highest to lowest
)

# 5. Plot the top N symptoms
N = 5                                       # Number of top symptoms to display
top_counts = symptom_counts.head(N)         # Select the top N entries
plt.figure(figsize=(8, 5))                  # Set the plot size (width, height in inches)
plt.barh(top_counts.index, top_counts.values)  # Draw horizontal bars
plt.xlabel("Frequency")                     # Label the x-axis
plt.title(f"Top {N} Reported Symptoms (Total Entries: {len(df)})")
                                             # Add a dynamic title
plt.gca().invert_yaxis()                    # Invert y-axis to have highest bar at top
plt.tight_layout()                          # Adjust layout to prevent clipping
plt.show()                                  # Render the chart