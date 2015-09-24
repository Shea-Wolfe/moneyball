

def get_years_best(data,year):
    ret = data[data.yearID == year].groupby('playerID').agg('mean')
    cleaned = ret['AB'] >100
    ret = ret[cleaned]
    ret = (((ret.H+ret.BB+ret.HBP)/(ret.AB+ret.BB+ret.HBP+ret.SF))/ret.salary)*1000000
    ret.order(ascending=False)
    return ret
