from neo4jrestclient.client import GraphDatabase
#from neo4j.v1 import GraphDatabase
#from py2neo import Node
#from py2neo import cypher
from neo4jrestclient import client

db = GraphDatabase("http://localhost:11012", username="neo4j", password="neo4j")
node = 'subjects'
q= 'MERGE (n:label {name:{node}})'  
results = db.query(q, returns=(client.Node))
