import pandas as pd
import matplotlib.pyplot as plt

# site_list = ['ID05183 Enfield Town - MCC Site 1 - 13.02.2020.xlsx', 'ID05183 Enfield Town - MCC Site 10 - 13.02.2020.xlsx','ID05183 Enfield Town - MCC Site 11 - 13.02.2020.xlsx','ID05183 Enfield Town - MCC Site 14 - 13.02.2020.xlsx', 'ID05183 Enfield Town - MCC Site 18 - 13.02.2020.xlsx' ]

site_list = []
number_of_sites = int(input("Enter the number of sites present: "))
for i in range (number_of_sites):
        site_list.append('ID05046 Enfield Town Center - MCC Site ' + str(i+1)+ ' - 05.12.2019.xlsx')

# Ask for the size of the tables which contain rolling hour PCU values
rolling_hour_start1 = (int(input("Enter the Excel row number for which the first rolling hour table starts: ")) - 1)
rolling_hour_end1 = (int(input("Enter the row number that it ends on: ")))
rolling_hour_start2 = (int(input("Enter the Excel row number for which the second rolling hour table starts: ")) - 1)
rolling_hour_end2 = (int(input("Enter the row number that it ends on: ")))
rolling_hour_start3 = (int(input("Enter the Excel row number for which the third rolling hour table starts: ")) - 1)
rolling_hour_end3 = (int(input("Enter the row number that it ends on: ")))

# Create empty list to populate with the rolling hour tables from each excel spreadsheet.
rolling_hour_list = []

# Loop through each spreadsheet, locating each rolling hour table, joining them horizontally and add them to rolling_hour_list
for i in range(len((site_list))):
    data = pd.read_excel(site_list[i], "PCU Data", header=None)

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
max_value_index = combined_rolling_hours["Sum"].idxmax()

# # Create a separate data frame (just the time stamps column), to use at the end in order to ID the Peak time
rolling_hour_times = df.iloc[rolling_hour_start1:rolling_hour_end1, 0]
rolling_hour_times.reset_index(drop=True, inplace=True)
#
# # Identify the time corresponding to the max value index
largest_peak_time = rolling_hour_times.iloc[max_value_index]

# Create the final table of results
PCU_table = pd.concat([rolling_hour_times, combined_rolling_hours.Sum], axis=1)

# print result
print("The peak hour with the greatest PCU flow is: " + str(largest_peak_time))

AM_peak_end = 0 + int(input("Enter the number of time intervals for the AM peak range, including the start and finish: "))
inter_peak_start = AM_peak_end + 1
inter_peak_end = inter_peak_start + int(input("Enter the number of time intervals for the Inter-peak range, do not include the start but do include the finish. If there is a gap in the data, enter the size of the gap: "))
PM_peak_start = inter_peak_end + 1

AM_peak_range = combined_rolling_hours.Sum.iloc[0:AM_peak_end]
inter_peak_range = combined_rolling_hours.Sum.iloc[inter_peak_start:inter_peak_end]
PM_peak_range = combined_rolling_hours.Sum.iloc[PM_peak_start:rolling_hour_end1]

try:
    AM_peak_max_value_index = AM_peak_range.idxmax()
    inter_peak_max_value_index = inter_peak_range.idxmax()
    PM_peak_max_value_index = PM_peak_range.idxmax()

    AM_peak_time = rolling_hour_times.iloc[AM_peak_max_value_index]
    inter_peak_time = rolling_hour_times.iloc[inter_peak_max_value_index]
    PM_peak_time = rolling_hour_times.iloc[PM_peak_max_value_index]


    print('The AM peak is: ' + str(AM_peak_time),
          'The Inter-peak is: ' + str(inter_peak_time),
          'The PM peak is: ' + str(PM_peak_time),
          sep="\n"
          )
except NameError:
    print("")
except ValueError:
    print("")

see_table_option = input("Do you want to see a table of result? Type y or n: ")
if see_table_option == "y":
    print(PCU_table)

pd.plotting.register_matplotlib_converters()
plt.plot(rolling_hour_times, combined_rolling_hours.Sum)
plt.ylabel('Total Network PCUs')
plt.xlabel('Survey Time')
plt.show()