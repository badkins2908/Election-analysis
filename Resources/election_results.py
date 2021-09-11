#In this project, our final Python script will need to be able to deliver the following
# information when the script is run:
    #Total number of votes cast
    #A complete list of candidates who received votes
    #Total number of votes each candidate received
    #Percentage of votes each candidate won
    #The winner of the election based on popular vote

import os
import csv

##########
# Assign a variable to save the file to a path.
txt_file = os.path.join("Analysis", "election_analysis.txt")

#with open(txt_file, "w") as txt_file:
     #Begin writing to text file
     #txt_file.write("Election Results\n------------------\n")

# Assign a variable for the file to load and the path.
csv_file = os.path.join("Resources", "election_results.csv")

##########
#Initialize global total vote counter variable
total_votes = 0

#Create a candidate and county array to append into
candidate_options = []
county_options = []

#Declare empty dictionary for candidates and counties
candidate_votes = {}
county_votes = {}




#Winning Candidate, Winning County, and Winning Count Tracker
winning_candidate = ""
winning_countyname = ""
winning_percentage = 0
winning_count = 0
winning_county = 0

#################
# Open the election results and read the file
with open(csv_file) as election_data:
     # Read the file object with the reader function
     file_reader = csv.reader(election_data)

     #Read and print the header row
     headers = next(file_reader)
     #print(headers)

     #Count up all votes
     for row in file_reader:
          total_votes +=1
         #Print the candidate name and county from each row, then append to array
          candidate_name = row[2]
          county_name = row[1]

          if candidate_name not in candidate_options:
               candidate_options.append(candidate_name)
               #Begin tracking candidate's votes count
               candidate_votes[candidate_name] = 0

          #Aligned with for loop, add a vote to that candidate's count
          candidate_votes[candidate_name] += 1

          if county_name not in county_options:
               county_options.append(county_name)
               #Begin tracking county votes count
               county_votes[county_name] = 0

          #Aligned with for loop, add a vote to the county's count
          county_votes[county_name] += 1

# Save the results to our text file.
with open(txt_file, "w") as txt_file:

     # Print the final vote count to the terminal.
     election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n")
     print(election_results, end="")
     # Save the final vote count to the text file.
     txt_file.write(election_results)

     print("\nCounty Votes:\n")
     txt_file.write("\nCounty Votes:\n")

     ##Determine the percentage of votes for each candidate and county
     # by looping through the counts
     # Iterate through county's list
     for county_name in county_votes:
          # Get the vote count for each county
          coun_votes = county_votes[county_name]
          # Calculate the percentage of votes
          coun_vote_percentage = float(coun_votes) / float(total_votes) * 100

          county_results = (
               f"{county_name}: {coun_vote_percentage:.1f}% ({coun_votes:,})\n")
          print(county_results)
          txt_file.write(county_results)

          # Determining largest county turnout
          # 1.Determine if the votes are greater than the winning count
          if (coun_votes > winning_county):
               # 2. If true then set winning_count = can_votes and winning_percent to can_percent
               winning_county = coun_votes
               # 3. Set the winning_candidate equal to the candidate's name
               winning_countyname = county_name

     winning_county_results = (
          f"\n-------------------------\n"
          f"Largest County Turnout: {winning_countyname}\n"
          f"-------------------------\n")
     print(winning_county_results)
     txt_file.write(winning_county_results)

     #Iterate through candidate's list
     for candidate_name in candidate_votes:
          #Get the vote count for a candidate
          can_votes = candidate_votes[candidate_name]
         #Calculate the percentage of votes
          can_vote_percentage = float(can_votes) / float(total_votes) * 100

          candidate_results = (
               f"{candidate_name}: {can_vote_percentage:.1f}% ({can_votes:,})\n")
          print(candidate_results)
          txt_file.write(candidate_results)

          # Determining the winning vote count and candidate
          # 1.Determine if the votes are greater than the winning count
          if (can_votes > winning_count) and (can_vote_percentage > winning_percentage):
          # 2. If true then set winning_count = can_votes and winning_percent to can_percent
               winning_count = can_votes
               winning_percentage = can_vote_percentage
          # 3. Set the winning_candidate equal to the candidate's name
               winning_candidate = candidate_name

     winning_candidate_summary = (
          f"------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"------------------\n")
     print(winning_candidate_summary)
     txt_file.write(winning_candidate_summary)
