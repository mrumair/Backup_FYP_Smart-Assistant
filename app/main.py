from flask import Flask , render_template , request 
from neo4jrestclient.client import GraphDatabase
from flask_bootstrap import Bootstrap
from model import post
from model import BotBehaviour
from model import *
from spacy1122 import *
db = GraphDatabase("http://localhost:11012", username="neo4j", password="neo4j")
app = Flask(__name__ , template_folder='template')

Bootstrap(app)
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
	print("Value of cBit6: ",cBit6)
	#cBit6 = post.checkBit()
	if (cBit6==1):
		tempS = "Please Enter Venue of Meeting!"

	# elif (cBit6 == 22):
	# 	tempS = "Please Enter the Object of Meeting!"
	# 	print ("Object missing")
	# elif (cBit6 == 2):
	# 	tempS = "Please Enter the Subject of Meeting!"
	# 	print( "subjetc Missing")

	elif (cBit6 == 7):
		tempS = "Please Enter the Time of Meeting!"
	elif(cBit6 == 4):
		tempS = "Please Enter the Time and Venue of Meeting!"
	# elif(cBit6 == 9):
	# 	tempS = "Please All the Time and Venue of Meeting!"
	else :
		tempS = "Complete Information! Your information has been saved!!"
		text  =""


	#prompting....




	respVar = tempS
	text_Show = text
	showText = text_Show
	return render_template("index.html", respVar = respVar , showText = showText )
#	return render_template('index.html')

@app.route('/show')
def myForm2():
	showVar = show
	return render_template("index.html", showVar = showVar)
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