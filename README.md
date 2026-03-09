✈️ Airline Flight Delay Analysis Dashboard
📌 Project Overview

This project focuses on analyzing airline flight delays using data analytics and visualization techniques. The objective is to explore patterns in flight delays and identify factors that influence delays such as airline type, weather conditions, runway traffic, and distance.

The project performs data cleaning, data processing, statistical analysis, and visualization using Python libraries like NumPy, Pandas, Matplotlib, and Seaborn.

An interactive dashboard selection system allows users to view different sets of visual analytics.
                  ______________________________________________________________________________________________________________________

🎯 Objectives

Perform data preprocessing and cleaning on airline datasets

Analyze flight delay patterns across airlines

Identify relationships between distance, weather conditions, and delays

Create interactive dashboards for visualization

Demonstrate data manipulation and visualization techniques in Python
                  ______________________________________________________________________________________________________________________

🗂 Dataset

The dataset contains 30,000 rows and 50 columns, representing different attributes of airline operations.

Key Features
Column	Description
flight_id	Unique flight identifier
airline	Airline company
origin_airport	Departure airport
destination_airport	Arrival airport
day_of_week	Day of flight
distance_km	Distance between airports
weather_condition	Weather conditions during flight
wind_speed_kmh	Wind speed at departure
runway_traffic	Air traffic at airport
departure_delay_minutes	Departure delay
arrival_delay_minutes	Arrival delay
month	Month of flight
year	Year of flight

Additional columns (feature_1 – feature_37) simulate extended operational data.
                  ______________________________________________________________________________________________________________________

📊 Dashboards

The system provides two dashboards, each containing four visualizations.

Dashboard 1

Focuses on flight delay distribution and operational factors

Average Delay by Airline (Bar Chart)

Distance vs Delay (Scatter Plot)

Delay Category Distribution (Pie Chart)

Weather Condition Distribution (Donut Chart)

Dashboard 2

Focuses on statistical and trend analysis

Arrival Delay Distribution (Histogram)

Feature Correlation (Heatmap)

Monthly Delay Trend (Line / Area Chart)

Delay Spread by Airline (Box Plot)
                  ______________________________________________________________________________________________________________________

🖥 How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/sanagaraj15/airline_flight_delay.git
2️⃣ Navigate to the project folder
**cd airline-delay-analysis**
3️⃣ Install required libraries
**pip install pandas numpy matplotlib seaborn**
4️⃣ Run the project
**python main.py**

You will be prompted to select a dashboard:

1 → Dashboard 1
2 → Dashboard 2
                  ______________________________________________________________________________________________________________________

👨‍💻 Author
Nagaraj S A
