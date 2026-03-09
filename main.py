import pandas as pd

from data_cleaning import clean_data
from data_processing import process_data
from data_manipulation import airline_delay_statistics

from visualization import dashboard1, dashboard2


def main():

    print("Loading dataset...")

    df = pd.read_csv("airline_delay_dataset_strong_patterns.csv")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset info:")
    print(df.info())


    # -----------------------------
    # DATA CLEANING
    # -----------------------------
    df = clean_data(df)


    # -----------------------------
    # DATA PROCESSING
    # -----------------------------
    df = process_data(df)


    # -----------------------------
    # DATA MANIPULATION
    # -----------------------------
    print("\nAirline Delay Statistics:\n")

    stats = airline_delay_statistics(df)

    print(stats)


    # -----------------------------
    # DASHBOARD SWITCH
    # -----------------------------
    print("\n====== AIRLINE DELAY DASHBOARD ======\n")
    print("1 → Dashboard 1")
    print("2 → Dashboard 2")

    choice = input("\nSelect dashboard (1 or 2): ")

    if choice == "1":
        dashboard1(df)

    elif choice == "2":
        dashboard2(df)

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()