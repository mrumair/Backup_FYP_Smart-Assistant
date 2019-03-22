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

graph = Graph("http://localhost:11005", username="neo4j", password="neo4j")

# cBit2=3

class register_user:
	def __init__(self):
		#relationpropertydate = ""
		self.tempNameStore = ""
	def createTeacher(fname , lname , country , Institute , desigination  , city  ,email, passw, num , typo , ftime , ttime ):
		tfname = fname
		tlname = lname
		temail = email
		tcountry =  country
		tinst = Institute
		tdeg = desigination 
		tcity = city
		tpassw = passw
		tnum = num
		ttypo = typo
		tftime = ftime
		tttime = ttime
		query= 'MERGE (n:SignUp { firstName:{rfname} ,lastName:{rlname} ,Country:{rcounty} ,Institute:{rinst} ,Desigination:{rdeg} , City:{rcity}  ,   Email: {remail} , Password :{rpassw} , Tel : {rnum}, Type : {rtype}  , from_Time : {rftime}  , to_Time : {rttime} }) RETURN n.userName' 
		post=graph.run(query, rfname = tfname  , rlname = tlname  , rcounty = tcountry , rinst = tinst, rdeg = tdeg, rcity = tcity   , remail = temail , rpassw = tpassw , rnum = tnum , rtype = ttypo  , rftime = tftime , rttime = tttime ) 
		print("register successfully!")
		print(post.data())

	def createStudent(fname , lname , country , Institute   , city , regNumber ,email, passw, num , typo , session , degree , serialnum  ):
		tfname = fname
		tlname = lname
		temail = email

		tcountry =  country
		tinst = Institute
	
		tcity = city
		tregNo = regNumber
		tpassw = passw
		tnum = num
		ttypo = typo
	
		query= 'MERGE (n:SignUp { firstName:{rfname} ,lastName:{rlname} ,Country:{rcounty} ,Institute:{rinst}  , City:{rcity} ,Registration_Number:{rregNo} ,   Email: {remail} , Password :{rpassw} , Tel : {rnum}, Type : {rtype}  , Session :{rsession} , Degree: {rdegree} , SerialNumber : {rserialnum}}) RETURN n.userName' 
		post=graph.run(query, rfname = tfname  , rlname = tlname  , rcounty = tcountry , rinst = tinst,  rcity = tcity  , rregNo = tregNo , rsession = session , rdegree = degree , rserialnum = serialnum, remail = temail , rpassw = tpassw , rnum = tnum , rtype = ttypo   , ) 
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


	def editProfile(fname , lname , typee , num , email , passw  ):

		sfname = fname
		slname = lname
		stypee = typee
		semail = email
		snum = num
		spassw = passw


		query= 'MERGE (n:SignUp {firstName: {rfname} , lastName:{rlname} ,Type:{rtype}}) SET n.Tel = {rnum}, n.Password = {rpassw} , n.Email = {remail} RETURN n' 
		post=graph.run(query, rfname = sfname  , rlname = slname  , rtype = stypee , rnum= snum , rpassw = spassw , remail = email) 
		print("Updated successfully!")
		print(post.data())



register_user.editProfile('Sana' , 'Razzaq' , 'student' , '080810' , 'ejjkajk', '1223')







			