#from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from py2neo import Graph
import re
import spacy
import en_core_web_sm

db = Graph("http://localhost:11002", username="neo4j", password="neo4j")


class inferencing:   
    def locations(self, p1,p2,rel):
        loc_list=[]
        location_query='MATCH (a:Again)-[r]->(b:Again) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.venue)'
        results = db.run(location_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            loc_list=r[0]
        return loc_list

    def times(self,p1,p2,rel):
        print(p1,p2,rel)
        time_list=[]
        time_query='MATCH (a:Again)-[r]->(b:Again) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.time)'
        results = db.run(time_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            time_list=r[0]
        print ("function lIst" , time_list)
        return time_list


    def dates(self ,p1,p2,rel):
        date_list=[]
        date_query='MATCH (a:Again)-[r]->(b:Again) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.date)'
        results = db.run(date_query, name_a=p1, name_b=p2,  rl="meet",r_name=rel)
        for r in results:
            date_list=r[0]
        return date_list                





nlp = spacy.load('en_core_web_sm')
# person1="Rabeeya Saleem"
# person2="Taliah Tajammal"
# relation='meet'
# b = inferencing()
# r= b.locations(person1,person2,relation)
# for i in range(0, len(r)):
#   print (r[i])
# r=b.times(person1,person2,relation)
# for i in range(0, len(r)):
#   print (r[i])
# r=dates(person1,person2,relation)
# print(r)





