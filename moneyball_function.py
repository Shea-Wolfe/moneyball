

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
