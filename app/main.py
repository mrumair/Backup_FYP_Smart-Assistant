from flask import Flask , render_template , request 
from neo4jrestclient.client import GraphDatabase
from flask_bootstrap import Bootstrap
from model import post
from model import BotBehaviour
from model import *
from spacy1122 import *
from infer_fnc import *
from infer_fnc import inferencing

db = GraphDatabase("http://localhost:11012", username="neo4j", password="neo4j")
app = Flask(__name__ , template_folder='template')

Bootstrap(app)
ip = []
osystem = []
@app.route('/') 
def index():    
	return  render_template('index.html')

global flagBit4
textspacy = text_spacy()



# @app.route('/' , methods = ['GET' , 'POST'])
# def openLogin():
# 	return render_template("index.html", showVar = showVar)


@app.route('/' ,  methods=['GET' , 'POST'])
def myForm():
	#return render_template('index.html')
	text_Show = "Hello EveryOne! "
	text = request.form['text_store']
	textspacy.function_spacy(text)
	cBit6 = textspacy.foo()
	text_Edit = text
	ctempTime6 = textspacy.fooList()
	for i in range(0, len(ctempTime6)):
		print("Time inferencing values : ", ctempTime6[i])
	print("Value of cBit6: ",cBit6)
	#cBit6 = post.checkBit()
	if (cBit6==1):
		tempS = "Please Enter Venue of Meeting!"
		tempPrompt = "Where u Want to Meet?"


	# elif (cBit6 == 22):
	# 	tempS = "Please Enter the Object of Meeting!"
	# 	print ("Object missing")
	# elif (cBit6 == 2):
	# 	tempS = "Please Enter the Subject of Meeting!"
	# 	print( "subjetc Missing")

	elif (cBit6 == 7):
		tempS = "Please Enter the Time of Meeting!"
		tempPrompt = "When u want to Meet?"
	elif(cBit6 == 4):
		tempS = "Please Enter the Time and Venue of Meeting!"
		tempPrompt = "When and Where u Want to Meet?"
	# elif(cBit6 == 9):
	# 	tempS = "Please All the Time and Venue of Meeting!"
	else :
		tempS = "Complete Information! Your information has been saved!!"
		tempPrompt = "Great! Your Meeting has been Successfully Scheduled!"
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
	# 	contents =f.read()
	# 	print("Readed Data", contents)
	# 	# print("You Print",contents[i])



	textSystem = tempPrompt 
	# osystem.append(textSystem)
	# print (osystem)
	# for i in range (0, len(osystem)):
	# 	print("Value of System Prompt" , osystem[i])

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

	

	return render_template("index.html", respVar = respVar , showText = showText  , ctempTime6 = ctempTime6 , ip = ip )
#	return render_template('index.html')

@app.route('/res')
def myForm2():
	
	return render_template("newStore.html")
		#return render_template('index.html')
		



# @app.route('/')
# def result():
	#cBit5 = post.function_spacy()



# def myFormPrompt():
# 	#return render_template('index.html')
# 	text = request.form['text_store_Prompt']
# 	textspacy.function_spacy(text)
# 	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)  