from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
import en_core_web_sm
from tqdm import tqdm
from model import post
from model import BotBehaviour
from model import *
from infer_fnc import *
from infer_fnc import inferencing
from signup import *

global tempS
tempSelf=3
tempsSelf = 3

cBit3=3
cBitMed=3

# cBit2=3

class text_spacy:
	def __init__(self):
		relationpropertydate = ""
		self.cBit2 = 0
		self.tempTime2 = []
		self.tempLoc2 = []
		self.cBits2 =0

	def foo(self):
		# global cBit3
		#global tempSelf
		#global cBit2
		# ctempTime3 = self.tempTime2
		cBit3=self.cBit2
		return cBit3

	def foos(self):
		# global cBit3
		#global tempSelf
		#global cBit2
		# ctempTime3 = self.tempTime2
		cBits3=self.cBits2
		return cBits3


	def fooList(self):
		# global cBit3
		#global tempSelf
		#global cBit2
		ctempTime3 = self.tempTime2
		# print ("time List" , ctempTime3)
		return ctempTime3
	

	def fooLocList(self):
		# global cBit3
		#global tempSelf
		#global cBit2
		ctempLoc3 = self.tempLoc2

		# print ("time List" , ctempTime3)
		return ctempLoc3
	# def infChecker():
	# 	if (self.cBit2!= 0):
	# 		tempTime = abc.times(subjectClear , objectClear , relationclear)
	# 		print("check inference time funct called......")
	# 		self.tempTime2 = tempTime
	# 	return self.tempTime2


	def function_spacy(self,docx12):
		cBit3=0
		clearsubject = ""
		relationclear = ""
		upper = ""
		seond = ""
		relationproperty = ""
		
		timeProperty = ""
		institute = ""
    
		#global upper
		value_doc = docx12
		nlp = spacy.load('en_core_web_sm')
		docx1 = nlp(value_doc)

#docx1 = nlp("I am Rabeeya Saleem and have a meeting with Taliah Tajammal at 8pm on 22 december in PU")
		for token in docx1:
			subject = (token.text , token.pos_ , token.tag_ , token.dep_)
			print(subject )
			pos = (token.pos_)
			if pos is 'PRON'  :
				nodetodraw = token.text
				print(nodetodraw , "is node")
				 
				clearsubject = token.text
			deep = (token.dep_)
			if deep is 'dobj':
				relationship = token.text
				print(relationship , "is a relationship")
				relationclear = relationship
				#post.functiona(relationship)
		person = []
		#global upper
		for num in docx1.ents:
			entitites = (num.label_)
			if entitites is "PERSON":
				person.append(num.text)
				upper="Umair"
				seond=person[0]
				#seond=person[-1]
				print("subject is: ", upper)
				print("object is: ", seond)
				#print(person , "is lasoknkan")
				subjectClear = upper
				objectClear = seond
		for token in docx1.ents:
			entity = (token.label_ )
			if entity is 'ORG':
				organization = token.text
				print(organization , "is an organization")
				institute = organization
		#		post.functiona(organization)
			if entity is 'LOC':
				location = token.text
				print(location , "is an location")
		#		post.functiona(location)
			if entity is 'DATE':
				date = token.text
				print(date , "is a Date")
				relationpropertydate = date
		#		post.functiona(date)
			if entity is 'PERSON':
				person = []
				person = token.text
				print(person , "is a person")
				#post.functiona(person)

				
				#entity1 = token.text

			if entity is 'NORP':
				nationalities = token.text
				print(nationalities , "is a nationality")
		#		post.functiona(nationalities)

			if entity is 'FAC':
				fac = token.text
				print(fac , "is a building")
		#		post.functiona(fac)

			if entity is 'GPE':
				gpe = token.text
				print(gpe , "is a cities")
				institute = gpe
		#		post.functiona(gpe)

			if entity is 'PRODUCT':
				produxt = token.text
				print(produxt , "is a product")
		#		post.functiona(product)

			if entity is 'EVENT':
				event = token.text
				print(event , "is a event")
		#		post.functiona(event)

			if entity is 'WORK_OF_ART':
				woa = token.text
				print(woa , "is a work of art")
		#		post.functiona(woa)

			if entity is 'LAW':
				law = token.text
				print(law , "is a Law")
		#		post.functiona(law)

			if entity is 'LANGUAGE':
				lang = token.text
				print(lang , "is a Language")
		#		post.functiona(lang)

			if entity is 'TIME':
				time = token.text
				print(time , "is a Time")
				timeProperty = time
		#		post.functiona(time)

			print(entity)
			if entity is 'PERCENT':
				percent = token.text
				print(percent , "is a percent")
		#		post.functiona(percent)

			if entity is 'MONEY':
				money = token.text
				print(money , "is a money")
		#		post.functiona(money)

			if entity is 'QUANTITY':
				quant = token.text
				print(quant , "is a quantity")
		#		post.functiona(quant)

			if entity is 'ORDINAL':
				ordinal = token.text
				print(ordinal , "is a ordinal")
		#		post.functiona(ordinal)

			if entity is 'CARDINAL':
				cardinal = token.text
				print(cardinal , "is a CARDINAL")
		#		post.functiona(cardinal)

		self.cBit2=post.validateInfo(institute , timeProperty )
		if (self.cBit2==0):
			tempSelf = self.cBit2

			#text_spacy.foo(cBit2)			
			#global cBit3
			#cBit3=0
			print("Flag-0 ... Adding the data")
			post.createNodeQueru(subjectClear , "subject")
			post.createNodeQueru(objectClear , "object")
			post.createqueryrelation(subjectClear ,objectClear , relationclear ,timeProperty , institute )
			#global cBit3
			#cBit3=1
		else:
			print("Flag -1 ... incomplete info")
			tempSelf=self.cBit2

			#print("Value of tempSelf is :", tempSelf)
			#text_spacy.foo(cBit2)
		if (self.cBit2!= 0):
			abc = inferencing()
			tempTime = []
			tempTime = abc.times(subjectClear , objectClear , relationclear)
			print("check inference time funct called......")

			for i in range(len(tempTime)):
				print ("time Inferenced yoyoyoyo" ,tempTime[i])
			self.tempTime2 = tempTime
		return self.tempTime2

		if (self.cBit2!= 0):
			xyz = inferencing()
			temoLoc = []
			temoLoc = xyz.locations(subjectClear , objectClear , relationclear)
			print("check location time funct called......")

			for i in range(len(temoLoc)):
				print ("location Inferenced yoyoyoyo" ,temoLoc[i])
			self.tempLoc2 = temoLoc
		return self.tempLoc2

		#print (clearsubject  , "is I we they you")
		#print (relationclear  , "is exact relationship")
		#print (relationproperty  , "is exact relationproperty")
		#print (relationpropertydate  , "is exact relationpropertydate")
		#print (institute  , "is exact institute")

		#print (upper, "is exact institute")
		#print (seond, "is exact institute")
		#post.relationa(upper, seond, relationclear)

		#post.createNode(upper ,seond, relationclear, relationproperty, relationpropertydate, institute, "subject" , "object")
		#post.askQ()
		# self.cBit2=post.validateInfo(institute , timeProperty , subjectClear ,objectClear)

		# self.cBits2 = post.validateSubObj(subjectClear , objectClear)
		# if (self.cBits2 == 0):
		# 	tempsSelf = self.cBits2
		# 	print ("Flag-0 ... Subject Object Added")

		# 	self.cBit2=post.validateInfo(institute , timeProperty )
		# 	if (self.cBit2==0):
		# 		tempSelf = self.cBit2

		# 		#text_spacy.foo(cBit2)			
		# 		#global cBit3
		# 		#cBit3=0
		# 		print("Flag-0 ... Adding the data")
		# 		post.createNodeQueru(subjectClear , "subject")
		# 		post.createNodeQueru(objectClear , "object")
		# 		post.createqueryrelation(subjectClear ,objectClear , relationclear ,timeProperty , institute )
		# 		#global cBit3
		# 		#cBit3=1
		# 	else:
		# 		print("Flag -1 ... incomplete info")
		# 		tempSelf=self.cBit2

		# 		#print("Value of tempSelf is :", tempSelf)
		# 		#text_spacy.foo(cBit2)
		# 	if (self.cBit2!= 0):
		# 		abc = inferencing()
		# 		tempTime = []
		# 		tempTime = abc.times(subjectClear , objectClear , relationclear)
		# 		print("check inference time funct called......")

		# 		for i in range(len(tempTime)):
		# 			print ("time Inferenced yoyoyoyo" ,tempTime[i])
		# 		self.tempTime2 = tempTime
		# 	return self.tempTime2

		# 	if (self.cBit2!= 0):
		# 		xyz = inferencing()
		# 		temoLoc = []
		# 		temoLoc = xyz.locations(subjectClear , objectClear , relationclear)
		# 		print("check location time funct called......")

		# 		for i in range(len(temoLoc)):
		# 			print ("location Inferenced yoyoyoyo" ,temoLoc[i])
		# 		self.tempLoc2 = temoLoc
		# 	return self.tempLoc2

		# else:
		# 	print("Flag -1 ... incomplete SubObj info")
		# 	tempsSelf=self.cBits2





		

# abc = inferencing()
# 			tempTime = abc.times(subjectClear , objectClear , relationclear)
# 			self.tempTime2 = tempTime

		#return cBit3

  

	# def checkBit():
	# 	global cBit3
	# 	cBit5
	# 	if (cBit3==0):
	# 		cBit5=0
	# 	else:
	# 		cBit5=1
	# 	return cBit5


		#return cBit3

		

#bbh = BotBehaviour()
#tempS = bbh.askQ()

# abc = post()
# show = abc.showallnode()





	#MATCH (u:User {username:'admin'}), (r:Role {name:'ROLE_WEB_USER'})
	#CREATE (u)-[:HAS_ROLE]->(r)


	#MATCH (p:label12)-[r:new]->(c:label12) 
	#SET r.type = "neww" 