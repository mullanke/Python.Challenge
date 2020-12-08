# Dependencies
import pandas as pd

# Create references
budget_csv = "Resources/budget_data.csv"

# Read the csv and print
budget_df = pd.read_csv(budget_csv)
print(budget_df)

# Calculate the total number of months
num_months = budget_df["Date"].count()
print(f"Total number of months: {num_months}")
    # Total number of months: 86

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = budget_df["Profit/Losses"].sum()
print(f"Net total amount of profit/losses: ${net_total}")
    # Net total amount of profit/losses: $38382578

# Calculate the average of the changes in "Profit/Losses" over the entire period

# Subtract the starting value from the ending value for each value
diff = budget_df['Profit/Losses'].diff()

# Add new column for difference
budget_df["Difference"] = diff

# Sum up the difference values in the Difference column
sum_of_diff = budget_df["Difference"].sum()

# Find number of diff values in the Difference column and calculate average
num_of_diff = budget_df["Difference"].count()
avg_of_change = sum_of_diff / num_of_diff
avg_of_change = round(avg_of_change, 2)

print(f"Average Change: ${avg_of_change}")
    #Average Change: $-2315.12

# Calculate the greatest increase in profits (date and amount) over the entire period

# Put in descending order
budget_df_descending = budget_df.sort_values("Difference", ascending=False)

# Reset index
budget_df_descending = budget_df_descending.reset_index(drop=True)

# Greatest increase amount
greatest_increase_amount = budget_df_descending.iloc[0]["Difference"]

# Greatest increase date
greatest_increase_date = budget_df_descending.iloc[0]["Date"]

print(f"Greatest increase amount: ${greatest_increase_amount}")
print(f"Greatest increase date: {greatest_increase_date}")

budget_df_descending.head()
    # Greatest increase amount: $1926159.0
    # Greatest increase date: Feb-2012

# Calculate the greatest decrease in losses (date and amount) over the entire period

# Put in ascending order
budget_df_ascending = budget_df.sort_values("Difference")

# Reset index
budget_df_ascending = budget_df_ascending.reset_index(drop=True)

# Greatest decrease amount
greatest_decrease_amount = budget_df_ascending.iloc[0]["Difference"]

# Greatest decrease date
greatest_decrease_date = budget_df_ascending.iloc[0]["Date"]

print(f"Greatest decrease amount: ${greatest_decrease_amount}")
print(f"Greatest decrease date: {greatest_decrease_date}")

budget_df_ascending.head()
    # Greatest decrease amount: $-2196167.0
    # Greatest decrease date: Sep-2013
    
# Print the analysis to the terminal
print("-------------------------------")
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {num_months}")
print("Total: ${:,.2f}".format(net_total))
print("Average Change: ${:,.2f}".format(avg_of_change))
print("Greatest Increase in Profits: " + greatest_increase_date + ", ${:,.2f}".format(greatest_increase_amount))
print("Greatest Decrease in Profits: " + greatest_decrease_date + ", ${:,.2f}".format(greatest_decrease_amount))


with open("PyBank_Results.txt", 'w') as file:

    file.write("---------------------------------------------------\r\n")
    file.write("Financial Analysis\r\n")
    file.write(
        "----------------------------------------------------------\r\n")
    file.write(f"Total Months: {num_months}\r\n")
    file.write("Total: ${:,.2f}\r\n".format(net_total))
    file.write("Average Change: ${:,.2f}\r\n".format(avg_of_change))
    file.write("Greatest Increase in Profits: " + greatest_increase_date +
               ", ${:,.2f}\r\n".format(greatest_increase_amount))
    file.write("Greatest Decrease in Profits: " + greatest_decrease_date +
               ", ${:,.2f}\r\n".format(greatest_decrease_amount))
