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

#global flagBit
#flagBit = 0

class post:

  def createNodeQueru(subjects , propertys):
    node = subjects
    type_s = propertys
    query= 'MERGE (n:Again {name:{sname} , type: {type}}) RETURN n.name' 
    post=graph.run(query,sname=node , type = propertys ) 
    print("node creates") 
    print(post.data())
    
    #neo4jupyter.draw(graph_object_py2neo, {"Nodes_type": "Att"})
    #DataFrame(graph.data("MATCH (a) RETURN a.name"))
  def createqueryrelation(subjct , objct , relation , propTime , propVenue):
    sub = subjct
    obj = objct
    rel_type = relation
    Time_prop = propTime
    Venue_prop = propVenue
    query = 'match (u:Again{name :{subs}}), (r:Again{name:{objs}}) create (u)-[n:meet{name :{rel} ,time:{timep}, venue :{venuep} }]->(r) return n'
    post = graph.run (query, subs = sub , objs = obj , rel = rel_type  , timep = Time_prop , venuep = Venue_prop )
    print ("relation created")
    print (post.data())


  def setProperty(labeln , propertyn):
    lab= labeln
    prop=propertyn
    query = 'MERGE (n:Again{name :{labs}}) set n.name = {pros}'
    post = graph.run(query, labs=lab , pros = propo)
    print ("Updating")
    print(post.data())

  def relationTime(subject ,relation , Time):
    sub = subject
    rel = relation
    time = Time
    query = 'MATCH (a:Again{name : {subs}})-[r:meet{name:{rels}}]->() set r.Time = {tim} RETURN r.Time, r.Date_is , r.Venue_is'
    post = graph.run(query , subs = sub , rels = rel  , tim = time)
    print ("time updated")
    print(post.data())

  def relationDate(subject ,relation , Date):
    sub = subject
    rel = relation
    date = Date
    query = 'MATCH (a:Again{name : {subs}})-[r:meet{name:{rels}}]->() set r.Date_is = {tim} RETURN r.Time, r.Date_is , r.Venue_is'
    post = graph.run(query , subs = sub , rels = rel  , tim = date)
    print ("date updated")
    print(post.data())


  def relationVenue(subject ,relation , Venue):
    sub = subject
    rel = relation
    venue = Venue
    query = 'MATCH (a:Again{name : {subs}})-[r:meet{name:{rels}}]->() set r.Venue = {tim} RETURN r.Time, r.Date_is , r.Venue_is'
    post = graph.run(query , subs = sub , rels = rel  , tim = venue)
    print ("time updated")
    print(post.data())


# def validateInfo( institute , timep , subjectv, objectv):


  #definning functionss for validation
  def validateInfo( institute , timep ):
    cBit=0
    if (institute==""):
      #listStore3 = "Please Enter complete Information"
      cBit=1

    if (timep == ""):
      cBit = 7 


    # if (subjectv == ""):
    #   cBit = 2

    # if(objectv =="" ):
    #   cBit = 22

    if (institute =="" and timep == ""):
      cBit = 4

    # if (institute =="" and timep == "" and objectv == "" and subjectv == ""):
    #   cBit = 9

    return cBit

  # def checkBit()
  #   if 
      

   










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

    q= 'MATCH (n:Again) WHERE NOT (n)--() RETURN n'
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

      a= 'start n=node(*) match (n:Again)-[r:meet]-(:Again) where exists(r.venue) return r'
      #resultV = graph.query(a, returns=(client.Relationship))

      b= 'start n=node(*) match (n:Again)-[r:meet]-(:Again) where exists(r.time) return r'
      #resultT = graph.query(b, returns=(client.Relationship))

      c= 'start n=node(*) match (n:Again)-[r:meet]-(:Again) where exists(r.name) return r'
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

