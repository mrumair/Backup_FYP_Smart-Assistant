from neo4jrestclient.client import GraphDatabase
from py2neo.cypher import cypher_escape
import time
import datetime
from py2neo import Graph, Node, Relationship
from neo4jrestclient import client
from datetime import datetime
from dateutil import parser



graph = Graph("http://localhost:11012", username="neo4j", password="neo4j")


class post:

  def createNodeQueru(subjects , propertys):
    node = subjects
    type_s = propertys
    query= 'MERGE (n:MeetingRecord {name:{sname} , type: {type}}) RETURN n.name' 
    post=graph.run(query,sname=node , type = propertys ) 
    print("node creates") 
    print(post.data())

  def createqueryrelation(subjct , objct , relation , propTime , propVenue , propDate):
    sub = subjct
    obj = objct
    rel_type = relation
    Time_prop = propTime
    Venue_prop = propVenue
    date_prop = propDate
    query =  'MERGE (u1:MeetingRecord { name: {subs} }) MERGE (u2:MeetingRecord { name:{objs} }) MERGE (u1)-[:meet {name: {rel} , time:{timep} , venue:{venuep} , date :{datep}}]-(u2)'
    post = graph.run (query, subs = sub , objs = obj , rel = rel_type  , timep = Time_prop , venuep = Venue_prop , datep = date_prop )
    print ("relation created")
    print (post.data())


  def setProperty(labeln , propertyn):
    lab= labeln
    prop=propertyn
    query = 'MERGE (n:MeetingRecord{name :{labs}}) set n.name = {pros}'
    post = graph.run(query, labs=lab , pros = propo)
    print ("Updating")
    print(post.data())

  def relationTime(subject ,relation , Time):
    sub = subject
    rel = relation
    time = Time
    query = 'MATCH (a:MeetingRecord{name : {subs}})-[r:meet{name:{rels}}]->() set r.Time = {tim} RETURN r.Time, r.Date_is , r.Venue_is'
    post = graph.run(query , subs = sub , rels = rel  , tim = time)
    print ("time updated")
    print(post.data())

  def relationDate(subject ,relation , Date):
    sub = subject
    rel = relation
    date = Date
    query = 'MATCH (a:MeetingRecord{name : {subs}})-[r:meet{name:{rels}}]->() set r.Date_is = {tim} RETURN r.Time, r.Date_is , r.Venue_is'
    post = graph.run(query , subs = sub , rels = rel  , tim = date)
    print ("date updated")
    print(post.data())


  def relationVenue(subject ,relation , Venue):
    sub = subject
    rel = relation
    venue = Venue
    query = 'MATCH (a:MeetingRecord{name : {subs}})-[r:meet{name:{rels}}]->() set r.Venue = {tim} RETURN r.Time, r.Date_is , r.Venue_is'
    post = graph.run(query , subs = sub , rels = rel  , tim = venue)
    print ("time updated")
    print(post.data())


  def ObjectSelection(abc):
    listStoreVar = []

    name = abc
    
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
  def check(person,institute,time,date , title):
    cBit=0
    if (person != "" and institute == "" and time == "" and date == "" and title == ""):
      cBit = 100
    if (person == "" and institute == "" and time != "" and date == "" and title == ""):
      cBit = 101 
    if (person != "" and institute == "" and time != "" and date == "" and title == ""):
      cBit = 102
    if (person != "" and institute == "" and time == "" and date != "" and title == ""):
      cBit = 103
    if (person == "" and institute == "" and time == "" and date != "" and title == ""):
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
    if (person == "" and institute == "" and time == "" and date == "" and title != ""):
      cBit = 110
    if (person == "" and institute == "" and time != "" and date == "" and title != ""):
      cBit = 111
    if (person == "" and institute == "" and time == "" and date != "" and title != ""):
      cBit = 112
    if (person == "" and institute != "" and time == "" and date != "" and title != ""):
      cBit = 113
    if (person != "" and institute == "" and time == "" and date == "" and title != ""):
      cBit = 114

    

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


  def createNode(sub,obj,rel, relp1, relp2, relp3, propertys, propertyo):
    user = db.labels.create("Person")
    u1= db.nodes.create(name = sub, position = propertys)
    user.add(u1)
    u2 = db.nodes.create(name = obj , position = propertyo)
    user.add(u2)
    u1.relationships.create(rel ,u2 , Time = relp1 , Date_is = relp2 , Venue_is = relp3)
    return None

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

    q= 'MATCH (n:MeetingRecord) WHERE NOT (n)--() RETURN n'
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

      a= 'start n=node(*) match (n:MeetingRecord)-[r:meet]-(:MeetingRecord) where exists(r.venue) return r'
      #resultV = graph.query(a, returns=(client.Relationship))

      b= 'start n=node(*) match (n:MeetingRecord)-[r:meet]-(:MeetingRecord) where exists(r.time) return r'
      #resultT = graph.query(b, returns=(client.Relationship))

      c= 'start n=node(*) match (n:MeetingRecord)-[r:meet]-(:MeetingRecord) where exists(r.name) return r'
 
    return listStore

