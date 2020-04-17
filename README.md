# Peak-Hour-
A script to automate the calculation of the hour of the day with the largest traffic flow, fom traffic survey data.

Download the script.

Ensure the survey data to be analysed is in the same folder as the script.

Ensure the 'tfl PCUs' tab is selected on the PCU Data page, for each spreadsheet.

Identify the first and last Row number, in excel, of the rolling hour tables. I.e. Rolling hour value 07:00 starts on row 72 and ends on row 72.
If more than one rolling hour table is present, note them all. The program will ask for this input.

If the sites are labelled in numerical order and the only change to the filename is the site number, use the loop on lines 13 - 16 to populate the site_list.
Otherwise populate the list by hand on line 11.
