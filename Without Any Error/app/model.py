#IN MODEL.PY DATA STORE TO DATABASE AND INPUT VALUE IS TO BE VALIDATE
#2015-CS-05
#2015-CS-160
#2015-CS-161
from neo4jrestclient.client import GraphDatabase
from py2neo.cypher import cypher_escape
import time
import datetime
from py2neo import Graph, Node, Relationship
from neo4jrestclient import client
from datetime import datetime
from dateutil import parser



graph = Graph("http://localhost:11005", username="neo4j", password="neo4j")


class post:

  def RetrAgenda():
    listStoreAg = list()
    #queryNode = 'MATCH (n:UserMeeting) WHERE (n)--() RETURN n'
    queryNode = 'start n=node(*) match (n:MeetingRecord{type:"Agenda"})-[:has]-() return distinct n'
    results = graph.run(queryNode)

    for r in results:
      listStoreAg.append(r[0]["name"])

    return listStoreAg


  def RetrMembers():
    listStoreAg = list()
    #queryNode = 'MATCH (n:MeetingRecord) WHERE (n)--() RETURN n'
    queryNode = 'start n=node(*) match (n:SignUp) return n.firstName+" "+n.lastName'
    results = graph.run(queryNode)

    # print("PRINTING MEMS........................................................")
    # for u in results:
    #   print("mems are: ",u)

    for r in results:
      listStoreAg.append(r[0])

    return listStoreAg


  def RetrAgendaId(name):
    listStoreAg = list()
    fypName = name
    agenda_Text = "Agenda"
    #queryNode = 'MATCH (n:UserMeeting) WHERE (n)--() RETURN n'
    queryNode = 'start n=node(*) match (n:MeetingRecord{name:{fname},type:{agText} })-[:has]-() return n.agendaID'
    results = graph.run(queryNode, fname=fypName, agText=agenda_Text)

    for r in results:
      listStoreAg.append(r[0])

    return listStoreAg

    #a= 'start n=node(*) match (n:UserMeeting)-[r:meet]-(:UserMeeting) where exists(r.venue) return r'
      #resultV = graph.query(a, returns=(client.Relationship))
      #agName, "Agenda" agId,agTitle,agDetail,agNoOfMems,agSupervisor,agSecSupervisor,reg1, reg2, reg3, reg4
  def CreateNode_Ag(subjects , propertys, agendaId, agtitle, detail, noofmems, supervisor, secSupervisor, reg1, reg2, reg3, reg4):
    title = subjects
    nodeType = propertys
    tagendaId = agendaId
    ttitle = agtitle
    tdetail = detail
    tnoofmems = noofmems
    tsupervisor = supervisor
    tsecsupervisor = secSupervisor
    treg1 = reg1
    treg2 = reg2
    treg3 = reg3
    treg4 = reg4
    query= 'MERGE (n:MeetingRecord {name:{sname} , type: {type}, agendaID:{sagId}, title:{stitl}, detail: {sdetail}, noOfmems: {snoofmems}, supervisor:{ssupervisor}, secondSupervisor:{ssecsup}, memRegNo1:{srg1}, memRegNo2:{srg2}, memRegNo3:{srg3}, memRegNo4:{srg4} }) RETURN n.name' 
    post=graph.run(query,sname=title , type = nodeType , sagId=tagendaId, stitl=ttitle, sdetail=tdetail, snoofmems=tnoofmems,ssupervisor=tsupervisor, ssecsup=tsecsupervisor, srg1=treg1, srg2=treg2, srg3=treg3, srg4=treg4 ) 
    print("Node Created!!") 
    print(post.data())

  def CreateRelation_Ag(subjct , objct , relation):
    sub = subjct
    obj = objct
    rel_type = relation
    query =  'MERGE (u1:MeetingRecord { name: {subs} }) MERGE (u2:MeetingRecord { name:{objs} }) MERGE (u1)-[:has {name: {rel}}]-(u2)'
    # MERGE (user:UserMeeting {name:"Jane"}) MERGE (friend:UserMeeting {name:"John"}) MERGE (user)-[r:KNOWS]->(friend)
    # query = 'MERGE (u:UserMeeting{name :{subs}}) MERGE(r:UserMeeting{name:{objs}}) MERGE   (u)-[n:meet{name :{rel} ,time:{timep}, venue :{venuep} }]->(r)'
    post = graph.run (query, subs = sub , objs = obj , rel = rel_type )
    print ("Relation Created")
    print (post.data())

# Create Node Function
  def createNodeQueru(subjects , propertys):
    node = subjects
    type_s = propertys
    query= 'MERGE (n:MeetingRecord {name:{sname} , type: {type}}) RETURN n.name' 
    post=graph.run(query,sname=node , type = propertys ) 
    # print("node creates") 
    # print(post.data())
#create relationship in graph DB node 
  def createqueryrelation(subjct , objct , relation , propTime , propVenue , propDate):
    sub = subjct
    obj = objct
    rel_type = relation
    Time_prop = propTime
    Venue_prop = propVenue
    date_prop = propDate
    query =  'MERGE (u1:MeetingRecord { name: {subs} }) MERGE (u2:MeetingRecord { name:{objs} }) MERGE (u1)-[:meet {name: {rel} , time:{timep} , venue:{venuep} , date :{datep}}]-(u2)'
    post = graph.run (query, subs = sub , objs = obj , rel = rel_type  , timep = Time_prop , venuep = Venue_prop , datep = date_prop )
    # print ("relation created")
    # print (post.data())

#set Agenda_ID
  def setAgendaId(subject , relation , agenId, randNo):
    sub = subject
    rel = relation
    agenda_Id = agenId
    rand_No = randNo
    query = 'MATCH (a:MeetingRecord{name : {subs}})-[r:meet{randNo: {ranN}}]->() set r.agendaID = {agId} RETURN r.agendaID'
    post = graph.run(query , subs = sub ,  rels = rel  , agId = agenda_Id, ranN = rand_No)
    print ("time updated")
    print(post.data())


# get the list of object and match with userInput
  def ObjectSelection(input_name):
    listStoreVar = []

    name = input_name
    
    print(name)

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

    for r in postVar:
      global tempNameStore
      tempNameStore=(postVar[0]["n.firstName"])
      print ("list is " , tempNameStore)
      # tempNameStore2 = (postVar[0]["n.lastName"])

      return tempNameStore


#check time , date , venue and object name and return bit value
  def validateInfo( institute , timep , date , objectv):
    cBit=0
    if(objectv == "" and institute == "" and time == "" and date == ""):
      cBit = '0000'
    elif(objectv == "" and institute == "" and time == "" and date != ""):
      cBit = '0001'
    elif(objectv == "" and institute == "" and time != "" and date == ""):
      cBit = '0010'
    elif(objectv == "" and institute == "" and time != "" and date != ""):
      cBit = '0011'
    elif(objectv == "" and institute != "" and time == "" and date == ""):
      cBit = '0100'
    elif(objectv == "" and institute != "" and time == "" and date != ""):
      cBit = '0101'
    elif(objectv == "" and institute == "" and time != "" and date != ""):
      cBit = '0110'
    elif(objectv == "" and institute != "" and time != "" and date != ""):
      cBit = '0111'
    elif(objectv != "" and institute == "" and time == "" and date == ""):
      cBit = '1000'
    elif(objectv != "" and institute == "" and time == "" and date != ""):
      cBit = '1001'
    elif(objectv != "" and institute == "" and time != "" and date == ""):
      cBit = '1010'
    elif(objectv != "" and institute == "" and time != "" and date != ""):
      cBit = '1011'
    elif(objectv != "" and institute != "" and time == "" and date == ""):
      cBit = '1100'
    elif(objectv == "" and institute == "" and time == "" and date != ""):
      cBit = '1101'
    elif(objectv != "" and institute != "" and time != "" and date == ""):
      cBit = '1110'
    elif(objectv != "" and institute != "" and time != "" and date != ""):
      cBit = '0'

    return cBit

#CHeck the null attributes and return bit value accordingly.
  def checkDo(person, institute, time, date, title):
    cBit=0
    if (person != "" and institute == "" and time == "" and date == "" and title == ""):
      cBit = 100
    if (person == "" and institute == "" and time != "" and date == "" and title == ""):
      cBit = 101 
    if (person == "" and institute == "" and time == "" and date != "" and title == ""):
      cBit = 102
    if (person != "" and institute == "" and time == "" and date != "" and title == ""):
      cBit = 103
    if (person != "" and institute == "" and time != "" and date == "" and title == ""):
      cBit = 104
    if (person == "" and institute != "" and time == "" and date == "" and title == ""):
      cBit = 105
    if (person != "" and institute != "" and time == "" and date == "" and title == ""):
      cBit = 106
    if (person != "" and institute != "" and time != "" and date == "" and title == ""):
      cBit = 107
    if (person != "" and institute != "" and time == "" and date != "" and title == ""):
      cBit = 108
    if (person != "" and institute != "" and time != "" and date != "" and title == ""):
      cBit = 109
    if (person == "" and institute == "" and time != "" and date != "" and title == ""):
      cBit = 110
    if (person == "" and institute != "" and time != "" and date == "" and title == ""):
      cBit = 111
    if (person == "" and institute != "" and time == "" and date != "" and title == ""):
      cBit = 112
    if (person != "" and institute == "" and time != "" and date != "" and title == ""):
      cBit = 113
    if (person == "" and institute != "" and time != "" and date != "" and title == ""):
      cBit = 114
    if (person != "" and institute == "" and time == "" and date != "" and title == ""):
      cBit = 115
    if (person == "" and institute == "" and time == "" and date == "" and title != ""):
      cBit = 116
    if (person != "" and institute == "" and time == "" and date == "" and title != ""):
      cBit = 117
    if (person == "" and institute == "" and time != "" and date == "" and title != ""):
      cBit = 118
    if (person == "" and institute == "" and time == "" and date != "" and title != ""):
      cBit = 119
    if (person != "" and institute == "" and time != "" and date == "" and title != ""):
      cBit = 120
    if (person != "" and institute == "" and time == "" and date != "" and title != ""):
      cBit = 121
    if (person != "" and institute != "" and time == "" and date == "" and title != ""):
      cBit = 122
    if (person == "" and institute != "" and time == "" and date == "" and title != ""):
      cBit = 123
    if (person != "" and institute != "" and time != "" and date == "" and title != ""):
      cBit = 124
    if (person != "" and institute == "" and time != "" and date != "" and title != ""):
      cBit = 125
    if (person != "" and institute != "" and time == "" and date != "" and title != ""):
      cBit = 126
    if (person == "" and institute != "" and time != "" and date != "" and title != ""):
      cBit = 127
    if (person != "" and institute != "" and time != "" and date != "" and title != ""):
      cBit = 128

    return cBit

#CHeck the when attributes and return bit value accordingly.
  def checkWhen(person,institute):
    cBit=0
    if (person != "" and institute == ""):
      cBit = 200
    if (person != "" and institute != ""):
      cBit = 201 

    return cBit

#CHeck the what attributes and return bit value accordingly.

  def checkWhat(person1,person2):
    cBit=0
    if(person1 !="" and person2 ==""):
      cBit = 800
    if(person1 !="" and person2 !=""):
      cBit = 801
    return cBit

#CHeck the what location attributes and return bit value accordingly.

  def checkWhatLoc(person,time, date, institute):
    cBit=0
    if (person != "" and institute == "" and time == "" and date == ""):
      cBit = 400
    return cBit

#CHeck the whatTime attributes and return bit value accordingly.

  def checkWhatTime(person,time, date, institute):
    cBit=0
    if (person != "" and institute == "" and time == "" and date == ""):
      cBit = 420
    return cBit

#CHeck the who attributes and return bit value accordingly.

  def checkWho(title):
    cBit=0
    if (title!=""):
      cBit = 600
    return cBit


#CHeck the checkHow attributes and return bit value accordingly.

  def checkHow(person1,institute,date,title):
    cBit=0
    if(person1 != "" and institute != "" and date == "" and title == ""):
      cBit=700
    if(person1 != "" and institute == "" and date != "" and title == ""):
      cBit=701
    if(person1 == "" and institute == "" and date == "" and title != ""):
      cBit=702
    if(person1 != "" and institute == "" and date == "" and title == ""):
      cBit=703
    
    return cBit


#CHeck the whatAgenda attributes and return bit value accordingly. 

  def checkWhatAgenda(person,time,date,institute):
    cBit=0
    if(person != "" and time == "" and date == "" and institute == ""):
      cBit = 440
    if(person != "" and time != "" and date == "" and institute == ""):
      cBit = 441
    if(person != "" and time == "" and date != "" and institute == ""):
      cBit = 442
    if(person != "" and time == "" and date == "" and institute != ""):
      cBit = 443
    if(person != "" and time != "" and date != "" and institute == ""):
      cBit = 444
    if(person != "" and time != "" and date == "" and institute != ""):
      cBit = 445
    if(person != "" and time == "" and date != "" and institute != ""):
      cBit = 446
    if(person != "" and time != "" and date != "" and institute != ""):
      cBit = 447
    return cBit

#CHeck the where attributes and return bit value accordingly.

  def checkWhere(person,time,date):
    cBit=0
    if (person != "" and time == "" and date ==""):
      cBit = 300
    if (person != "" and time != "" and date == ""):
      cBit = 301 
    if (person != "" and time == "" and date !=""):
      cBit = 302 
    return cBit

#CHeck the which attributes and return bit value accordingly.

  def checkWhich(person1,person2,title,institute,degree,date):
    cBit=0
    if (person1 != "" and person2 == "" and title != "" and institute == "" and degree == "" and date == ""):
      cBit = 500
    if (person1 != "" and person2 == "" and title == "" and institute == "" and degree == "" and date == ""):
      cBit = 501
    if (person1 != "" and person2 != "" and title == "" and institute == "" and degree == "" and date == ""):
      cBit = 502
    if (person1 != "" and person2 == "" and title == "" and institute != "" and degree == "" and date == ""):
      cBit = 503
    if (person1 != "" and person2 == "" and title == "" and institute == "" and degree == "" and date == ""):
      cBit = 504
    if (person1 != "" and person2 == "" and title == "" and institute == "" and degree == "" and date != ""):
      cBit = 505  
    return cBit
