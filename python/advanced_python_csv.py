f = open('faculty.csv', 'r')

w = open('emails.csv', 'w')

# Question 5
for line in f:
    professor = line.replace('\n','').split(',')
    w.write(professor[3] + '\n')

w.close()
