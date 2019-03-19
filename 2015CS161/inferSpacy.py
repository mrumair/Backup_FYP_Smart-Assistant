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
        title=""
        degree=""
    
        #global upper
        value_doc = docx12
        nlp = spacy.load('en_core_web_sm')
        docx1 = nlp(value_doc)


        infer = inferencing()
        title_list = []
        title_list = infer.title()
        for i in range(len(title_list)):
            print (title_list[i])
        for tok in docx1:
            for t in title_list:
                if t == tok.text:
                    title= t



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
            if deep is 'dobj' or pos is 'VERB':
                relationship = token.text
                print(relationship , "is a relationship")
                relationclear = relationship
         
        person = []

        for num in docx1.ents:
            if num.text != title:
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

        infer = inferencing()
        title_list = []
        title_list = infer.title()
        for i in range(len(title_list)):
            print (title_list[i])
        for tok in docx1:
            for t in title_list:
                if t == tok.text:
                    title= t
        print(title,"is title")

        for token in docx1.ents: 
            if token.text != title:
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


        print(relationclear , relationpropertydate , timeProperty , varGlo ,institute, person , objectClear , "data after infer Spacy")
        

        if check == '?':
            infertype = inferencing()
            subtype = []
            subject= varGlo
            print(subjectClear,"subjectClear")
            print(varGlo,"varGlo")
            subtype = infertype.personType(varGlo)
            print(subtype,"type of login person")
 
            for token11 in docx1:
                quest = ""
                t=(token11.text)
                mylist = ["Do","Did","When","Where","Will","What","Which","How","Who","Is"]
                for q in mylist:
                    if t==q:
                        quest=q      
                        if (quest == "Do" or quest == "do" or quest == "Did" or quest == "did"):
                            print("Do/ Did question")
                            qinfer = inferencing()
                            inferData = []
                            print(objectClear, institute, timeProperty, relationpropertydate, title)
                            #Get bit value from function of model.py and on basis of return bit value find data.
                            self.cBit2=post.checkDo(objectClear, institute, timeProperty, relationpropertydate, title)
                            #Person based question
                            if (self.cBit2 == 100):
                                inferData = qinfer.qPerson(subject, objectClear, relationclear)
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Location based question    
                            if (self.cBit2 == 101):
                                inferData = qinfer.qTime(subject , relationclear, timeProperty)
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Date based question
                            if (self.cBit2 == 102):
                                inferData = qinfer.qDate(subject , relationclear, relationpropertydate)
                                print("check meeting on date")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person and Date based question
                            if (self.cBit2 == 103):
                                inferData = qinfer.qPerDate(subject , objectClear, relationclear, relationpropertydate)
                                print("check meeting on person and date")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person and Time based question
                            if (self.cBit2 == 104):
                                inferData = qinfer.qPerTime(subject , objectClear, relationclear, timeProperty)
                                print("check meeting on person and time")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Location based question
                            if (self.cBit2 == 105):
                                inferData = qinfer.qLoc(subject , relationclear, institute)
                                print("check meeting on location")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person and Location based question
                            if (self.cBit2 == 106):
                                inferData = qinfer.qPerLoc(subject , objectClear, relationclear, institute)
                                print("check meeting on person and location")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person ,Location and Time based question
                            if (self.cBit2 == 107):
                                inferData = qinfer.qPerLocTime(subject , objectClear, relationclear, timeProperty, institute)
                                print("check meeting on person,location,time")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Location and Date based question
                            if (self.cBit2 == 108):
                                inferData = qinfer.qPerLocDate(subject , objectClear, relationclear, relationpropertydate, institute)
                                print("check meeting on person,location,date")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Location, Time and Date based question
                            if (self.cBit2 == 109):
                                inferData = qinfer.qPerLocDateTime(subject , objectClear, relationclear, relationpropertydate, timeProperty, institute)
                                print("check meeting on person,location,date,time")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Time and Date based question
                            if (self.cBit2 == 110):
                                inferData = qinfer.qTimeDate(subject , relationclear, relationpropertydate, timeProperty)
                                print("check meeting on time,date")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Time and Location based question
                            if (self.cBit2 == 111):
                                inferData = qinfer.qTimeLoc(subject , relationclear, timeProperty, institute)
                                print("check meeting on time,loc")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Date and Location based question
                            if (self.cBit2 == 112):
                                inferData = qinfer.qDateLoc(subject, relationclear, relationpropertydate, institute)
                                print("check meeting on date,loc")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Time and Date based question
                            if (self.cBit2 == 113):
                                inferData = qinfer.qPerDateTime(subject, objectClear, relationclear, relationpropertydate, timeProperty)
                                print("check meeting on person,date,time")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Time, Date and Location based question
                            if (self.cBit2 == 114):
                                inferData = qinfer.qDateTimeLoc(subject, relationclear, relationpropertydate, timeProperty, institute)
                                print("check meeting on loc,date,time")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person and Date based question
                            if (self.cBit2 == 115):
                                inferData = qinfer.qPerDate(subject, objectClear, relationclear, relationpropertydate)
                                print("check meeting on person and date")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Title based question
                            if (self.cBit2 == 116):
                                inferData = qinfer.qTitle(subject, relationclear, title)
                                print("check meeting on title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person and Title based question
                            if (self.cBit2 == 117):
                                inferData = qinfer.qPerTitle(subject, objectClear, relationclear, title)
                                print("check meeting on person,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Time ad Title based question
                            if (self.cBit2 == 118):
                                inferData = qinfer.qTimeTitle(subject, relationclear, timeProperty, title)
                                print("check meeting on Time,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Date ad Title based question
                            if (self.cBit2 == 119):
                                inferData = qinfer.qDateTitle(subject, relationclear, relationpropertydate, title)
                                print("check meeting on Date,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Time ad Title based question
                            if (self.cBit2 == 120):
                                inferData = qinfer.qPerTimeTitle(subject, objectClear, relationclear, timeProperty, title)
                                print("check meeting on person time ,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Date ad Title based question
                            if (self.cBit2 == 121):
                                inferData = qinfer.qPerDateTitle(subject, objectClear, relationclear, relationpropertydate, title)
                                print("check meeting on person date ,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Location and Title based question
                            if (self.cBit2 == 122):
                                inferData = qinfer.qPerLocTitle(subject, objectClear, relationclear, institute, title)
                                print("check meeting on person loc ,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Location and Title based question
                            if (self.cBit2 == 123):
                                inferData = qinfer.qLocTitle(subject, relationclear, institute, title)
                                print("check meeting on loc ,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Location ad Title based question
                            if (self.cBit2 == 124):
                                inferData = qinfer.qPerTimeLocTitle(subject, objectClear, relationclear, timeProperty, institute, title)
                                print("check meeting on loc person time,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Location ad Title based question
                            if (self.cBit2 == 125):
                                inferData = qinfer.qPerDateTimeTitle(subject, objectClear, relationclear, relationpropertydate, timeProperty, title)
                                print("check meeting on loc ,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Location ad Title based question
                            if (self.cBit2 == 126):
                                inferData = qinfer.qPerDateLocTitle(subject, objectClear, relationclear, relationpropertydate, institute, title)
                                print("check meeting on loc ,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Location ad Title based question
                            if (self.cBit2 == 127):
                                inferData = qinfer.qDateTimeLocTitle(subject, relationclear, relationpropertydate, timeProperty, institute, title)
                                print("check meeting on loc ,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Location ad Title based question
                            if (self.cBit2 == 128):
                                inferData = qinfer.qPerDateTimeLocTitle(subject, objectClear, relationclear, relationpropertydate, timeProperty, institute, title)
                                print("check meeting on loc ,title")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData

                        if (quest == "Which" or quest == "which"):
                            print("Which question")
                            #Personal data question                        
                            if subtype=="student" or subtype=="teacher":
                                qinfer = inferencing()
                                inferData = []
                                self.cBit2=post.checkWhich(subject,objectClear,title,institute,degree,relationpropertydate)
                                print(self.cBit2,"cBit2")
                                #Find members of project
                                if(self.cBit2==500):
                                    for q in docx1:
                                        if q.text=="members" or q.text=="member" or q.text=="students" or q.text=="student":
                                            inferData = qinfer.qProMem(title)
                                            print("check names of members of project")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                #Find project names I am supervising
                                if(self.cBit2==501):  
                                    for q in docx1:      
                                        if q.text=="projects" or q.text=="project":
                                            inferData = qinfer.qProName(subject)
                                            print("check names of project i am supervising/doing")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                #Find projects name I am doing with Person
                                if(self.cBit2==502):
                                    for q in docx1:
                                        if q.text=="projects" or q.text=="project":
                                            inferData = qinfer.qPerProName(subject,objectClear)
                                            print("check names of project i am doing with person")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                #Find students of specific city, country and institute
                                if(self.cBit2==503):
                                    for q in docx1:
                                        if q.text=="student" or q.text=="students":
                                            inferData = qinfer.qStdLoc(subject, institute)
                                            print("check which students are from city")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                if(self.cBit2==504):
                                    for q in docx1:
                                        if q.text=="doing" or q.text=="from":
                                            for q in docx1:
                                                degree=""
                                                if q.text=="CS" or (q.text=="Computer" or q.text=="Science"):
                                                    degree="CS"
                                                    inferData = qinfer.qStdDegree(subject, degree)
                                                    print("check which student from degree")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if q.text=="CE" or (q.text=="Computer" or q.text=="Engineering"):
                                                    degree="CE"
                                                    inferData = qinfer.qStdDegree(subject,degree)
                                                    print("check which student from degree")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if q.text=="EE" or q.text=="Electrical" or q.text=="Engineering":
                                                    degree="EE"
                                                    inferData = qinfer.qStdDegree(subject,degree)
                                                    print("check which student from degree")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if q.text=="ME" or q.text=="Mechanical" or q.text=="Engineering":
                                                    degree="ME"
                                                    inferData = qinfer.qStdDegree(subject,degree)
                                                    print("check which student from degree")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if q.text=="CHE" or q.text=="Chemical" or q.text=="Engineering":
                                                    degree="CHE"
                                                    inferData = qinfer.qStdDegree(subject,degree)
                                                    print("check which student from degree")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if q.text=="CV" or q.text=="Civil" or q.text=="Engineering":
                                                    degree="CV"
                                                    inferData = qinfer.qStdDegree(subject,degree)
                                                    print("check which student from degree")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if degree=="" or q.text=="graduation":
                                                    degree1="MSc"
                                                    degree2="PHd"
                                                    inferData = qinfer.qStdDegGrad(subject,degree1,degree2)
                                                    print("check which student from degree")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData

                                            for q in docx1:
                                                degree=""
                                                if q.text=="PHD" or q.text=="PHd" or q.text=="Phd":
                                                    for q in docx1:
                                                        if q.text=="CS" or (q.text=="Computer" or q.text=="Science"):
                                                            degree=""
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CE" or (q.text=="Computer" or q.text=="Engineering"):
                                                            degree="PHd CE"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="EE" or q.text=="Electrical" or q.text=="Engineering":
                                                            degree="PHd EE"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="ME" or q.text=="Mechanical" or q.text=="Engineering":
                                                            degree="PHd ME"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CHE" or q.text=="Chemical" or q.text=="Engineering":
                                                            degree="PHd CHE"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CV" or q.text=="Civil" or q.text=="Engineering":
                                                            degree="PHd CV"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if degree=="":
                                                            degree="PHd"
                                                            inferData = qinfer.qStdDegPer(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                            for q in docx1:
                                                degree=""
                                                if q.text=="MSC" or q.text=="Msc" or q.text=="Master" or q.text=="Masters":
                                                    for q in docx1:
                                                        if q.text=="CS" or (q.text=="Computer" or q.text=="Science"):
                                                            degree="MSc CS"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CE" or (q.text=="Computer" or q.text=="Engineering"):
                                                            degree="MSc CE"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="EE" or q.text=="Electrical" or q.text=="Engineering":
                                                            degree="MSc EE"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="ME" or q.text=="Mechanical" or q.text=="Engineering":
                                                            degree="MSc ME"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CHE" or q.text=="Chemical" or q.text=="Engineering":
                                                            degree="MSc CHE"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CV" or q.text=="Civil" or q.text=="Engineering":
                                                            degree="MSc CV"
                                                            inferData = qinfer.qStdDegree(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if degree=="":
                                                            degree="MSc"
                                                            inferData = qinfer.qStdDegPer(subject,degree)
                                                            print("check which student from degree")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData

                                if(self.cBit2==505):
                                    for q in docx1:
                                        #Find students of specific session
                                        if q.text=="session"or q.text=="year":
                                            for q in docx1:
                                                if q.text=="students" or q.text=="student":
                                                    inferData = qinfer.qStdSession(subject,relationpropertydate)
                                                    print("check which student from session")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                if(self.cBit2==504):
                                #Find which students have gmail or yahoo account
                                    if q.text=="gmail" or q.text=="yahoo":
                                        email=q.text
                                        for qq in docx1:
                                            if qq.text=="students" or qq.text=="student":
                                                inferData = qinfer.qStdEmail(subject,email)
                                                print("check which student have gmail,yahoo account")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                if(self.cBit2==502):
                                    if q.text=="teacher" or q.text=="teachers":
                                        inferData = qinfer.qStdTechLoc(subject,institute)
                                        print("check which teachers are from city")
                                        for i in range(len(inferData)):
                                            print (inferData[i])
                                        self.tempTime2 = inferData
                                #Find Which teachers are lecturar
                                if(self.cBit2==504):
                                    if q.text=="Lecturar" or q.text=="Professor":
                                        rank=q.text
                                        for qq in docx1:
                                            if qq.text=="teachers" or qq.text=="teacher":
                                                inferData = qinfer.qStdTechRank(subject,rank)
                                                print("check which teachers are lecturar")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                if(self.cBit2==502):
                                    if q.text=="Lecturar" or q.text=="Assistant Professor" or q.text=="Professor":
                                        rank=q.text
                                        for qq in docx1:
                                            if qq.text=="teachers" or qq.text=="teacher":
                                                inferData = qinfer.qStdTechRankLoc(subject,rank,institute)
                                                print("check which teachers are lecturar in loc")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                            
                        if (quest == "Who"):
                            print("Who question")
                            self.cBit2=post.checkWho(title)
                            if(self.cBit2==600):
                                qinfer = inferencing()
                                inferData = []
                                for q in docx1:
                                    if q.text=="members" or q.text=="member":
                                        based=q
                                        print(based," based question")
                                        inferData = qinfer.qProMem(title)
                                        print("check who are members of project")
                                        for i in range(len(inferData)):
                                            print (inferData[i])
                                        self.tempTime2 = inferData
                                    if q.text=="supervisor" or q.text=="first supervisor":
                                        based=q
                                        print(based," based question")
                                        inferData = qinfer.qProSup(title)
                                        print("check who is supervisor or first supervisor of project")
                                        for i in range(len(inferData)):
                                            print (inferData[i])
                                        self.tempTime2 = inferData
                                    if q.text=="co-supervisor" or q.text=="cosupervisor" or q.text=="second":
                                        based=q
                                        print(based," based question")
                                        inferData = qinfer.qProCoSup(title)
                                        print("check who is second supervisor or co-supervisor of project")
                                        for i in range(len(inferData)):
                                            print (inferData[i])
                                        self.tempTime2 = inferData


                        if (quest == "How"):
                            print("How question")
                            #personal data question
                            self.cBit2=post.checkHow(subject,institute,relationpropertydate,title)
                            qinfer = inferencing()
                            inferData = []
                            if subtype=="Student" or subtype=="Teacher":
                                if(self.cBit2==700):
                                    for q in docx1:
                                        if q.text=="student" or q.text=="students":                                        
                                            inferData = qinfer.qStdLocCnt(subject,institute)
                                            qper=str(inferData)
                                            print("check how students are from city")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                if(self.cBit2==701):
                                    for q in docx1:
                                        if q.text=="session"or q.text=="year":
                                            for q in docx1:
                                                if q.text=="students" or q.text=="student":
                                                    inferData = qinfer.qStdSesCnt(subject,relationpropertydate)
                                                    print("check how student from session")
                                                    qper=str(inferData)
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                if(self.cBit2==703):
                                    for q in docx1:
                                        if q.text=="gmail" or q.text=="yahoo":
                                            email=q.text
                                            for qq in docx1:
                                                if qq.text=="students" or qq.text=="student":
                                                    inferData = qinfer.qStdEmailCnt(subject,email)
                                                    inferData=str(inferData)
                                                    print("check how student have gmail,yahoo account")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                        if q.text=="Lecturar" or q.text=="Professor":
                                            rank=q.text
                                            inferData = qinfer.qStdTechRankCnt(subject,rank)
                                            print("check which teachers are lecturar")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                if(self.cBit2==700):
                                    for q in docx1:
                                        if q.text=="Lecturar" or q.text=="Assistant Professor" or q.text=="Professor":
                                            rank=q.text
                                            inferData = qinfer.qStdTechRankLocCnt(subject,rank,institute)
                                            print("check which teachers are lecturar in loc")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                if(self.cBit2==702):
                                    for q in docx1:
                                        if q.text=="members" or q.text=="member":
                                            based=q
                                            print(based," based question")
                                            inferData = qinfer.qMemCnt(title)
                                            print("check How many members of project")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                if(self.cBit2==703):
                                    for q in docx1:
                                        if q.text=="project" or q.text=="projects":
                                            based=q
                                            print(based," based question") 
                                            inferData = qinfer.qPrjCnt(subject)
                                            inferData = str(inferData)
                                            print(inferData,"retuurn value")
                                            print("check How many projects i am supervising")
                                            # for i in range(len(qper)):
                                            #     print (qper[i])
                                            self.tempTime2 = inferData                            

                        if (quest == "When"):
                            print("When question")
                            qinfer = inferencing()
                            inferData = []
                            #meeting based question
                            self.cBit2=post.checkWhen(objectClear, institute)
                            if (self.cBit2 == 200):
                                inferData = qinfer.qPerson(subject, objectClear, relationclear)
                                print("check when have meeting with person")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            if (self.cBit2 == 201):
                                inferData = qinfer.qPerLoc(subject, objectClear, relationclear, institute)
                                print("check when have meeting with person at location")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData 

                        if (quest == "Where"):
                            print("Where question")
                            qinfer = inferencing()
                            inferData = []
                            #meeting based question
                            self.cBit2=post.checkWhere(objectClear, timeProperty,relationpropertydate)
                            if (self.cBit2 == 300):
                                inferData = qinfer.qMeetPer(subject, objectClear, relationclear)
                                print("check where have meeting with person")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            if (self.cBit2 == 301):
                                inferData = qinfer.qMeetPerTime(subject, objectClear, relationclear, timeProperty)
                                print("check where have meeting with person at time")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                             if (self.cBit2 == 302):
                                inferData = qinfer.qMeetPerDate(subject, objectClear, relationclear, relationpropertydate)
                                print("check where have meeting with person at time")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData


                        if (quest == "What"):
                            if (objectClear!=""):
                                objtype = []
                                objtype = infertype.personType(subjectClear)
                                print(objtype,"objtype")
                                print(subtype,"subtype")
                            #meeting based question
                            print("What question")
                            for q in docx1:
                                qinfer = inferencing()
                                inferData = []
                                if subtype=="student" and objtype=="":
                                    self.cBit2=post.checkWhat(subject,objectClear)
                                    if(self.cBit2==800):
                                        for q in docx1:
                                            if q.text=="password":                                        
                                                inferData = qinfer.qStdwhatMyPsd(subject)
                                                # qper=str(qper)
                                                print("check what my password")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="registeration" or q.text=="regID" or q.text=="regid":
                                                inferData = qinfer.qStdWhatMyReg(subject)
                                                inferData=str(inferData)
                                                print("check what my reg")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="email" or q.text=="id":
                                                inferData = qinfer.qStdWhatMyEmail(subject)
                                                # qper=str(qper)
                                                print("check what my email")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="phone" or q.text=="contact":
                                                inferData = qinfer.qStdWhatMyPhone(subject)
                                                # qper=str(qper)
                                                print("check what my tel")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
#################################################################################################################

                                if subtype=="student" and objtype=="student":
                                    self.cBit2=post.checkWhat(subject,objectClear)
                                    if(self.cBit2==801):
                                        for q in docx1:
                                            if q.text=="email" or q.text=="email id":
                                                print("check what is email of stdent")
                                                inferData = qinfer.qStdWhatEmail(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what email")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="degree":
                                                inferData = qinfer.qStdWhatDegree(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what degree sana have")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="city":
                                                inferData = qinfer.qStdWhatCity(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what city of student")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="country":
                                                inferData = qinfer.qStdWhatCountry(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what city of student")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="contact" or q.text=="phone":
                                                inferData=("You cannot access someone contact number")
                                                self.tempTime2 = inferData
                                            if q.text=="password":
                                                inferData=("You cannot access someone password")
                                                self.tempTime2 = inferData

                                if subtype=="Student" and objtype=="Teacher":
                                    self.cBit2=post.checkWhat(subject,objectClear)
                                    if(self.cBit2==801):
                                        for q in docx1:
                                            if q.text=="available" or q.text=="availability" or q.text=="time":
                                                print("check availability")
                                                inferData = qinfer.qStdWhatTechTime(objectClear)
                                                # qper=str(qper)
                                                print("check what available time of teacher")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="email" or q.text=="email id":
                                                inferData = qinfer.qStdWhatTechEmail(objectClear)
                                                # qper=str(qper)
                                                print("check what email of teacher")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="rank" or q.text=="designation":
                                                inferData = qinfer.qStdWhatTechRank(objectClear)
                                                # qper=str(qper)
                                                print("check what rank of teacher")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData

                                        if subtype=="Teacher" and objtype=="Student":
                                            if q.text=="email" or q.text=="email id":
                                                inferData = qinfer.qStdWhatEmail(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what email")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="degree":
                                                inferData = qinfer.qStdWhatDegree(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what degree sana have")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="city":
                                                inferData = qinfer.qStdWhatCity(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what city of student")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="country":
                                                inferData = qinfer.qStdWhatCountry(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what city of student")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="contact" or q.text=="phone":
                                                inferData = qinfer.qStdWhatPhone(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what phone of student")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="password":
                                                inferData=("You cannot access someone password")
                                                self.tempTime2 = inferData

                                if subtype=="Teacher" and objtype=="Teacher":
                                    self.cBit2=post.checkWhat(subject,objectClear)
                                    if(self.cBit2==801):
                                        for q in docx1:
                                            if q.text=="available" or q.text=="availability" or q.text=="time":
                                                print("check availability")
                                                inferData = qinfer.qStdWhatTechTime(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what available time of teacher")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="email" or q.text=="email id":
                                                inferData = qinfer.qStdWhatTechEmail(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what email of teacher")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="rank" or q.text=="designation":
                                                inferData = qinfer.qStdWhatTechRank(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what rank of teacher")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="city":
                                                inferData = qinfer.qStdWhatTechCity(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what city of student")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="country":
                                                inferData = qinfer.qStdWhatTechCountry(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what city of student")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="contact" or q.text=="phone":
                                                inferData = qinfer.qStdWhatTechPhone(subject,objectClear)
                                                # qper=str(qper)
                                                print("check what phone of student")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="password":
                                                inferData=("You cannot access someone password")
                                                self.tempTime2 = inferData

                            # print(docx1,"token value")
                            ##########################################################################################
                            if subtype=="Student" or objtype=="Teacher" or objtype=="student":
                                #######################################################
                                for q in docx1:
                                    if q.text=="location" or q.text=="venue":
                                        based=q
                                        print(based,"location based question")
                                        print(subjectClear,"subjectClear")
                                        self.cBit2=post.checkWhatLoc(objectClear, timeProperty, relationpropertydate, institute)
                                        if (self.cBit2 == 400):
                                            inferData = qinfer.qWhatLoc(subject , objectClear, relationclear)
                                            print("check what  location of meeting with person ")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                    if q.text=="time":
                                        based=q
                                        print(based," based question")
                                        print(objectClear)
                                        self.cBit2=post.checkWhatTime(objectClear, timeProperty, relationpropertydate, institute)
                                        if (self.cBit2 == 420):
                                            inferData = qinfer.qWhatTime(subject,objectClear, relationclear)
                                            print("check what time of meeting with person ")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData

                                    if q.text=="agenda" or q.text=="title":
                                        based=q
                                        print(based,"based question")
                                        self.cBit2=post.checkWhatAgenda(objectClear,timeProperty,relationpropertydate,institute)
                                        if (self.cBit2 == 440):
                                            print(subject,objectClear,"subjectClear,objectClear")
                                            inferData = qinfer.qWhatAgenda(subject,objectClear)
                                            print("check what agenda of meeting with person ")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 441):
                                            inferData = qinfer.qWhatAgendaTime(subject,objectClear,timeProperty)
                                            print("check what agenda of meeting with person and time ")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 442):
                                            inferData = qinfer.qWhatAgendaDate(subject,objectClear,relationpropertydate)
                                            print("check what agenda of meeting with person and date ")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 443):
                                            inferData = qinfer.qWhatAgendaVenue(subject,objectClear,institute)
                                            print("check what agenda of meeting with person and institute ")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 444):
                                            inferData = qinfer.qWhatAgendaDateTime(subject,objectClear,relationpropertydate,timeProperty)
                                            print("check what agenda of meeting with person, date and time ")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 445):
                                            inferData = qinfer.qWhatAgendaTimeVenue(subject,objectClear,timeProperty,institute)
                                            print("check what agenda of meeting with person, time and venue ")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 446):
                                            inferData = qinfer.qWhatAgendaDateVenue(subject,objectClear,relationpropertydate,institute)
                                            print("check what agenda of meeting with person, time and venue ")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 447):
                                            inferData = qinfer.qWhatAgendaAll(subject,objectClear,timeProperty ,relationpropertydate,institute)
                                            print("check what agenda of meeting with person, time, date and venue ")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                    
                                    if q.text=="projects" or q.text=="project":
                                        self.cBit2=post.checkWhat(subject,objectClear)
                                        if(self.cBit2==800):
                                            inferData = qinfer.qWhatPrjName(subject)
                                            print("check names of project i am supervising")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if(self.cBit2==801)
                                            inferData = qinfer.qWhatPerPrjName(subject,objectClear)
                                            print("check names of project i am doing with person")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData

                                    if q.text=="members" or q.text=="member":
                                        self.cBit2=post.checkWho(title)
                                        if(self.cBit2==600):
                                            qdata = qinfer.qWhatPrjMem(title)
                                            print("check names of members of project")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData

            return self.tempTime2



