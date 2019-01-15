from flask import Flask , render_template , request 
from neo4jrestclient.client import GraphDatabase
from flask_bootstrap import Bootstrap
import spacy
from model import post
from spacy1122 import *
db = GraphDatabase("http://localhost:11002", username="neo4j", password="neo4j")
app = Flask(__name__, template_folder='template')
Bootstrap(app)
@app.route('/') 
def index():
	return app.send_static_file('index.html')

@app.route('/' ,  methods=['GET' , 'POST'])
def myForm():
		text = request.form['text']
		testClass.splitSentence(text)
		return app.send_static_file('index.html')
if __name__ == '__main__':
	app.run(debug=True) 