from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
import en_core_web_sm
from tqdm import tqdm
from model import post
from model import *
from infer_fnc import *
from infer_fnc import inferencing
from signup import *
from dateTimeVal import DTValidate
from random import randint

global tempS
tempSelf=3
tempsSelf = 3
tBit3= 3
cBit3=3
cBitMed=3

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
        self.sRandNum = randint(1000,9999)
        self.sAgenId = randint(100,999)

    def agenIdFoo(self):
        cagen = self.sAgenId
        return cagen

    def randFoo(self):
        cran = self.sRandNum
        return cran

    def subFoo(self):
        csub = self.sSubject
        return csub

    def objFoo(self):
        cobj = self.sObject
        return cobj  

    def foo(self):
      
        cBit3=self.cBit2
        return cBit3

    def fooTime(self):
       
        tBit3=self.tBit
        return tBit3

    def foos(self):
       
        cBits3=self.cBits2
        return cBits3


    def fooList(self):
       
        ctempTime3 = self.tempTime2
        return ctempTime3
    

    def fooLocList(self):
      
        ctempLoc3 = self.tempLoc2

        return ctempLoc3
 


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
                self.sSubject = subjectClear
                self.sObject = objectClear
        for token in docx1.ents:
            entity = (token.label_ )
            if entity is 'ORG':
                organization = token.text
                print(organization , "is an organization")
                institute = organization
            if entity is 'LOC':
                location = token.text
                print(location , "is an location")
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

            if entity is 'LANGUAGE':
                lang = token.text
                print(lang , "is a Language")

            if entity is 'TIME':
                time = token.text
                print(time , "is a Time")
                timeProperty = time
            print(entity)
            if entity is 'PERCENT':
                percent = token.text
                print(percent , "is a percent")

            if entity is 'MONEY':
                money = token.text
                print(money , "is a money")

            if entity is 'QUANTITY':
                quant = token.text
                print(quant , "is a quantity")

            if entity is 'ORDINAL':
                ordinal = token.text
                print(ordinal , "is a ordinal")

            if entity is 'CARDINAL':
                cardinal = token.text
                print(cardinal , "is a CARDINAL")


        #CHECK DATE AND TIME VALUES
        if(relationpropertydate == "" and timeProperty == ""):
            print("You have to enter date and Time first")
            relationpropertydate = ""
            timeProperty = ""
        elif (relationpropertydate == "" and timeProperty != "" ):
            print("You should have to enter Date")
        elif(relationpropertydate != "" and timeProperty == ""):
            print("You have to enter Time")
        else:
            self.tBit = DTValidate.DateTimeValidaion(relationpropertydate , timeProperty )
            if(self.tBit == 0):
                relationpropertydate = ""
                timeProperty = ""
                print (relationpropertydate)
                print(timeProperty)
                print("You Didnot enter the Correct TIme or Date")
            else:
                print(relationpropertydate)
                print(timeProperty)
                print("you Entered Correct")

        if check == '.':
            self.cBit2=post.validateInfo(institute , timeProperty , relationpropertydate , objectClear)     
            if (self.cBit2=='0'):
                tempSelf = self.cBit2
                print("Flag-0 ... Adding the data")
                post.createNodeQueru(subjectClear , "subject")
                post.createNodeQueru(objectClear , "object")
                rand_Num = self.sRandNum
                agendaID = 0
                post.createqueryrelation(subjectClear ,objectClear , relationclear ,timeProperty , institute ,relationpropertydate, rand_Num, agendaID)
            else:
                print("Flag -1 ... incomplete info")
                tempSelf=self.cBit2

            if(self.cBit2 == '0000'):
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

            elif (self.cBit2 == '0001'):
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

            elif (self.cBit2 == '0010'):
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
            elif(self.cBit2 == '0011'):
                abc = inferencing()
                tempLoc = []
                tempLoc = abc.locations(subjectClear , objectClear , relationclear)
                print("check inference location")
                for i in range(len(tempLoc)):
                    print ("Select" ,tempLoc[i])
                self.tempTime2 = tempLoc

            elif(self.cBit2 == '0100'):
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

            elif(self.cBit2 == '0101'):

                abc = inferencing()
                tempTime = []
                tempTime = abc.times(subjectClear , objectClear , relationclear)
                print("check inference time")
                for i in range(len(tempTime)):
                    print ("Select" ,tempTime[i])
                self.tempTime2 = tempTime
            elif(self.cBit2 == '0110'):
                abc = inferencing()
                tempDate = []
                tempDate = abc.dates(subjectClear , objectClear , relationclear)
                print("check inference dates")
                for i in range(len(tempDate)):
                    print ("Select" ,tempDate[i])
                self.tempTime2 = tempDate
            elif(self.cBit2 == '0111'):
                tempTime = ""
                self.tempTime2 = tempTime

            elif(self.cBit2== '1000'):
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


            elif(self.cBit2 == '1001'):
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
            elif(self.cBit2 == '1010'):
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
            elif(self.cBit2 == '1011'):
                abc = inferencing()
                tempLoc = []
                tempLoc = abc.locations(subjectClear , objectClear , relationclear)
                print("check inference location")
                for i in range(len(tempLoc)):
                    print ("Select" ,tempLoc[i])
                self.tempTime2 = tempLoc
            elif(self.cBit2 == '1100'):
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

            elif(self.cBit2 == '1101'):
                abc = inferencing()
                tempTime = []
                tempTime = abc.times(subjectClear , objectClear , relationclear)
                print("check inference time")
                for i in range(len(tempTime)):
                    print ("Select" ,tempTime[i])
                self.tempTime2 = tempTime
            elif(self.cBit2 == '1110'):
                abc = inferencing()
                tempDate = []
                tempDate = abc.dates(subjectClear , objectClear , relationclear)
                print("check inference dates")
                for i in range(len(tempDate)):
                    print ("Select" ,tempDate[i])
                self.tempTime2 = tempDate
       
            if (self.cBit2==000):            
                tempTime = []                
                self.tempTime2 =""

            return self.tempTime2


    #Function for creation of Agenda and its relationships with other nodes
    def FypFunction(self,agTitle,agName,agDetail,agNoOfMems,agSupervisor,agSecSupervisor,reg1, reg2, reg3, reg4, agMems):

        #call function for creating node
        subj = text_spacy.subFoo(self)
        objc = text_spacy.objFoo(self)
        agId = self.sAgenId
        ranNo = self.sRandNum
        rel = "meet"
        agen = agName
        memList = agMems

        #setting property of relationship 'meet'
        post.setAgendaId(subj, rel, agId, ranNo )

        #creating agenda node....
        post.CreateNode_Ag(agen, "Agenda", agId,agTitle,agDetail,agNoOfMems,agSupervisor,agSecSupervisor,reg1, reg2, reg3, reg4)
        post.CreateRelation_Ag(agen, subj, "has")
        post.CreateRelation_Ag(agen, objc, "has")
        for r in memList:
            post.CreateRelation_Ag(agen, r, "has")

    #Function for creating relationships of other nodes with already created agenda
    def FypFunctionDD(self, agName, memList):
        subj = self.sSubject
        objc = self.sObject
        objcList = memList
        agen = agName

        ranNo = self.sRandNum
        agId = post.RetrAgendaId(agName)
        rel = "meet"

        print("Subject is: ",subj)
        print("Object is: ",objc)
        print("Agenda ID is: ", agId[0])
        agIdVar = agId[0]

        #setting property of relationship 'meet'
        post.setAgendaId(subj, rel, agIdVar, ranNo)


        post.CreateRelation_Ag(agen, subj, "has")
        post.CreateRelation_Ag(agen, objc, "has")
        for r in objcList:
            post.CreateRelation_Ag(agen, r, "has")

    #Function for retrieving agenda members list
    def RetrieveAgenda():
        listStoreAg = list()
        listStoreAg=post.RetrAgenda()

        if (len(listStoreAg) == 0):
            listStoreAg.append("No Agenda has been created before")

        return listStoreAg

    #Function for creating agenda members list
    def RetrieveMembers():
        listStoreAg = list()
        listStoreAg=post.RetrMembers()

        for r in listStoreAg:
            print("mems are in func: ", r)
        return listStoreAg

       