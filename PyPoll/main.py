#import library

import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

outputfile= os.path.join('Analysis', "Polling_Data.txt")
with open(election_csv, newline="") as election_file:
    election_reader = csv.reader(election_file, delimiter= ",")
    election_header = next(election_file)

    total_votes = 0
    candidate_name = {}
    candidates_votes = []
    winning_candidate=[]
    candidates_dict = {}
    most_votes = 0

    #candidate name 

    for candidates in election_reader:
        total_votes += 1
        candidates_votes.append(candidates[0])
        candidate = (candidates[2])
        if candidate in candidates_dict:
            candidates_dict[candidate]+=1
        else:
            candidates_dict[candidate]=1 

    #cand1_perc_vote = ("{:.2%}".format(candidates_dict[0]/total_votes))
    #cand2_perc_vote = ("{:.2%}".format(candidates_dict[1]/total_votes))
    #cand3_perc_vote = ("{:.2%}".format(candidates_dict[2]/total_votes))
    #cand4_perc_vote = ("{:.2%}".format(candidates_dict[3]/total_votes))
        
    print(candidates_dict.items())
    #print(candidates_dict.get(0))
    for candidate, candidates_votes in candidates_dict.items():

        percent_of_vote = ("{:.2%}".format(candidates_votes/total_votes))
        
        #print(f"{candidate}: {percent_of_vote} ({candidates_votes})\n")
        if candidates_votes > most_votes:
            most_votes = candidates_votes
            candidates = candidate
     


    output =(
    f"------------------------------\n"
    f"    Election Results:\n"
    f"------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------------------\n"
    #f"{candidate}: {cand1_perc_vote} ({candidates_dict[0]})\n"
    #f"{candidate}: {cand2_perc_vote} ({candidates_dict[1]})\n"
    #f"{candidate}: {cand3_perc_vote} ({candidates_dict[2]})\n"
    #f"{candidate}: {cand4_perc_vote} ({candidates_dict[3]})\n"
    f"------------------------------\n"
    f"WINNER:  {candidates}\n"
    )

    print(output)

    #with open(outputfile, "w") as txt_file:
        #txt_file.write(output)    
        
    








#print("------------------------------")
#print("    Election Results:")
#print("------------------------------")
#print(f"Total Votes: {total_votes}")
#print(f"")