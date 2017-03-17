import os, sys, json, re
import datetime

def open_data(period):
    path = "page_years/"
    data = {}
    for F in os.listdir(path):
        year = re.split("_", F)[0]
        if in_period(period, year):
            lang = re.split("_", F)[-1].replace(".json", "")

            with open(path+F, "r", encoding="utf-8") as f:
                tmp = json.load(f)
            if "total" in tmp:
                data.update(tmp["total"]["absolute"])


    return data

def in_period(period, year):

    if len(period) == 1:
        if period[0] == int(year): return True
    else:
        if int(year) >= period[0] and int(year) < period[1]: return True
    return False



def parse_key(key):

    key = re.split("#", key)[2]
    key = re.split("_", key)
    if len(key) > 2: 
        key[2] = "".join(key[2:])
        
    else:
        key.append(1)
    return "#".join([str(x) for x in key[:3]])

def clean_unique_issues(data):
    res = {}
    for key in data:
        if parse_key(key) not in res:
            res.update({parse_key(key) : data[key]})
        else:
            res[parse_key(key)] += data[key]
    return [x+"#"+str(res[x]) for x in res]

def get_date_for_year(i, numbers, year):

    days = int(round(365/len(numbers)))*i
    tdelta = datetime.timedelta(days=days)
    date = datetime.date(int(year), 1, 1)+tdelta
    return str(date.year)+"-"+str(date.month)+"-"+str(date.day)+"#MD"
    
def get_date_for_month(i, numbers, D):
    
    D = re.split("-", D)
    days = int(round(30/len(numbers)))*i
    tdelta = datetime.timedelta(days=days)
    date = datetime.date(int(D[0]), int(D[1]), 1)+tdelta
    return str(date.year)+"-"+str(date.month)+"-"+str(date.day)+"#D"
    


def clean_incomplete_datetimes(data):

    no_months = {}
    no_dates = {}
    for x in data:
        issn, date, number, wordcount = re.split("#", x)
        date_tmp = re.split("-", date)
        if len(date_tmp) == 1:
            if issn+"#"+date_tmp[0] not in no_months:
                no_months.update({issn+"#"+date_tmp[0]:[x]})
            else:
                no_months[issn+"#"+date_tmp[0]].append(x)

        elif len(date_tmp) == 2:
            if issn+"#"+date_tmp[0]+"-"+date_tmp[1] not in no_dates:
                no_dates.update({issn+"#"+date_tmp[0]+"-"+date_tmp[1]:[x]})
            else:
                no_dates[issn+"#"+date_tmp[0]+"-"+date_tmp[1]].append(x)


    date_map = {}
    for key in no_months:
        numbers = no_months[key].sort()
        year = re.split("#", key)[-1]
        date_map.update({no_months[key][i]:get_date_for_year(i, no_months[key], year) for i in range(len(no_months[key]))})


    for key in no_dates:
        date_tag = re.split("#", key)[-1]
        date_map.update({no_dates[key][i]:get_date_for_month(i, no_dates[key], date_tag) for i in range(len(no_dates[key]))})

    for i in range(len(data)):
        datetag = re.split("#", data[i])[1]
        if data[i] in date_map:
            data[i] = data[i].replace(datetag, date_map[data[i]])
        else:
            data[i] = data[i].replace(datetag, datetag+"#")
            

    return data


if __name__ == "__main__":

    data = open_data([1771, 1910])
    print(len(data))
    data = clean_unique_issues(data)
    print(len(data))
    data = clean_incomplete_datetimes(data)
    print(len(data))
    with open("issuedates.csv", "w", encoding="utf-8") as f:
        for row in data:
            f.write('"'+'","'.join(re.split("#", row))+'"'+"\n")

