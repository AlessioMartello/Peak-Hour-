# This script works for Intelligent Data Traffic flow surveys. Following the same format as those found on Sheet 'PCU Data' of the Enfield Town sites found here: FILE LOCATION.
# For Enfield Town 05.12.2019 there are 20 sites, the rolling hour indices are:37,55,93,111,149,167
# Make sure to change the PCU tab to 'tfl PCUs'

import pandas as pd

# Optional display to see entire data frame, if displaying.
# pd.set_option("display.max_rows", None, "display.max_columns", None)

# Load in the sites. The combination of which you'd like the peak of. Ensure they are in the same folder as this script.
# Enter manually into the list. Or if they are labelled in order, numerically, use the loop.
# Sites = ['ID05183 Enfield Town - MCC Site 1 - 13.02.2020.xlsx', 'ID05183 Enfield Town - MCC Site 10 - 13.02.2020.xlsx','ID05183 Enfield Town - MCC Site 11 - 13.02.2020.xlsx','ID05183 Enfield Town - MCC Site 14 - 13.02.2020.xlsx', 'ID05183 Enfield Town - MCC Site 18 - 13.02.2020.xlsx' ]

Sites = []
number_of_sites = int(input("Enter the number of sites present: "))
for i in range (number_of_sites):
        Sites.append('ID04572 Paddington - MCC Site ' +str(i+1) + ' - 16.05.2019.xlsx')

rolling_hour_start1 = (int(input("Enter the row number for which the first rolling hour table starts: ")) - 1)
rolling_hour_end1 = (int(input("Enter the row number that it ends on: ")))
rolling_hour_start2 = (int(input("Enter the row number for which the second rolling hour table starts: ")) - 1)
rolling_hour_end2 = (int(input("Enter the row number that it ends on: ")))
rolling_hour_start3 = (int(input("Enter the row number for which the third rolling hour table starts: ")) - 1)
rolling_hour_end3 = (int(input("Enter the row number that it ends on: ")))

rolling_hour_list = []

for i in range(len((Sites))):
    data = pd.read_excel(Sites[i], "PCU Data", header=None)

    # Create initial data frame
    df = pd.DataFrame(data)

    # Locate the rolling hour data frames (without the Time stamp) and reset their indices
    df1 = df.iloc[rolling_hour_start1:rolling_hour_end1, 1:19]
    df1.reset_index(drop=True, inplace=True)
    df2 = df.iloc[rolling_hour_start2:rolling_hour_end2, 1:19]
    df2.reset_index(drop=True, inplace=True)
    df3 = df.iloc[rolling_hour_start3:rolling_hour_end3, 1:19]
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
rolling_hour_times = df.iloc[rolling_hour_start1:rolling_hour_end1, 0]
rolling_hour_times.reset_index(drop=True, inplace=True)

# Identify the time corresponding to the max value index
PeakTime = rolling_hour_times.iloc[maxValueIndex]

# make final result
PCU_table = pd.concat([rolling_hour_times, combined_rolling_hours.Sum], axis=1)
print(PCU_table)

# print result
print("The peak hour is: " + str(PeakTime))
