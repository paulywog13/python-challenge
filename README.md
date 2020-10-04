# python-challenge

Challenge 1 PyBank- Monthly Revenue Analysis
    Analyze a banks monthly revenue values using python to find summary values as well as average change from a given data resource. 

Files included in this challenge:
    budget_data.csv     main.py     Budget_data.txt     README.md

Libraries Needed:
    os      csv

The goal of this activity was to use Python to analyze the banking revenue data provided in order to find the outcomes required for the homework assigment. I utilized the following for loop to capture the data needed to calculate and print the information required:
    
    for row in pybankreader: 
        month_count += 1
        total_revenue += int(row[1])
        months.append(row[0])
        total_revenue_change = int(row[1])-previous_revenue
        revenue_changes.append(total_revenue_change)
        previous_revenue = int(row[1])
        greatest_increase = max(revenue_changes)
        greatest_decrease = min(revenue_changes)

Within this for loop are two lists that as the loop was processed were filled with the data values so that I could use the the following code to index which month was associated with the correct greatest increase and greatest decrease in revenue values:

    max_month = months[revenue_changes.index(greatest_increase)]    
    min_month = months[revenue_changes.index(greatest_decrease)]

The results of my python code should produce and output the following values when processed through the Python program:

Financial Analysis
----------------------------
Total months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Increase in Profits: Sep-2013 ($-2196167)



Challenge 2 PyPoll- Poll Voting Analysis
    Analyze the results of a voting poll to find the total votes cast, candidates, each candidates total votes, percentage for of votes for each candidate, and the winning candidate from a given data resource. 

Files included in this challenge:
    election_data.csv       main.py     Polling_Data.txt        README.md

Libraries Needed:
    os      csv

The goal of this activity was to use Python to analyze the election poll data provided in order to find the outcomes required for the homework assigment. I used a few of for loops in my code in order to generage the values needed. The following for loop was used first in order to capture the data needed to capture the candidates and vote totals for each of the candidates in the poll data.

    for candidates in election_reader:
        total_votes += 1
        candidates_votes.append(candidates[0])
        candidate = (candidates[2])
        if candidate in candidates_dict:
            candidates_dict[candidate]+=1
        else:
            candidates_dict[candidate]=1 

The next for loop used the data collected from the previous loop to calculate the winner of the election by identifying who received the most votes:

    for candidate, candidates_votes in candidates_dict.items():
        
        if candidates_votes > most_votes:
            most_votes = candidates_votes
            candidates = candidate

And the final loop I wrote was the most challenging as I had to included it within my output script in order to print the values for each candidate. I initially attempted to use this information in the above for loop above as it uses the same data but it would only place the last place candidate in my output when I ran the program. One of the TAs helped me identify this issue and how to correct it by including the code within the output.

    for candidate, candidates_votes in candidates_dict.items():   
            #vote percentage calculation and output format for the the results
            percent_of_vote = ("{:.2%}".format(candidates_votes/total_votes))
            txt_file.write(f"{candidate}: {percent_of_vote} ({candidates_votes})\n")
            print(f"{candidate}: {percent_of_vote} ({candidates_votes})")

Also included in the above for loop was formating information I had to research for in order to have the percent values for each candidate to be shown in % format. 

Overall the final results of my code should produce the following results:

     Election Results:
------------------------------
Total Votes: 3521001
------------------------------

Khan: 63.00% (2218231)
Correy: 20.00% (704200)
Li: 14.00% (492940)
O'Tooley: 3.00% (105630)
------------------------------
WINNER:  Khan