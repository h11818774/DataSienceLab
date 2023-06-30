from datetime import datetime
from dateutil.relativedelta import relativedelta

date_string = "31-10-2022"

# Split the string into day, month, and year
day, month, year = map(int, date_string.split("-"))

# Get the current date
current_date = datetime.now().date()

# Create a new date object using the extracted values
calculated_date = datetime(year, month, day).date()

# Calculate the difference in months
diff_in_months = relativedelta(current_date, calculated_date).months

# Print the calculated date, the current date, and the difference in months
print("Calculated Date:", calculated_date)
print("Current Date:", current_date)
print("Difference in Months:", diff_in_months)
