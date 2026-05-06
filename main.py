# main.py

import pandas as pd
from risk_engine import assess_risk
import numpy as np
import matplotlib.pyplot as plt

def convert_rating(value):
    rating_map = {
        "very low": 1,
        "low": 2,
        "medium": 3,
        "high": 4,
        "very high": 5,
        "critical": 5
    }

    value = str(value).strip().lower()

    if value.isdigit():
        return int(value)

    if value in rating_map:
        return rating_map[value]

    raise ValueError(f"Invalid rating value: {value}")

def load_risk_data(file_path):
    """
    Loads cybersecurity risk data from a CSV file.
    """
    return pd.read_csv(file_path)


def convert_rating(value):
    rating_map = {
        "very low": 1,
        "low": 2,
        "medium": 3,
        "high": 4,
        "very high": 5,
        "critical": 5
    }

    value = str(value).strip().lower()

    # Clean unwanted characters from CSV values
    value = value.replace("|", "")
    value = value.replace("'", "")
    value = value.replace('"', "")
    value = value.strip()

    if value in rating_map:
        return rating_map[value]

    try:
        return int(float(value))
    except ValueError:
        raise ValueError(f"Invalid rating value found in CSV: {value}")


def assess_all_risks(dataframe):
    """
    Applies the risk assessment engine to every row in the dataset.
    """

    assessed_risks = []

    for _, row in dataframe.iterrows():
        result = assess_risk(
            asset=row["asset"],
            threat=row["threat"],
            vulnerability=row["vulnerability"],
            likelihood=convert_rating(row["likelihood"]),
            impact=convert_rating(row["impact"]),
        )

        assessed_risks.append(result)

    return pd.DataFrame(assessed_risks)


def save_report(dataframe, output_path):
    """
    Saves the assessed risks to a CSV report.
    """
    dataframe.to_csv(output_path, index=False)

def create_risk_chart(dataframe):
    risk_counts = dataframe["risk_level"].value_counts()

    plt.figure(figsize=(8, 5))
    risk_counts.plot(kind="bar")
    plt.title("Cybersecurity Risk Level Distribution")
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Risks")
    plt.tight_layout()
    plt.savefig("reports/risk_level_chart.png")
    plt.show()

def create_risk_chart(dataframe):

    risk_counts = dataframe["risk_level"].value_counts()

    plt.figure(figsize=(8, 5))

    risk_counts.plot(kind="bar")

    plt.title("Cybersecurity Risk Level Distribution")
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Risks")

    plt.tight_layout()

    # Save chart into reports folder
    plt.savefig("reports/risk_level_chart.png")

    print("\nChart saved successfully in reports folder.")

    plt.show()

def main():
    input_file = "data/risk_data.csv"
    output_file = "reports/risk_assessment_report.csv"

    print("Loading cybersecurity risk data...")
    risk_data = load_risk_data(input_file)

    print("Assessing risks...")
    assessed_risks = assess_all_risks(risk_data)

    print("\nCybersecurity Risk Assessment Results:")
    print(assessed_risks)

    create_risk_chart(assessed_risks)

    print("\nSaving report...")
    save_report(assessed_risks, output_file)

    print(f"\nReport saved successfully: {output_file}")


if __name__ == "__main__":
    main()