from flask import Flask , render_template , request  , redirect , Response ,url_for
from neo4jrestclient.client import GraphDatabase
from flask_bootstrap import Bootstrap
from model import post
from model import *
from spacy1122 import *
from infer_fnc import *
from infer_fnc import inferencing
from meetList import *
from signup import *
from delMem import * 
from reschedule import *
import json
import urllib
from datetime import date
from datetime import time
from datetime import datetime
from time import strptime
from os import *
import datetime
from knowledge import *
from datetime import datetime
from dateutil import parser
from signup import register_user
from inferSpacy import *


db = GraphDatabase("http://localhost:11002", username="neo4j", password="neo4j")
app = Flask(__name__ , template_folder='template')

Bootstrap(app)
ip = []
ipi = []
osystem = []

gloVar = ""
ahoVar = ""
aho4Var = ""
typpOf = ""
contact = ""
lname = ""
gloVarDateTime = ""


#CALLING FOR HOMEPAGE
@app.route('/')
def homeX():
    return render_template('home.html')

#CALLING FOR MEETING DASHBOARD
@app.route('/dash' , methods = ['GET']) 
def index():   
    meetTemp=[]
    meetTemp=TodayMeetings(gloVar)
    lenToday = len(meetTemp)
    print(lenToday ,  "todayLenght")
    if(meetTemp == ""):
        print("list is"  , meetTemp)
    print("Value before Index" , gloVar) 
    return  render_template('index.html' , gloVar = gloVar , lenToday = lenToday)

#CALLING FOR DASHBOARD THAT WILL SCHEDULLED MEETING AFTER VALIDATIONS
@app.route('/dash' ,  methods=['GET' , 'POST'])
def myForm():
    tempSaveBit = 0
    meetToday=[]
    meetToday=TodayMeetings(gloVar)
    lenToday = len(meetToday)
    print(lenToday ,  "todayLenght")
    if(meetToday == ""):
        print("list is Today"  , meetToday)
    text_Show = "Hello EveryOne! "
    text = request.form['text_store']
    kvBit = kv_spacy.function_kv_spacy(gloVar , text  )
    tempS = ""
    tempPrompt = ""
    textspacy.function_spacy(text , gloVar)
    cBit6 = textspacy.foo()
    text_Edit = text
    ctempTime6 = textspacy.fooList()
    print(kvBit , "main Function knowledge Called")
    if(kvBit !=1):
        print("Your Bit is" ,kvBit)
        for i in range(0, len(ctempTime6)):
            print("Time inferencing values : ", ctempTime6[i])
        ctempLoc6 = textspacy.fooLocList()
        for i in range(0, len(ctempLoc6)):
            print("Location inferencing values : ", ctempLoc6[i])
        print("Value of cBit6: ",cBit6)
       
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
            tempPrompt = "Your Meeting Has Been SCHEDULED Successfully. Do you have any AGENDA for this meeting?  Click below button to write AGENDA details!"
            text_Edit = ""
            tempSaveBit=1
    elif(kvBit == 1):
        print("your Bit is " , kvBit)
        tempS = "No Your Meeting Has Been SCHEDULED Successfully"
        tempPrompt = "Not You Meeting Has Been SCHEDULED Successfully"
        text_Edit = ""
    respVar = tempS
    text_Show = text_Edit
    showText = text_Show
    textSystem = tempPrompt 
    temp = text
    ip.append("User: "+temp)
    ip.append("System: " +textSystem) 
    print (ip)
    for i in range(0, len(ip)):
        print ("value is ",ip[i])
    print ("Value in Index:" , gloVar)
    return render_template("index.html", respVar = respVar , showText = showText  , ctempTime6 = ctempTime6 , ip = ip , gloVar = gloVar, tempSaveBit=tempSaveBit )

#CALLING FOR TO SHOW MEETING LIST
@app.route('/meetings', methods=['GET', 'POST'])
def showMeet():
    meetTemp=[]
    meetTemp=meet_list(gloVar, "meeting")
    print(meetTemp)
    meetToday=[]
    meetToday=TodayMeetings(gloVar)
    lenToday = len(meetToday)
    print(lenToday ,  "todayLenght")
    if(meetToday == ""):
        print("list is Today"  , meetToday)
    if(meetTemp == ""):
        print("list is"  , meetTemp)
    return render_template('meetings.html', meetTemp=meetTemp , gloVar = gloVar , lenToday = lenToday)

#CALLING FOR RESCHDULED LIST USING GET METHOD 
@app.route('/rescheduled', methods=['GET' ])
def showReMeet():
    meetToday=[]
    meetToday=TodayMeetings(gloVar)
    lenToday = len(meetToday)
    print(lenToday ,  "todayLenght")
    if(meetToday == ""):
        print("list is Today"  , meetToday)
    meetHead2 ="Reschedule your Meetings" 
    meetHead = meetHead2
    meetTemp=[]
    meetTemp=ReschuleMeetingList(gloVar)
    if(meetTemp == ""):
        print("list is"  , meetTemp)
    return render_template('reschedule.html', meetTemp=meetTemp , gloVar = gloVar , lenToday = lenToday , meetHead = meetHead )

#CALLING FOR RESCHEDULING OF MEETING LIST
@app.route('/rescheduled' ,  methods=['GET' , 'POST'])
def rescheduled_form():
    meetToday=[]
    meetToday=TodayMeetings(gloVar)
    lenToday = len(meetToday)
    print(lenToday ,  "todayLenght")
    if(meetToday == ""):
        print("list is Today"  , meetToday)
    enTime = request.form ['utime']
    enDate = request.form ['udate']
    enVenue = request.form ['uvenue']
    select = request.form['res_meet']
    print(enTime , enDate , enVenue ,select , "reschedled member")
    Res_spacy.function_res_spacy(gloVar , select, enTime , enDate , enVenue )
    print("change Meeting called")
    return render_template("reschedule.html" , gloVar = gloVar , lenToday = lenToday)

global flagBit4
textspacy = text_spacy()

#CALLING FOR AGENDA/MEMBERS RETRIEVING
@app.route('/dashMedAg')
def medForm():
    ipAg = list()
    ipMem = list()
    ipMem = text_spacy.RetrieveMembers()
    ipAg = text_spacy.RetrieveAgenda()
    return render_template('indexMedAg.html', ipAg=ipAg, ipMem=ipMem)

#CALLING FOR AGENDA SELECTION/CREATION
@app.route('/dashMedAg' , methods=['GET', 'POST'])
def medFormX():
    if request.method=='POST':
        agMems = list()
        agTitle = request.form['agendadrop']
        agMems = request.form.getlist('memdrop')
        ts = text_spacy()
        ts.FypFunctionDD(agTitle, agMems)

    return render_template('index.html') 

#CALLING FOR RETRIEVING MEMBERS LIST/AGENDA
@app.route('/dashAg')
def myFormAgX():
    ipMem = list()
    ipMem = text_spacy.RetrieveMembers()
    return render_template('indexAg.html', ipMem=ipMem)

#CALLING FOR AGENDA CREATION
@app.route('/dashAg', methods=['GET', 'POST'])
def myFormAg():
    if request.method == 'POST':
        agTitle = request.form['agtitle']
        agName = request.form['pName']
        agDetail = request.form['detail']
        agNoOfMems = request.form['noofmems']
        agSupervisor = request.form['supervisor']
        agSecSupervisor = request.form['sec_supervisor']
        reg1 = request.form['mem1']
        reg2 = request.form['mem2']
        reg3 = request.form['mem3']
        reg4 = request.form['mem4']
        agMems = request.form.getlist('memdrop')

        textspacy.FypFunction(agTitle,agName,agDetail,agNoOfMems,agSupervisor,agSecSupervisor,reg1, reg2, reg3, reg4, agMems)
    return render_template('index.html')

#CALL INFERENCING 
@app.route ('/infer' )
def infer():
    return render_template('inferencing.html' , gloVar = gloVar)

#INFER DATA ON BASIS OF USERINPUT
@app.route('/infer' , methods = ['GET', 'POST'])
def inferencing():
    print('Call Main infer')
    text_Show = "Hello EveryOne! "
    text = request.form['text_store']
    print(text)

    inferspac = Infer_spacy()
    inferspac.Infer_fun_spacy( text , gloVar)
    ctempTime6 = inferspac.fooList()
    cBit6 = inferspac.foo()
    print(cBit6 , 'Bit value in inferencing')
    ctempLoc6 = inferspac.fooLocList()
    text_Edit = text
    tempS = ""
    tempPrompt = ""
    meetToday=[]
    meetToday=TodayMeetings(gloVar)
    lenToday = len(meetToday)
    print(lenToday ,  "todayLenght")
    if(meetToday == ""):
        print("list is Today"  )
    
    if(cBit6 == 100):
        tempPrompt = ctempTime6
    elif(cBit6 == 101):
         tempPrompt = ctempTime6
    elif(cBit6 == 102):
         tempPrompt = ctempTime6

    elif(cBit6 == 103):
         tempPrompt = ctempTime6
    elif(cBit6 == 104):
        tempPrompt = ctempTime6
    elif(cBit6 == 105):
        tempPrompt = ctempTime6
    elif(cBit6 == 106):
         tempPrompt = ctempTime6
    elif(cBit6 == 107):
        tempPrompt = ctempTime6
    elif(cBit6 == 108):
         tempPrompt = ctempTime6
    elif(cBit6 == 109):
         tempPrompt = ctempTime6
    elif(cBit6 == 110):
        tempPrompt = ctempTime6
    elif(cBit6 == 111):
        tempPrompt = ctempTime6
    elif(cBit6 == 112):
         tempPrompt = ctempTime6
    elif(cBit6 == 113):
        tempPrompt = ctempTime6
    elif(cBit6 == 114):
         tempPrompt = ctempTime6
    elif(cBit6 == 115):
         tempPrompt = ctempTime6
    elif(cBit6 == 116):
         tempPrompt = ctempTime6
    elif(cBit6 == 117):
         tempPrompt = ctempTime6
    elif(cBit6 == 118):
         tempPrompt = ctempTime6
    elif(cBit6 == 119):
         tempPrompt = ctempTime6
    elif(cBit6 == 120):
         tempPrompt = ctempTime6
    elif(cBit6 == 121):
         tempPrompt = ctempTime6
    elif(cBit6 == 122):
         tempPrompt = ctempTime6
    elif(cBit6 == 123):
         tempPrompt = ctempTime6
    elif(cBit6 == 124):
         tempPrompt = ctempTime6
    elif(cBit6 == 125):
         tempPrompt = ctempTime6
    elif(cBit6 == 126):
         tempPrompt = ctempTime6
    elif(cBit6 == 127):
         tempPrompt = ctempTime6
    elif(cBit6 == 128):
         tempPrompt = ctempTime6

    elif(cBit6 == 200):
        tempPrompt = ctempTime6
    elif(cBit6 == 201):
        tempPrompt = ctempTime6

    elif(cBit6 == 300):
        tempPrompt = ctempTime6
    elif(cBit6 == 301):
        tempPrompt = ctempTime6
    elif(cBit6 == 302):
        tempPrompt = ctempTime6

    elif(cBit6 == 400):
         tempPrompt = ctempTime6
    elif(cBit6 == 420):
         tempPrompt = ctempTime6

    elif(cBit6 == 440):
         tempPrompt = ctempTime6
    elif(cBit6 == 441):
        tempPrompt = ctempTime6
    elif(cBit6 == 442):
        tempPrompt = ctempTime6
    elif(cBit6 == 443):
         tempPrompt = ctempTime6
    elif(cBit6 == 444):
         tempPrompt = ctempTime6
    elif(cBit6 == 445):
         tempPrompt = ctempTime6
    elif(cBit6 == 446):
        tempPrompt = ctempTime6
    elif(cBit6 == 447):
         tempPrompt = ctempTime6

    elif(cBit6 == 500):
         tempPrompt = ctempTime6
    elif(cBit6 == 501):
        tempPrompt = ctempTime6
    elif(cBit6 == 502):
         tempPrompt = ctempTime6
    elif(cBit6 == 503):
         tempPrompt = ctempTime6
    elif(cBit6 == 504):
        tempPrompt = ctempTime6
    elif(cBit6 == 505):
         tempPrompt = ctempTime6

    elif(cBit6 == 600):
         tempPrompt = ctempTime6

    elif(cBit6 == 700):
        tempPrompt = ctempTime6
    elif(cBit6 == 701):
         tempPrompt = ctempTime6
    elif(cBit6 == 702):
         tempPrompt = ctempTime6
    elif(cBit6 == 703):
         tempPrompt = ctempTime6

    elif(cBit6 == 800):
         tempPrompt = ctempTime6
    elif(cBit6 == 801):
         tempPrompt = ctempTime6

    elif(cBit6 == 0):
        tempPrompt = "Person not exist"


    respVar = tempS
    text_Show = text_Edit
    showText = text_Show
  
    textSystem = str(ctempTime6) 
    bltext = textSystem.replace('[',"")
    brtext = bltext.replace(']',"")
    ftext = brtext.replace('"',"")
    
    temp = text
    ipi.append("User: "+temp)
    ipi.append("System: " +ftext) #add to list
    print (ipi)
    for i in range(0, len(ipi)):
        print ("value is ",ipi[i])
    print ("Value in Index:" , gloVar)

    return render_template ('inferencing.html' , gloVar = gloVar , lenToday = lenToday  , respVar = respVar , showText = showText  , ip = ipi )

#Call list of upcomming meetings for deletion
@app.route('/DelMeet' , methods = ['GET'] )
def deleteMeet():
    meetTemp=[]
    meetTemp=meet_list(gloVar, "meeting")
    meetToday=[]
    meetToday=TodayMeetings(gloVar)
    lenToday = len(meetToday)
    print(lenToday ,  "todayLenght")
    if(meetToday == ""):
        print("list is Today"  , meetToday)
    if(meetTemp == ""):
        print("list is"  , meetTemp)
    return render_template('deleteMeeting.html', meetTemp=meetTemp , gloVar = gloVar , lenToday = lenToday)


#CALL DELETE MEETING FOR DELETION OF AN UPCOMMING MEETING
@app.route('/DelMeet' , methods = ['GET' ,'POST'] )
def deleteMeeting():
    deleteString = request.form['del_meet']
    print(deleteString)
    Del_spacy.function_del_spacy(gloVar , deleteString)
    meetToday=[]
    meetToday=TodayMeetings(gloVar)
    lenToday = len(meetToday)
    print(lenToday ,  "todayLenght")
    if(meetToday == ""):
        print("list is Today"  , meetToday)
    return render_template('deleteMeeting.html' , lenToday = lenToday)


#CALL LIST OF TODAY'S MEETING
@app.route('/today', methods=['GET', 'POST'])
def todayMeeting():
    meetTemp=[]
    meetTemp=TodayMeetings(gloVar)
    lenToday = len(meetTemp)
    print(lenToday ,  "todayLenght")
    if(meetTemp == ""):
        print("list is"  , meetTemp)
    return render_template('todayMeet.html', meetTemp=meetTemp , gloVar = gloVar, lenToday = lenToday)


#CALL SIGNUP PAGE
@app.route('/reg')
def indexRegister():
    return render_template("signupO.html")

#REGISTER A USER ON BASIS OF ITS PROPERTY
@app.route('/reg' ,  methods=['GET' , 'POST'])
def Register_form():
    checked=request.form['typer']
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
    dText = request.form ['rank']
    instText = request.form ['Institute']
    dText = request.form ['rank']
    if (checked == "student"):
        StringRegNo = DTValidate.splitString(regText)
        StringDegree = StringRegNo[1]
        print(StringDegree)
        StringSession = StringRegNo[0]
        print(StringSession)
        StringSerialNum = StringRegNo[2]
        print(StringSerialNum)
        print(StringRegNo , StringDegree , StringSession , StringRegNo)
        print ("student Register")
        register_user.createStudent (fText , lText , countText , instText,   cityText, regText,  eText , pText , nText , checked , StringSession , StringDegree , StringSerialNum )
    
    elif(checked == "teacher"):
        register_user.createTeacher(fText , lText , countText , instText, dText ,  cityText, eText , pText , nText , checked , ftText , ttText)
        print("Tecaher Register")
    else:
        checked = "other"
        print("You have no Selected Type")
    return render_template("signupO.html")

#CALL SIGN_IN PAGE
@app.route('/log')
def index_login():
    return render_template("loginO.html")
#CALL FOR USER SIGN_IN ACCORDING TO MATCH WITH CREDENTIA;
@app.route('/log' ,  methods=['GET' , 'POST'])
def login_form():
    global gloVar
    global ahoVar
    global aho4Var
    global typpOf
    global contact
    global fname
    global lname
    global country
    global city
    global institutee
    global regnumber
    global availTo
    global availFrom
    global desigination
    global Session
    global degree

    elText = request.form ['login_email']
    plText = request.form['login_pass']
    ru = register_user()
    ahoVar=ru.userReturnEmail(elText , plText)
    print("Email is: ", ahoVar)


    aho4Var=ru.userReturnPass(elText , plText)
    print("Password: ", aho4Var)

    fname=ru.userReturnName(elText , plText)
    print("Name First is : ", fname)
    
    typpOf=ru.userReturnType(elText , plText)
    print("type of: ", typpOf)

    lname=ru.userReturnLastName(elText , plText)
    print("username: ", lname)

    country = ru.userReturnCountry(elText , plText)
    print("country:" , country)

    city = ru.userReturnCity(elText , plText)
    print("city:" , city)


    institutee = ru.userReturnInstitute(elText , plText)
    print("Institute is:" , institutee)


    regnumber = ru.userReturnRegistrationNum(elText , plText)
    print("registration number" , regnumber)

    degree = ru.userReturnDegree(elText , plText)
    print("degree is:" , degree)

    Session = ru.userReturnSession(elText , plText)
    print("session is " , Session)


    availTo = ru.Availtime_to(elText , plText)
    print("availTo" , availTo)

    availFrom = ru.Availtime_from (elText , plText)
    print("availFrom " , availFrom)

    desigination = ru.rank_teacher(elText , plText)
    print("desigination" , desigination)


    gloVar = fname + " " +lname
    print("full Name"  , gloVar)
    contact=ru.userReturnContactNumber(elText , plText)
    print("contact number: ", contact)

    error = None
    if request.method == 'POST':
        if ahoVar is None and  aho4Var is None:
            error = "Invalid Credentials Please Try again"
        else:
            return redirect('http://localhost:5000/dash')
    return render_template('loginO.html' , error = error)


    return render_template("loginO.html")
 
 #SHOW PROFILE OF USER   
@app.route('/profile' , methods = ['GET' , 'POST'])
def high_property():
    meetToday=[]
    meetToday=TodayMeetings(gloVar)
    lenToday = len(meetToday)
    print(lenToday ,  "todayLenght")

    if(meetToday == ""):
        print("list is Today"  , meetToday)
    return render_template("profile.html" ,  gloVar= gloVar  , lenToday = lenToday, ahoVar = ahoVar , aho4Var =aho4Var , contact = contact , fname = fname , lname = lname , typpOf = typpOf , city = city , country =country , institutee = institutee , desigination = desigination , regnumber = regnumber , degree = degree , Session = Session , availTo = availTo , availFrom = availFrom)

#CALL FOR PROFILE EDIT PAGE
@app.route('/eprofile' , methods = ['GET']  )
def edit_member():
    print("edit 1 called")
    meetToday=[]
    meetToday=TodayMeetings(gloVar)
    lenToday = len(meetToday)
    print(lenToday ,  "todayLenght")

    if(meetToday == ""):
        print("list is Today"  , meetToday)
    return render_template("editprofile.html", lenToday =lenToday , gloVar= gloVar , ahoVar = ahoVar , aho4Var =aho4Var , contact = contact , fname = fname  , lname = lname , typpOf = typpOf , city = city , country =country , institutee = institutee , desigination = desigination , regnumber = regnumber , degree = degree , Session = Session , availTo = availTo , availFrom = availFrom)

#CALL FOR PROFILE EDIT OF USER
@app.route('/eprofile' ,  methods=['GET' , 'POST'])
def login_edit_1():
    print("edit main caled")
    fiText = request.form['edit_fname']
    lnText = request.form['edit_lname']
    elText = request.form ['email_edit']
    plText = request.form['Password']
    ccText = request.form['contact']
    TText = request.form['typo']
    meetToday=[]
    meetToday=TodayMeetings(gloVar)
    lenToday = len(meetToday)
    print(lenToday ,  "todayLenght")
    if(meetToday == ""):
        print("list is Today"  , meetToday)
    print(fiText , lnText , TText , ccText , elText , plText)
    register_user.editProfile(fiText , lnText , TText , ccText , elText , plText )

    return render_template("editprofile.html" , lenToday = lenToday)





#CALL FOR RUN A FLASK WEB
if __name__ == '__main__':
    app.run(debug=True)  