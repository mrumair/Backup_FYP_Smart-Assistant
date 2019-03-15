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
from dateTimeVal import DTValidate
# from main import gloVar

global tempS
tempSelf=3
tempsSelf = 3
tBit3= 3
cBit3=3
cBitMed=3

# cBit2=3

class Infer_spacy:
    def __init__(self):
        relationpropertydate = ""
        self.cBit2 = 0
        self.tempTime2 = []
        self.tempLoc2 = []
        self.cBits2 =0
        self.tBit =0 

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
      
        ctempLoc3 = self.tempLoc2

        return ctempLoc3
 


    def Infer_fun_spacy(self,docx12,varGlo ):
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
        subtype=[]
        objtype=[]
    
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
                    print (check , "check punc")

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
         
        person = []

        for num in docx1.ents:
            entitites = (num.label_)
            if entitites is "PERSON":
                person.append(num.text)
                upper= varGlo
                seond=person[0]

                subjectClear = upper
                objectClear = seond
                tempObj = post.ObjectSelection(objectClear)
                if (tempObj == True):
                    objectClear = seond
                else:
                    objectClear = ""


                print("subject is: ", subjectClear)
                print("object is: ", objectClear)
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

            if entity is 'PERSON':
                person = []
                person = token.text
                print(person , "is a person")

            if entity is 'NORP':
                nationalities = token.text
                print(nationalities , "is a nationality")


            if entity is 'FAC':
                fac = token.text
                print(fac , "is a building")
        #       post.functiona(fac)

            if entity is 'GPE':
                gpe = token.text
                print(gpe , "is a cities")
                institute = gpe
        

            if entity is 'PRODUCT':
                produxt = token.text
                print(produxt , "is a product")

            if entity is 'EVENT':
                event = token.text
                print(event , "is a event")

            if entity is 'WORK_OF_ART':
                woa = token.text
                print(woa , "is a work of art")

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


        print(relationclear , relationpropertydate , timeProperty , varGlo , person , objectClear , "data after infer Spacy")

        if check == '?':
            qst=[]
            #print(objectClear,"object")
            #check type of subject and object
            infertype = inferencing()
            subtype = []
            subject= subjectClear
            subtype = infertype.persontype(varGlo)
            # subjectClear="Batool Gohar"
            print(subtype,"type of login person")
            
            for token11 in docx1:
                quest = ""
                t=(token11.text)
                mylist = ["Do","Did","When","Where","Will","What","Which","How","Who","Is"]
                for q in mylist:
                    if t==q:
                        quest=q      
                        if (quest == "Do" or quest == "Did"):
                            print("Do/ Did question")
                            relationclear="meeting"
                            #title="Semantics"
                            title=""
                            self.cBit2=post.check(objectClear, institute , timeProperty ,relationpropertydate,title)
                            print(subject,objectClear)
                            #meeting based questions with no title
                            if (self.cBit2 == 100):
                                qinfer = inferencing()
                                qper = []
                                qper = qinfer.qperson(subject , objectClear , relationclear)
                                print("check meeting wih person")
                                for i in range(len(qper)):
                                    print (qper[i])
                                self.tempTime2 = qper
                            if (self.cBit2 == 101):
                                qinfer = inferencing()
                                qtime = []
                                qtime = qinfer.qtime(subject , relationclear, timeProperty)
                                print("check meeting on time")
                                for i in range(len(qtime)):
                                    print (qtime[i])
                                self.tempTime2 = qtime
                            if (self.cBit2 == 102):
                                qinfer = inferencing()
                                qpertime = []
                                qpertime = qinfer.qpertime(subject , objectClear, relationclear, timeProperty)
                                print("check meeting on person and time")
                                for i in range(len(qpertime)):
                                    print (qpertime[i])
                                self.tempTime2 = qpertime
                            if (self.cBit2 == 103):
                                qinfer = inferencing()
                                qperdate = []
                                qperdate = qinfer.qperdate(varGlo , person, relationclear, relationpropertydate)
                                print("check meeting on person and date" , subjectClear , objectClear , relationclear , relationpropertydate)
                                for i in range(len(qperdate)):
                                    print (qperdate[i])
                                self.tempTime2 = qperdate
                            if (self.cBit2 == 104):
                                qinfer = inferencing()
                                qdate = []
                                print(varGlo , relationclear , relationpropertydate , "dahDHAiodhaIODHAdhoH")
                                qdate = qinfer.qdate(varGlo , relationclear, relationpropertydate)
                                print("check meeting on date")
                                for i in range(len(qdate)):
                                    print (qdate[i])
                                self.tempTime2 = qdate
                            if (self.cBit2 == 105):
                                qinfer = inferencing()
                                qloc = []
                                qloc = qinfer.qloc(varGlo , relationclear, institute)
                                print("check meeting on location")
                                for i in range(len(qloc)):
                                    print (qloc[i])
                                self.tempTime2 = qloc
                            if (self.cBit2 == 106):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qperloc(subject , objectClear, relationclear, institute)
                                print("check meeting on person and location")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc
                            if (self.cBit2 == 107):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qperloctime(subject , objectClear, relationclear, institute, timeProperty)
                                print("check meeting on person,location,time")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc
                            if (self.cBit2 == 108):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qperlocdate(subject , objectClear, relationclear, institute, relationpropertydate)
                                print("check meeting on person,location,date")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc
                            if (self.cBit2 == 109):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qperlocdatetime(subjectClear , objectClear, relationclear, institute, relationpropertydate,time)
                                print("check meeting on person,location,date,time")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc

                            if (self.cBit2 == 110):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qpertitle(subject , title)
                                print("check meeting on person,title")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc
                            if (self.cBit2 == 111):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qpertitletime(subject , title,timeProperty)
                                print("check meeting on time,title")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc
                            if (self.cBit2 == 112):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qpertitledate(subject , title,relationpropertydate)
                                print("check meeting on date,title")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc
                            if (self.cBit2 == 113):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qpertitlevenue(subject , title, institute)
                                print("check meeting on venue,title")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc
                            if (self.cBit2 == 114):
                                qinfer = inferencing()
                                qperloc = []
                                qperloc = qinfer.qpertitleper(subject , title, objectClear)
                                print("check meeting on person,title")
                                for i in range(len(qperloc)):
                                    print (qperloc[i])
                                self.tempTime2 = qperloc



            return self.tempTime2



