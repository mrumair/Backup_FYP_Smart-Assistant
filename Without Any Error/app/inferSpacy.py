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
            if (objectClear != ""):
                objtype = infertype.personType(objectClear)
                print(subtype,"type of other person")
 
            for token11 in docx1:
                quest = ""
                t=(token11.text)
                mylist = ["Do","Did","When","Where","What","Which","How","Who"]
                for q in mylist:
                    if t==q:
                        quest=q 
                        #When user ask do type questions.     
                        if (quest == "Do" or quest == "do" or quest == "Did" or quest == "did"):
                            print("Do/Did question")
                            qinfer = inferencing()
                            inferData = []
                            print(objectClear, institute, timeProperty, relationpropertydate, title)
                            #Get bit value from function of model.py and on basis of return bit value find data.
                            self.cBit2=post.checkDo(objectClear, institute, timeProperty, relationpropertydate, title)
                            #Person based question
                            if (self.cBit2 == 100):
                                inferData = qinfer.qPerson(subject, objectClear, relationclear)
                                print("Check meeting on basis of person.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Time based question    
                            if (self.cBit2 == 101):
                                inferData = qinfer.qTime(subject, relationclear, timeProperty)
                                print("Check meeting on basis of time.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Date based question
                            if (self.cBit2 == 102):
                                inferData = qinfer.qDate(subject, relationclear, relationpropertydate)
                                print("Check meeting on basis of date.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person and Date based question
                            if (self.cBit2 == 103):
                                inferData = qinfer.qPerDate(subject, objectClear, relationclear, relationpropertydate)
                                print("Check meeting on basis of person and date.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person and Time based question
                            if (self.cBit2 == 104):
                                inferData = qinfer.qPerTime(subject, objectClear, relationclear, timeProperty)
                                print("Check meeting on basis of person and time.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Location based question
                            if (self.cBit2 == 105):
                                inferData = qinfer.qLoc(subject, relationclear, institute)
                                print("Check meeting on basis of location.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person and Location based question
                            if (self.cBit2 == 106):
                                inferData = qinfer.qPerLoc(subject, objectClear, relationclear, institute)
                                print("Check meeting on basis of person and location.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Location and Time based question
                            if (self.cBit2 == 107):
                                inferData = qinfer.qPerLocTime(subject, objectClear, relationclear, timeProperty, institute)
                                print("Check meeting on basis of person, location and time.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Location and Date based question
                            if (self.cBit2 == 108):
                                inferData = qinfer.qPerLocDate(subject, objectClear, relationclear, relationpropertydate, institute)
                                print("Check meeting on basis of person, location and date.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Location, Time and Date based question
                            if (self.cBit2 == 109):
                                inferData = qinfer.qPerLocDateTime(subject, objectClear, relationclear, relationpropertydate, timeProperty, institute)
                                print("Check meeting on basis of person, location, date and time.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Time and Date based question
                            if (self.cBit2 == 110):
                                inferData = qinfer.qTimeDate(subject, relationclear, relationpropertydate, timeProperty)
                                print("Check meeting on basis of time and date.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Time and Location based question
                            if (self.cBit2 == 111):
                                inferData = qinfer.qTimeLoc(subject, relationclear, timeProperty, institute)
                                print("Check meeting on basis of time and location.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Date and Location based question
                            if (self.cBit2 == 112):
                                inferData = qinfer.qDateLoc(subject, relationclear, relationpropertydate, institute)
                                print("Check meeting on basis of date and location.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Time and Date based question
                            if (self.cBit2 == 113):
                                inferData = qinfer.qPerDateTime(subject, objectClear, relationclear, relationpropertydate, timeProperty)
                                print("Check meeting on basis of person, date and time.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Time, Date and Location based question
                            if (self.cBit2 == 114):
                                inferData = qinfer.qDateTimeLoc(subject, relationclear, relationpropertydate, timeProperty, institute)
                                print("Check meeting on basis of location, date and time.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person and Date based question
                            if (self.cBit2 == 115):
                                inferData = qinfer.qPerDate(subject, objectClear, relationclear, relationpropertydate)
                                print("Check meeting on basis of person and date.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Title based question
                            if (self.cBit2 == 116):
                                inferData = qinfer.qTitle(subject, relationclear, title)
                                print("Check meeting on basis of title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person and Title based question
                            if (self.cBit2 == 117):
                                inferData = qinfer.qPerTitle(subject, objectClear, relationclear, title)
                                print("Check meeting on basis of person and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Time ad Title based question
                            if (self.cBit2 == 118):
                                inferData = qinfer.qTimeTitle(subject, relationclear, timeProperty, title)
                                print("Check meeting on basis of time and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Date ad Title based question
                            if (self.cBit2 == 119):
                                inferData = qinfer.qDateTitle(subject, relationclear, relationpropertydate, title)
                                print("Check meeting on basis of date and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Time ad Title based question
                            if (self.cBit2 == 120):
                                inferData = qinfer.qPerTimeTitle(subject, objectClear, relationclear, timeProperty, title)
                                print("Check meeting on basis of person, time and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Date ad Title based question
                            if (self.cBit2 == 121):
                                inferData = qinfer.qPerDateTitle(subject, objectClear, relationclear, relationpropertydate, title)
                                print("Check meeting on basis of person, date and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Location and Title based question
                            if (self.cBit2 == 122):
                                inferData = qinfer.qPerLocTitle(subject, objectClear, relationclear, institute, title)
                                print("Check meeting on basis of person, location and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Location and Title based question
                            if (self.cBit2 == 123):
                                inferData = qinfer.qLocTitle(subject, relationclear, institute, title)
                                print("Check meeting on basis of location and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Time, Location and Title based question
                            if (self.cBit2 == 124):
                                inferData = qinfer.qPerTimeLocTitle(subject, objectClear, relationclear, timeProperty, institute, title)
                                print("Check meeting on basis of location, person, time and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Date, Time and Title based question
                            if (self.cBit2 == 125):
                                inferData = qinfer.qPerDateTimeTitle(subject, objectClear, relationclear, relationpropertydate, timeProperty, title)
                                print("Check meeting on basis of person, date, time and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Date, Location and Title based question
                            if (self.cBit2 == 126):
                                inferData = qinfer.qPerDateLocTitle(subject, objectClear, relationclear, relationpropertydate, institute, title)
                                print("Check meeting on basis of person, date, location and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Date, Time, Location and Title based question
                            if (self.cBit2 == 127):
                                inferData = qinfer.qDateTimeLocTitle(subject, relationclear, relationpropertydate, timeProperty, institute, title)
                                print("Check meeting on basis of date, time, location and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            #Person, Date, Time, Location and Title based question
                            if (self.cBit2 == 128):
                                inferData = qinfer.qPerDateTimeLocTitle(subject, objectClear, relationclear, relationpropertydate, timeProperty, institute, title)
                                print("Check meeting on basis of person, date, time, location and title.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData

                        #When user ask which type of questions.
                        if (quest == "Which" or quest == "which"):
                            print("Which question")
                            #Personal data question                        
                            if subtype=="student" or subtype=="teacher":
                                qinfer = inferencing()
                                inferData = []
                                #Get bit value from function of model.py and on basis of return bit value find data.
                                self.cBit2=post.checkWhich(subject,objectClear,title,institute,relationpropertydate)
                                print(self.cBit2,"cBit2")
                                #Find members of project
                                if(self.cBit2==500):
                                    for q in docx1:
                                        if q.text=="members" or q.text=="member" or q.text=="students" or q.text=="student":
                                            if title == "":
                                                inferData = "This title not exist in system."
                                                self.tempTime2 = inferData
                                            inferData = qinfer.qProMem(title)
                                            print("Check project members name.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                #Find project names I am supervising
                                if(self.cBit2==501):  
                                    for q in docx1:      
                                        if q.text=="projects" or q.text=="project":
                                            inferData = qinfer.qProName(subject)
                                            print("Check names of project I am supervising.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                #Find projects name I am doing with person
                                if(self.cBit2==502):
                                    for q in docx1:
                                        if q.text=="projects" or q.text=="project":
                                            inferData = qinfer.qPerProName(subject, objectClear)
                                            print("Check names of project I am doing with person.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                
                                #Find students of specific city or country
                                if(self.cBit2==503):
                                    for q in docx1:
                                        if q.text=="student" or q.text=="students":
                                            inferData = qinfer.qStdLoc(subject, institute)
                                            print("Check which students are from city/country/institute.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                 #Find which teachers are from specific city or country
                                        if q.text=="teacher" or q.text=="teachers":
                                            inferData = qinfer.qStdTechLoc(subject, institute)
                                            print("Check which teachers are from city or country.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                #Find which teachers are lecturar or professor from specific city or country
                                        if q.text=="Lecturar" or q.text=="Professor":
                                            rank=q.text
                                            for qq in docx1:
                                                if qq.text=="teachers" or qq.text=="teacher":
                                                    inferData = qinfer.qStdTechRankLoc(subject, rank, institute)
                                                    print("Check which teachers are lecturar or professor from city/country.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                #Find students of specific degree
                                if(self.cBit2==504):
                                    for q in docx1:
                                         #Find which students have gmail or yahoo account
                                        if q.text=="gmail" or q.text=="yahoo":
                                            for q in docx1:
                                                if q.text=="students" or q.text=="student":
                                                    print(q.text)
                                                    inferData = qinfer.qStdEmail(subject, email)
                                                    print("Check which student have gmail or yahoo account.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                   
                                    #Find which teachers are lecturar or professor
                                        if q.text=="Lecturar" or q.text=="Professor":
                                            rank=q.text
                                            for qq in docx1:
                                                if qq.text=="teachers" or qq.text=="teacher":
                                                    inferData = qinfer.qStdTechRank(subject, rank)
                                                    print("Check which teachers are lecturar or professor.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                    
                                        if q.text=="doing" or q.text=="from":
                                            for q in docx1:
                                                #Check which students are doing graduation in CS, CE, ME, EE, CHE and CV
                                                degree=""
                                                if q.text=="CS" or (q.text=="Computer" or q.text=="Science"):
                                                    degree="CS"
                                                    inferData = qinfer.qStdDegree(subject, degree)
                                                    print("Check which student are from degree in CS.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if q.text=="CE" or (q.text=="Computer" or q.text=="Engineering"):
                                                    degree="CE"
                                                    inferData = qinfer.qStdDegree(subject, degree)
                                                    print("Check which student are from degree in CE.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if q.text=="EE" or q.text=="Electrical" or q.text=="Engineering":
                                                    degree="EE"
                                                    inferData = qinfer.qStdDegree(subject, degree)
                                                    print("Check which student are from degree in ME.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if q.text=="ME" or q.text=="Mechanical" or q.text=="Engineering":
                                                    degree="ME"
                                                    inferData = qinfer.qStdDegree(subject, degree)
                                                    print("Check which student are from degree in ME.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if q.text=="CHE" or q.text=="Chemical" or q.text=="Engineering":
                                                    degree="CHE"
                                                    inferData = qinfer.qStdDegree(subject, degree)
                                                    print("Check which student are from degree in CHE.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if q.text=="CV" or q.text=="Civil" or q.text=="Engineering":
                                                    degree="CV"
                                                    inferData = qinfer.qStdDegree(subject, degree)
                                                    print("Check which student are from degree in CV.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                                if degree=="" or q.text=="graduation":
                                                    degree1="MSc"
                                                    degree2="PHd"
                                                    inferData = qinfer.qStdDegGrad(subject, degree1, degree2)
                                                    print("Check which student are doing graduation.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData

                                            for q in docx1:
                                                degree=""
                                                #Check which students are doing PHd in CS, CE, ME, EE, CHE and CV
                                                if q.text=="PHD" or q.text=="PHd" or q.text=="Phd":
                                                    for q in docx1:
                                                        if q.text=="CS" or (q.text=="Computer" or q.text=="Science"):
                                                            degree=""
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing PHd in CS.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CE" or (q.text=="Computer" or q.text=="Engineering"):
                                                            degree="PHd CE"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing PHd in CE.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="EE" or q.text=="Electrical" or q.text=="Engineering":
                                                            degree="PHd EE"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing PHd in EE.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="ME" or q.text=="Mechanical" or q.text=="Engineering":
                                                            degree="PHd ME"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing PHd in ME.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CHE" or q.text=="Chemical" or q.text=="Engineering":
                                                            degree="PHd CHE"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing PHd in CHE.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CV" or q.text=="Civil" or q.text=="Engineering":
                                                            degree="PHd CV"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing PHd in CV.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if degree=="":
                                                            degree="PHd"
                                                            inferData = qinfer.qStdDegPer(subject, degree)
                                                            print("Check which student are doing PHd.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                            for q in docx1:
                                                degree=""
                                                #Check which students are doing MSC in CS, CE, ME, EE, CHE and CV
                                                if q.text=="MSC" or q.text=="Msc" or q.text=="Master" or q.text=="Masters":
                                                    for q in docx1:
                                                        if q.text=="CS" or (q.text=="Computer" or q.text=="Science"):
                                                            degree="MSc CS"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing MSc in CS.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CE" or (q.text=="Computer" or q.text=="Engineering"):
                                                            degree="MSc CE"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing MSc in CE.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="EE" or q.text=="Electrical" or q.text=="Engineering":
                                                            degree="MSc EE"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing MSc in EE.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="ME" or q.text=="Mechanical" or q.text=="Engineering":
                                                            degree="MSc ME"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing MSc in ME.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CHE" or q.text=="Chemical" or q.text=="Engineering":
                                                            degree="MSc CHE"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing MSc in CHE.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if q.text=="CV" or q.text=="Civil" or q.text=="Engineering":
                                                            degree="MSc CV"
                                                            inferData = qinfer.qStdDegree(subject, degree)
                                                            print("Check which student are doing MSc in CV.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData
                                                        if degree=="":
                                                            degree="MSc"
                                                            inferData = qinfer.qStdDegPer(subject, degree)
                                                            print("Check which student are doing MSc.")
                                                            for i in range(len(inferData)):
                                                                print (inferData[i])
                                                            self.tempTime2 = inferData

                                if(self.cBit2==505):
                                    for q in docx1:
                                        #Find students of specific session
                                        if q.text=="session"or q.text=="year":
                                            for q in docx1:
                                                if q.text=="students" or q.text=="student":
                                                    inferData = qinfer.qStdSession(subject, relationpropertydate)
                                                    print("Check which student are of session.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                               
                                

                        #When user ask who type question   
                        if (quest == "Who"):
                            print("Who question")
                            self.cBit2=post.checkWho(title)
                            if(self.cBit2==600):
                                qinfer = inferencing()
                                inferData = []
                                for q in docx1:
                                    if q.text=="members" or q.text=="member":
                                        based=q
                                        #Find members of project
                                        print(based," based question")
                                        inferData = qinfer.qProMem(title)
                                        print("Check who are members of project.")
                                        for i in range(len(inferData)):
                                            print (inferData[i])
                                        self.tempTime2 = inferData
                                    if q.text=="supervisor" or q.text=="first supervisor":
                                        based=q
                                        #Find supervisor of project
                                        print(based," based question")
                                        inferData = qinfer.qProSup(title)
                                        print("Check who is supervisor or first supervisor of project.")
                                        for i in range(len(inferData)):
                                            print (inferData[i])
                                        self.tempTime2 = inferData
                                    if q.text=="co-supervisor" or q.text=="cosupervisor" or q.text=="second":
                                        based=q
                                        #Find co-supervisor of project
                                        print(based," based question")
                                        inferData = qinfer.qProCoSup(title)
                                        print("Check who is second supervisor or co-supervisor of project.")
                                        for i in range(len(inferData)):
                                            print (inferData[i])
                                        self.tempTime2 = inferData

                        #when user ask how type question
                        if (quest == "How"):
                            print("How question")
                            #personal data question
                            self.cBit2=post.checkHow(subject,institute,relationpropertydate,title)
                            qinfer = inferencing()
                            inferData = []
                            if subtype=="student" or subtype=="teacher":
                                if(self.cBit2==700):
                                    for q in docx1:
                                        if q.text=="student" or q.text=="students": 
                                            #Find how many students of specific city/country/institute                                       
                                            inferData = qinfer.qStdLocCnt(subject,institute)
                                            qper=str(inferData)
                                            print("Check how many students are from city/country/institute.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                if(self.cBit2==701):
                                    for q in docx1:
                                        if q.text=="session"or q.text=="year":
                                            for q in docx1:
                                                if q.text=="students" or q.text=="student":
                                                    #Find how many students of specific session 
                                                    inferData = qinfer.qStdSesCnt(subject,relationpropertydate)
                                                    print("Check how many student from session.")
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
                                                    #Find how many students have gmail or yahoo account
                                                    inferData = qinfer.qStdEmailCnt(subject,email)
                                                    inferData=str(inferData)
                                                    print("Check how many student have gmail/yahoo account.")
                                                    for i in range(len(inferData)):
                                                        print (inferData[i])
                                                    self.tempTime2 = inferData
                                        if q.text=="Lecturar" or q.text=="Professor":
                                            rank=q.text
                                            #Find how many teachers are lecturar or professor
                                            inferData = qinfer.qStdTechRankCnt(subject,rank)
                                            print("Check how many teachers are lecturar.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                if(self.cBit2==700):
                                    for q in docx1:
                                        if q.text=="Lecturar" or q.text=="Professor":
                                            rank=q.text
                                            #Find how many teachers are lecturar or professor from specific city/country/institute
                                            inferData = qinfer.qStdTechRankLocCnt(subject,rank,institute)
                                            print("Check how many teachers are lecturar in location.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                if(self.cBit2==702):
                                    for q in docx1:
                                        if q.text=="members" or q.text=="member":
                                            based=q
                                            #Find how many members of project
                                            print(based," based question")
                                            inferData = qinfer.qMemCnt(title)
                                            print("Check how many members of project.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                if(self.cBit2==703):
                                    for q in docx1:
                                        if q.text=="project" or q.text=="projects":
                                            based=q
                                            #Find how many projects I am supervising 
                                            print(based," based question") 
                                            inferData = qinfer.qPrjCnt(subject)
                                            inferData = str(inferData)
                                            print("Check how many projects i am supervising.")
                                            self.tempTime2 = inferData                            

                        #when user ask when type question
                        if (quest == "When"):
                            print("When question")
                            qinfer = inferencing()
                            inferData = []
                            #meeting based question
                            self.cBit2=post.checkWhen(objectClear, institute)
                            if (self.cBit2 == 200):
                                #Find when have meeting with person
                                inferData = qinfer.qPerson(subject, objectClear, relationclear)
                                print("Check when have meeting with person.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            if (self.cBit2 == 201):
                                #Find when have meeting with person at location
                                inferData = qinfer.qPerLoc(subject, objectClear, relationclear, institute)
                                print("Check when have meeting with person at location.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData 

                        #when user ask where type question
                        if (quest == "Where"):
                            print("Where question")
                            qinfer = inferencing()
                            inferData = []
                            #meeting based question
                            self.cBit2=post.checkWhere(objectClear, timeProperty,relationpropertydate)
                            if (self.cBit2 == 300):
                                #Find where have meeting with person
                                inferData = qinfer.qMeetPer(subject, objectClear, relationclear)
                                print("Check where have meeting with person.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            if (self.cBit2 == 301):
                                #Find where have meeting with person at time
                                inferData = qinfer.qMeetPerTime(subject, objectClear, relationclear, timeProperty)
                                print("Check where have meeting with person at time.")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData
                            if (self.cBit2 == 302):
                                #Find where have meeting with person on date
                                inferData = qinfer.qMeetPerDate(subject, objectClear, relationclear, relationpropertydate)
                                print("Check where have meeting with person at time")
                                for i in range(len(inferData)):
                                    print (inferData[i])
                                self.tempTime2 = inferData

                        #when user ask what type question 
                        if (quest == "What"):
                            
                            #meeting based question
                            print("What question")
                            for q in docx1:
                                qinfer = inferencing()
                                inferData = []
                                #when login type is student and object type also student
                                if subtype=="student" and objtype=="student":
                                    self.cBit2=post.checkWhat(subject,objectClear)
                                    if(self.cBit2==801):
                                        for q in docx1:
                                            if q.text=="email" or q.text=="email id":
                                                #Find email of student
                                                inferData = qinfer.qStdWhatEmail(subject,objectClear)
                                                print("Check what email of student.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="degree":
                                                #Find degree of student
                                                inferData = qinfer.qStdWhatDegree(subject,objectClear)
                                                print("Check what degree student doing.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="city":
                                                #Find city of student
                                                inferData = qinfer.qStdWhatCity(subject,objectClear)
                                                print("Check what city of student.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="country":
                                                #Find country of student
                                                inferData = qinfer.qStdWhatCountry(subject,objectClear)
                                                print("Check what country of student.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            #You cannot access other students contact number and password
                                            if q.text=="contact" or q.text=="phone":
                                                inferData=("You cannot access someone contact number")
                                                self.tempTime2 = inferData
                                            if q.text=="password":
                                                inferData=("You cannot access someone password")
                                                self.tempTime2 = inferData

                                #when login type is student and object type is teacher
                                if subtype=="student" and objtype=="teacher":
                                    self.cBit2=post.checkWhat(subject,objectClear)
                                    if(self.cBit2==801):
                                        for q in docx1:
                                            if q.text=="available" or q.text=="availability":
                                                #Find availabile time of teacher
                                                print("check availability")
                                                inferData = qinfer.qStdWhatTechTime(subject,objectClear)
                                                print("Check what available time of teacher.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="email" or q.text=="email id":
                                                #Find email of teacher
                                                inferData = qinfer.qStdWhatTechEmail(subject,objectClear)
                                                print("Check what email of teacher.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="rank" or q.text=="designation":
                                                #Find rank of teacher
                                                inferData = qinfer.qStdWhatTechRank(subject,objectClear)
                                                print("Check what rank of teacher.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData

                                    #when login type is teacher and object type is student
                                if subtype=="teacher" and objtype=="student":
                                    self.cBit2=post.checkWhat(subject,objectClear)
                                    if(self.cBit2==801):
                                        for q in docx1:
                                            if q.text=="email" or q.text=="email id":
                                                #Find email of student
                                                inferData = qinfer.qStdWhatEmail(subject,objectClear)
                                                print("Check what email of student.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="degree":
                                                #Find degree of student
                                                inferData = qinfer.qStdWhatDegree(subject,objectClear)
                                                print("Check what degree person doing.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="city":
                                                #Find city of student
                                                inferData = qinfer.qStdWhatCity(subject,objectClear)
                                                print("Check what city of student.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="country":
                                                #Find country of student
                                                inferData = qinfer.qStdWhatCountry(subject,objectClear)
                                                print("Check what country of student.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="contact" or q.text=="phone":
                                                #Find phone number of student
                                                inferData = qinfer.qStdWhatPhone(subject,objectClear)
                                                print("Check what phone of student.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="password":
                                                #You cannot access password of student
                                                inferData=("You cannot access someone password")
                                                self.tempTime2 = inferData

                                #when login type is teacher and object type is also teacher
                                if subtype=="teacher" and objtype=="teacher":
                                    self.cBit2=post.checkWhat(subject,objectClear)
                                    if(self.cBit2==801):
                                        for q in docx1:
                                            if q.text=="available" or q.text=="availability" or q.text=="time":
                                                #Find available time of teacher
                                                print("check availability")
                                                inferData = qinfer.qStdWhatTechTime(subject,objectClear)
                                                print("Check what available time of teacher.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="email" or q.text=="email id":
                                                #Find email of teacher
                                                inferData = qinfer.qStdWhatTechEmail(subject,objectClear)
                                                print("Check what email of teacher.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="rank" or q.text=="designation":
                                                #Find rank of teacher
                                                inferData = qinfer.qStdWhatTechRank(subject,objectClear)
                                                print("Check what rank of teacher.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="city":
                                                #Find city of teacher
                                                inferData = qinfer.qStdWhatTechCity(subject,objectClear)
                                                print("Check what city of teacher.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="country":
                                                #Find country of teacher
                                                inferData = qinfer.qStdWhatTechCountry(subject,objectClear)
                                                print("Check what city of teacher.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="contact" or q.text=="phone":
                                                #Find contact number of teacher
                                                inferData = qinfer.qStdWhatTechPhone(subject,objectClear)
                                                print("Check what phone number of teacher.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData
                                            if q.text=="password":
                                                #You cannot access password
                                                inferData=("You cannot access someone password")
                                                self.tempTime2 = inferData

                            #when login type is student
                            if subtype=="student" or subtype=="teacher":
                                for q in docx1:
                                    if q.text=="location" or q.text=="venue":
                                        based=q
                                        print(based,"location based question")
                                        print(subjectClear,"subjectClear")
                                        self.cBit2=post.checkWhatLoc(objectClear, timeProperty, relationpropertydate, institute)
                                        if (self.cBit2 == 400):
                                            #Find location of meeting
                                            inferData = qinfer.qWhatLoc(subject, objectClear, relationclear)
                                            print("Check what location of meeting with person.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData

                                    if q.text=="time":
                                        based=q
                                        print(based," based question")
                                        print(objectClear)
                                        self.cBit2=post.checkWhatTime(objectClear, timeProperty, relationpropertydate, institute)
                                        if (self.cBit2 == 420):
                                            #Find time of meeting
                                            inferData = qinfer.qWhatTime(subject, objectClear, relationclear)
                                            print("Check what time of meeting with person.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData

                                    if q.text=="agenda" or q.text=="title":
                                        based=q
                                        print(based,"based question")
                                        self.cBit2=post.checkWhatAgenda(objectClear,timeProperty,relationpropertydate,institute)
                                        if (self.cBit2 == 440):
                                            #Find agenda of meeting on basis of person
                                            inferData = qinfer.qWhatAgenda(subject,objectClear)
                                            print("Check what agenda of meeting with person.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 441):
                                            #Find agenda of meeting on basis of person and time
                                            inferData = qinfer.qWhatAgendaTime(subject,objectClear,timeProperty)
                                            print("Check what agenda of meeting with person and time.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 442):
                                            #Find agenda of meeting on basis of person and date
                                            inferData = qinfer.qWhatAgendaDate(subject,objectClear,relationpropertydate)
                                            print("Check what agenda of meeting with person and date.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 443):
                                            #Find agenda of meeting on basis of person and venue
                                            inferData = qinfer.qWhatAgendaVenue(subject,objectClear,institute)
                                            print("Check what agenda of meeting with person and location.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 444):
                                            #Find agenda of meeting on basis of person, date and time
                                            inferData = qinfer.qWhatAgendaDateTime(subject,objectClear,relationpropertydate,timeProperty)
                                            print("Check what agenda of meeting with person, date and time.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 445):
                                            #Find agenda of meeting on basis of person, time and venue 
                                            inferData = qinfer.qWhatAgendaTimeVenue(subject,objectClear,timeProperty,institute)
                                            print("Check what agenda of meeting with person, time and venue.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 446):
                                            #Find agenda on basis of  date and location
                                            inferData = qinfer.qWhatAgendaDateVenue(subject,objectClear,relationpropertydate,institute)
                                            print("Check what agenda of meeting with person, time and venue.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if (self.cBit2 == 447):
                                            #Find agenda on basis of person, date, time and location
                                            inferData = qinfer.qWhatAgendaAll(subject,objectClear,timeProperty ,relationpropertydate,institute)
                                            print("Check what agenda of meeting with person, time, date and venue.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                    
                                    if q.text=="projects" or q.text=="project":
                                        self.cBit2=post.checkWhat(subject,objectClear)
                                        if(self.cBit2==800):
                                            #Find names of project I am spervising
                                            inferData = qinfer.qWhatPrjName(subject)
                                            print("Check names of project I am supervising.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData
                                        if(self.cBit2==801):
                                            #Find project name with person
                                            inferData = qinfer.qWhatPerPrjName(subject,objectClear)
                                            print("Check names of project I am doing with person.")
                                            for i in range(len(inferData)):
                                                print (inferData[i])
                                            self.tempTime2 = inferData

                                        if q.text=="members" or q.text=="member":
                                            self.cBit2=post.checkWho(title)
                                            if(self.cBit2==600):
                                                #Find project members
                                                qdata = qinfer.qWhatPrjMemName(title)
                                                print("Check names of members of project.")
                                                for i in range(len(inferData)):
                                                    print (inferData[i])
                                                self.tempTime2 = inferData

            return self.tempTime2



