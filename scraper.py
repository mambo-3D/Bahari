"""
Arbitrage Betting Scraper Prototype
-----------------------------------
Author: Dennis Mambo Mulwa
Description:
    This script fetches betting odds from a mock API endpoint,
    processes the data using pandas, and checks for arbitrage opportunities.
"""

import requests
import pandas as pd
from typing import List, Dict, Any


# -------------------------------
# Utility Functions
# -------------------------------
def fetch_odds(api_url: str) -> List[Dict[str, Any]]:
    """
    Fetch odds data from bookmaker API.

    Args:
        api_url (str): The API endpoint.

    Returns:
        List[Dict[str, Any]]: A list of matches with odds data.
    """
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise error if status code != 200
        return response.json().get("matches", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def calculate_arbitrage(odds: List[float]) -> bool:
    """
    Check if a set of odds presents an arbitrage opportunity.

    Formula: Sum(1 / odd) < 1 → Arbitrage exists.

    Args:
        odds (List[float]): List of odds for possible outcomes.

    Returns:
        bool: True if arbitrage opportunity exists, False otherwise.
    """
    try:
        total = sum(1 / odd for odd in odds if odd > 0)
        return total < 1
    except ZeroDivisionError:
        return False


def process_matches(matches: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Convert raw match data into a structured DataFrame
    and add arbitrage flag.

    Args:
        matches (List[Dict[str, Any]]): Raw match data.

    Returns:
        pd.DataFrame: Processed data with arbitrage detection.
    """
    rows = []
    for match in matches:
        home = match.get("home_team", "Unknown")
        away = match.get("away_team", "Unknown")
        odds = [o.get("odd_value") for o in match.get("odds", []) if o.get("odd_value")]

        rows.append({
            "Home": home,
            "Away": away,
            "Odds": odds,
            "Arbitrage": calculate_arbitrage(odds)
        })

    return pd.DataFrame(rows)


# -------------------------------
# Main Program
# -------------------------------
def main():
    # Example API endpoint (replace with real one later)
    api_url = "https://api.example.com/v1/matches"

    print("Fetching odds data...")
    matches = fetch_odds(api_url)

    if not matches:
        print("No data found. Exiting.")
        return

    print("Processing matches...")
    df = process_matches(matches)

    # Save results
    output_file = "arbitrage_results.csv"
    df.to_csv(output_file, index=False)

    print(f"Results saved to {output_file}")
    print(df.head())  # Show sample output in console


if __name__ == "__main__":
    main()
