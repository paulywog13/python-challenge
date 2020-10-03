#import library

import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

outputfile= os.path.join('Analysis', "Polling_Data.txt")
with open(election_csv, newline="") as election_file:
    election_reader = csv.reader(election_file, delimiter= ",")
    election_header = next(election_file)

    total_votes = 0
    candidates_votes = []
    winning_candidate=[]
    candidates_dict = {}
    most_votes = 0

     

    for candidates in election_reader:
        total_votes += 1
        candidates_votes.append(candidates[0])
        candidate = (candidates[2])
        if candidate in candidates_dict:
            candidates_dict[candidate]+=1
        else:
            candidates_dict[candidate]=1 

   
    
    for candidate, candidates_votes in candidates_dict.items():
        
        if candidates_votes > most_votes:
            most_votes = candidates_votes
            candidates = candidate
     
    with open(outputfile, "w") as txt_file:
    
        output =(
        f"------------------------------\n"
        f"    Election Results:\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------------\n"
        )
        print(output)
        txt_file.write(output)
        for candidate, candidates_votes in candidates_dict.items():
            percent_of_vote = ("{:.2%}".format(candidates_votes/total_votes))
            txt_file.write(f"{candidate}: {percent_of_vote} ({candidates_votes})\n")
            print(f"{candidate}: {percent_of_vote} ({candidates_votes})\n")
        txt_file.write(f"------------------------------\n")
        print(f"------------------------------")
        txt_file.write(f"WINNER:  {candidates}\n")
        print(f"WINNER:  {candidates}")   

    

        
        
    








#print("------------------------------")
#print("    Election Results:")
#print("------------------------------")
#print(f"Total Votes: {total_votes}")
#print(f"")