from neo4jrestclient.client import GraphDatabase
from py2neo.cypher import cypher_escape
#from neo4j.v1 import GraphDatabase
#from py2neo import Node
#from py2neo import cypher
#import neo4jupyter
#import jgraph
import time
import datetime
from py2neo import Graph, Node, Relationship
from neo4jrestclient import client
from datetime import datetime
from dateutil import parser

#from pandas import DataFrame

graph = Graph("http://localhost:11012", username="neo4j", password="neo4j")

#global flagBit
#flagBit = 0

class post:

  def createNodeQueru(subjects , propertys):
    node = subjects
    type_s = propertys
    query= 'MERGE (n:UserMeeting {name:{sname} , type: {type}}) RETURN n.name' 
    post=graph.run(query,sname=node , type = propertys ) 
    print("node creates") 
    print(post.data())
    
    #neo4jupyter.draw(graph_object_py2neo, {"Nodes_type": "Att"})
    #DataFrame(graph.data("MATCH (a) RETURN a.name"))d
  def createqueryrelation(subjct , objct , relation , propTime , propVenue , propDate):
    sub = subjct
    obj = objct
    rel_type = relation
    Time_prop = propTime
    Venue_prop = propVenue
    date_prop = propDate
    query =  'MERGE (u1:UserMeeting { name: {subs} }) MERGE (u2:UserMeeting { name:{objs} }) MERGE (u1)-[:meet {name: {rel} , time:{timep} , venue:{venuep} , date :{datep}}]-(u2)'
    # MERGE (user:UserMeeting {name:"Jane"}) MERGE (friend:UserMeeting {name:"John"}) MERGE (user)-[r:KNOWS]->(friend)
    # query = 'MERGE (u:UserMeeting{name :{subs}}) MERGE(r:UserMeeting{name:{objs}}) MERGE   (u)-[n:meet{name :{rel} ,time:{timep}, venue :{venuep} }]->(r)'
    post = graph.run (query, subs = sub , objs = obj , rel = rel_type  , timep = Time_prop , venuep = Venue_prop , datep = date_prop )
    print ("relation created")
    print (post.data())


  def setProperty(labeln , propertyn):
    lab= labeln
    prop=propertyn
    query = 'MERGE (n:UserMeeting{name :{labs}}) set n.name = {pros}'
    post = graph.run(query, labs=lab , pros = propo)
    print ("Updating")
    print(post.data())

  def relationTime(subject ,relation , Time):
    sub = subject
    rel = relation
    time = Time
    query = 'MATCH (a:UserMeeting{name : {subs}})-[r:meet{name:{rels}}]->() set r.Time = {tim} RETURN r.Time, r.Date_is , r.Venue_is'
    post = graph.run(query , subs = sub , rels = rel  , tim = time)
    print ("time updated")
    print(post.data())

  def relationDate(subject ,relation , Date):
    sub = subject
    rel = relation
    date = Date
    query = 'MATCH (a:UserMeeting{name : {subs}})-[r:meet{name:{rels}}]->() set r.Date_is = {tim} RETURN r.Time, r.Date_is , r.Venue_is'
    post = graph.run(query , subs = sub , rels = rel  , tim = date)
    print ("date updated")
    print(post.data())


  def relationVenue(subject ,relation , Venue):
    sub = subject
    rel = relation
    venue = Venue
    query = 'MATCH (a:UserMeeting{name : {subs}})-[r:meet{name:{rels}}]->() set r.Venue = {tim} RETURN r.Time, r.Date_is , r.Venue_is'
    post = graph.run(query , subs = sub , rels = rel  , tim = venue)
    print ("time updated")
    print(post.data())


  def ObjectSelection(abc):
    listStoreVar = []

    name = abc
    
    print(name)
    #tempQuery = 'start n=node(*) where n.Email:{remail} and n.Password:{rpassw} return n'
    # tempQuery = 'match(n:SignUp) where n.firstName  ={namenew} return n'
    tempQuery = 'match(n:SignUp)  unwind n.firstName + " "+  n.lastName as uname with uname as fullname where fullname = {namenew} return fullname'
    postVar = graph.run(tempQuery , namenew = name ).data()
    print(postVar)
    if not postVar:
      print ("No data found")
      result = False
      print(result)
      
    else:
      print("Data found against")
      result = True
      print (result)

    return result

      # print (listStoreNew)



    # print (listStoreNew)
    

 


    # print("Node returned: ", postVar[])

    for r in postVar:
      global tempNameStore
      tempNameStore=(postVar[0]["n.firstName"])
      print ("list is " , tempNameStore)
      # tempNameStore2 = (postVar[0]["n.lastName"])

      return tempNameStore


# def validateInfo( institute , timep , subjectv, objectv):


  #definning functionss for validation
 




  def timeNew(DateVar):
    dBit = 0
    DateTime = DateVar

    now=datetime.now()
    print (now.month)
    print (now.day)
    print (now.year)
    print (str(now.month)+"/"+str(now.day)+"/"+str(now.year))


    dt = parser.parse(DateTime)
    new = dt.date()
    print(new) 
    print (str(new.month)+"/"+str(new.day)+"/"+str(new.year))

    print(new.year)
    print(now.year)

    if (new.year > now.year):
      dBit = 11
      print (dBit)
      print("you enter th correct date ")
    
    elif(new.year == now.year and new.month > now.month ):
      print ("Same Year but month should be greater")
      dBit = 22
      print (dBit)
    
    
    elif(new.year == now.year and new.month == now.month and new.day >= now.day):
        print ("Same year same month but date greates")
        dBit =33
        print (dBit)
    else:
      print ("you did not enter Correct day")
      print (dBit)
    return dBit




  def timeChecking(TimeVar):
    tBit = 0
    TempTime = TimeVar

    currentDT = datetime.now()
    print (currentDT)
    print ("Current Hour is: %d" % currentDT.hour)
    print ("Current Minute is: %d" % currentDT.minute)
    print("Input Time:" , TempTime)
    b=time.strptime(TempTime,'%H:%M')
    print("time is " , b.tm_hour)
    print("time mints is " , b.tm_min )

    if (  b.tm_hour > currentDT.hour):
      tBit = 11 
      print (tBit)
      print("you enter th correct hour")
    
    elif( b.tm_hour  == currentDT.hour and  b.tm_min  > currentDT.minute ):
      print ("Same Hour but mint should be greater")
      tBit = 22
      print (tBit)
    

    else:
      print ("you did not enter Correct Hour")
      print (tBit)
    return tBit





  def validateInfo( institute , timep , date , objectv):
    cBit=0
    if (institute==""):
      #listStore3 = "Please Enter complete Information"
      cBit=1

    if (timep == ""):
      cBit = 7 

    if (date == ""):
      cBit = 11

    if (objectv == ""):
      cBit = 111


    # if (subjectv == ""):
    #   cBit = 2

    # if(objectv =="" ):
    #   cBit = 22

    if (institute =="" and timep == "" ):
      cBit = 4

    if (date =="" and timep == ""):
      cBit = 44

    if (date =="" and institute == ""):
      cBit = 444

    if (date =="" and institute == "" and timep == ""):
      cBit = 333
    if (date =="" and institute == "" and timep == "" and objectv == ""):
      cBit = 666
    if (date !="" and institute != "" and timep != "" and objectv!= ""):
      cBit = 000

    return cBit
  def check(person,institute,time,date):
    cBit=0
    if (person != "" and institute == "" and time == "" and date == ""):
      cBit = 100
    if (person == "" and institute == "" and time != "" and date == ""):
      cBit = 101 
    if (person != "" and institute == "" and time != "" and date == ""):
      cBit = 102
    if (person != "" and institute == "" and time == "" and date != ""):
      cBit = 103
    if (person == "" and institute == "" and time == "" and date != ""):
      cBit = 104
    if (person == "" and institute != "" and time == "" and date == ""):
      cBit = 105
    if (person != "" and institute != "" and time == "" and date == ""):
      cBit = 106

    return cBit

  def checkwhen(person,institute):
    cBit=0
    if (person != "" and institute == ""):
      cBit = 200
    if (person != "" and institute != ""):
      cBit = 201 

    return cBit

  def checkwhatloc(person,time, date, institute):
    cBit=0
    if (person != "" and institute == "" and time == "" and date == ""):
      cBit = 400
    if (person != "" and institute != "" and time == "" and date == ""):
      cBit = 201 

    return cBit

  def checkwhattime(person,time, date, institute):
    cBit=0
    if (person != "" and institute == "" and time == "" and date == ""):
      cBit = 500
    if (person != "" and institute != "" and time == "" and date == ""):
      cBit = 201 

    return cBit

  def checkwhere(person,time):
    cBit=0
    if (person != "" and time == ""):
      cBit = 300
    if (person != "" and time != ""):
      cBit = 301 

    return cBit




  # def checkBit()
  #   if 
      

   
  # def validateSubObj( subjectv , objectv):
  #   cBits = 0
  #   if(subjectv == ""):
  #     cBits = 1
  #   if(objectv == ""):
  #     cBits =2
  #   return cBits









    #def functiona(subjct):
    # label_of_node = subjct
    # with db.session() as session:
   # nodecreate = session.run("CREATE (n:new{name : %s) return n")
      #with db.session() as graph_session:
      #db.session().run(nodecreate)
        #global u1
        #u1 = db.nodes.create(name =subjct , position = property)
        #user.add(u1)
         
       # u2 = db.nodes.create(name=objct)
       # user.add(u2) 
        #u1.relationships.create("", u2)
    #def relationa(subject,objectc,relation):
      #cqlNodeQuery = "MATCH(x:label12) where x.name = 'subject' RETURN x"
      #with db.session() as graphDB_Session:
       #     nodes = graphDB_Session.run(cqlNodeQuery)
        #    for node in nodes:
#                print(node)

#MERGE (n:label {name:'6', type: 'digits' })MERGE (test2:label {name:'8'})MERGE (n)-[:how {r:'123'}]->(test2)
# create relationship between two existing node
#MATCH (u:label {name:'abc'}), (r:label {name:'xyz'}) CREATE (u)-[:HAS_ROLE]->(r)
# search and set property
# MERGE (n:label {name: 'abc'})
# SET n.age = 34, n.coat = 'Yellow'
# RETURN n
  def createNode(sub,obj,rel, relp1, relp2, relp3, propertys, propertyo):
    user = db.labels.create("Person")
    u1= db.nodes.create(name = sub, position = propertys)
    user.add(u1)
    u2 = db.nodes.create(name = obj , position = propertyo)
    user.add(u2)
    u1.relationships.create(rel ,u2 , Time = relp1 , Date_is = relp2 , Venue_is = relp3)
    return None

# class BoatBahviour:
#   def askQ(self):
#     q= 'MATCH (n:Follow) WHERE NOT (n)--() RETURN n'
#     results = db.query(q, returns=(client.Node))
#     if q == "":
#       print("You are good to go!")
#     else:
#       for r in results:
#         print("What is %s ?" % (r[0]["name"]))

# b=BoatBahviour()
# b.askQ()
# class BotBehaviour:

#   def askQ(self):
#     listStore = list()
#     namea = "Umair"
#     query= 'MATCH (n:Person) WHERE NOT (n)--()  and n.name = {snhd} RETURN n '
#     results = graph.run(query , snhd = namea) 
#     if query == "":
#       print("You are good to go!")
#     else:
#       for r in results:
#         #print("Who is %s ?" % (r[0]["name"]))
#         listStore.append("Who is %s ?" % (r[0]["name"]))
#     return listStore

#   def showNode(self):
#     listStore2 = list()
#     namea = "Umair"
#     query= 'MATCH (n:Person) Where n.name = {snhd} RETURN n'
#     results = graph.run(query , snhd = namea)
#     if query == "":
#       print("You are good to go!")
#     else:
#       for r in results:
#         #print("Who is %s ?" % (r[0]["name"]))
#         listStore2.append("Who is %s ?" % (r[0]["name"]))
#     return listStore2


class BotBehaviour:
  def askQ(self):
    listStore = list()
    aName = ""
    tempStore = ""
    tempStoreN = ""
    tempStoreT = ""
    tempStoreV = ""
    aTime = ""
    aVenue = ""
    #print("starting of the function")

    q= 'MATCH (n:UserMeeting) WHERE NOT (n)--() RETURN n'
    results=graph.run(q)
    print("Result:", list(results))

    print("Resulting Node: ", list(results)[name]) 
    #results = graph.query(q, returns=(client.Node))
    for r in list(results):
      tempStore = list(results)

    print("Temp:", tempStore)

    if tempStore != "":
      print("found the empty node")
      for r in results:
        listStore.append("Who is %s ?" % (r[0]["name"]))
    else:
      print("not found the empty node")

      a= 'start n=node(*) match (n:UserMeeting)-[r:meet]-(:UserMeeting) where exists(r.venue) return r'
      #resultV = graph.query(a, returns=(client.Relationship))

      b= 'start n=node(*) match (n:UserMeeting)-[r:meet]-(:UserMeeting) where exists(r.time) return r'
      #resultT = graph.query(b, returns=(client.Relationship))

      c= 'start n=node(*) match (n:UserMeeting)-[r:meet]-(:UserMeeting) where exists(r.name) return r'
      #resultN = graph.query(c, returns=(client.Relationship))
      
      # for r in resultV:
      #   tempStoreV = (r[0]["name"])

      # for r in resultT:
      #   tempStoreT = (r[0]["name"])

      # for r in resultN:
      #   tempStoreN = (r[0]["name"])

      # if((tempStoreN!="") and (tempStoreT!="") and (tempStoreV!="")):
      #   listStore.append("Everything is Okay")
      # else:
      #   listStore.append("Please Enter complete information")
    return listStore


        #print("Test Output is:"+r[0]["name"])
      #print("tempStoreN is:"+tempStoreN)


      #aTime= 'MATCH (n)-[r:meet]->() RETURN r.time'
      #aVenue= 'MATCH (n)-[r:meet]->() RETURN r.venue'
      #print("Testing:"+resultN)
      # if (tempStoreN !=""):
      #   listStore.append("All is fine")
      # else:
      #   listStore.append("PLease enter complete information")
      #results = graph.query(aRel, returns=(client.Node))



       # p = Pypher()
        #p.MATCH.node('u', labels=).RETURN.u
        #query.relationships.create(relation,objectc)
      #  p='MATCH (u:label12)-[r:likes]->(m:label12) WHERE u.name="Rabeeya Saleem" RETURN u, type(r), m'
       # q = 'MATCH (u:label12 {name:'subject'}), (r:label12 {name:'objectc'}) CREATE (u)-[b:relation]->(r)'
        #results = db.query(p, returns=(client.Node, str, client.Node))
        #for r in results:
        #print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
# The output:
# (Marco)-[likes]->(Punk IPA)
# (Marco)-[likes]->(Hoegaarden Rosee)

        #subject.relationships.create(relation,objectc,Time=time,Date=date,Venue=venue)
        #return None
tempVar = "Rabeeya Saleem"
post.ObjectSelection(tempVar)
post.timeNew("18 March 2019")
post.timeChecking("20:09")