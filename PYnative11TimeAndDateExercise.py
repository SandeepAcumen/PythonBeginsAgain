#1
'''
import datetime
print("Current date and time is ",datetime.datetime.now())

print(datetime.datetime.now().time())

'''
#2
'''
from datetime import datetime

date_string = "Feb 25 2020 4:20PM"
datatime_object = datetime.strptime(date_string,'%b %d %Y %I:%M%p')
print(datatime_object)

'''
#3
'''
from datetime import datetime,timedelta
give_date = datetime(2022,2,25)

days_to_subtract =7
res_date = give_date - timedelta(days=days_to_subtract)
print(res_date)

'''

#4
'''
from datetime import datetime

given_date = datetime(2020,2,25)
print("Given date is")
print(given_date.strftime('%A %d %B %Y'))

'''

#5
'''
from datetime import datetime
given_date = datetime(2020,7,26)
print(given_date.today().weekday())
print(given_date.strftime('%A'))

'''

#6
'''
from datetime import datetime,timedelta
given_date = datetime(2020, 3, 22, 10, 00, 00)
days_to_add =7
res_date = given_date + timedelta(days=days_to_add, hours=12)
print(res_date)
'''

#7
'''
import time
millisecond = int(round(time.time() *10000))
print(millisecond)

'''

#8

'''
from datetime import datetime
given_date = datetime(2020,2,2025)
string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)

'''

#9

'''l

from datetime import datetime
from dateutil.relativedelta import relativedelta

given_date  = datetime(2020,2,25).date()

months_to_add = 4
new_date = given_date + relativedelta(months = + months_to_add)
print(new_date)


'''






































































