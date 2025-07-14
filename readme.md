# Symptom Frequency Tracker for Clinical Intake Data

A simple Python-based tool to log patient symptoms, persist the data, and visualize the most common symptoms over time. Ideal for showcasing data collection, cleaning, and visualization skills in a healthcare context.

---

## Project Overview

- **Purpose:** Capture symptom reports from users or clinicians, store them with timestamps in a CSV file, and display the top N most frequently reported symptoms in a bar chart.
- **Technologies:** Python, pandas, matplotlib
- **Use Case:** Hospital intake nurses can log patient symptoms and identify prevalent health concerns quickly.

---

## Features

- **Persistent Data Storage:** Creates or loads a `symptoms_log.csv` file to save symptom entries between runs.
- **Interactive Logging:** Prompts the user to enter symptoms via the console and timestamps each entry.
- **Aggregation & Analysis:** Uses pandas to count and sort symptom frequencies.
- **Visualization:** Generates a clean horizontal bar chart of the top 5 reported symptoms.

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/symptom-frequency-tracker.git
   cd symptom-frequency-tracker
   ```
2. **Create a virtual environment** (optional but recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install pandas matplotlib
   ```

---

## Usage

1. Open a terminal and navigate to the project folder.
2. Run the script:
   ```bash
   python symptom_tracker.py
   ```
3. When prompted, type a symptom and press Enter. Press Enter on a blank line to finish logging.
4. View the generated bar chart of the top 5 symptoms.

---

## File Structure

```
├── symptom_tracker.py      # Main script
├── symptoms_log.csv        # Generated CSV log (auto-created)
└── README.md               # Project documentation
```

---

## Screenshot

> *(Replace with your own screenshot after running the script.)*

---

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact & Portfolio

- **GitHub:** [https://github.com/your-username](https://github.com/your-username)
- **LinkedIn:** [https://www.linkedin.com/in/your-profile](https://www.linkedin.com/in/your-profile)
- **Project Live Demo:** *(Link to Streamlit app if deployed)*

