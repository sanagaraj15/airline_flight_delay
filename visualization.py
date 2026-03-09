import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# =========================
# DASHBOARD 1
# =========================
def dashboard1(df):

    sns.set_style("whitegrid")

    fig, axes = plt.subplots(2,2, figsize=(14,10))


    # Bar Chart
    avg_delay = df.groupby("airline")["arrival_delay_minutes"].mean()

    axes[0,0].bar(avg_delay.index,
                  avg_delay.values,
                  color=sns.color_palette("Set2"))

    axes[0,0].set_title("Average Delay by Airline")
    axes[0,0].tick_params(axis='x', rotation=45)


    # Scatter Plot
    axes[0,1].scatter(df["distance_km"],
                      df["arrival_delay_minutes"],
                      alpha=0.3,
                      color="purple")

    axes[0,1].set_title("Distance vs Delay")


    # Pie Chart
    conditions = [
        df["arrival_delay_minutes"] < 30,
        df["arrival_delay_minutes"] < 60,
        df["arrival_delay_minutes"] < 120
    ]

    labels = ["Low Delay","Moderate Delay","Severe Delay"]

    df["delay_category"] = np.select(conditions,labels,default="High Delay")

    delay_counts = df["delay_category"].value_counts()

    axes[1,0].pie(delay_counts,
                  labels=delay_counts.index,
                  autopct="%1.1f%%",
                  colors=sns.color_palette("pastel"),
                  startangle=90,
                  labeldistance=1.2)

    axes[1,0].set_title("Delay Category Distribution")


    # Donut Chart
    weather_counts = df["weather_condition"].value_counts()

    wedges, texts = axes[1,1].pie(weather_counts,
                                  labels=weather_counts.index,
                                  colors=sns.color_palette("Set3"),
                                  startangle=90)

    centre_circle = plt.Circle((0,0),0.60,fc='white')
    axes[1,1].add_artist(centre_circle)

    axes[1,1].set_title("Weather Distribution")

    plt.suptitle("AIRLINE DELAY DASHBOARD 1")

    plt.tight_layout()

    plt.show()



# =========================
# DASHBOARD 2
# =========================
def dashboard2(df):

    sns.set_style("whitegrid")

    fig, axes = plt.subplots(2,2, figsize=(14,10))


    # Histogram
    axes[0,0].hist(df["arrival_delay_minutes"],
                   bins=30,
                   color="orange",
                   edgecolor="black")

    axes[0,0].set_title("Arrival Delay Distribution")


    # Heatmap
    important_cols = [
        "distance_km",
        "wind_speed_kmh",
        "runway_traffic",
        "departure_delay_minutes",
        "arrival_delay_minutes",
        "month"
    ]

    corr = df[important_cols].corr()

    sns.heatmap(corr,
                annot=True,
                cmap="coolwarm",
                ax=axes[0,1])

    axes[0,1].set_title("Correlation Heatmap")


    # Line Graph
    monthly_delay = df.groupby("month")["arrival_delay_minutes"].mean()

    axes[1,0].plot(monthly_delay.index,
                   monthly_delay.values,
                   color="green")

    axes[1,0].fill_between(monthly_delay.index,
                           monthly_delay.values,
                           color="green",
                           alpha=0.3)

    axes[1,0].set_title("Monthly Delay Trend")


    # Boxplot
    sns.boxplot(data=df,
                x="airline",
                y="arrival_delay_minutes",
                palette="pastel",
                ax=axes[1,1])

    axes[1,1].set_title("Delay Spread by Airline")

    axes[1,1].tick_params(axis='x', rotation=45)

    plt.suptitle("AIRLINE DELAY DASHBOARD 2")

    plt.tight_layout()

    plt.show()