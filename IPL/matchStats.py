import csv

infile = open(r"C:\Users\Shree\PycharmProjects\pythonProject\HellowWorld\Ethans\IPL\matches.csv", 'r')
reader_csv = csv.DictReader(infile)

def showTeams():
    print('''
1. Sunrisers Hyderabad
2. Rising Pune Supergiant
3. Kolkata Knight Riders
4. Chennai Super Kings
5. Rajasthan Royals
6. Royal Challengers Bangalore
7. Mumbai Indians
8. Kings XI Punjab
9. Deccan Chargers
10. Kochi Tuskers Kerala''')

    id_team = int(input("\nChoose you team = "))
    if id_team == 1:
        team_name = "Sunrisers Hyderabad"
        return team_name
    elif id_team == 2:
        team_name = "Rising Pune Supergiant"
        return team_name
    elif id_team == 3:
        team_name = "Kolkata Knight Riders"
        return team_name
    elif id_team == 4:
        team_name = "Chennai Super Kings"
        return team_name
    elif id_team == 5:
        team_name = "Rajasthan Royals"
        return team_name
    elif id_team == 6:
        team_name = "Royal Challengers Bangalore"
        return team_name
    elif id_team == 7:
        team_name = "Mumbai Indians"
        return team_name
    elif id_team == 8:
        team_name = "Kings XI Punjab"
        return team_name
    elif id_team == 9:
        team_name = "Deccan Chargers"
        return team_name
    elif id_team == 10:
        team_name = "Kochi Tuskers Kerala"
        return team_name


def tossWin(team_entered):
    toss = 0
    toss_winner = 0
    listToss = []
    for row in reader_csv:
        if row['TEAM1'] == team_entered or row['TEAM2'] == team_entered:
            toss += 1
        if row['TOSS_WINNER'] == team_entered:
            toss_winner += 1
    listToss.append(toss)
    listToss.append(toss_winner)
    infile.seek(0)
    return listToss


def yearWise_WonPlayed(team_entered):
    dictYearWise = {}
    for year_played in range(2008, 2018):
        dictYearWise_data = {}
        match_played = 0
        match_won = 0
        for row in reader_csv:
            if row['SEASON'] == str(year_played) and (row['TEAM1'] == team_entered or row['TEAM2'] == team_entered):
                match_played += 1
            if row['SEASON'] == str(year_played) and row['WINNER'] == team_entered:
                match_won += 1
        dictYearWise_data['Total'] = match_played
        dictYearWise_data['Won'] = match_won
        dictYearWise[year_played] = dictYearWise_data
        infile.seek(0)
    return dictYearWise


def locationWise(team_entered):
    dictLocation = {}
    result_dict = {}
    unique_city = []
    for row in reader_csv:
        for key, value in row.items():
            result_dict.setdefault(key, []).append(value)
    unique_city = set(result_dict['CITY'])

    for city in unique_city:
        count = 0
        dictLocation_data = {}
        match_played = 0
        match_won = 0
        for row in reader_csv:
            if row['CITY'] == str(city) and (row['TEAM1'] == team_entered or row['TEAM2'] == team_entered):
                match_played += 1
            if row['CITY'] == str(city) and row['WINNER'] == team_entered:
                match_won += 1
        dictLocation_data['total'] = match_played
        dictLocation_data['won'] = match_won
        dictLocation[city] = dictLocation_data
        infile.seek(0)
    return dictLocation


if __name__ == '__main__':
    print("I am Phenol Verma")
    team_selected = showTeams()
    # print(yearWise_WonPlayed(team_selected))
    # unique_city = set(reader_csv_dict.keys())
    print(tossWin(team_selected))
    # print("Total Matches played:", tossWin(listToss))
    # print("No of times toss won:", tossWin(listToss[1]))
    # print("Toss winning percentage is", round(float(listToss[1] / listToss[0] * 100), 2))




