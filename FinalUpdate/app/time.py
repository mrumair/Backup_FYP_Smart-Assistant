import datetime
import time
from dateutil import parser

#check time validation
def timeChecking(TimeVar):
	tBit = 0
	TempTime = TimeVar
	currentDT = datetime.datetime.now()
	print (currentDT)
	print ("Current Hour is: %d" % currentDT.hour)
	print ("Current Minute is: %d" % currentDT.minute)
	print("Input Time:" , TempTime)
	b=time.strptime(TempTime,'%H:%M')
	print("time is " , b.tm_hour)
	print("time mints is " , b.tm_min )
	if (  b.tm_hour > currentDT.hour):
		tBit = 22 
		print (tBit)
		print("you enter th correct hour")
	elif( b.tm_hour  == currentDT.hour and  b.tm_min  > currentDT.minute ):
		print ("Same Hour but mint should be greater")
		tBit = 33
		print (tBit)
	else:
		print ("you did not enter Correct Hour")
		print (tBit)
	return tBit

