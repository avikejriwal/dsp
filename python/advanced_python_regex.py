# PLACE YOUR CODE HERE
import re

f = open('faculty.csv', 'r')

data = []

degrees = {}

# Question 1
for line in f:
    professor = line.replace('\n','').split(',')
    data.append(professor)
    degs = professor[1].replace('.','').split(' ')
    for deg in degs:
        if deg not in degrees:
            degrees[deg] = 1
        else:
            degrees[deg] += 1

print(degrees)

titles = {}
# Question 2
for professor in data:
    title = ' '.join(professor[2].split(' ')[:-2])
    if title not in titles:
        titles[title] = 1
    else:
        titles[title] += 1

print(titles)

# Question 3
emails = []
for professor in data:
    emails.append(professor[3])

print(emails[1:])

# Question 4:
domains = {}
for email in emails:
    domain = '@' + email.split('@')[-1]
    if domain not in domains:
        domains[domain] = 1
    else:
        domains[domain] += 1

print(domains)

# Question 5

w = open('emails.csv', 'w')

for email in emails[1:]:
    w.write(email + '\n')

w.close()
