import os, sys, re
import csv
import pandas
import datetime
import statistics
from visualization_tools import stacked_bar_chart as SBC


BLUE_COLORS = ("#87a2de", 
               "#6389e0", 
               "#4979e5", 
               "#3269e7", 
               "#215de7", 
               "#0f51e8", 
               "#044aea", 
               "#083db7", 
               "#06349d") 

def open_data():

    with open("../unified/issuedates.csv", "r", encoding="utf-8") as f:
        csvreader = csv.reader(f)
        return [x for x in csvreader]

def visualize_group(df, cap, cut_out, colors, y_scale):

    df = df.fillna(0)
    df_indices = [x for x in df.index if int(x) > 0]
    df =  df.loc[df_indices,:]
    
    if cut_out:
        if int(cut_out) <= max(df.index):
            df = df[:cut_out]
    
    if cap:
        df_bottom_indices = [x for x in df.index if int(x) < int(cap)]
        df_bottom = df.loc[df_bottom_indices,:]
        df_top = df[int(cap):].sum()
        df_top.name = str(cap)+"+"
        df = df_bottom.append(df_top)
    
    df = df.transpose()
    SBC(df, colors, y_scale)

def filter_by_language(data, lang):

    with open("../originals/circulation090217/newspapers-utf8.csv", "r", encoding="utf-8") as f:
        csvreader = csv.reader(f)
        lang_data ={x[0].lower():x[9] for x in csvreader}
    return [x for x in data if x[0].lower() in lang_data and lang_data[x[0].lower()] == lang]
    


def dict_to_DataFrame(data):
    res = {}
    for year in data:
        year_scores = []
        for issn in data[year]:
            if type(data[year][issn]) == list:
                try:
                    score = statistics.mode(data[year][issn])
                except:
                    MAX = 0
                    c = 0
                    for i in data[year][issn]:
                        if data[year][issn].count(i) > c and i > MAX:
                            MAX = i
                            c = data[year][issn].count(i)
                    score = MAX
            else:
                score = data[year][issn]
            year_scores.append(score)
        year_scores = {i:year_scores.count(i) for i in year_scores}
        res.update({year:year_scores})

    return pandas.DataFrame(res)

if __name__ == "__main__":

    if len(sys.argv) != 7:
        sys.exit("proper arguments: group|language|cut-off|cap|colorscale|y-scale")


    data = open_data()

    GROUP, LANGUAGE, CUT_OFF, CAP, COLOR, Y_SCALE = sys.argv[1:]


    if LANGUAGE in ("fin", "swe"):
        data = filter_by_language(data, LANGUAGE)

    if GROUP not in ("week", "month", "year"):
        sys.exit("proper group names: 'week', 'month', 'year'")

    try:
        CUT_OFF = int(CUT_OFF)
    except:
        CUT_OFF = False

    try:
        CAP = int(CAP)
    except:
        CAP = False

    try:
        Y_SCALE = int(Y_SCALE)
    except:
        Y_SCALE = False
        

    weeks = {}
    months = {}
    years = {}



    for X in data:
        try:
            issn, date, note, number, wordcount = X
        except:
            print(X)
            sys.exit()
        date = re.split("-", date)
        year = int(date[0])
        week = datetime.date(int(date[0]), int(date[1]), int(date[2])).isocalendar()[1]-1
        month = int(date[1])-1
    
        if year not in weeks:
            weeks.update({year:{issn:[0 for x in range(54)]}})
        else:
            if issn not in weeks[year]:
                weeks[year].update({issn:[0 for x in range(54)]})

        weeks[year][issn][week] += 1

        if year not in months:
            months.update({year:{issn:[0 for x in range(12)]}})
        else:
            if issn not in months[year]:
                months[year].update({issn:[0 for x in range(12)]})

        months[year][issn][month] += 1

        if year not in years:
            years.update({year:{issn:0}})
        else:
            if issn not in years[year]:
                years[year].update({issn:0})

        years[year][issn] += 1

    groups = {"week":weeks, "month":months, "year":years}

    visualize_group(dict_to_DataFrame(groups[GROUP]), CAP, CUT_OFF, COLOR, Y_SCALE)




    
