#import library

import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

#def election_results(election_data)



with open(election_csv, newline="") as election_file:
    election_reader = csv.reader(election_file, delimiter= ",")
    election_header = next(election_file)

    votes =[]
    total_votes = 0
    candidate_votes = []

    candidates_dict = {}

    #candidate name 

    for candidate in election_reader:

        votes.append(candidate[0])
        total_votes = (len(votes))
        candidate = (candidate[2])
        if candidate in candidates_dict:
            candidates_dict[candidate]+=1 #Creating a count in the dictionary
        else:
            candidates_dict = 1 #Candidate in Dictionary











#print("------------------------------")
#print("    Election Results:")
#print("------------------------------")
#print(f"Total Votes: {total_votes}")
#print(f"")
