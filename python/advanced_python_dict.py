import csv
import re

f = open('faculty.csv', 'r')
reader = csv.reader(f)

listProf = list(reader)[1:]

# Q6
dictData = {}

for prof in listProf:
    lastName = prof[0].split(' ')[-1]
    title = ' '.join(prof[2].split(' ')[:-2])
    degree = prof[1][1:]
    if lastName in dictData:
        dictData[lastName].append([degree, title, prof[3]])
    else:
        dictData[lastName] = [degree, title, prof[3]]

for key, value in dictData.items():
    print(key, value)

print('')

#Q7
dictData = {}

for prof in listProf:
    firstName = prof[0].split(' ')[0]
    lastName = prof[0].split(' ')[-1]
    tup = (firstName, lastName)
    title = ' '.join(prof[2].split(' ')[:-2])
    degree = prof[1][1:]
    if tup in dictData:
        dictData[tup].append([degree, title, prof[3]])
    else:
        dictData[tup] = [degree, title, prof[3]]

for key, value in sorted(dictData.items(), key=lambda x: x[0]):
    print(key, value)

print('')
#Q8

for key, value in dictData.items():
    print(key, value)
