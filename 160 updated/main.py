from flask import Flask , render_template , request  , redirect , Response ,url_for
from neo4jrestclient.client import GraphDatabase
from flask_bootstrap import Bootstrap
from model import post
from model import BotBehaviour
from model import *
from spacy1122 import *
from infer_fnc import *
from infer_fnc import inferencing
from meetList import *
from signup import *
from delMem import * 
import json
import urllib
from datetime import date
from datetime import time
from datetime import datetime
from time import strptime
from os import *
import datetime
from datetime import datetime
from dateutil import parser

from signup import register_user


db = GraphDatabase("http://localhost:11012", username="neo4j", password="neo4j")
app = Flask(__name__ , template_folder='template')

Bootstrap(app)
ip = []
osystem = []

gloVar = "abcd"
ahoVar = ""
aho4Var = ""
typpOf = ""
contact = ""
lname = ""
gloVarDateTime = ""

@app.route('/dash') 
def index():   

    print("Value before Index" , gloVar) 
    return  render_template('index.html' , gloVar = gloVar)

# @app.route('/meetings')
# def showAll():

#     return render_template('meetings.html' , gloVar= gloVar)

@app.route('/')
def homeX():
    return render_template('home.html')




@app.route('/meetings', methods=['GET', 'POST'])
def showMeet():

    meetTemp=[]
    meetTemp=meet_list(gloVar, "meeting")
    print(meetTemp)

    if(meetTemp == ""):
        print("list is"  , meetTemp)

    return render_template('meetings.html', meetTemp=meetTemp , gloVar = gloVar)


@app.route('/rescheduled', methods=['GET' ,])
def showReMeet():

    meetTempName  =[]
    meetTempTime  = []
    meetTempDate  = []
    meetTempVenue = []
    meetHead2 ="with Whom You Wants to Have Rescheduled Meet?" 
    meetHead = meetHead2
    meetTempName  = meet_dateTime_name(gloVar, "meeting")
    meetTempTime  = meet_dateTime_time(gloVar ,"meeting")
    meetTempDate  = meet_dateTime_date (gloVar ,"meeting")
    meetTempVenue = meet_dateTime_Venue(gloVar , "meeting")



    # if(meetTemp == ""):
    #     print("list is"  , meetTemp)
    return render_template('reschedule.html' ,meetTempName=meetTempName ,  meetTempTime = meetTempTime  ,meetTempDate = meetTempDate , meetTempVenue = meetTempVenue, gloVar = gloVar , meetHead = meetHead )


@app.route('/rescheduled' ,  methods=['GET' , 'POST'])
def rescheduled_form():

    enText = request.form ['Name_res']
    snText = request.form ['select_name']
    etText = request.form ['Time_res']
    stText = request.form ['select_time']
    print(stText , "select time")
    edText = request.form ['Date_res']
    sdText = request.form ['select_date']
    evText = request.form ['Venue_res']
    svText = request.form ['select_venue']
    print(enText , "reschedled member")

    changeMeet(gloVar , "meeting" , enText ,etText ,edText , evText , snText , stText , sdText , svText )

    print("change Meeting called")


    return render_template("reschedule.html" , gloVar = gloVar )




# tempSub = request.form ['txt_store']
# print(tempSub)

global flagBit4
textspacy = text_spacy()


@app.route("/member" , methods=['GET' , 'POST'])
def showMember():
    memberTem = []
   

    memberTem= post.ObjectSelection(gloVar)

    print(memberTem)
    # if (memberTem == ""):
    #     print ("list is of Member" , memberTem[1])
    return render_template('index.html' , memberTem = memberTem)

# @app.route('/' , methods = ['GET' , 'POST'])
# def openLogin():
#   return render_template("index.html", showVar = showVar)

@app.route('/dash' ,  methods=['GET' , 'POST'])
def myForm():
    #return render_template('index.html')
    text_Show = "Hello EveryOne! "
    text = request.form['text_store']
    textspacy.function_spacy(text , gloVar)
    cBit6 = textspacy.foo()
    text_Edit = text
    ctempTime6 = textspacy.fooList()
    for i in range(0, len(ctempTime6)):
        print("Time inferencing values : ", ctempTime6[i])


    ctempLoc6 = textspacy.fooLocList()
    for i in range(0, len(ctempLoc6)):
        print("Location inferencing values : ", ctempLoc6[i])

    print("Value of cBit6: ",cBit6)
    tempS = ""
    tempPrompt = ""

    if (cBit6 == '0000'):
        tempS = "Please Enter the Name Participant , Date , Venue and Time of Meeting"
        tempPrompt = "Please Enter the Name Participant , Date , Venue and Time of Meeting"
    elif (cBit6=='0001'):
        tempS = "Please Enter the Name Participant , Venue and Time of Meeting"
        tempPrompt = "Please Enter the Name Participant , Venue and Time of Meeting"
    elif (cBit6=='0010'):
        tempS = "Please Enter the Name Participant , Date and Time of Meeting"
        tempPrompt = "Please Enter the Name Participant , Date and Time of Meeting"
    elif (cBit6=='0011'):
        tempS = "Please Enter the Name Participant and Venue of Meeting"
        tempPrompt = "Please Enter the Name Participant and Venue of Meeting"
    elif (cBit6=='0100'):
        tempS = "Please Enter the Name Participant, Date and  Time of Meeting"
        tempPrompt = "Please Enter the Name Participant , Date and Time of Meeting"
    elif (cBit6=='0101'):
        tempS = "Please Enter the Name Participant  and Date of Meeting"
        tempPrompt = "Please Enter the Name Participant  and Date of Meeting"
    elif (cBit6=='0110'):
        tempS = "Please Enter the Name Participant and Date of Meeting"
        tempPrompt = "Please Enter the Name Participant and Date of Meeting"
    elif (cBit6=='0111'):
        tempS = "Please Enter the Name Participant of Meeting"
        tempPrompt = "Please Enter the Name Participant  of Meeting"
    elif (cBit6=='1000'):
        tempS = "Please Enter the Date , Venue and Time of Meeting"
        tempPrompt = "Please Enter the  Date , Venue and Time of Meeting"
    elif (cBit6=='1001'):
        tempS = "Please Enter the   Venue and Time of Meeting"
        tempPrompt = "Please Enter the  Venue and Time of Meeting"
    elif (cBit6=='1010'):
        tempS = "Please Enter the  Venue and Date of Meeting"
        tempPrompt = "Please Enter the Venue and Date of Meeting"
    elif (cBit6=='1011'):
        tempS = "Please Enter the  Venue  of Meeting"
        tempPrompt = "Please Enter the  Venue of Meeting"
    elif (cBit6=='1100'):
        tempS = "Please Enter the Date and Time of Meeting"
        tempPrompt = "Please Enter the Date and Time of Meeting"
    elif (cBit6=='1101'):
        tempS = "Please Enter the  Time of Meeting"
        tempPrompt = "Please Enter the  Time of Meeting"
    elif (cBit6=='1110'):
        tempS = "Please Enter the  Date of Meeting"
        tempPrompt = "Please Enter the Date of Meeting"
    elif (cBit6=='0'):
        tempS = "Your Meeting Has Been SCHEDULED Successfully"
        tempPrompt = "Your Meeting Has Been SCHEDULED Successfully"
        text_Edit = ""

    # elif (cBit6 == 7):
    #     tempS = "Please Enter the Time of Meeting!"
    #     tempPrompt = "WHEN you want to meet?"

    # elif (cBit6 == 11):
    #     tempS = "Please Enter the Date of Meeting!"
    #     tempPrompt = "WHEN you want to meet?"


    # elif(cBit6 == 4):
    #     tempS = "Please Enter the Time and Venue of Meeting!"
    #     tempPrompt = "WHEN and WHERE you want to meet?"

    # elif(cBit6 == 44):
    #     tempS = "Please Enter the Time and Date of Meeting!"
    #     tempPrompt = "WHEN you want to meet?"

    # elif(cBit6 == 444):
    #     tempS = "Please Enter the Venue and Date of Meeting!"
    #     tempPrompt = "WHERE and WHEN you want to meet?"

    # elif(cBit6 == 333):
    #     tempS = "Please Enter the Time, Venue and Date of Meeting!"
    #     tempPrompt = "WHEN and WHERE you want to meet?"
    # # elif(cBit6 == 9):
    # #   tempS = "Please All the Time and Venue of Meeting!"
    # elif (cBit6 == 111):
    #     tempS = "You Cant"
    #     # tempS = "You Can't Sheduled Meeting with this Persong"
    #     tempPrompt = "Alas! Your Meeting has not been Successfully SCHEDULED!!"
    #     text_Edit = ""


    # elif (cBit6 == 666):
    #     tempS = "Please Enter Time, Venue , Date and Name of Person whom you want to Meet"
    #     # tempS = "You Can't Sheduled Meeting with this Persong"
    #     tempPrompt = "When Were Whom and Which Time Want to Have Meeting"
    #     text_Edit = ""

    # elif(cBit6 == 000):
    #     tempS = "Complete Information! Your information has been saved!!"
    #     tempPrompt = "Great! Your Meeting has been Successfully SCHEDULED!!"
    #     text_Edit = ""


    elif(cBit6 == 100):
        tempS = "Question"
        tempPrompt = "Object based question"
    elif(cBit6 == 101):
        tempS = "Question"
        tempPrompt = "time based question"
    elif(cBit6 == 102):
        tempS = "Question"
        tempPrompt = "time and person based question"
    elif(cBit6 == 103):
        tempS = "Question"
        tempPrompt = "date and person based question"
    elif(cBit6 == 104):
        tempS = "Question"
        tempPrompt = "date based question"
    elif(cBit6 == 105):
        tempS = "Question"
        tempPrompt = "location based question"
    elif(cBit6 == 106):
        tempS = "Question"
        tempPrompt = "location and person based question"
    elif(cBit6 == 200):
        tempS = "Question"
        tempPrompt = "when based question"
    elif(cBit6 == 201):
        tempS = "Question"
        tempPrompt = "when based question with location"
    elif(cBit6 == 300):
        tempS = "Question"
        tempPrompt = "where based question"
    elif(cBit6 == 301):
        tempS = "Question"
        tempPrompt = "where based question with time"
    elif(cBit6 == 400):
        tempS = "Question"
        tempPrompt = "what location based question"
    elif(cBit6 == 500):
        tempS = "Question"
        tempPrompt = "what time based question"

    



    #prompting....



    respVar = tempS
    text_Show = text_Edit
    showText = text_Show
    # f= open("MyInput.txt","a+")
    # f.write("\n"+ (text_Show ))
    # # ("This is line %d\r\n" % (i+1))
    # f.close() 

    # f=open("MyInput.txt", "r")
    textSystem = tempPrompt 
    temp = text
    ip.append("User: "+temp)
    ip.append("System: " +textSystem) #add to list
    print (ip)
    for i in range(0, len(ip)):
        print ("value is ",ip[i])
    print("value is : AKHSHKHSIOH")
    print ("Value in Index:" , gloVar)
    return render_template("index.html", respVar = respVar , showText = showText  , ctempTime6 = ctempTime6 , ip = ip , gloVar = gloVar )
#   return render_template('index.html')

@app.route('/DelMeet' , methods = ['GET'] )
def deleteMeet():
    meetTemp=[]
    meetTemp=meet_list(gloVar, "meeting")

    if(meetTemp == ""):
        print("list is"  , meetTemp)

    return render_template('deleteMeeting.html', meetTemp=meetTemp , gloVar = gloVar)

@app.route('/DelMeet' , methods = ['GET' ,'POST'] )
def deleteMeeting():
    deleteString = request.form['del_meet']
    print(deleteString)
    Del_spacy.function_del_spacy(gloVar , deleteString)
    # print("Deletion Called")

    return render_template('deleteMeeting.html')





@app.route('/today', methods=['GET', 'POST'])
def todayMeeting():

    meetTemp=[]
    meetTemp=TodayMeetings(gloVar)

    if(meetTemp == ""):
        print("list is"  , meetTemp)

    return render_template('todayMeet.html', meetTemp=meetTemp , gloVar = gloVar)



@app.route('/reg')
def indexRegister():
    return render_template("signupO.html")






@app.route('/reg' ,  methods=['GET' , 'POST'])
def Register_form():

    checked=request.form['typer']
    print(checked)
    fText = request.form['fname']
    lText = request.form['lname']
    pText = request.form ['password']
    eText = request.form ['email']
    nText = request.form ['pnumber']
    ftText = request.form['from-time']
    ttText = request.form ['to-time']
    countText = request.form ['country']
    cityText = request.form ['city']
    regText = request.form ['regNum']
    StringRegNo = DTValidate.splitString(regText)
    StringDegree = StringRegNo[0]
    print(StringDegree)
    StringSession = StringRegNo[1]
    
    print(StringSession)
    StringSerialNum = StringRegNo[2]
    print(StringSerialNum)
    print(StringRegNo , StringDegree , StringSession , StringRegNo)
    instText = request.form ['Institute']
    dText = request.form ['rank']
    if (checked == "student"):
        print ("student Register")
        register_user.createStudent (fText , lText , countText , instText,   cityText, regText,  eText , pText , nText , checked , StringSession , StringDegree , StringSerialNum )
    
    elif(checked == "teacher"):
        register_user.createTeacher(fText , lText , countText , instText, dText ,  cityText, eText , pText , nText , checked , ftText , ttText)

        print("Tecaher Register")
    else:
        checked = "other"
        print("You have no Selected Type")
    return render_template("signupO.html")
    
@app.route('/profile' , methods = ['GET' , 'POST'])
def high_property():
    return render_template("profile.html" ,  gloVar= gloVar , ahoVar = ahoVar , aho4Var =aho4Var , contact = contact , lname = lname , typpOf = typpOf)
     

@app.route('/log')
def index_login():
    return render_template("loginO.html")

@app.route('/log' ,  methods=['GET' , 'POST'])
def login_form():
    global gloVar
    global ahoVar
    global aho4Var
    global typpOf
    global contact
    global lname
    # if request.method == 'GET': 
        # tText = request.form ['']


    elText = request.form ['login_email']
    plText = request.form['login_pass']

    ru = register_user()
    ahoVar=ru.userReturnEmail(elText , plText)
    print("Name: ", ahoVar)


    aho4Var=ru.userReturnPass(elText , plText)
    print("Password: ", aho4Var)

    gloVar=ru.userReturnName(elText , plText)
    print("username: ", gloVar)
    

    typpOf=ru.userReturnType(elText , plText)
    print("type of: ", typpOf)

    lname=ru.userReturnLastName(elText , plText)
    print("username: ", lname)

    contact=ru.userReturnContactNumber(elText , plText)
    print("username: ", contact)

    error = None
    if request.method == 'POST':
        if ahoVar is None and  aho4Var is None:
            error = "Invalid Credentials Please Try again"
        else:
            return redirect('http://localhost:5000/dash')
    return render_template('loginO.html' , error = error)


    return render_template("loginO.html")

@app.route('/eprofile')
def edit_member():
    return render_template("editprofile.html",  gloVar= gloVar , ahoVar = ahoVar , aho4Var =aho4Var , contact = contact , lname = lname , typpOf = typpOf)

@app.route('/eprofile' ,  methods=['GET' , 'POST'])
def login_edit():


    fiText = request.form['edit_fname']
    lnText = request.form['edit_lname']
    elText = request.form ['email_edit']
    print(elText , "this is")
    plText = request.form['Password']
    ccText = request.form['contact']
    TText = request.form['typo']


    register_user.editProfile(fiText , lnText , TText , ccText , elText , plText )




    



    return render_template("editprofile.html")





if __name__ == '__main__':
    app.run(debug=True)  