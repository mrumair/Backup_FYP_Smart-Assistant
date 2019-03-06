# from datetime import tzinfo, timedelta, datetime

# def ObtainDate():
#     isValid=False
#     while not isValid:
#         userIn = raw_input("Type Date: mm/dd/yy: ")
#         try:
#             d1 = datetime.strptime(userIn, "%m/%d/%y")
#             isValid=True
#         except:
#             print ("Invalid Format!")
#     return d1

# t = (ObtainDate() - datetime.now()).total_seconds()
# print (t)


from datetime import date
from datetime import time
from datetime import datetime
from time import strptime
from os import *

# nowDate = "02/9/2019"

# d = datetime.strptime(nowDate, "%m/%d/%Y")
# # date_format = "%m-%d-%Y"
# # datetime_obj = datetime.strptime(str(data[name]), "%Y-%m-%d")
# print(d.date())


# today = str(date.today())
# print(today)   # '2017-12-26'

# diff = str(d) -str(today)
# print(diff)


from datetime import datetime
from dateutil import parser



def timeNew(DateVar):
	tBit = 0
	DateTime = DateVar

	now=datetime.now()
	print (now.month)
	print (now.day)
	print (now.year)
	print (str(now.month)+"/"+str(now.day)+"/"+str(now.year))


	dt = parser.parse(DateTime)
	new = dt.date()
	print(new) 
	print (str(new.month)+"/"+str(new.day)+"/"+str(new.year))

	print(new.year)
	print(now.year)

	if (new.year > now.year):
		tBit = 11
		print (tBit)
		print("you enter th correct date ")
	
	elif(new.year == now.year and new.month > now.month ):
		print ("Same Year but month should be greater")
		tBit = 22
		print (tBit)
	
	
	elif(new.year == now.year and new.month == now.month and new.day >= now.day):
			print ("Same year same month but date greates")
			tBit =33
			print (tBit)
	else:
		print ("you did not enter Correct day")
		print (tBit)
	return tBit


timeNew("18 March 2019")
# d = datetime.strptime(str(new), "%Y/%m/%d")

# print (d.month)
# print (d.day)
# print (d.year)
# print (str(d.month)+"/"+str(d.day)+"/"+str(d.year))


# # date_format = "%m-%d-%Y"
# datetime_obj = datetime.strptime(str(data[name]), "%Y-%m-%d")

# print (currenthour+":"+mm+":"+ss)