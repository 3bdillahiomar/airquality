# Air Quality Data Distribution
# Descriptive Statistics
# Graphical Analysis
# Comparing Results of the two variables

# Omar, Abdillahi Osman
# ITC, Unievrsity of Twente
# January, 2024 

# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\Zako3\Downloads\air_quality\statistics\airqualitydata.csv"
air_quality_data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
air_quality_data.head()

# Setting the style for the plots
sns.set(style="whitegrid")

# Creating histograms and boxplots for the chosen variables
fig, axes = plt.subplots(2, 4, figsize=(20, 10))

# Histograms
sns.histplot(air_quality_data['NL49007_PM25'], ax=axes[0, 0], kde=True, color='skyblue')
sns.histplot(air_quality_data['NL49007_PM10'], ax=axes[0, 1], kde=True, color='olive')
sns.histplot(air_quality_data['LTD_4969_PM25'], ax=axes[0, 2], kde=True, color='gold')
sns.histplot(air_quality_data['LTD_4969_PM10'], ax=axes[0, 3], kde=True, color='teal')

# Boxplots
sns.boxplot(x=air_quality_data['NL49007_PM25'], ax=axes[1, 0], color='skyblue')
sns.boxplot(x=air_quality_data['NL49007_PM10'], ax=axes[1, 1], color='olive')
sns.boxplot(x=air_quality_data['LTD_4969_PM25'], ax=axes[1, 2], color='gold')
sns.boxplot(x=air_quality_data['LTD_4969_PM10'], ax=axes[1, 3], color='teal')

# Setting titles
axes[0, 0].set_title('Histogram of NL49007 PM2.5')
axes[0, 1].set_title('Histogram of NL49007 PM10')
axes[0, 2].set_title('Histogram of LTD_4969 PM2.5')
axes[0, 3].set_title('Histogram of LTD_4969 PM10')
axes[1, 0].set_title('Boxplot of NL49007 PM2.5')
axes[1, 1].set_title('Boxplot of NL49007 PM10')
axes[1, 2].set_title('Boxplot of LTD_4969 PM2.5')
axes[1, 3].set_title('Boxplot of LTD_4969 PM10')

plt.tight_layout()
plt.show()


# Save the figure
fig.savefig('hist_boxplot.png', dpi=300)

!pip install statsmodels
import statsmodels.api as sm

# Preparing data for linear regression models
# Dropping rows with NaN values for accurate model estimation
nl49007_data = air_quality_data[['NL49007_PM25', 'NL49007_PM10']].dropna()
ltd_4969_data = air_quality_data[['LTD_4969_PM25', 'LTD_4969_PM10']].dropna()

# Linear Model for NL49007
X_nl = sm.add_constant(nl49007_data['NL49007_PM25']) # adding a constant
model_nl = sm.OLS(nl49007_data['NL49007_PM10'], X_nl).fit()

# Linear Model for LTD_4969
X_ltd = sm.add_constant(ltd_4969_data['LTD_4969_PM25']) # adding a constant
model_ltd = sm.OLS(ltd_4969_data['LTD_4969_PM10'], X_ltd).fit()

# Getting the summaries of the models
nl_summary = model_nl.summary()
ltd_summary = model_ltd.summary()

nl_summary, ltd_summary


# Calculating descriptive statistics for the specified columns
nl49007_pm25_stats = nl49007_data['NL49007_PM25'].describe()
nl49007_pm10_stats = nl49007_data['NL49007_PM10'].describe()
ltd_4969_pm25_stats = ltd_4969_data['LTD_4969_PM25'].describe()
ltd_4969_pm10_stats = ltd_4969_data['LTD_4969_PM10'].describe()

# Organizing the statistics in a more readable format
stats_summary = pd.DataFrame({
    'NL49007_PM25': nl49007_pm25_stats,
    'NL49007_PM10': nl49007_pm10_stats,
    'LTD_4969_PM25': ltd_4969_pm25_stats,
    'LTD_4969_PM10': ltd_4969_pm10_stats
})

stats_summary.T  # Transposing for better readability


# Plotting the linear regression models

fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# Plot for NL49007
sns.regplot(x='NL49007_PM25', y='NL49007_PM10', data=nl49007_data, ax=axes[0], color='blue', line_kws={'color': 'red'})
axes[0].set_title('Linear Model: NL49007 PM10 vs PM2.5')
axes[0].set_xlabel('PM2.5 Levels (NL49007)')
axes[0].set_ylabel('PM10 Levels (NL49007)')

# Plot for LTD_4969
sns.regplot(x='LTD_4969_PM25', y='LTD_4969_PM10', data=ltd_4969_data, ax=axes[1], color='green', line_kws={'color': 'orange'})
axes[1].set_title('Linear Model: LTD_4969 PM10 vs PM2.5')
axes[1].set_xlabel('PM2.5 Levels (LTD_4969)')
axes[1].set_ylabel('PM10 Levels (LTD_4969)')

plt.tight_layout()
plt.show()

# Save the figure

#fig.savefig('linear_model.png', dpi=300)


# Plotting the scatter plot for both NL49007 and LTD_4969
plt.figure(figsize=(10, 6))

# Scatter plot for NL49007
plt.scatter(nl49007_data['NL49007_PM25'], nl49007_data['NL49007_PM10'], color='blue', alpha=0.5, label='NL49007')

# Scatter plot for LTD_4969
plt.scatter(ltd_4969_data['LTD_4969_PM25'], ltd_4969_data['LTD_4969_PM10'], color='green', alpha=0.5, label='LTD_4969')

# Adding titles and labels
plt.title('Scatter Plot: PM2.5 vs PM10 Levels at NL49007 and LTD_4969')
plt.xlabel('PM2.5 Levels')
plt.ylabel('PM10 Levels')
plt.legend()

plt.show()

# Save the figure

fig.savefig('scat_plot.png', dpi=300)
