from neo4jrestclient import client
from py2neo import Graph
import re
import spacy
import en_core_web_sm

graph1 = Graph("http://localhost:11012", username="neo4j", password="neo4j")
   
def meet_list(p,rel):
    person_list=[]
    venue_list=[]
    time_list=[]
    date_list=[]
    meeting_list=[] 
    mlist_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={p_name} AND type(r)={rl} AND r.name={r_name} And r.venue is not null AND r.time is not null RETURN a.name,r.venue,r.time , b.name , r.date' 
    results = graph1.run(mlist_query,rl="meet",p_name=p,r_name=rel)
    for r in results:
        person_list=r[0]
        venue_list=r[1]
        #date_list=r[2]
        time_list=r[2]
        member_list = r[3]
        date_list = r[4]
        meet=(person_list +"! You have meeting with "+member_list+" at "+time_list+" in "+venue_list+" on "+ str(date_list)+"!")
        meeting_list.append(meet)
    return meeting_list


nlp = spacy.load('en_core_web_sm')
# person="Umair"
# relation="meeting"
# r=meet_list(person,relation)
# print("printing youyouhaha")
# for i in range(0,len(r)):
#     print(r[i])