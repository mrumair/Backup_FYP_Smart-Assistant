from neo4jrestclient.client import GraphDatabase
from py2neo.cypher import cypher_escape
#from neo4j.v1 import GraphDatabase
#from py2neo import Node
#from py2neo import cypher
#import neo4jupyter
#import jgraph
from py2neo import Graph, Node, Relationship
from neo4jrestclient import client
#from pandas import DataFrame

graph = Graph("http://localhost:11012", username="neo4j", password="neo4j")

# cBit2=3

class register_user:
	def __init__(self):
		#relationpropertydate = ""
		self.tempNameStore = ""

	def createUser(uname , fname , lname , email, passw, num , typo):
		suname = uname 
		sfname = fname
		slname = lname
		semail = email
		spassw = passw
		snum = num
		stypo = typo
		query= 'MERGE (n:SignUp {userName :{runame} , firstName:{rfname} ,lastName:{rlname} , Email: {remail} , Password :{rpassw} , Tel : {rnum}, Type : {rtype}}) RETURN n.userName' 
		post=graph.run(query,runame =suname , rfname = sfname  , rlname = slname , remail = semail , rpassw = spassw , rnum = snum , rtype = stypo  ) 
		print("register successfully!")
		print(post.data())





	def userReturnEmail(self ,email, passw):
		semail = email
		spassw = passw
		#tempQuery = 'start n=node(*) where n.Email:{remail} and n.Password:{rpassw} return n'
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Email'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		#print("Node returned: ", postVar[])

		

		for r in postVar:
			global tempNameStore
			
			tempNameStore=(postVar[0]["n.Email"])
			return tempNameStore



	def userReturnPass(  self ,email, passw):
		semail = email
		spassw = passw
		#tempQuery = 'start n=node(*) where n.Email:{remail} and n.Password:{rpassw} return n'
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Password'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		#print("Node returned: ", postVar[])
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Password"])
			return tempNameStore




	def userReturnName(  self ,email, passw):
		semail = email
		spassw = passw
		#tempQuery = 'start n=node(*) where n.Email:{remail} and n.Password:{rpassw} return n'
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.firstName , n.lastName'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		#print("Node returned: ", postVar[])
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.firstName"])
			# tempNameStore2 = (postVar[0]["n.lastName"])

			return tempNameStore


	def userReturnLastName(  self ,email, passw):
		semail = email
		spassw = passw
		#tempQuery = 'start n=node(*) where n.Email:{remail} and n.Password:{rpassw} return n'
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN  n.lastName'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		#print("Node returned: ", postVar[])
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.lastName"])
			# tempNameStore2 = (postVar[0]["n.lastName"])

			return tempNameStore


	def userReturnContactNumber(  self ,email, passw):
		semail = email
		spassw = passw
		#tempQuery = 'start n=node(*) where n.Email:{remail} and n.Password:{rpassw} return n'
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Tel'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		#print("Node returned: ", postVar[])
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Tel"])
			# tempNameStore2 = (postVar[0]["n.lastName"])

			return tempNameStore


	def userReturnType(  self ,email, passw):
		semail = email
		spassw = passw
		#tempQuery = 'start n=node(*) where n.Email:{remail} and n.Password:{rpassw} return n'
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Type'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		#print("Node returned: ", postVar[])
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Type"])
			# tempNameStore2 = (postVar[0]["n.lastName"])

			return tempNameStore





			