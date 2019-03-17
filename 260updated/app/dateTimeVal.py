from datetime import date
from datetime import time
from datetime import datetime
from time import strptime
from os import *
import datetime
from datetime import datetime
from dateutil import parser
import time

class DTValidate:
	def CovertDate():
		CurrentDate = datetime.now()

		new = CurrentDate
	
		
		cday = new.day
		cmonth = new.month
		cyear = new.year



		if (cmonth == 1 ):
			cmonth = "January"
		if (cmonth == 2 ):
			cmonth = "February"
		if(cmonth ==3 ):
			cmonth = "March"
		if(cmonth ==4 ):
			cmonth = "April"
		if(cmonth ==5):
			cmonth = "May"
		if(cmonth ==6 ):
			cmonth = "June"
		if(cmonth ==7 ):
			cmonth = "July"
		if(cmonth == 8 ):
			cmonth = "August"
		if(cmonth == 9):
			cmonth = "September"
		if(cmonth ==10 ):
			cmonth = "October"
		if(cmonth ==11 ):
			cmonth = "November"
		if(cmonth ==12 ):
			cmonth = "December"

		stringDate = str(cday) +" "+ str(cmonth) +" "+ str(cyear)
		print(stringDate)
		return stringDate





	def CurrentDate():
		Current = datetime.now()
		print(Current)
		print(Current.day)
		print(Current.month)
		print(Current.year)
		print (str(Current.month)+" "+str(Current.day)+" "+str(Current.year))
		stringDate = str(Current.month)+" "+str(Current.day)+" "+str(Current.year)
		print(stringDate)
		return stringDate


	def DateValid(dateInput):
		dateV = dateInput
		dt = parser.parse(dateV)
		new = dt.date()
		print(new) 
		dBit = 0
		Current = datetime.now()
		print(Current.day)
		print(Current.month)
		print(Current.year)
		print(new.year)
		print(new.month)
		if(new.year == Current.year and new.month == Current.month and new.day == Current.day):
			dBit = 1
			print(dBit  , "BIT VALUE")
		else:
			dBit = 0
			print(dBit)
		print(dBit ,"Return Value")
		return dBit


	def DateTimeValidaion(DateVar , TimeVar):
		tBit = 0
		DateTime = DateVar
		TimeIn = TimeVar
		print(TimeIn)

		currentDT = datetime.now()
		print(currentDT)
		print ("Current Hour is: %d" % currentDT.hour)
		print ("Current Minute is: %d" % currentDT.minute)

		b=time.strptime(TimeIn,'%H:%M')
		print("time is " , b.tm_hour)
		print("time mints is " , b.tm_min )

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
		
		
		elif(new.year == now.year and new.month == now.month and new.day > now.day):
			print ("Same year same month but date greates")
			tBit =33
			print (tBit)

		elif(new.year == now.year and new.month == now.month and new.day == now.day and b.tm_hour > currentDT.hour):
			print("Year Month Date Same and Hour greates the Current")
			tBit = 34
			print(tBit)

		elif(new.year == now.year and new.month == now.month and new.day == now.day and b.tm_hour == currentDT.hour and b.tm_min > currentDT.minute):
			print("Year Month Date  Hour Same but minutes greates the Current")
			tBit = 35
			print(tBit)
		else:
			print ("you did not enter Correct date and Time")
			print (tBit)
		return tBit


	def splitString(SplitData):
		word = SplitData
		afterSplit = word.split('-')
		Session = afterSplit[0]
		Degree = afterSplit[1]
		RollNo = afterSplit[2]
		print(afterSplit)
		return afterSplit
		print ('Session is',Session , 'DEgree is', Degree ,'RollNo is',  RollNo)


# month date year
#DTValidate.splitString('2015-CS-160')
# DTValidate.CovertDate()
# DTValidate.CurrentDate()
# DTValidate.DateValid("11 March 2019")