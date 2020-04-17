# Peak-Hour-
A script to automate the calculation of the hour of the day with the largest traffic flow, fom traffic survey data.

This script works for Intelligent Data Traffic flow surveys. Following the same format as those found on Sheet 'PCU Data' of the Enfield Town sites.

Download the most rescent script.

Ensure the survey data to be analysed is in the same folder as the script.

Ensure the 'tfl PCUs' tab is selected on the PCU Data page, for each spreadsheet.

Note how many sites are to be analysed.

Identify the first and last Row number, in excel, of the rolling hour tables. I.e. Rolling hour value 07:00 starts on row 72 and ends on row 128.
If more than one rolling hour table is present, note them all. 
The program will ask for the start and end of three rolling_hour tables to be input. If only one or two exist, enter these and for the third enter an arbitrary value outside of the range of any data.
I.e if the parameters for the first table are 37 and 55. The second: 93 and 111. The third dont exist, enter 94 and 95 when prompted.

If the sites are labelled in numerical order and the only change to the filename is the site number, use the loop on lines 13 - 16 to populate the site_list.
Otherwise populate the list by hand on line 11.
