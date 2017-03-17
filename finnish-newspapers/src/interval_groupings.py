import os, sys, re
import csv
import pandas
import datetime


def open_data():

    with open("../unified/issuedates.csv", "r", encoding="utf-8") as f:
        csvreader = csv.reader(f)
        return [x for x in csvreader]



if __name__ == "__main__":


    data = open_data()
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

    for year in weeks:
        for issn in weeks[year]:
            score = statistics.mode(weeks[year][issn])
            print(year, issn, score)
    
