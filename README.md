# Bahari
# ⚡ Arbitrage Betting Scraper Prototype

## 📖 Overview
This project is a prototype for an **arbitrage betting scraper** built with Python.  
It fetches odds from bookmaker APIs, processes the data with **pandas**,  
and checks for **arbitrage opportunities** using the formula:

\[
\text{Arbitrage if } \sum \frac{1}{\text{odd}} < 1
\]

The results are saved in a CSV file for further analysis.

---

## 🚀 Features
- Fetches odds data from an API (replaceable with real bookmaker APIs).
- Processes and structures raw match data into a clean DataFrame.
- Detects arbitrage opportunities automatically.
- Exports results to **CSV** for reporting or visualization.
- Modular, well-commented code with error handling.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **requests** → For fetching data from APIs.
- **pandas** → For data manipulation and analysis.

---

## 📂 Project Structure
