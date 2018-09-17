import csv
import pprint
import random

def getScheduleInfo():
    single = {}
    multiple = []
    dates = []
    with open('support.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            row['magicNumber'] = random.randint(1,101)
            multiple.append(row)
    return multiple

# def getPickOrder():
#     # grab object run through names based on rank randomize put into order

def specialOrder(list):
    return sorted(list, key = lambda i: (i['Rank'], i['magicNumber']),reverse=True)

def assignDate(lista):
    for person in lista:
        # print type(person)
        # print person
        if int(person['Rank']) == 3:
            print pprint.pprint(person['Name'])
            print person.keys()[person.values().index('1')]


def scheduleMe():
    # pprint.pprint(specialOrder(getScheduleInfo()))
    assignDate(specialOrder(getScheduleInfo()))

scheduleMe()    

