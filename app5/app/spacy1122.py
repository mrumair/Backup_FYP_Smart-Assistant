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
# from main import gloVar

global tempS
tempSelf=3
tempsSelf = 3
tBit3= 3
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
        self.tBit =0 
        self.sSubject = ""
        self.sObject = ""

    def subFoo(self):
        csub = self.sSubject
        return csub

    def objFoo(self):
        cobj = self.sObject
        return cobj

    def foo(self):
        # global cBit3
        #global tempSelf
        #global cBit2
        # ctempTime3 = self.tempTime2
        cBit3=self.cBit2
        return cBit3

    def fooTime(self):
        # global cBit3
        #global tempSelf
        #global cBit2
        # ctempTime3 = self.tempTime2
        tBit3=self.tBit
        return tBit3

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
    #   if (self.cBit2!= 0):
    #       tempTime = abc.times(subjectClear , objectClear , relationclear)
    #       print("check inference time funct called......")
    #       self.tempTime2 = tempTime
    #   return self.tempTime2


    def function_spacy(self,docx12,varGlo ):
        cBit3=0
        tBit3 = 0
        clearsubject = ""
        relationclear = ""
        objectClear = ""
        subjectClear = ""
        upper = ""
        seond = ""
        relationproperty = ""
        relationpropertydate = ""
        
        timeProperty = ""
        institute = ""
        check = ""
        quest = ""
    
        #global upper
        value_doc = docx12
        nlp = spacy.load('en_core_web_sm')
        docx1 = nlp(value_doc)



        for token1 in docx1:
            check = ""
            t = (token1.text)
            punc_list = ['.' , '?' ]
            for p in punc_list:
                if t==p:
                    check = t
                    print (check , "check print")

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
                upper= varGlo
                seond=person[0]

                #seond=person[-1]
                
                #print(person , "is lasoknkan")
                subjectClear = upper
                objectClear = seond
                tempObj = post.ObjectSelection(objectClear)
                if (tempObj == True):
                    objectClear = seond
                else:
                    objectClear = ""


                print("subject is: ", subjectClear)
                print("object is: ", objectClear)

                self.sSubject = subjectClear
                self.sObject = objectClear
        for token in docx1.ents:
            entity = (token.label_ )
            if entity is 'ORG':
                organization = token.text
                print(organization , "is an organization")
                institute = organization
        #       post.functiona(organization)
            if entity is 'LOC':
                location = token.text
                print(location , "is an location")
        #       post.functiona(location)
            if entity is 'DATE':
                date = token.text
                print(date , "is a Date")
                relationpropertydate = date
                self.tBit = post.timeNew(date)

                if (self.tBit == 0):
                    relationpropertydate = ""
                    print(relationpropertydate)
                    print(date , "is a Time")
                    print(relationpropertydate ,"Before validateInfo Check")
                else:
                    relationpropertydate = date
                    print(date , "is a Time")
        #       post.functiona(date)
            if entity is 'PERSON':
                person = []
                person = token.text
                print(person , "is a person")
                #post.functiona(person)

                
                #entity1 = token.text

            if entity is 'NORP':
                nationalities = token.text
                print(nationalities , "is a nationality")
        #       post.functiona(nationalities)

            if entity is 'FAC':
                fac = token.text
                print(fac , "is a building")
        #       post.functiona(fac)

            if entity is 'GPE':
                gpe = token.text
                print(gpe , "is a cities")
                institute = gpe
        #       post.functiona(gpe)

            if entity is 'PRODUCT':
                produxt = token.text
                print(produxt , "is a product")
        #       post.functiona(product)

            if entity is 'EVENT':
                event = token.text
                print(event , "is a event")
        #       post.functiona(event)

            if entity is 'WORK_OF_ART':
                woa = token.text
                print(woa , "is a work of art")
        #       post.functiona(woa)

            if entity is 'LAW':
                law = token.text
                print(law , "is a Law")
        #       post.functiona(law)

            if entity is 'LANGUAGE':
                lang = token.text
                print(lang , "is a Language")
        #       post.functiona(lang)

            if entity is 'TIME':
                time = token.text
                print(time , "is a Time")

                timeProperty = time

                time = token.text
                print(time , "is a Time")
                timeProperty = time
                self.tBit = post.timeChecking(time)

                if (self.tBit == 0):
                    timeProperty = ""
                    print(timeProperty)
                    print(time , "is a Time")
                    print(timeProperty ,"Before validateInfo Check")
                else:
                    timeProperty = time
                    print(time , "is a Time")
        #       post.functiona(time)

            print(entity)
            if entity is 'PERCENT':
                percent = token.text
                print(percent , "is a percent")
        #       post.functiona(percent)

            if entity is 'MONEY':
                money = token.text
                print(money , "is a money")
        #       post.functiona(money)

            if entity is 'QUANTITY':
                quant = token.text
                print(quant , "is a quantity")
        #       post.functiona(quant)

            if entity is 'ORDINAL':
                ordinal = token.text
                print(ordinal , "is a ordinal")
        #       post.functiona(ordinal)

            if entity is 'CARDINAL':
                cardinal = token.text
                print(cardinal , "is a CARDINAL")
        #       post.functiona(cardinal)

        if check == '.':
            self.cBit2=post.validateInfo(institute , timeProperty , relationpropertydate , objectClear)     
            if (self.cBit2==0):
                tempSelf = self.cBit2

                #text_spacy.foo(cBit2)          
                #global cBit3
                #cBit3=0
                print("Flag-0 ... Adding the data")
                post.createNodeQueru(subjectClear , "subject")
                post.createNodeQueru(objectClear , "object")
                # print(relationclear,"is relationclear")
                post.createqueryrelation(subjectClear ,objectClear , relationclear ,timeProperty , institute ,relationpropertydate)
                #global cBit3
                #cBit3=1
            else:
                print("Flag -1 ... incomplete info")
                tempSelf=self.cBit2

                #print("Value of tempSelf is :", tempSelf)
                #text_spacy.foo(cBit2)





            if (self.cBit2 == 111):
                # tempTime = []
                tempTime = ""
                self.tempTime2 = tempTime


            if (self.cBit2 == 666):
                tempTime = ""
                self.tempTime2 = tempTime


            if (self.cBit2==7):
                abc = inferencing()
                tempTime = []
                tempTime = abc.times(subjectClear , objectClear , relationclear)
                print("check inference time")
                for i in range(len(tempTime)):
                    print ("Select" ,tempTime[i])
                self.tempTime2 = tempTime

            


            if (self.cBit2==1):
                abc = inferencing()
                tempLoc = []
                tempLoc = abc.locations(subjectClear , objectClear , relationclear)
                print("check inference location")
                for i in range(len(tempLoc)):
                    print ("Select" ,tempLoc[i])
                self.tempTime2 = tempLoc

            if (self.cBit2==11):
                abc = inferencing()
                tempDate = []
                tempDate = abc.dates(subjectClear , objectClear , relationclear)
                print("check inference dates")
                for i in range(len(tempDate)):
                    print ("Select" ,tempDate[i])
                self.tempTime2 = tempDate

            if (self.cBit2==4):
                abc = inferencing()
                tempTime = []
                tempTime = abc.times(subjectClear , objectClear , relationclear)
                tempLoc = abc.locations(subjectClear,objectClear,relationclear)
                for r in tempLoc:
                    tempTime.append(r)

                print("check inference time and location")

                for i in range(len(tempTime)):
                    print ("Select" ,tempTime[i])
                self.tempTime2 = tempTime

            if (self.cBit2==44):
                abc = inferencing()
                tempTime = []
                tempTime = abc.times(subjectClear , objectClear , relationclear)
                tempDate = abc.dates(subjectClear,objectClear,relationclear)
                for r1 in tempDate:
                    tempTime.append(r1)

                print("check inference time and date")

                for i in range(len(tempTime)):
                    print ("Select" ,tempTime[i])
                self.tempTime2 = tempTime

            if (self.cBit2==444):
                abc = inferencing()
                tempTime = []
                tempLoc = abc.locations(subjectClear , objectClear , relationclear)
                tempDate = abc.dates(subjectClear,objectClear,relationclear)
                for r2 in tempDate:
                    tempLoc.append(r2)

                print("check inference location and date")

                for i in range(len(tempLoc)):
                    print ("Select" ,tempLoc[i])
                self.tempTime2 = tempLoc

            if (self.cBit2==333):
                abc = inferencing()
                tempTime = []
                tempTime = abc.times(subjectClear , objectClear , relationclear)
                tempLoc = abc.locations(subjectClear,objectClear,relationclear)
                tempDate = abc.dates(subjectClear,objectClear,relationclear)
                for r3 in tempLoc:
                    tempTime.append(r3)

                for r4 in tempDate:
                    tempTime.append(r4)

                print("check inference time, location and date")

                for i in range(len(tempTime)):
                    print ("Select" ,tempTime[i])
                self.tempTime2 = tempTime 

        if check == '?':
            for token11 in docx1:
                quest = ""
                t=(token11.text)
                mylist = ["Do","When","Where","Will","What"]
                for q in mylist:
                    if t==q:
                        quest=q
                        if (quest == "Do"):
                            print("Do question")
                            relationclear="meeting"
                            print(objectClear, institute,timeProperty,relationpropertydate)
                            self.cBit2=post.check(objectClear, institute , timeProperty ,relationpropertydate)
                            if (self.cBit2 == 100):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qperson(subjectClear , objectClear , relationclear)
                                print("check meeting wih person")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper
                            if (self.cBit2 == 101):
                                qinfer = inferencing()
                                qtime = []
                                qtime = qinfer.qtime(subjectClear , relationclear, timeProperty)
                                print("check meeting on time")
                                for i in range(len(qtime)):
                                    print (qtime[i])
                                self.tempTime2 = qtime
                            if (self.cBit2 == 102):
                                qinfer = inferencing()
                                qpertime = []
                                qpertime = qinfer.qpertime(subjectClear , objectClear, relationclear, timeProperty)
                                print("check meeting on person and time")
                                for i in range(len(qpertime)):
                                    print (qpertime[i])
                                self.tempTime2 = qpertime
                            if (self.cBit2 == 103):
                                qinfer = inferencing()
                                qperdate = []
                                qperdate = qinfer.qperdate(subjectClear , objectClear, relationclear, relationpropertydate)
                                print("check meeting on person and date")
                                for i in range(len(qperdate)):
                                    print (qperdate[i])
                                self.tempTime2 = qperdate
                            if (self.cBit2 == 104):
                                qinfer = inferencing()
                                qdate = []
                                qdate = qinfer.qdate(subjectClear , relationclear, relationpropertydate)
                                print("check meeting on date")
                                for i in range(len(qdate)):
                                    print (qdate[i])
                                self.tempTime2 = qdate
                            if (self.cBit2 == 105):
                                qinfer = inferencing()
                                qloc = []
                                qloc = qinfer.qloc(subjectClear , relationclear, institute)
                                print("check meeting on location")
                                for i in range(len(qloc)):
                                    print (qloc[i])
                                self.tempTime2 = qloc
                            if (self.cBit2 == 106):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qperloc(subjectClear , objectClear, relationclear, institute)
                                print("check meeting on person and location")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc
                        if (quest == "When"):
                            print("When question")
                            relationclear="meeting"
                            self.cBit2=post.checkwhen(objectClear, institute)
                            if (self.cBit2 == 200):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qmeetper(subjectClear , objectClear , relationclear)
                                print("check when have meeting with person")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper
                            if (self.cBit2 == 201):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qmeetperloc(subjectClear , objectClear , relationclear, institute)
                                print("check when have meeting with person at location")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper                      
                        if (quest == "Where"):
                            print("Where question")
                            relationclear="meeting"
                            self.cBit2=post.checkwhere(objectClear, timeProperty)
                            if (self.cBit2 == 300):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qmeetloc(subjectClear , objectClear , relationclear)
                                print("check where have meeting with person")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper
                            if (self.cBit2 == 301):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qmeetloctime(subjectClear , objectClear , relationclear, timeProperty)
                                print("check where have meeting with person at time")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper

                        if (quest == "What"):
                            print("What question")
                            print(docx1,"token value")
                            print(objectClear,subjectClear,"subject object Clear")
                            for q in docx1:
                                if q.text=="location" or q.text=="venue":
                                    based=q
                                    print(based,"location based question")
                                    relationclear="meeting"
                                    print(objectClear)
                                    self.cBit2=post.checkwhatloc(objectClear, timeProperty, relationpropertydate, institute)
                                    if (self.cBit2 == 400):
                                        qinfer = inferencing()
                                        qper = []
                                        qper = qinfer.qwhatloc(subjectClear , objectClear , relationclear)
                                        print("check what  location of meeting with person ")
                                        for i in range(len(qper)):
                                            print (qper[i])
                                        self.tempTime2 = qper
                                    # if (self.cBit2 == 401):
                                    #     qinfer = inferencing()
                                    #     qper = []
                                    #     qper = qinfer.qwhat(subjectClear , objectClear , relationclear,)
                                    #     print("check what  location of meeting with person ")
                                    #     for i in range(len(qper)):
                                    #         print (qper[i])
                                    #     self.tempTime2 = qper


                                if q.text=="time":
                                    based=q
                                    print(based," based question")
                                    relationclear="meeting"
                                    print(objectClear)
                                    self.cBit2=post.checkwhattime(objectClear, timeProperty, relationpropertydate, institute)
                                    if (self.cBit2 == 500):
                                        qinfer = inferencing()
                                        qper = []
                                        qper = qinfer.qwhattime(subjectClear , objectClear , relationclear)
                                        print("check what time of meeting with person ")
                                        for i in range(len(qper)):
                                            print (qper[i])
                                        self.tempTime2 = qper



        if check == '?':
            for token11 in docx1:
                quest = ""
                t=(token11.text)
                mylist = ["Do","When","Where","Will","What"]
                for q in mylist:
                    if t==q:
                        quest=q
                        if (quest == "Do"):
                            print("Do question")
                            relationclear="meeting"
                            print(objectClear, institute,timeProperty,relationpropertydate)
                            self.cBit2=post.check(objectClear, institute , timeProperty ,relationpropertydate)
                            if (self.cBit2 == 100):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qperson(subjectClear , objectClear , relationclear)
                                print("check meeting wih person")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper
                            if (self.cBit2 == 101):
                                qinfer = inferencing()
                                qtime = []
                                qtime = qinfer.qtime(subjectClear , relationclear, timeProperty)
                                print("check meeting on time")
                                for i in range(len(qtime)):
                                    print (qtime[i])
                                self.tempTime2 = qtime
                            if (self.cBit2 == 102):
                                qinfer = inferencing()
                                qpertime = []
                                qpertime = qinfer.qpertime(subjectClear , objectClear, relationclear, timeProperty)
                                print("check meeting on person and time")
                                for i in range(len(qpertime)):
                                    print (qpertime[i])
                                self.tempTime2 = qpertime
                            if (self.cBit2 == 103):
                                qinfer = inferencing()
                                qperdate = []
                                qperdate = qinfer.qperdate(subjectClear , objectClear, relationclear, relationpropertydate)
                                print("check meeting on person and date")
                                for i in range(len(qperdate)):
                                    print (qperdate[i])
                                self.tempTime2 = qperdate
                            if (self.cBit2 == 104):
                                qinfer = inferencing()
                                qdate = []
                                qdate = qinfer.qdate(subjectClear , relationclear, relationpropertydate)
                                print("check meeting on date")
                                for i in range(len(qdate)):
                                    print (qdate[i])
                                self.tempTime2 = qdate
                            if (self.cBit2 == 105):
                                qinfer = inferencing()
                                qloc = []
                                qloc = qinfer.qloc(subjectClear , relationclear, institute)
                                print("check meeting on location")
                                for i in range(len(qloc)):
                                    print (qloc[i])
                                self.tempTime2 = qloc
                            if (self.cBit2 == 106):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qperloc(subjectClear , objectClear, relationclear, institute)
                                print("check meeting on person and location")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc
                        if (quest == "When"):
                            print("When question")
                            relationclear="meeting"
                            self.cBit2=post.checkwhen(objectClear, institute)
                            if (self.cBit2 == 200):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qmeetper(subjectClear , objectClear , relationclear)
                                print("check when have meeting with person")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper
                            if (self.cBit2 == 201):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qmeetperloc(subjectClear , objectClear , relationclear, institute)
                                print("check when have meeting with person at location")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper                      
                        if (quest == "Where"):
                            print("Where question")
                            relationclear="meeting"
                            self.cBit2=post.checkwhere(objectClear, timeProperty)
                            if (self.cBit2 == 300):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qmeetloc(subjectClear , objectClear , relationclear)
                                print("check where have meeting with person")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper
                            if (self.cBit2 == 301):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qmeetloctime(subjectClear , objectClear , relationclear, timeProperty)
                                print("check where have meeting with person at time")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper

                        if (quest == "What"):
                            print("What question")
                            print(docx1,"token value")
                            print(objectClear,subjectClear,"subject object Clear")
                            for q in docx1:
                                if q.text=="location" or q.text=="venue":
                                    based=q
                                    print(based,"location based question")
                                    relationclear="meeting"
                                    print(objectClear)
                                    self.cBit2=post.checkwhatloc(objectClear, timeProperty, relationpropertydate, institute)
                                    if (self.cBit2 == 400):
                                        qinfer = inferencing()
                                        qper = []
                                        qper = qinfer.qwhatloc(subjectClear , objectClear , relationclear)
                                        print("check what  location of meeting with person ")
                                        for i in range(len(qper)):
                                            print (qper[i])
                                        self.tempTime2 = qper
                                    # if (self.cBit2 == 401):
                                    #     qinfer = inferencing()
                                    #     qper = []
                                    #     qper = qinfer.qwhat(subjectClear , objectClear , relationclear,)
                                    #     print("check what  location of meeting with person ")
                                    #     for i in range(len(qper)):
                                    #         print (qper[i])
                                    #     self.tempTime2 = qper


                                if q.text=="time":
                                    based=q
                                    print(based," based question")
                                    relationclear="meeting"
                                    print(objectClear)
                                    self.cBit2=post.checkwhattime(objectClear, timeProperty, relationpropertydate, institute)
                                    if (self.cBit2 == 500):
                                        qinfer = inferencing()
                                        qper = []
                                        qper = qinfer.qwhattime(subjectClear , objectClear , relationclear)
                                        print("check what time of meeting with person ")
                                        for i in range(len(qper)):
                                            print (qper[i])
                                        self.tempTime2 = qper
        







            


        if (self.cBit2==000):
            tempTime = []
            self.tempTime2 =""


        return self.tempTime2

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
        #   tempsSelf = self.cBits2
        #   print ("Flag-0 ... Subject Object Added")

        #   self.cBit2=post.validateInfo(institute , timeProperty )
        #   if (self.cBit2==0):
        #       tempSelf = self.cBit2

        #       #text_spacy.foo(cBit2)          
        #       #global cBit3
        #       #cBit3=0
        #       print("Flag-0 ... Adding the data")
        #       post.createNodeQueru(subjectClear , "subject")
        #       post.createNodeQueru(objectClear , "object")
        #       post.createqueryrelation(subjectClear ,objectClear , relationclear ,timeProperty , institute )
        #       #global cBit3
        #       #cBit3=1
        #   else:
        #       print("Flag -1 ... incomplete info")
        #       tempSelf=self.cBit2

        #       #print("Value of tempSelf is :", tempSelf)
        #       #text_spacy.foo(cBit2)
        #   if (self.cBit2!= 0):
        #       abc = inferencing()
        #       tempTime = []
        #       tempTime = abc.times(subjectClear , objectClear , relationclear)
        #       print("check inference time funct called......")

        #       for i in range(len(tempTime)):
        #           print ("time Inferenced yoyoyoyo" ,tempTime[i])
        #       self.tempTime2 = tempTime
        #   return self.tempTime2

        #   if (self.cBit2!= 0):
        #       xyz = inferencing()
        #       temoLoc = []
        #       temoLoc = xyz.locations(subjectClear , objectClear , relationclear)
        #       print("check location time funct called......")

        #       for i in range(len(temoLoc)):
        #           print ("location Inferenced yoyoyoyo" ,temoLoc[i])
        #       self.tempLoc2 = temoLoc
        #   return self.tempLoc2

        # else:
        #   print("Flag -1 ... incomplete SubObj info")
        #   tempsSelf=self.cBits2





        

# abc = inferencing()
#           tempTime = abc.times(subjectClear , objectClear , relationclear)
#           self.tempTime2 = tempTime

        #return cBit3

  

    # def checkBit():
    #   global cBit3
    #   cBit5
    #   if (cBit3==0):
    #       cBit5=0
    #   else:
    #       cBit5=1
    #   return cBit5


        #return cBit3



#bbh = BotBehaviour()
#tempS = bbh.askQ()

# abc = post()
# show = abc.showallnode()





    #MATCH (u:User {username:'admin'}), (r:Role {name:'ROLE_WEB_USER'})
    #CREATE (u)-[:HAS_ROLE]->(r)


    #MATCH (p:label12)-[r:new]->(c:label12) 
    #SET r.type = "neww" 

    def FypFunction(self, title, detail, noofmems, supervisor, members):
        #call function for creating node
        subj = text_spacy.subFoo(self)
        objc = text_spacy.objFoo(self)
        agen = title
        post.CreateNode_Ag(agen, "Agenda", detail, noofmems, supervisor)
        post.CreateRelation_Ag(agen, subj, "has")
        post.CreateRelation_Ag(agen, objc, "has")



    def RetrieveMembers(self, text):
        print("Text from there:", text)
        listStoreAg = list()
        listStoreAg=post.RetrieveAgenda(self)

        # for r in listStoreAg:
        #     print("mems are in func: ", r)
        return listStoreAg
