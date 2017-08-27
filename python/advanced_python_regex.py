# J. Gambino
# Metis Pre-work
# August 26, 2017


# I understand how regular expressions could be used here, but the data was clean enough I saw no need to do so.
# Below is the download of the Jupyter I used.

# coding: utf-8

# ### Import Data

# In[1]:

import csv


# In[2]:

with open('faculty.csv') as csvfile:
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

names = names[1::]
degrees = degrees[1::]
titles = titles[1::]
emails = emails[1::]


# ### Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

# In[3]:

degrees_each = []

for ii in range(0,len(degrees)):
    to_append = degrees[ii].split()

    for ii in range(0,len(to_append)):
        degrees_each.append(to_append[ii])


# In[4]:

degree_rename = {'0': 'no degree', 'M.S.': 'MS', 'Ph.D': 'PhD', 'Ph.D.': 'PhD', 'Sc.D.': 'ScD', 'B.S.Ed.': 'BSEd'}


# In[5]:

for ii in range(0,len(degrees_each)):
    if degree_rename.get(degrees_each[ii]):
        degrees_each[ii] = degree_rename.get(degrees_each[ii])
        #print(degrees_each[ii])


# In[6]:

print('There are {} unique degrees among the faculty.'.format(len(set(degrees_each))))


# In[7]:

from collections import Counter


# In[8]:

Counter(degrees_each)


# ### Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor

# In[12]:

# Simpler than before
for ii in range(0,len(titles)):
    if titles[ii] == 'Assistant Professor is Biostatistics':
        titles[ii] = 'Assistant Professor of Biostatistics'


# In[13]:

titles_each = list(set(titles))


# In[14]:

print('There are {} unique titles among the faculty.'.format(len(set(titles_each))))


# In[16]:

Counter(titles)


# ### Q3. Search for email addresses and put them in a list. Print the list of email addresses.

# In[21]:

email_domains = []
for email in emails:
    domain = email.split('@')[1]
    email_domains.append(domain)

email_domains = list(set(email_domains))


# In[22]:

email_domains


# In[ ]:
