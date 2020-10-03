#import library

import os
import csv

#define input path in order to read and ananlyze data
election_csv = os.path.join("Resources", "election_data.csv")

#define output path for analysis data
outputfile= os.path.join('Analysis', "Polling_Data.txt")
with open(election_csv, newline="") as election_file:
    election_reader = csv.reader(election_file, delimiter= ",")
    #skip the header line
    election_header = next(election_file)
    
    #define variables for analysis including lists and a candidate dictionary to recall values later
    total_votes = 0
    candidates_votes = []
    winning_candidate=[]
    candidates_dict = {}
    most_votes = 0

    #for loop to tally total votes 
    #Dictionary included in for loop to store each candidate's name and their total number of votes    

    for candidates in election_reader:
        total_votes += 1
        candidates_votes.append(candidates[0])
        candidate = (candidates[2])
        if candidate in candidates_dict:
            candidates_dict[candidate]+=1
        else:
            candidates_dict[candidate]=1 

   #for loop using the dictionary key(candidate) and values(candidate_votes) to identify the winning candidate
    
    for candidate, candidates_votes in candidates_dict.items():
        
        if candidates_votes > most_votes:
            most_votes = candidates_votes
            candidates = candidate

    #output file to write analysis results to text file

    with open(outputfile, "w") as txt_file:
    
        output =(
        f"------------------------------\n"
        f"      Election Results:       \n"
        f"------------------------------\n"
        f"Total Votes: {total_votes}    \n"
        f"------------------------------\n"
        )
        print(output)
        txt_file.write(output)
        
        #for loop to for each candidate in order to generate their vote percentage and vote total based upon the total number of votes
        
        for candidate, candidates_votes in candidates_dict.items():
            
            #vote percentage calculation and output format for the the results
            percent_of_vote = ("{:.2%}".format(candidates_votes/total_votes))
            txt_file.write(f"{candidate}: {percent_of_vote} ({candidates_votes})\n")
            print(f"{candidate}: {percent_of_vote} ({candidates_votes})")
        txt_file.write(f"------------------------------\n")
        print(f"------------------------------")
        txt_file.write(f"WINNER:  {candidates}\n")
        print(f"WINNER:  {candidates}")   

    
