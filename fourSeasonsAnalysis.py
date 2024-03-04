
# Examining Differences in Air Quality Along Yearly Time Scales
# Author: Omar, Abdillahi Osman
# Methodology: We will define the airquality data into 4 seasons, and then
#              examine the differences in the air quality between the seasons.
#              We will also examine the differences in air quality between the neighborhood of
#              Amsterdam, The Netherlands.

# Import Libraries
import pandas as pd

# Define the get_season function
def get_season(month):
    if 3 <= month <= 5:
        return 'Spring'
    elif 6 <= month <= 8:
        return 'Summer'
    elif 9 <= month <= 11:
        return 'Autumn'
    else:
        return 'Winter'

# Load the air quality data again
air_quality_data = pd.read_csv(r"C:\Users\Zako3\Downloads\air_quality\statistics\airqualitydata.csv")

# Convert 'Time' column to datetime and set it as the index
air_quality_data['Time'] = pd.to_datetime(air_quality_data['Time'], format='%Y%m%d %H:%M')
air_quality_data.set_index('Time', inplace=True)

# Add a 'Season' column using the get_season function
air_quality_data['Season'] = air_quality_data.index.month.map(get_season)


# Specify the numeric columns for PM2.5 and PM10 for each sensor
pm25_columns = ['NL49007_PM25', 'NL49012_PM25', 'NL49014_PM25', 'NL49016_PM25', 'NL49017_PM25', 'NL49704_PM25', 'LTD_4969_PM25', 'LTD_55037_PM25', 'LTD_8802_PM25', 'LTD_23231_PM25', 'LTD_32517_PM25', 'LTD_32999_PM25']
pm10_columns = ['NL49007_PM10', 'NL49012_PM10', 'NL49014_PM10', 'NL49016_PM10', 'NL49017_PM10', 'NL49704_PM10', 'LTD_4969_PM10', 'LTD_32999_PM10', 'LTD_55037_PM10', 'LTD_8802_PM10', 'LTD_23231_PM10', 'LTD_32517_PM10']

# Group by 'Season' and calculate the mean for PM2.5 columns and PM10 columns separately for each sensor and each season
pm25_seasonal_means = air_quality_data.groupby('Season')[pm25_columns].mean()
pm10_seasonal_means = air_quality_data.groupby('Season')[pm10_columns].mean()

# Reset index to have 'Season' as a column again
pm25_seasonal_means = pm25_seasonal_means.reset_index()
pm10_seasonal_means = pm10_seasonal_means.reset_index()

# Rename columns to indicate the component and sensor in the column name
pm25_seasonal_means.columns = ['Season'] + [col.replace('_PM25', '_PM2.5_annual') 
                                            for col in pm25_columns]
pm10_seasonal_means.columns = ['Season'] + [col.replace('_PM10', '_PM10_annual') 
                                            for col in pm10_columns]

# Merge the PM2.5 and PM10 seasonal means dataframes on the 'Season' column
final_seasonal_means = pd.merge(pm25_seasonal_means, pm10_seasonal_means, on='Season')

# Print the final_seasonal_means DataFrame
#print(final_seasonal_means)

# Specify the path where you want to save the new CSV file
output_csv_path = r"C:\Users\Zako3\Downloads\air_quality\statistics\final_seasonal_means.csv"

# Write the final_seasonal_means DataFrame to the new CSV file
final_seasonal_means.to_csv(output_csv_path, index=False)

# Print a message to confirm the file has been saved
print(f"The data has been saved to {output_csv_path}")
