#This script works for Intelligent Data Traffic flow surveys. Following the same format as those found on Sheet 'PCU Data' of the Enfield Town sites found here: FILE LOCATION.

import pandas as pd

# Optional display to see entire data frame, if displaying.
# pd.set_option("display.max_rows", None, "display.max_columns", None)

# Load in the sites. The combination of which you'd like the peak of. Ensure they are in the same folder as this script.
xLs = pd.ExcelFile('ID05183 Enfield Town - MCC Site 1 - 07.03.2020.xlsx')
xLs1 = pd.ExcelFile('ID05183 Enfield Town - MCC Site 10 - 07.03.2020.xlsx')
xLs2 = pd.ExcelFile('ID05183 Enfield Town - MCC Site 11 - 07.03.2020.xlsx')
xLs3 = pd.ExcelFile('ID05183 Enfield Town - MCC Site 14 - 07.03.2020.xlsx')
xLs4 = pd.ExcelFile('ID05183 Enfield Town - MCC Site 18 - 07.03.2020.xlsx')

# Enter the corresponding site variables as above.
Sites = [xLs, xLs1, xLs2, xLs3, xLs4]

rolling_hour_list = []

for i in range(len((Sites))):
    data = pd.read_excel(Sites[i], "PCU Data")

    # Create initial data frame
    df = pd.DataFrame(data)

    # Locate the rolling hour data frames (without the Time stamp) and reset their indices
    df1 = df.iloc[34:55, 1:19]
    df1.reset_index(drop=True, inplace=True)
    df2 = df.iloc[91:112, 1:19]
    df2.reset_index(drop=True, inplace=True)
    df3 = df.iloc[148:169, 1:19]
    df3.reset_index(drop=True, inplace=True)

    # Join the rolling hour data frames (without time) horizontally
    rolling_hour = pd.concat([df1, df2, df3], axis=1)

    # Add each combined rolling hour to the rolling hour list
    rolling_hour_list.append(rolling_hour)

# Combine the rolling hour list of dataframes horizontally, into one dataFrame
combined_rolling_hours = pd.concat(rolling_hour_list, axis=1)

# Create new column, called "sum" that contains the total of each row
combined_rolling_hours["Sum"] = combined_rolling_hours.sum(axis=1)

# Identify the index of the maximum value in the "sum" column
maxValueIndex = combined_rolling_hours["Sum"].idxmax()

# Create a separate data frame (just the time stamps column), to use at the end in order to ID the Peak time
rolling_hour_times = df.iloc[34:55, 0]
rolling_hour_times.reset_index(drop=True, inplace=True)

# Identify the time corresponding to the max value index
PeakTime = rolling_hour_times.iloc[maxValueIndex]

# print result
print("The peak hour is: " + str(PeakTime))
