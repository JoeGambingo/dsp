# J. Gambino
# Metis Pre-work
# August 27, 2017

# Below is the download of the Jupyter I used.

# coding: utf-8

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


# ### Clean values first

# In[3]:

# First remove whitespace from before degree
for ii in range(0,len(degrees)):
    if degrees[ii][0] == ' ':
        degrees[ii] = degrees[ii][1::]


# In[4]:

# Make entries consistent
degree_rename = {'PhD': 'Ph.D.', 'Ph.D': 'Ph.D.', 'MD MPH Ph.D': 'M.D. M.P.H. Ph.D.', 'ScD': 'Sc.D.', '0': 'no degree', 'JD MA MPH MS PhD': 'J.D. M.A. M.P.H. M.S. Ph.D.'}
title_rename = {'Assistant Professor is Biostatistics': 'Assistant Professor of Biostatistics'}


# In[5]:

degrees_clean = [degree_rename.get(abbrev, abbrev) for abbrev in degrees]
titles_clean = [title_rename.get(t, t) for t in titles]


# In[6]:

degrees = degrees_clean
titles = titles_clean


# ### Q6. Create a dictionary in the below format:
# ```
# faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
#                  'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
# ```

# In[7]:

faculty_dict = {}
for ii in range(0, len(names)):
    last_name = names[ii].split()[-1]
    degree = degrees[ii]
    title = titles[ii]
    email = emails[ii]

    if last_name in faculty_dict:
        current_value = faculty_dict[last_name]
        current_value.append([degree, title, email])
        faculty_dict[last_name] = current_value
    else:
        faculty_dict[last_name] = [[degree, title, email]]


# ### Q7. The previous dictionary does not have the best design for keys. Create a new dictionary with keys as:

# ```
# professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],
#                 ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],
#                 ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
#                 ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
#                 ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
# ```

# In[8]:

faculty_dict_better = {}
for ii in range(0, len(names)):
    first_name = names[ii].split()[0]
    last_name = names[ii].split()[-1]
    degree = degrees[ii]
    title = titles[ii]
    email = emails[ii]

    faculty_dict_better[(first_name, last_name)] = [[degree, title, email]]


# ### Q8. It looks like the current dictionary is printing by first name. Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

# In[25]:

for (key, value) in faculty_dict_better.items():
    print(key, value)
