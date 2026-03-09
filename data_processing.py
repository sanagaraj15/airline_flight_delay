import numpy as np

def create_total_delay(df):

    df["total_delay"] = df["departure_delay_minutes"] + df["arrival_delay_minutes"]

    return df


def categorize_delay(df):

    conditions = [
        df["arrival_delay_minutes"] <= 20,
        df["arrival_delay_minutes"] <= 60,
        df["arrival_delay_minutes"] <= 120
    ]

    categories = [
        "Low Delay",
        "Moderate Delay",
        "High Delay"
    ]

    df["delay_category"] = np.select(conditions, categories, default="Severe Delay")

    return df


def process_data(df):

    print("Starting Data Processing...")

    df = create_total_delay(df)

    df = categorize_delay(df)

    print("Data Processing Completed")

    return df