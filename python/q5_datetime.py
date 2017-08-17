# J. Gambino
# Metis Pre-work
# 8-16-2017

from datetime import datetime

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

datetime_start = datetime.strptime(date_start, '%m-%d-%Y')
datetime_stop = datetime.strptime(date_stop, '%m-%d-%Y')

delta = datetime_stop - datetime_start
print('a)', delta.days)

####b)
date_start = '12312013'
date_stop = '05282015'

datetime_start = datetime.strptime(date_start, '%m%d%Y')
datetime_stop = datetime.strptime(date_stop, '%m%d%Y')

delta = datetime_stop - datetime_start
print('b)', delta.days)


####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

datetime_start = datetime.strptime(date_start, '%d-%b-%Y')
datetime_stop = datetime.strptime(date_stop, '%d-%b-%Y')

delta = datetime_stop - datetime_start
print('c)', delta.days)
