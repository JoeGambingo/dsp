# J. Gambino
# Metis Pre-work
# August 26, 2017

# Import Libraries
import csv

# Parse email address
with open('python/faculty.csv') as csvfile:
    faculty = csv.reader(csvfile)

    names = []
    degrees = []
    titles = []
    emails = []

    for row in faculty:
        names.append(row[0])
        degrees.append(row[1])
        titles.append(row[2])
        emails.append(row[3])

#names = names[1::]
#degrees = degrees[1::]
#titles = titles[1::]
emails = emails[1::]

#for ii in range(0,len(emails)):
#    print(emails[ii])

# Write to CSV File
with open('python/emails.csv', 'w+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    for value in emails:
        writer.writerow([value])
