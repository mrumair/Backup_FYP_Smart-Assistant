from neo4jrestclient.client import GraphDatabase
from py2neo.cypher import cypher_escape
from py2neo import Graph, Node, Relationship
from neo4jrestclient import client

graph = Graph("http://localhost:11002", username="neo4j", password="neo4j")

#CLASS FOR USER REGISTRATION
class register_user:
	def __init__(self):
		self.tempNameStore = ""
		

		#FUNCTION TO REGISTER A TEACHER
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




		#FUNCTION TO REGISTER A STUDENT
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



		#RETURN EMAIL OF A REGISTERED USER
	def userReturnEmail(self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Email'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Email"])
			return tempNameStore



	#RETURN PASSWORD OF A REGISTERED USER
	def userReturnPass(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Password'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Password"])
			return tempNameStore



	#RETURN FIRSTNAME OF A REGISTERED USER
	def userReturnName(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.firstName '
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.firstName"])
			return tempNameStore


	#RETURN LAST NAME OF A REGISTERED USER
	def userReturnLastName(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN  n.lastName'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.lastName"])
			return tempNameStore

	#RETURN CONTACT NUMBER OF A REGISTERED USER
	def userReturnContactNumber(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Tel'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Tel"])
			return tempNameStore


	#RETURN USER TYPE OF A REGISTERED USER
	def userReturnType(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Type'
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Type"])
			return tempNameStore



	def userReturnCity(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN  n.City '
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.City"])
			return tempNameStore


	def userReturnCountry(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Country '
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Country"])
			return tempNameStore



	def userReturnInstitute(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Institute '
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Institute"])
			return tempNameStore



	def userReturnSession(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Session '
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Session"])
			return tempNameStore


	def userReturnDegree(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Degree '
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Degree"])
			return tempNameStore


	def userReturnRegistrationNum(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Registration_Number '
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Registration_Number"])
			return tempNameStore



	def Availtime_to(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.to_Time '
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.to_Time"])
			return tempNameStore


	def Availtime_from(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.from_Time '
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.from_Time"])
			return tempNameStore



	def rank_teacher(  self ,email, passw):
		semail = email
		spassw = passw
		tempQuery = 'Match (n:SignUp {Email: {remail} , Password :{rpassw} } ) RETURN n.Desigination '
		postVar = graph.run(tempQuery, remail = semail, rpassw = spassw).data()
		for r in postVar:
			global tempNameStore
			tempNameStore=(postVar[0]["n.Desigination"])
			return tempNameStore



#FUNCTION TO EDIT PROFILE
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

			