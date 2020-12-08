# Dependencies
import pandas as pd
import os

# Create reference to the csv file and read
csv_file = "Resources/election_data.csv"
election_data_df = pd.read_csv(csv_file)

# Print
print(election_data_df)

# The total number of votes cast
num_votes = election_data_df["Voter ID"].count()

print(f"Total number of votes cast: {num_votes}")
    # Total number of votes cast: 3521001

# A complete list of candidates who received votes
list_candidates = election_data_df["Candidate"].unique()
print("List of candidates who have received votes:")
print(list_candidates)
    # ['Khan' 'Correy' 'Li' "O'Tooley"]
    
# Calculate the total number of votes each candidate won
num_votes_list = []
for candidate in list_candidates:
    votes_for_candidate_df = election_data_df.loc[election_data_df["Candidate"] == candidate]
    num_votes_candidate = votes_for_candidate_df["Voter ID"].count()
    num_votes_list.append(num_votes_candidate)

print("Number of votes each candidate won:")
print(num_votes_list)
    # [2218231, 704200, 492940, 105630]
    
# Calculate the percentage of votes each candidate won
percent_votes_list = []
for vote_count in num_votes_list:
    percent_votes_candidate = (vote_count / num_votes) * 100
    percent_votes_candidate = round(percent_votes_candidate, 2)
    percent_votes_list.append(percent_votes_candidate)

print("Percentage of votes each candidate won:")
print(percent_votes_list)
    # [63.0, 20.0, 14.0, 3.0]
    
# Calculate the winner of the election based on popular vote.

# Make dictionary of lists
election_results_dict = {
    "Candidates": list_candidates,
    "Number of Votes": num_votes_list,
    "Percentage of Votes (%)": percent_votes_list
    
}

# Create dataframe from dictionary of lists
election_results_df = pd.DataFrame(election_results_dict)

# Sort results in descending order to determine winner
election_results_descending_df = election_results_df.sort_values(
    "Number of Votes", ascending=False)

# Reset index
election_results_descending_df = election_results_descending_df.reset_index(
    drop=True)

# Set a variable for winner
winner = election_results_descending_df.iloc[0]['Candidates']
print(f"Winner: {winner}")

# Format values
election_results_descending_df["Percentage of Votes (%)"] = election_results_descending_df["Percentage of Votes (%)"].astype(
    str) + '%'
election_results_descending_df["Number of Votes"] = election_results_descending_df["Number of Votes"].astype(
    float)

# Print in descending order
election_results_descending_df

# Print analysis
print("---------------------------------------------------------------")
print("Election Results")
print("---------------------------------------------------------------")
print("Total votes: {:,.0f}".format(num_votes))
print("---------------------------------------------------------------")
print(election_results_descending_df.to_string(index=False))
print("---------------------------------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------------------------------")

# Export text file
with open("election_results.txt", 'w') as file:

    file.write(
        "---------------------------------------------------------------\r\n")
    file.write("Election Results\r\n")
    file.write(
        "--------------------------------------------------------------\r\n")
    file.write("Total votes: {:,.0f}".format(num_votes) + "\r\n")
    file.write(
        "--------------------------------------------------------------\r\n")
    file.write(election_results_descending_df.to_string(
        index=False) + "\r\n")
    file.write(
        "--------------------------------------------------------------\r\n")
    file.write(f"Winner: {winner}\r\n")
    file.write(
        "--------------------------------------------------------------\r\n")
