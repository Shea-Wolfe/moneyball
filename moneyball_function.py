

def get_years_best(data,year):
    ret = data[data.yearID == year].groupby(['playerID','G_c','G_1b','G_2b',
                                            'G_3b','G_ss','G_of']).agg('mean')
    cleaned = ret['AB'] >100
    ret = ret[cleaned]
    ret = (((ret.H+ret.BB+ret.HBP)/
            (ret.AB+ret.BB+ret.HBP+ret.SF))/ret.salary)*1000000
    return ret

def get_top_pitchers(data,year):
    ret = data[data.yearID == year].groupby(['playerID']).agg('mean')
    cleaned = ret['AB'] >20
    ret = ret[cleaned]
    cleaned = ret.G_p > 10
    ret = ret[cleaned]
    ret = (((ret.H+ret.BB+ret.HBP)/
            (ret.AB+ret.BB+ret.HBP+ret.SF))/ret.salary)*1000000
    return ret

def build_positions(series, position,ab=100,games=50):
    players = []
    for x in range(ab):
        if series.index[x][position] > games:
            players.append(series.index[x][0])
    return players

def get_player_names(master_data, team):
    count  = 0
    for player in master_data.playerID.values:
        if player in team:
            print(master_data.nameFirst.values[count], master_data.nameLast.values[count])
        count += 1
