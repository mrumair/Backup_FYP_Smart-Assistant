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
        location_query='MATCH (a:MeetingRecord)-[r]->(b:MeetingRecord) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.venue)'
        results = db.run(location_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            loc_list=r[0]
        return loc_list

    def times(self,p1,p2,rel):
        print(p1,p2,rel)
        time_list=[]
        time_query='MATCH (a:MeetingRecord)-[r]->(b:MeetingRecord) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.time)'
        results = db.run(time_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            time_list=r[0]
        print ("function lIst" , time_list)
        return time_list


    def dates(self ,p1,p2,rel):
        date_list=[]
        date_query='MATCH (a:MeetingRecord)-[r]->(b:MeetingRecord) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.date)'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN b.name,r.venue,r.date,r.time'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} RETURN b.name,r.venue,r.date'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} RETURN b.name,r.venue,r.date'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} RETURN b.name,r.venue,r.time'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} RETURN b.name,r.venue,r.time'
        results = db.run(meet_query, name_a=p1, rl="meet",r_name=rel, r_date=date)

        for r in results:
            person_list=r[0]
            venue_list=r[1]
            time_list=r[2]
            meet=("Yes, You have meeting on with "+person_list+"' in '"+venue_list+"' at '"+time_list+"'.'")
            meetlist.append(meet)

        if not results.data():
            meet="No, You have no meeting on "+date+"."
            meetlist.append(meet)

        print(meetlist)
        return meetlist

    def qloc(self, p1, rel, loc):
        print(p1,rel,loc,"qloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN b.name,r.time,r.date'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN b.name,r.time,r.date'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN b.name,r.time,r.date,r.venue'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN b.name,r.time,r.date'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN b.name,r.venue'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.time={r_time} AND r.name={r_name} RETURN b.name,r.venue'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN r.venue'
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
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN r.time'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            time_list=r[0]
            meet=("You have meeting with "+p2+" in '"+time_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+"."
            meetlist.append(meet)
        return meetlist


    def qperson(self, p1, p2, rel):
        print(p1,p2,rel,"qperson")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN b.name,r.venue,r.date,r.time'
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

#101
    def qtime(self, p1, rel, time):
        print(p1,rel,time,"qtime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} RETURN b.name,r.venue,r.date'
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

#102
    def qpertime(self, p1, p2, rel, time):
        print(p1,p2,rel,time,"qpertime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} RETURN b.name,r.venue,r.date'
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

#107
    def qperloctime(self, p1, p2, rel,venue,time):
        print(p1,p2,rel,venue,time,"qperloctime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} and r.venue={r_venue} RETURN b.name,r.date'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel, r_time=time,r_venue=venue)
        for r in results:
            person_list=r[0]
            date_list=r[1]
            meet=("Yes, You have meeting with "+person_list+"' on '"+date_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" at "+time+"."
            meetlist.append(meet)
        return meetlist

#103
    def qperdate(self, p1, p2, rel, date):
        print(p1,p2,rel,date,"qperdate")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} RETURN b.name,r.venue,r.time'
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

#do 108
    def qperlocdate(self, p1, p2, rel,loc,date):
        print(p1,p2,rel,loc,date,"qperlocdate")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} and r.venue={r_venue} RETURN b.name,r.time'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel,r_venue=loc, r_date=date)
        for r in results:
            person_list=r[0]
            time_list=r[1]
            meet=("You have meeting with "+person_list+"' at '"+time_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" on "+date+"."
            meetlist.append(meet)
        return meetlist
#do 109
    def qperlocdatetime(self, p1, p2, rel,loc,date,time):
        print(p1,p2,rel,loc,date,time,"qperlocdatetime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} and r.venue={r_venue} and r.time={r_time} RETURN b.name'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel,r_venue=loc, r_date=date,r_time=time)
        for r in results:
            person_list=r[0]
           
            meet=("You have meeting with "+person_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" on "+date+"."
            meetlist.append(meet)
        return meetlist

#104
    def qdate(self, p1, rel, date):
        print(p1,rel,date,"qdate")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} RETURN b.name,r.venue,r.time'
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

#105
    def qloc(self, p1, rel, loc):
        print(p1,rel,loc,"qloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN b.name,r.time,r.date'
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

 #106
    def qperloc(self, p1, p2, rel, loc):
        print(p1,p2,rel,loc,"qperloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN b.name,r.time,r.date'
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
       # meet_query='Match (a:MeetingRecord)-[r]->(b:MeetingRecord) where a.name="Misha Zaheer" AND b.name="Saleha Mirza" AND type(r)="meet" AND r.name="meeting" RETURN b.name,r.time,r.date,r.venue'
        meet_query='Match (a:MeetingRecord)-[r]->(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN b.name,r.time,r.date,r.venue'
        results = db.run(meet_query,name_a=p1, name_b=p2, rl="meet",r_name=rel)
        print(results,"no results")
        for r in results:
            print(r,"results in loop")
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

#201
    def qmeetperloc(self, p1, p2, rel, loc):
        print(p1,p2,rel,loc,"qmeetperloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN b.name,r.time,r.date'
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

#300
    def qmeetloc(self, p1, p2, rel):
        print(p1,p2,rel,"qmeetloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN b.name,r.venue'
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

#301
    def qmeetloctime(self, p1, p2, rel,time):
        print(p1,p2,rel,time,"qmeetloctime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.time={r_time} AND r.name={r_name} RETURN b.name,r.venue'
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

#400
    def qwhatloc(self, p1, p2, rel):
        print(p1,p2,rel,"qwhatloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN r.venue'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            venue_list=r[0]
            meet=("You have meeting with "+p2+" in '"+venue_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+"."
            meetlist.append(meet)
        return meetlist

#420
    def qwhattime(self, p1, p2, rel):
        print(p1,p2,rel,"qwhattime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN r.time'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            time_list=r[0]
            meet=("You have meeting with "+p2+" in '"+time_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+"."
            meetlist.append(meet)
        return meetlist

    def qwhatagenda(self, p1, p2):
        print(p1,p2,"qwhatagenda")
        agenda_list=[]
        person_list=[]
        data=[]
        #venue_list=[]
        #date_list=[]
        #time_list=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} and r.AgendaId=c.AgendaId return c.title'
        results = db.run(agenda_query, name_a=p1, name_b=p2, rl="meet")
        for r in results:
            agenda_list=r[0]
            meet=("The agenda of your meeting with "+p2+" in '"+agenda_list+"'.")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting with "+p2+" on any agenda."
            data.append(meet)
        return data

    def qpertitle(self, p1, title):
        print(p1,title,"qwhatagenda")
        agenda_list=[]
        person_list=[]
        data=[]
        #venue_list=[]
        #date_list=[]
        #time_list=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)="meet" and a.name={name_a} and  c.title={title} and r.AgendaId=c.AgendaId return b.name,r.time,r.date,r.venue'
        results = db.run(agenda_query, name_a=p1, rl="meet",title=title)
        for r in results:
            person_list=r[0]
            date_list=r[2]
            time_list=r[1]
            venue_list=r[3]
            meet=("Yes, You have meeting on "+title+"with "+person_list+"' in '"+venue_list+"' at '"+time_list+" on "+date_list+".'")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting on "+title+"."
            data.append(meet)
        return data

    def qpertitletime(self, p1, title,time):
        print(p1,title,"qwhatagenda")
        agenda_list=[]
        person_list=[]
        data=[]
        #venue_list=[]
        #date_list=[]
        #time_list=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)="meet" and a.name={name_a} and  c.title={title} and r.time={time} and r.AgendaId=c.AgendaId return b.name,r.date,r.venue'
        results = db.run(agenda_query, name_a=p1, rl="meet",title=title,time=time)
        for r in results:
            person_list=r[0]
            date_list=r[1] 
            venue_list=r[2]
            meet=("Yes, You have meeting on "+title+"with "+person_list+"' in '"+venue_list+" on "+date_list+".'")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting on "+title+"."
            data.append(meet)
        return data

    def qpertitledate(self, p1, title,date):
        print(p1,title,"qwhatagenda")
        agenda_list=[]
        person_list=[]
        data=[]
        #venue_list=[]
        #date_list=[]
        #time_list=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)="meet" and a.name={name_a} and  c.title={title} and r.date={date} and r.AgendaId=c.AgendaId return b.name,r.time,r.venue'
        results = db.run(agenda_query, name_a=p1, rl="meet",title=title,date=date)
        for r in results:
            person_list=r[0]
            time_list=r[1] 
            venue_list=r[2]
            meet=("Yes, You have meeting on "+title+"with "+person_list+"' in '"+venue_list+" on "+time_list+".'")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting on "+title+"."
            data.append(meet)
        return data
    def qpertitlevenue(self, p1, title,venue):
        print(p1,title,venue,"qwhatagenda")
        agenda_list=[]
        person_list=[]
        data=[]
        #venue_list=[]
        #date_list=[]
        #time_list=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)="meet" and a.name={name_a} and  c.title={title} and r.venue={venue} and r.AgendaId=c.AgendaId return b.name,r.time,r.date'
        results = db.run(agenda_query, name_a=p1, rl="meet",title=title,venue=venue)
        for r in results:
            person_list=r[0]
            time_list=r[1] 
            date_list=r[2]
            meet=("Yes, You have meeting on "+title+"with "+person_list+"' on '"+date_list+" on "+time_list+".'")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting on "+title+"."
            data.append(meet)
        return data

    def qpertitleper(self, p1, title,p2):
        print(p1,title,"qwhatagenda")
        agenda_list=[]
        person_list=[]
        data=[]
        #venue_list=[]
        #date_list=[]
        #time_list=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)="meet" and a.name={name_a} and b.name={name_b} and c.title={title} and r.AgendaId=c.AgendaId return b.venue,r.time,r.date'
        results = db.run(agenda_query, name_a=p1, rl="meet",title=title,name_b=p2)
        for r in results:
            venue_list=r[0]
            time_list=r[1] 
            date_list=r[2]
            meet=("Yes, You have meeting on "+title+"with "+venue_list+"' on '"+date_list+" on "+time_list+".'")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting on "+title+"."
            data.append(meet)
        return data

    def qwhatagendatime(self, p1, p2,time):
        print(p1,p2,time,"qwhatagendatime")
        agenda_list=[]
        person_list=[]
        data=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} and r.time={time} and r.AgendaId=c.AgendaId return c.title'
        results = db.run(agenda_query, name_a=p1, name_b=p2, rl="meet",time=time)
        for r in results:
            agenda_list=r[0]
            meet=("The agenda of your meeting with "+p2+" in '"+agenda_list+"'.")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting with "+p2+" on any agenda at "+time+"."
            data.append(meet)
        return data

    def qwhatagendadate(self, p1, p2,date):
        print(p1,p2,date,"qwhatagendadate")
        agenda_list=[]
        person_list=[]
        data=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} and r.date={date} and r.AgendaId=c.AgendaId return c.title'
        results = db.run(agenda_query, name_a=p1, name_b=p2, rl="meet",rl1="has",date=date)
        for r in results:
            agenda_list=r[0]
            meet=("The agenda of your meeting with "+p2+" in '"+agenda_list+"'.")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting with "+p2+" on any agenda on "+date+"."
            data.append(meet)
        return data

    def qwhatagendavenue(self, p1, p2,venue):
        print(p1,p2,venue,"qwhatagendavenue")
        agenda_list=[]
        person_list=[]
        data=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} and r.venue={venue} and r.AgendaId=c.AgendaId return c.title'
        results = db.run(agenda_query, name_a=p1, name_b=p2, rl="meet",rl1="has",venue=venue)
        for r in results:
            agenda_list=r[0]
            meet=("The agenda of your meeting with "+p2+" in '"+agenda_list+"'.")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting with "+p2+" on any agenda in "+venue+"."
            data.append(meet)
        return data

    def qwhatagendadatetime(self, p1, p2,date,time):
        print(p1,p2,date,time,"qwhatagendadatetime")
        agenda_list=[]
        person_list=[]
        data=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} and r.time={time} and r.date={date} and r.AgendaId=c.AgendaId return c.title'
        results = db.run(agenda_query, name_a=p1, name_b=p2, rl="meet",rl1="has",date=date,time=time)
        for r in results:
            agenda_list=r[0]
            meet=("The agenda of your meeting with "+p2+" in '"+agenda_list+"'.")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting with "+p2+" on any agenda on "+date+" at "+time+"."
            data.append(meet)
        return data

    def qwhatagendatimevenue(self, p1, p2,time,venue):
        print(p1,p2,time,venue,"qwhatagendatimevenue")
        agenda_list=[]
        person_list=[]
        data=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} and r.venue={venue} and r.time={time} and r.AgendaId=c.AgendaId return c.title'
        results = db.run(agenda_query, name_a=p1, name_b=p2, rl="meet",rl1="has",venue=venue,time=time)
        for r in results:
            agenda_list=r[0]
            meet=("The agenda of your meeting with "+p2+" in '"+agenda_list+"'.")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting with "+p2+" on any agenda at "+time+" in "+venue+"."
            data.append(meet)
        return data

    def qwhatagendadatevenue(self, p1, p2,date,venue):
        print(p1,p2,date,venue,"qwhatagendadatevenue")
        agenda_list=[]
        person_list=[]
        data=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} and r.venue={venue} and r.date={date} and r.AgendaId=c.AgendaId return c.title'
        results = db.run(agenda_query, name_a=p1, name_b=p2, rl="meet",rl1="has",venue=venue,date=date)
        for r in results:
            agenda_list=r[0]
            meet=("The agenda of your meeting with "+p2+" in '"+agenda_list+"'.")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting with "+p2+" on any agenda on "+date+" in "+venue+"."
            data.append(meet)
        return data

    def qwhatagendaall(self, p1, p2,time,date,venue):
        print(p1,p2,time,date,venue,"qwhatagendaall")
        agenda_list=[]
       
        data=[]
        agenda_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} and r.time={time} and r.date={date} and r.venue={venue} and r.AgendaId=c.AgendaId return c.title'
        results = db.run(agenda_query, name_a=p1, name_b=p2, rl="meet",rl1="has",venue=venue,date=date,time=time)
        for r in results:
            agenda_list=r[0]
            meet=("The agenda of your meeting with "+p2+" in '"+agenda_list+"'.")
            data.append(meet)
        if len(data)==0:
            meet="No, You have no meeting with "+p2+" on any agenda on "+date+" in "+venue+"."
            data.append(meet)
        return data

    def qwhatprojectname(self, p1):
        print(p1,"qwhatprojectname")
        project_list=[]
      
        data=[]
        project_query='Match (b:MeetingRecord)-[r1]->(c:MeetingRecord) where type(r1)={rl1} and c.firstSupervisor={sup} or c.secondSupervisor={sup} return collect(distinct c.title)'
        results = db.run(project_query, sup=p1, rl1="has")
        for r in results:
            project_list=r[0]
            #meet=("The names of project supervised by you are "+project_list+".")
            #data.append(project_list)
            data=project_list
        if len(data)==0:
            meet="You are not supervising any project"
            data.append(meet)
        return data

    def qwhatperprojectname(self, p1, p2):
        print(p1,p2,"qwhatperprojectname")
        project_list=[]
        data=[]
        project_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} and r.AgendaId=c.AgendaId return c.title'
        results = db.run(project_query, sup=p1, rl="meet",name_b=p2)
        for r in results:
            project_list=r[0]
            #meet=("The names of project supervised by you are "+project_list+".")
            #data.append(project_list)
            data=project_list
        if len(data)==0:
            meet="You are not doing any project"
            data.append(meet)
        return data

    def qwhatprojectmembers(self,title):
        print(title,"qwhatperprojectmembers")
        project_list=[]
        data=[]
        project_query='Match(a:MeetingRecord),(b:MeetingRecord) Match (b:MeetingRecord)-[r1]->(c:MeetingRecord) where type(r1)={rl1} and c.title={title} return collect(distinct b.name)'
        results = db.run(project_query, rl1="has",title=title)
        for r in results:
            project_list=r[0]
            #meet=("The names of project supervised by you are "+project_list+".")
            #data.append(project_list)
            data=project_list
        if len(data)==0:
            meet="You are not supervising any project"
            data.append(meet)
        return data

    def qhowmember(self,title):
        print(title,"qhowmember")
        project_list=[]
        data=[]
        project_query='Match (a:MeetingRecord)-[r1]->(c:MeetingRecord) where type(r1)={rl1} and c.title={title} return collect(distinct c.noOfMembers)'
        results = db.run(project_query, rl1="has",title=title)
        for r in results:
            project_list=r[0]
            #meet=("The names of project supervised by you are "+project_list+".")
            #data.append(project_list)
            data=project_list
        if len(data)==0:
            meet="This project has no member."
            data.append(meet)
        return data

    def qhowprojects(self,p1):
        print(p1,"qhowprojects")
        project_list=[]
        data=[]
        project_query='Match (a:MeetingRecord)-[r1]->(c:MeetingRecord) where type(r1)={rl1} and c.firstSupervisor={name_a} or c.secondSupervisor={name_a} return count(c)'
        results = db.run(project_query, rl1="has",name_a=p1)
        for r in results:
            project_list=r[0]
            print(project_list)
            #meet=("The names of project supervised by you are "+project_list+".")
            #data.append(project_list)
            data=project_list
        if data=="":
            meet="You are not supervising any project."
            data.append(meet)
        return data

    def qwhoprojectsup(self,title):
        print(title,"qwhoprojectsup")
        project_list=[]
        data=[]
        project_query='Match (a:MeetingRecord)-[r1]->(c:MeetingRecord) where type(r1)={rl1} and c.title={title} return collect(distinct c.firstSupervisor)'
        results = db.run(project_query, rl1="has",title=title)
        for r in results:
            project_list=r[0]
            print(project_list)
            # meet="The supervisor of "+title+" is "+r[0]+"."
            # data.append(meet)
            data=project_list
        if data=="":
            meet="You are not supervising any project."
            data.append(meet)
        return data

    def qwhoprojectcosup(self,title):
        print(title,"qwhoprojectsup")
        project_list=[]
        data=[]
        project_query='Match (a:MeetingRecord)-[r1]->(c:MeetingRecord) where type(r1)={rl1} and c.title={title} return collect(distinct c.secondSupervisor)'
        results = db.run(project_query, rl1="has",title=title)
        for r in results:
            project_list=r[0]
            print(project_list)
            # meet="The supervisor of "+title+" is "+r[0]+"."
            # data.append(meet)
            data=project_list
        if data=="":
            meet="You are not supervising any project."
            data.append(meet)
        return data

    #check person type
    def persontype(self, p1):
        per_type=[]
        person_query='Match(a:SignUp) where a.firstName={name_a}  return a.Type'
        results = db.run(person_query, name_a=p1)
        for r in results:
            per_type=r[0]
        return per_type




# inferencing.objInfer()


nlp = spacy.load('en_core_web_sm')




# person1="Umair"
# person2="Batool"
# relation='meet'
b = inferencing()
b.persontype('abcd')
# for i in range(0, len(r)):
#   print (r[i])
# r=b.times(person1,person2,relation)
# for i in range(0, len(r)):
#   print (r[i])
# r=b.dates(person1,person2,relation)
# print(r)





