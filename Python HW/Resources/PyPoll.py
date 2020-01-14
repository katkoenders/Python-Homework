#worked closely with Dominic during the Hackathon
# Incorporated the csv module
import csv
import os


file_to_load = os.path.join('.','Resources','election_data.csv')
file_to_output = os.path.join('election_analysis.txt')


candidate_count = {}
total_votes = 0 
votes_percentage = 0




with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:
        candidate_name = row[2]
        total_votes = total_votes + 1
        
    
        if candidate_name in candidate_count: 
            candidate_count[candidate_name] = candidate_count[candidate_name] + 1
            #print(f"incrementing: {candidate_name}")
        else:
            candidate_count[candidate_name] = 1
            print(f"adding: {candidate_name}")
  
    
print(candidate_count)
print(total_votes)
print(votes_percentage)\

highest_votes = 0
winner = ""
for key, value in candidate_count.items():
    percentage = value/total_votes * 100
    print(f"{key}: {percentage:.3f} ({value})")
    if value > highest_votes:
        highest_votes = value
        winner = key

print(f"Winner: ", winner)


with open(file_to_output, "w") as txt_file:
    results = (f"Election Results\n"
        f"-----------------\n"
        f"Total Votes: {total_votes}\n"
    f"-------------------\n")
    txt_file.write(results)
    for key, value in candidate_count.items():
        percentage = value/total_votes * 100
        percent = f"{key}: {percentage:.3f}% ({value})\n"
        if value > highest_votes:
            highest_votes = value
            winner = key
        txt_file.write(percent)
    winner = (f"--------------\n"
    f"Winner: {winner} ")        
    txt_file.write(winner)


#votes_percentage = (candidate_count / total_votes) * 100 

# output = (
        
#     f"Total Votes: {total_votes}\n")

#     )
    


                

   

# # Print the results and send the data to text file
# with open(file_to_output, "w") as txt_file:

#     # Print the final vote count (to terminal)
#     results = (
#         f"\n\nElection Results\n"
#         f"-------------------------\n"
#         f"Total Votes: {votes_total}\n"
#         f"-------------------------\n")
#     print(results, end="")

#     # Save the final vote count to the text file
#     txt_file.write(results)

#     #winning vote count and candidate
#     if (votes > win_count):
#         win_count = votes
#         winner = candidate

#         # Print each candidate's voter count and percentage (to terminal)
#         voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
#         print(voter_output, end="")

#         # Save each candidate's voter count and percentage to text file
#         txt_file.write(voter_output)

#     # Print the winning candidate (to terminal)
#     winner = (
#         f"-------------------------\n"
#         f"Winner: {winner}\n"
#         f"-------------------------\n")
#     print(win_candidate_summary)

#     # Save the winning candidate's name to the text file
#     txt_file.write(winner summary)




    


