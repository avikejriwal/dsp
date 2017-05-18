# PLACE YOUR CODE HERE
import pandas as pd
import re

fac_pd = pd.read_csv('faculty.csv')


# Q1

# stripping periods in degrees makes it a bit easier
facultyDegrees = fac_pd[' degree'].str.replace('\.', '')

diffDegrees = []
#get the different types of degrees
for deg in facultyDegrees:
    degrees = deg.split(' ')
    for degree in degrees:
        if degree not in diffDegrees and degree:
            diffDegrees.append(degree)

#count for each different degree
for degree in diffDegrees:
    count = sum(facultyDegrees.str.contains(degree))
    print(degree, count)

# Q2 get the titles and frequencies
print(fac_pd.groupby(' title')[' title'].count())


# Q3
text_file = open("emails.txt", "w")

emails = fac_pd[' email']
for email in emails:
    text_file.write(email + '  \n')

text_file.close()

# Q4: get unique email domains
domains = []
for email in emails:
    domain = '@' + '.'.join(re.split('[.@]', email)[1:])
    domains.append(domain)

domains = list(set(domains))

for domain in domains:
    count = sum(emails.str.contains(domain))
    print(domain, count)

# Q5
