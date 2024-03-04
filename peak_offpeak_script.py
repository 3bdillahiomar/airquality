# Examining Differences in Air Quality Between Off-Peak and Peak Hours Along Amsterdam's Bike Paths
# Omar, Abdillahi Osman
# ITC, Unievrsity of Twente
# January, 2024 

# Import libraries
import pandas as pd

# Load the datasets
sensor_locations_df = pd.read_csv(r"C:\Users\Zako3\Downloads\air_quality\sensor_location.csv")
air_quality_df = pd.read_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\airqualitydata.csv")

#print(air_quality_df.head())
print(sensor_locations_df.head())

# Convert 'Time' column to datetime
air_quality_df['Time'] = pd.to_datetime(air_quality_df['Time'])
print(air_quality_df['Time'].head())

# Define peak hours (7-9 AM and 4-6 PM)
peak_hours = [7, 8, 9, 16, 17, 18]

# Filter data for peak and off-peak hours
air_quality_df['hour'] = air_quality_df['Time'].dt.hour
peak_data = air_quality_df[air_quality_df['hour'].isin(peak_hours)]
off_peak_data = air_quality_df[~air_quality_df['hour'].isin(peak_hours)]

# Calculate average values for PM2.5 and PM10 during peak and off-peak hours
peak_pm25_means = peak_data.filter(like='PM25').mean().reset_index()
peak_pm25_means.columns = ['station_id', 'PM25']
print(peak_pm25_means)

off_peak_pm25_means = off_peak_data.filter(like='PM25').mean().reset_index()
off_peak_pm25_means.columns = ['station_id', 'PM25']
print(off_peak_pm25_means)

peak_pm10_means = peak_data.filter(like='PM10').mean().reset_index()
peak_pm10_means.columns = ['station_id', 'PM10']
print(peak_pm10_means)

off_peak_pm10_means = off_peak_data.filter(like='PM10').mean().reset_index()
off_peak_pm10_means.columns = ['station_id', 'PM10']
print(off_peak_pm10_means)

# Adjust the station_id column to match the sensor_locations DataFrame
peak_pm25_means['station_id'] = peak_pm25_means['station_id'].str.replace('_PM25', '')
off_peak_pm25_means['station_id'] = off_peak_pm25_means['station_id'].str.replace('_PM25', '')
peak_pm10_means['station_id'] = peak_pm10_means['station_id'].str.replace('_PM10', '')
off_peak_pm10_means['station_id'] = off_peak_pm10_means['station_id'].str.replace('_PM10', '')

print(peak_pm25_means['station_id'])
print(off_peak_pm25_means['station_id'])
print(peak_pm10_means['station_id'])
print(off_peak_pm10_means['station_id'])
      
# Merge the DataFrames
peak_pm25_means = peak_pm25_means.merge(sensor_locations_df, on='station_id')
off_peak_pm25_means = off_peak_pm25_means.merge(sensor_locations_df, on='station_id')
peak_pm10_means = peak_pm10_means.merge(sensor_locations_df, on='station_id')
off_peak_pm10_means = off_peak_pm10_means.merge(sensor_locations_df, on='station_id')

# Save the DataFrames to CSV files
peak_pm25_means.to_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\peak_pm25_means.csv", index=False)
off_peak_pm25_means.to_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\off_peak_pm25_means.csv", index=False)
peak_pm10_means.to_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\peak_pm10_means.csv", index=False)
off_peak_pm10_means.to_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\off_peak_pm10_means.csv", index=False)

# Calculate the difference between peak and off-peak values
peak_offpeak_pm25 = peak_pm25_means.merge(off_peak_pm25_means, on='station_id')
peak_offpeak_pm25['PM25_diff'] = peak_offpeak_pm25['PM25_x'] - peak_offpeak_pm25['PM25_y']
print(peak_offpeak_pm25)

peak_offpeak_pm10 = peak_pm10_means.merge(off_peak_pm10_means, on='station_id')
peak_offpeak_pm10['PM10_diff'] = peak_offpeak_pm10['PM10_x'] - peak_offpeak_pm10['PM10_y']
print(peak_offpeak_pm10)

# Save the DataFrames to CSV files
peak_offpeak_pm25.to_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\diff_peak_offpeak_pm25.csv", index=False)
peak_offpeak_pm10.to_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\diff_peak_offpeak_pm10.csv", index=False)

# Calculate the average difference between peak and off-peak values
print(peak_offpeak_pm25['PM25_diff'].mean())
print(peak_offpeak_pm10['PM10_diff'].mean())

# Calculate the average difference between peak and off-peak values for each sensor
peak_offpeak_pm25_means = peak_offpeak_pm25.groupby('station_id')['PM25_diff'].mean().reset_index()
print(peak_offpeak_pm25_means)

peak_offpeak_pm10_means = peak_offpeak_pm10.groupby('station_id')['PM10_diff'].mean().reset_index()
print(peak_offpeak_pm10_means)

# Save the DataFrames to CSV files
peak_offpeak_pm25_means.to_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\avg_diff_peak_offpeak_pm25_means.csv", index=False)
peak_offpeak_pm10_means.to_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\avg_diffpeak_offpeak_pm10_means.csv", index=False)

