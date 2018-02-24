import csv

f = open("nfl.csv", 'r')
#Assuming nfl.csv is present in the same path
nfl = list(csv.reader(f))
#Sample contents of the nfl list of lists.
#[['2009', '1', 'Pittsburgh Steelers', 'Tennessee Titans'], ['2009', '1', 'Minnesota Vikings', 'Cleveland Browns']]


# Define your function here.
def nfl_wins(team_name):
    #count number of lists 
    # where name = team_name
    team_last_name_list = team_name.split()
    team_last_name= team_last_name_list[1].lower()
    team_wins = team_last_name + "_" + "wins"
    
    count=0
    for i in nfl:
        if (i[2]==team_name):
            count+=1
    
    #team_wins = '_'.join(team_last_name, "wins")
    #print (team_wins)
    #team_wins = count
    print (team_wins, "=>", count)
    return count
    #return count, team_last_name

cowboys_wins=nfl_wins("Dallas Cowboys")
falcons_wins=nfl_wins("Atlanta Falcons")
