import csv
import pprint
import random

def getScheduleInfo():
    multiple = []
    with open('/Users/adolfomoreno/Desktop/scheduler/support-scheduler/support.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            row['magicNumber'] = random.randint(1,101)
            multiple.append(row)
    return multiple

def specialOrder(list):
    return sorted(list, key = lambda i: (i['Rank'], i['magicNumber']),reverse=True)

def assignDate(lista):
    dateCounter = {}
    primary = []
    secondary = []
    for person in lista:
        # print type(person)
        if int(person['Rank']) == 3:
            pprint.pprint(person['Name'])
            # pprint.pprint(person.keys()[person.index('1')])
            dateCounter[list(person.keys())[list(person.values()).index('1')]] = 1
            pprint.pprint(list(person.keys())[list(person.values()).index('1')])

            # dateList.append()
    pprint.pprint(dateCounter)
            # pprint.pprint(person.keys()[person.values().index('1')])


def scheduleMe():
    # pprint.pprint(specialOrder(getScheduleInfo()))
    assignDate(specialOrder(getScheduleInfo()))

scheduleMe()
