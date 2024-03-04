# Exposing Data Inconsistencies: Dependability Variations in Air Pollution Levels 
# in Amsterdam's Different Districts

# Author: Omar, A.O (s322099)
# Faculty of ITC, University of Twente

import pandas as pd
import numpy as np

# Load the air quality data from the CSV file
file_path = r"C:\Users\Zako3\Downloads\air_quality\statistics\airqualitydata.csv"
air_quality_data = pd.read_csv(file_path)

# Select columns that are related to sensor data (e.g., columns containing '_PM25' or '_PM10')
sensor_columns = [col for col in air_quality_data.columns if '_PM25' in col or '_PM10' in col]
sensor_data = air_quality_data[sensor_columns]

# Calculate Missing Data Factor (MDF) for sensor columns only
mdf = sensor_data.isna().mean()
mdf = 1 - mdf  # Inverting to get the proportion of non-missing data

# Calculate Coefficient of Variation (CV) for sensor columns only
cv = sensor_data.std() / sensor_data.mean()

# Inverse the CV to get the Consistency Factor (CF), as lower CV indicates higher consistency
cf = 1 / cv
cf.replace([np.inf, -np.inf], 0, inplace=True)  # Replace infinite values with 0

# Define weights for MDF and CF
w_mdf = 0.5
w_cf = 0.5

# Calculate the Reliability Score (RS)
reliability_score = w_mdf * mdf + w_cf * cf

# Normalize the reliability scores to be between 0 and 1
reliability_score_normalized = (reliability_score - reliability_score.min()) / (reliability_score.max() - reliability_score.min())

# Display the normalized reliability scores
reliability_scores_sorted = reliability_score_normalized.sort_values(ascending=False)
print(reliability_scores_sorted)

# Save the reliability scores to a CSV file
reliability_scores_sorted.to_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\reliability_scores.csv", header=True)
