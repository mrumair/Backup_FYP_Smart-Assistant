from flask import Flask , render_template , request  , redirect , Response
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
import json
import urllib

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
    # tempSub = request.form['subName']
    #print("subject: ", tempSub)
    meetTemp=[]
    meetTemp=meet_list(gloVar, "meeting")

    if(meetTemp == ""):
        print("list is"  , meetTemp)

    #print("printing hahahah")
    # for i in range(len(meetTemp)):
    #   print("M: ", meetTemp[i])
    return render_template('meetings.html', meetTemp=meetTemp , gloVar = gloVar)


global flagBit4
textspacy = text_spacy()



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

    # cBit9 = textspacy.foos()
    # print ("Value of cBit9 " , cBit9)
    #cBit6 = post.checkBit()
  #cBit6 = post.checkBit()
    if (cBit6==1):
        tempS = "Please Enter Venue of Meeting!"
        tempPrompt = "WHERE you want to meet?"


    # elif (cBit6 == 22):
    #   tempS = "Please Enter the Object of Meeting!"
    #   print ("Object missing")
    # elif (cBit6 == 2):
    #   tempS = "Please Enter the Subject of Meeting!"
    #   print( "subjetc Missing")

    elif (cBit6 == 7):
        tempS = "Please Enter the Time of Meeting!"
        tempPrompt = "WHEN you want to meet?"

    elif (cBit6 == 11):
        tempS = "Please Enter the Date of Meeting!"
        tempPrompt = "WHEN you want to meet?"


    elif(cBit6 == 4):
        tempS = "Please Enter the Time and Venue of Meeting!"
        tempPrompt = "WHEN and WHERE you want to meet?"

    elif(cBit6 == 44):
        tempS = "Please Enter the Time and Date of Meeting!"
        tempPrompt = "WHEN you want to meet?"

    elif(cBit6 == 444):
        tempS = "Please Enter the Venue and Date of Meeting!"
        tempPrompt = "WHERE and WHEN you want to meet?"

    elif(cBit6 == 333):
        tempS = "Please Enter the Time, Venue and Date of Meeting!"
        tempPrompt = "WHEN and WHERE you want to meet?"
    # elif(cBit6 == 9):
    #   tempS = "Please All the Time and Venue of Meeting!"
    elif(cBit6 == 000):
        tempS = "Complete Information! Your information has been saved!!"
        tempPrompt = "Great! Your Meeting has been Successfully SCHEDULED!!"
        text_Edit = ""


    #prompting....



    respVar = tempS
    text_Show = text_Edit
    showText = text_Show
    # f= open("MyInput.txt","a+")
    # f.write("\n"+ (text_Show ))
    # # ("This is line %d\r\n" % (i+1))
    # f.close() 

    # f=open("MyInput.txt", "r")
    # if f.mode == 'r':
    #   contents =f.read()
    #   print("Readed Data", contents)
    #   # print("You Print",contents[i])



    textSystem = tempPrompt 
    # osystem.append(textSystem)
    # print (osystem)
    # for i in range (0, len(osystem)):
    #   print("Value of System Prompt" , osystem[i])

    # tempBack = contents
    # print("BackUp" ,tempBack)
    # for i in range(0, len(contents)):
    #blank list
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

@app.route('/reg')
def indexRegister():
    return render_template("signupO.html")

@app.route('/reg' ,  methods=['GET' , 'POST'])
def Register_form():


    # if request.method == 'GET': 
    uText = request.form['uname']
    # uText = request.form['uname']
    fText = request.form['fname']
    lText = request.form['lname']
    pText = request.form ['password']
    eText = request.form ['email']
    nText = request.form ['pnumber']
    register_user.createUser(uText , fText , lText , eText , pText , nText , "student" )
    print ("student Register")
        # tText = request.form ['']


    # elText = request.form ['login_email']
    # plText = request.form['login_pass']



    # ahoVar=userReturnEmail(elText , plText)
    # print("Name: ", ahoVar)


    # aho4Var=userReturnPass(elText , plText)
    # print("Password: ", aho4Var)

    


    # lForm = request.form['login_form']

    # # uText = request.form['uname']
    # pForm = request.form['login_pass']
    

    # data = register_user.userLogin(lForm , pForm) 
    # print ("student Register" , data)

    return render_template("signupO.html")
    
        #return render_template('index.html')
        


# @app.route('/signin')
# def indexlogin():
#   return render_template("form2.html")

# @app.route('/signin' ,  methods=['GET' , 'POST'])
# def index_login():


#   lForm = request.form['login_form']

#   # uText = request.form['uname']
#   pForm = request.form['login_pass']
    

#   data = register_user.userLogin(lForm , pForm) 
#   print ("student Register" , data)
#   # tText = request.form ['']


#   # lForm = request.form['login_form']

#   # # uText = request.form['uname']
#   # pForm = request.form['login_pass']
    

#   # data = register_user.userLogin(lForm , pForm) 
#   # print ("student Register" , data)

#   return render_template("form2.html")




# @app.route('/')
# def result():
    #cBit5 = post.function_spacy()



# def myFormPrompt():
#   #return render_template('index.html')
#   text = request.form['text_store_Prompt']
#   textspacy.function_spacy(text)
#   return render_template('index.html')


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


 # 'admin' or request.form['login_pass'] != 'admin'
    error = None
    if request.method == 'POST':
        if ahoVar is None and  aho4Var is None:
            error = "Invalid Credentials Please Try again"
        else:
            return redirect('http://localhost:5000/dash')
    return render_template('loginO.html' , error = error)

  


    # lForm = request.form['login_form']

    # # uText = request.form['uname']
    # pForm = request.form['login_pass']
    

    # data = register_user.userLogin(lForm , pForm) 
    # print ("student Register" , data)

    return render_template("loginO.html")


@app.route('/profile')
def high_property():
    return render_template("profile.html" ,  gloVar= gloVar , ahoVar = ahoVar , aho4Var =aho4Var , contact = contact , lname = lname , typpOf = typpOf)




if __name__ == '__main__':
    app.run(debug=True)  