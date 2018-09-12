import csv
import math
with open(r"C:\Users\reema\Desktop\PythonStuff\election_data_0907.csv",encoding='utf-8') as csvfile:
  reader = csv.DictReader(csvfile)
  Candidates_considered = []
  Votes = []
  Votes_candidates=[]
  Unique_Candidates=[]
  Percentage_vote=[]
  output1=[]
  mynewlistsort=[]
  Percentage_votesort=[]
  Votesort=[]
  Percentage_vote1=[]
  for row in reader:

      Candidates_considered.append(row['Voter ID'])
      Votes_candidates.append(row['Candidate'])
Total_votes=len(Candidates_considered)

Unique_Candidates=set(Votes_candidates)
mynewlist = list(Unique_Candidates)
# print (Unique_Candidates)
# print (mynewlist)
# print (len(mynewlist))
Votes=  [0] * len(mynewlist)
# print (Votes)

# Loop unique candidates to get the count of votes they recived
for i in range(len(mynewlist)):
    count=0
    for candidates in Votes_candidates:
        if mynewlist[i]==candidates:
           count=count+1

    Votes[i]=Votes[i] + count
# print (Votes)
# print (mynewlist)
# print (Total_votes)

Percentage_vote = [x / Total_votes * 100 for x in Votes]
Percentage_vote = [round(x,3) for x in Percentage_vote]
#Percentage_vote = (Votes/Total_votes)
# print (Percentage_vote)
winner_index=Votes.index(max(Votes))
winner=mynewlist[winner_index]
# print (winner)

Percentage_vote1=[Percentage_vote]*1000
#print (Percentage_vote1)
#### Create sorted Lists
# mynewlistsort=mynewlist.sort(reverse=False )
# Percentage_votesort=Percentage_vote.sort(reverse=False )
# Votesort=Votes.sort(reverse=False )


Header1="Election Results "
Line0="    ----------------------------          "
Line1= f'      Total Votes: : {Total_votes}'
Line6= f'      Winner : {winner} '

print (f'{Header1}')
print (f'{Line0}\n')
print (f'{Line1}\n')
print (f'{Line0}\n')
for i in range(len(Percentage_vote)) :
    val=(f'      {mynewlist[i]}: {Percentage_vote[i]}% ({Votes[i]})')
    print(f'{val}\n')
print (f'{Line0}\n')
print (f'{Line6}')

file1 = open(r"C:\Users\reema\Desktop\PythonStuff\python-challenge\PyPoll\Electiont_output_final.csv","w")

file1.write(f'{Header1}\n')
file1.write(f'{Line0}\n')
file1.write(f'{Line1}\n')
file1.write(f'{Line0}\n')


for i in range(len(Percentage_vote)) :
    val=(f'       {mynewlist[i]}: {Percentage_vote[i]}% ({Votes[i]}) \n')
    file1.write(f'{val}\n')
file1.write(f'{Line0}\n')
file1.write(f'     {Line6}\n')

file1.close()

#
# Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
