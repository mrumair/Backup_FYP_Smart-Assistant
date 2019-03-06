#from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from py2neo import Graph
import re
import spacy
import en_core_web_sm

db = Graph("http://localhost:11012", username="neo4j", password="neo4j")


class inferencing:   
    def locations(self, p1,p2,rel):
        loc_list=[]
        location_query='MATCH (a:UserMeeting)-[r]->(b:UserMeeting) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.venue)'
        results = db.run(location_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            loc_list=r[0]
        return loc_list

    def times(self,p1,p2,rel):
        print(p1,p2,rel)
        time_list=[]
        time_query='MATCH (a:UserMeeting)-[r]->(b:UserMeeting) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.time)'
        results = db.run(time_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            time_list=r[0]
        print ("function lIst" , time_list)
        return time_list


    def dates(self ,p1,p2,rel):
        date_list=[]
        date_query='MATCH (a:UserMeeting)-[r]->(b:UserMeeting) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.date)'
        results = db.run(date_query, name_a=p1, name_b=p2,  rl="meet",r_name=rel)
        for r in results:
            date_list=r[0]
        return date_list  


    def objInfer():
        obList = []
        objQuery = 'MATCH(a:SignUp)  return a.firstName' 
        result = db.run(objQuery).data()
        print(result)
        for r in result:
            obList = r[0]
        return result  



    def qperson(self, p1, p2, rel):
        print(p1,p2,rel,"qperson")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN b.name,r.venue,r.date,r.time'
        results = db.run(meet_query, name_a=p1,name_b=p2, rl="meet",r_name=rel)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            date_list=r[2]
            time_list=r[3]
            meet=("Yes, You have meeting with "+person_list+" at '"+time_list+"' in '"+venue_list+"' on '"+date_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+"."
            meetlist.append(meet)
        return meetlist

    def qtime(self, p1, rel, time):
        print(p1,rel,time,"qtime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} RETURN b.name,r.venue,r.date'
        results = db.run(meet_query, name_a=p1, rl="meet",r_name=rel, r_time=time)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            date_list=r[2]
            meet=("Yes, You have meeting with "+person_list+"' in '"+venue_list+"' on '"+date_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting at "+time+"."
            meetlist.append(meet)
        return meetlist

    def qpertime(self, p1, p2, rel, time):
        print(p1,p2,rel,time,"qpertime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} RETURN b.name,r.venue,r.date'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel, r_time=time)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            date_list=r[2]
            meet=("Yes, You have meeting with "+person_list+"' in '"+venue_list+"' on '"+date_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" at "+time+"."
            meetlist.append(meet)
        return meetlist

    def qperdate(self, p1, p2, rel, date):
        print(p1,p2,rel,date,"qperdate")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} RETURN b.name,r.venue,r.time'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel, r_date=date)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            time_list=r[2]
            meet=("You have meeting with "+person_list+"' in '"+venue_list+"' at '"+time_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" on "+date+"."
            meetlist.append(meet)
        return meetlist

    def qdate(self, p1, rel, date):
        print(p1,rel,date,"qdate")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} RETURN b.name,r.venue,r.time'
        results = db.run(meet_query, name_a=p1, rl="meet",r_name=rel, r_date=date)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            time_list=r[2]
            meet=("Yes, You have meeting on with "+person_list+"' in '"+venue_list+"' at '"+time_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+date+"."
            meetlist.append(meet)
        return meetlist

    def qloc(self, p1, rel, loc):
        print(p1,rel,loc,"qloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN b.name,r.time,r.date'
        results = db.run(meet_query, name_a=p1, rl="meet",r_name=rel, r_venue=loc)
        for r in results:
            person_list=r[0]
            time_list=r[1]
            date_list=r[2]
            meet=("You have meeting with "+person_list+" at '"+time_list+"' in '"+date_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+loc+"."
            meetlist.append(meet)
        return meetlist

    def qperloc(self, p1, p2, rel, loc):
        print(p1,p2,rel,loc,"qperloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN b.name,r.time,r.date'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel, r_venue=loc)
        for r in results:
            person_list=r[0]
            time_list=r[1]
            date_list=r[2]
            meet=("You have meeting with "+person_list+" at '"+time_list+"' on '"+date_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with"+p2+" in "+loc+"."
            meetlist.append(meet)
        return meetlist

    def qmeetper(self, p1, p2, rel):
        print(p1,p2,rel,"qmeettime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN b.name,r.time,r.date,r.venue'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            person_list=r[0]
            time_list=r[1]
            date_list=r[2]
            venue_list=r[3]
            meet=("You have meeting with "+person_list+" at '"+time_list+"' on '"+date_list+"' in '"+venue_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+"."
            meetlist.append(meet)
        return meetlist

    def qmeetperloc(self, p1, p2, rel, loc):
        print(p1,p2,rel,loc,"qmeetperloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN b.name,r.time,r.date'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel,r_venue=loc)
        for r in results:
            person_list=r[0]
            time_list=r[1]
            date_list=r[2]
            meet=("You have meeting with "+person_list+" at '"+time_list+"' on '"+date_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" in "+loc+"."
            meetlist.append(meet)
        return meetlist

    def qmeetloc(self, p1, p2, rel):
        print(p1,p2,rel,"qmeetloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN b.name,r.venue'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            meet=("You have meeting with "+person_list+" in '"+venue_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+"."
            meetlist.append(meet)
        return meetlist

    def qmeetloctime(self, p1, p2, rel,time):
        print(p1,p2,rel,time,"qmeetloctime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.time={r_time} AND r.name={r_name} RETURN b.name,r.venue'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_time=time,r_name=rel)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            meet=("You have meeting with "+person_list+" in '"+venue_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" at "+time+"."
            meetlist.append(meet)
        return meetlist

    def qwhatloc(self, p1, p2, rel):
        print(p1,p2,rel,"qwhatloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN r.venue'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            venue_list=r[0]
            meet=("You have meeting with "+p2+" in '"+venue_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+"."
            meetlist.append(meet)
        return meetlist

    def qwhattime(self, p1, p2, rel):
        print(p1,p2,rel,"qwhattime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:UserMeeting)-[r]-(b:UserMeeting) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN r.time'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            time_list=r[0]
            meet=("You have meeting with "+p2+" in '"+time_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+"."
            meetlist.append(meet)
        return meetlist





# inferencing.objInfer()


nlp = spacy.load('en_core_web_sm')
# person1="Umair"
# person2="Batool"
# relation='meet'
# b = inferencing()
# r= b.locations(person1,person2,relation)
# for i in range(0, len(r)):
#   print (r[i])
# r=b.times(person1,person2,relation)
# for i in range(0, len(r)):
#   print (r[i])
# r=b.dates(person1,person2,relation)
# print(r)





