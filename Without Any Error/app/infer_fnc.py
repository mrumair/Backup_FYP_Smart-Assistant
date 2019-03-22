#from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from py2neo import Graph
import re
import spacy
import en_core_web_sm

db = Graph("http://localhost:11005", username="neo4j", password="neo4j")

class inferencing: 

#check person type
    def personType(self, p1):
        per_type=[]
        person_query='Match(a:SignUp) where a.firstName={name_a}  return a.Type'
        results = db.run(person_query, name_a=p1)
        for r in results:
            per_type=r[0]
        return per_type 

#Suggest locations on the basis of historic data       
    def locations(self, p1,p2,rel):
        loc_list=[]
        location_query='MATCH (a:MeetingRecord)-[r]->(b:MeetingRecord) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.venue)'
        results = db.run(location_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            loc_list=r[0]
        return loc_list

#Suggest times on the basis of historic data
    def times(self,p1,p2,rel):
        print(p1,p2,rel)
        time_list=[]
        time_query='MATCH (a:MeetingRecord)-[r]->(b:MeetingRecord) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.time)'
        results = db.run(time_query, name_a=p1, name_b=p2, rl="meet",r_name=rel)
        for r in results:
            time_list=r[0]
        print ("function lIst" , time_list)
        return time_list

#Suggest dates on the basis of historic data
    def dates(self ,p1,p2,rel):
        date_list=[]
        date_query='MATCH (a:MeetingRecord)-[r]->(b:MeetingRecord) WHERE type(r)={rl} AND r.name={r_name} AND a.name={name_a} AND b.name={name_b} RETURN collect (distinct r.date)'
        results = db.run(date_query, name_a=p1, name_b=p2,  rl="meet",r_name=rel)
        for r in results:
            date_list=r[0]
        return date_list  

#Get first name of sign user
    def objInfer():
        obList = []
        objQuery = 'MATCH(a:SignUp)  return a.firstName' 
        result = db.run(objQuery).data()
        print(result)
        for r in result:
            obList = r[0]
        return result  

#Get Title List
    def title(self):
        title_list = []
        title_query = "Match (a:MeetingRecord) return collect(distinct a.title)"
        results = db.run(title_query)
        for r in results:
            title_list = r[0]
        return title_list

#Find meeting details on basis of Person
    def qPerson(self, p1, p2, rel):
        meetlist=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        print(p1,p2,rel,"qperson")
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} RETURN r.venue,r.date,r.time'
        results = db.run(meet_query, name_a=p1,name_b=p2, rl="meet",r_name=rel)
        for r in results:
            venue_list=r[0]
            date_list=r[1]
            time_list=r[2]
            meet=("Yes, You have meeting at '"+time_list+"' in '"+venue_list+"' on '"+date_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+"."
            meetlist.append(meet)
        return meetlist

    def qMeetPer(self, p1, p2, rel):
        print(p1,p2,rel,"qmeetloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
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

    def qMeetPerTime(self, p1, p2, rel,time):
        print(p1,p2,rel,time,"qmeetloctime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.time={r_time} AND r.name={r_name} RETURN b.name,r.venue,r.date'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_time=time,r_name=rel)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            date_list=r[2]
            meet=("You have meeting with "+person_list+" in '"+venue_list+"' on "+date_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" at "+time+"."
            meetlist.append(meet)
        return meetlist

    def qMeetPerDate(self, p1, p2, rel,date):
        print(p1,p2,rel,date,"qmeetlocdate")
        meetlist=[]
        person_list=[]
        venue_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.date={r_date} AND r.name={r_name} RETURN b.name,r.venue,r.time'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_date=date,r_name=rel)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            time_list=r[2]
            meet=("You have meeting with "+person_list+" at "+time_list+" in '"+venue_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" at "+date+"."
            meetlist.append(meet)
        return meetlist

    #check my password        
    def qStdWhatMyPsd(self, p1):
        per_type=[]
        person_query='Match(a:SignUp) where a.name={name_a} return a.Password'
        results = db.run(person_query, name_a=p1)
        for r in results:
            per_type=r[0]
        return per_type


#Find meeting details on basis of Time        
    def qTime(self, p1, rel, time):
        print(p1,rel,time,"qtime")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
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

#Find meeting details on basis of Date
    def qDate(self, p1, rel, date):
        print(p1,rel,date,"qdate")
        meetlist=[]
        person_list=[]
        venue_list=[]
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

#Find meeting on basis of Person and Date        
    def qPerDate(self, p1, p2, rel, date):
        print(p1,p2,rel,date,"qperdate")
        meetlist=[]
        venue_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} RETURN r.venue,r.time'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel, r_date=date)
        for r in results:
            venue_list=r[0]
            time_list=r[1]
            meet=("You have meeting in '"+venue_list+"' at '"+time_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" on "+date+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person and Time
    def qPerTime(self, p1, p2, rel, time):
        print(p1,p2,rel,time,"qpertime")
        meetlist=[]
        venue_list=[]
        date_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} RETURN r.venue,r.date'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel, r_time=time)
        for r in results:
            venue_list=r[0]
            date_list=r[1]
            meet=("Yes, You have meeting in '"+venue_list+"' on '"+date_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" at "+time+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Location
    def qLoc(self, p1, rel, loc):
        print(p1,rel,loc,"qloc")
        meetlist=[]
        person_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN b.name,r.time,r.date'
        results = db.run(meet_query, name_a=p1, rl="meet",r_name=rel, r_venue=loc)
        for r in results:
            person_list=r[0]
            time_list=r[1]
            date_list=r[2]
            meet=("You have meeting with "+person_list+" at '"+time_list+"' on '"+date_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+loc+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person and Location
    def qPerLoc(self, p1, p2, rel, loc):
        print(p1,p2,rel,loc,"qperloc")
        meetlist=[]
        date_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} RETURN r.time,r.date'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel, r_venue=loc)
        for r in results:
            time_list=r[0]
            date_list=r[1]
            meet=("You have meeting at '"+time_list+"' on '"+date_list+"'.")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with"+p2+" in "+loc+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person, Location and Time
    def qPerLocTime(self, p1, p2, rel, venue, time):
        print(p1,p2,rel,venue,time,"qperloctime")
        meetlist=[]
        person_list=[]
        date_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} and r.venue={r_venue} RETURN b.name,r.date'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel, r_time=time,r_venue=venue)
        for r in results:
            person_list=r[0]
            date_list=r[1]
            meet=("Yes, You have meeting with "+person_list+"' on '"+date_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" at "+time+" in "+venue+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person, Location and Date
    def qPerLocDate(self, p1, p2, rel,date,loc):
        print(p1,p2,rel,loc,date,"qperlocdate")
        meetlist=[]
        person_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} and r.venue={r_venue} RETURN b.name,r.time'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel,r_venue=loc, r_date=date)
        for r in results:
            person_list=r[0]
            time_list=r[1]
            meet=("You have meeting with "+person_list+"' at '"+time_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" on "+date+" in "+loc+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person, Date, Time and Location
    def qPerLocDateTime(self, p1, p2, rel,date,time,loc):
        print(p1,p2,rel,loc,date,time,"qperlocdatetime")
        meetlist=[]
        person_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} and r.venue={r_venue} and r.time={r_time} RETURN b.name'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel,r_venue=loc, r_date=date,r_time=time)
        for r in results:
            person_list=r[0]
            meet=(" Yes, You have meeting with "+person_list+"'.'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" on "+date+" at "+time+" in "+loc+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Date and Time.
    def qTimeDate(self, p1, rel,date,time):
        print(p1,rel,date,time,"qtimedate")
        meetlist=[]
        person_list=[]
        venue_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} and r.time={r_time} RETURN b.name,r.venue'
        results = db.run(meet_query, name_a=p1, rl="meet",r_name=rel,r_date=date,r_time=time)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            meet=("You have meeting with "+person_list+"' in '"+venue_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+date+" at "+time+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Location and Time.
    def qTimeLoc(self, p1, rel, time, loc):
        print(p1,rel,loc,time,"qtimeloc")
        meetlist=[]
        person_list=[]
        date_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} and r.time={r_time} RETURN b.name,r.date'
        results = db.run(meet_query, name_a=p1,  rl="meet",r_name=rel,r_venue=loc,r_time=time)
        for r in results:
            person_list=r[0]
            date_list=r[1]
            meet=("You have meeting with "+person_list+"' on '"+date_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting at "+time+" in "+loc+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Location and Date.
    def qDateLoc(self, p1, rel, date, loc):
        print(p1,rel,loc,date,"qdateloc")
        meetlist=[]
        person_list=[]
        venue_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.venue={r_venue} and r.date={r_date} RETURN b.name,r.time'
        results = db.run(meet_query, name_a=p1, rl="meet",r_name=rel,r_venue=loc,r_date=date)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            meet=("You have meeting with "+person_list+"' at '"+venue_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+date+" in "+loc+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person, Location and Date.
    def qPerDateTime(self, p1, p2, rel, date, time):
        print(p1,p2,rel,time,date,"qperdatetime")
        meetlist=[]
        venue_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} and r.date={r_date} RETURN b.name,r.venue'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel,r_time=time,r_date=date)
        for r in results:
            person_list=r[0]
            venue_list=r[1]
            meet=("You have meeting in "+venue_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+date+" at "+time+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Location, Time and Date.
    def qDateTimeLoc(self, p1, rel, date, time,loc):
        print(p1,rel,loc,date,"qdatetimeloc")
        meetlist=[]
        person_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND type(r)={rl} AND r.name={r_name} AND r.time={r_time} AND r.venue={r_venue} and r.date={r_date} RETURN b.name'
        results = db.run(meet_query, name_a=p1, rl="meet",r_name=rel,r_time=time,r_date=date,r_venue=loc)
        for r in results:
            person_list=r[0]
            meet=("You have meeting in "+person_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+date+" at "+time+" in "+loc+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person and Date.
    def qPerDate(self, p1,p2, rel, date):
        print(p1,rel,p2,date,"qperdate")
        meetlist=[]
        venue_list=[]
        time_list=[]
        meet_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={name_a} AND b.name={name_b} AND type(r)={rl} AND r.name={r_name} AND r.date={r_date} RETURN r.venue,r.time'
        results = db.run(meet_query, name_a=p1, name_b=p2, rl="meet",r_name=rel,r_date=date)
        for r in results:
            venue_list=r[0]
            time_list=r[1]
            meet=("You have meeting in "+venue_list+" at "+time_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" on "+date+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Title
    def qTitle(self, p1, rel, title):
        print(p1,title,"qTitle")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)="meet" and r.name={r_name} and a.name={name_a} and c.title={title} and r.AgendaId=c.AgendaId return b.name,r.time,r.date,r.venue'
        results = db.run(meet_query, name_a=p1, r_name=rel,rl="meet",title=title)
        for r in results:
            person_list=r[0]
            time_list=r[1]
            date_list=r[2]
            venue_list=r[3]
            meet=("Yes, You have meeting on "+title+ " with "+person_list+" in '"+venue_list+"' at '"+time_list+" on "+date_list+".'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+title+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Title and Person
    def qPerTitle(self, p1, p2, rel, title):
        print(p1,p2,title,"qPerTitle")
        meetlist=[]
        venue_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)="meet" and r.name={r_name} and a.name={name_a} and b.name={name_b} and c.title={title} and r.AgendaId=c.AgendaId return r.time,r.date,r.venue'
        results = db.run(meet_query, name_a=p1, name_b=p2, r_name=rel,rl="meet",title=title)
        for r in results:
            time_list=r[0]
            date_list=r[1]
            venue_list=r[2]
            meet=("Yes, You have meeting in '"+venue_list+"' at '"+time_list+" on "+date_list+".'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+title+" with "+p1+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Title and Time
    def qTimeTitle(self, p1, rel, time, title):
        print(p1,title,"qTimeTitle")
        meetlist=[]
        person_list=[]
        venue_list=[]
        date_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)="meet" and r.name={r_name} and a.name={name_a} and r.time={r_time} and c.title={title} and r.AgendaId=c.AgendaId return b.name,r.date,r.venue'
        results = db.run(meet_query, name_a=p1, r_name=rel,rl="meet",title=title,r_time=time)
        for r in results:
            person_list=r[0]
            date_list=r[1]
            venue_list=r[2]
            meet=("Yes, You have meeting with '"+person_list+"' in '"+venue_list+" on "+date_list+".'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+title+" at "+time+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Title and Date
    def qDateTitle(self, p1, rel, date, title):
        print(p1,title,"qDateTitle")
        meetlist=[]
        person_list=[]
        venue_list=[]
        time_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)="meet" and r.name={r_name} and a.name={name_a} and r.date={r_date} and c.title={title} and r.AgendaId=c.AgendaId return b.name,r.time,r.venue'
        results = db.run(meet_query, name_a=p1, r_name=rel,rl="meet",title=title,r_date=date)
        for r in results:
            person_list=r[0]
            time_list=r[1]
            venue_list=r[2]
            meet=("Yes, You have meeting with '"+person_list+"' in '"+venue_list+" at "+time_list+".'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+title+" on "+date+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person, Title and Time
    def qPerTimeTitle(self, p1, p2, rel, time, title):
        print(p1,p2,title,"qPerTimeTitle")
        meetlist=[]
        venue_list=[]
        date_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and r.name={r_name} and a.name={name_a} and b.name={name_b} and r.time={r_time} and c.title={title} and r.AgendaId=c.AgendaId return r.date,r.venue'
        results = db.run(meet_query, name_a=p1, name_b=p2, r_name=rel, rl="meet", title=title, r_time=time)
        for r in results:
            date_list=r[0]
            venue_list=r[1]
            meet=("Yes, You have meeting in '"+venue_list+" on "+date_list+".'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+title+" at "+time+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person, Title and Date
    def qPerDateTitle(self, p1, p2, rel, date, title):
        print(p1,p2,title,"qPerDateTitle")
        meetlist=[]
        venue_list=[]
        time_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and r.name={r_name} and a.name={name_a} and b.name={name_b} and r.date={r_date} and c.title={title} and r.AgendaId=c.AgendaId return r.time,r.venue'
        results = db.run(meet_query, name_a=p1, name_b=p2, r_name=rel, rl="meet", title=title, r_date=date)
        for r in results:
            time_list=r[0]
            venue_list=r[1]
            meet=("Yes, You have meeting in '"+venue_list+" at "+time_list+".'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+title+" at "+date+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person, Title and Location
    def qPerLocTitle(self, p1, p2, rel, loc, title):
        print(p1,p2,title,"qPerLocTitle")
        meetlist=[]
        date_list=[]
        time_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and r.name={r_name} and a.name={name_a} and b.name={name_b} and r.venue={r_venue} and c.title={title} and r.AgendaId=c.AgendaId return r.time,r.date'
        results = db.run(meet_query, name_a=p1, name_b=p2, r_name=rel, rl="meet", title=title, r_venue=loc)
        for r in results:
            time_list=r[0]
            date_list=r[1]
            meet=("Yes, You have meeting on '"+date_list+" at "+time_list+".'")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+title+" in "+loc+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Title and Location
    def qLocTitle(self, p1, rel, loc, title):
        print(p1,title,"qPerLocTitle")
        meetlist=[]
        person_list=[]
        date_list=[]
        time_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and r.name={r_name} and a.name={name_a} and r.venue={r_venue} and c.title={title} and r.AgendaId=c.AgendaId return b.name,r.time,r.date'
        results = db.run(meet_query, name_a=p1, r_name=rel, rl="meet", title=title, r_venue=loc)
        for r in results:
            person_list=r[0]
            time_list=r[1]
            date_list=r[2]
            meet=("Yes, You have meeting with '"+person_list+" at "+time_list+" on '"+date_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+title+" in "+loc+"."
            meetlist.append(meet)
        return meetlist


#Find meeting on basis of Person, Title, Time and Location  
    def qPerTimeLocTitle(self, p1, p2, rel, time, loc, title):
        print(p1,p2,title,"qPerTimeLocTitle")
        meetlist=[]
        date_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and r.name={r_name} and a.name={name_a} and b.name={name_b} and r.venue={r_venue} and r.time={r_time} and c.title={title} and r.AgendaId=c.AgendaId return r.date'
        results = db.run(meet_query, name_a=p1, name_b=p2, r_name=rel, rl="meet", title=title, r_venue=loc, r_time=time)
        for r in results:
            date_list=r[0]
            meet=("Yes, You have meeting "+title +" on '"+date_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on "+title+" in "+loc+" at "+time+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person, Title, Time annd Date 
    def qPerDateTimeTitle(self, p1, p2, rel, date, time, title):
        print(p1,p2,title,"qPertimedateTitle")
        meetlist=[]
        date_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and r.name={r_name} and a.name={name_a} and b.name={name_b} and r.date={r_date} and r.time={r_time} and c.title={title} and r.AgendaId=c.AgendaId return r.venue'
        results = db.run(meet_query, name_a=p1, name_b=p2, r_name=rel, rl="meet", title=title, r_date=date, r_time=time)
        for r in results:
            date_list=r[0]
            meet=("Yes, You have meeting "+title +" on '"+venue_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with "+p2+" on "+title+" in "+loc+" on "+date+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person, Title, Date and Location  
    def qPerDateLocTitle(self, p1, p2, rel, date, loc, title):
        print(p1,p2,title,"qPerLocdateTitle")
        meetlist=[]
        time_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and r.name={r_name} and a.name={name_a} and b.name={name_b} and r.date={r_date} and r.venue={venue} and c.title={title} and r.AgendaId=c.AgendaId return r.time'
        results = db.run(meet_query, name_a=p1, name_b=p2, r_name=rel, rl="meet", title=title, r_date=date, r_venue=loc)
        for r in results:
            time_list=r[0]
            meet=("Yes, You have meeting "+title +" at '"+time_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with"+p2+" on "+title+" in "+loc+" on "+date+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Title, Date, Time and Location  
    def qDateTimeLocTitle(self, p1, rel, date, time, loc, title):
        print(p1,title,"qPerLocTitle")
        meetlist=[]
        person_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and r.name={r_name} and a.name={name_a} and r.time={r_time} and r.date={r_date} and r.venue={r_venue} and c.title={title} and r.AgendaId=c.AgendaId return b.name'
        results = db.run(meet_query, name_a=p1, r_name=rel, rl="meet", title=title, r_date=date, r_venue=loc,r_time=time)
        for r in results:
            person_list=r[0]
            meet=("Yes, You have meeting on"+title +" at '"+person_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting on"+title+" at "+time+" in "+loc+" on "+date+"."
            meetlist.append(meet)
        return meetlist

#Find meeting on basis of Person, Title, Date, Time and Location  
    def qPerDateTimeLocTitle(self, p1, p2, rel, date, time, loc, title):
        print(p1,p2,date,time,loc,title,"qPerLocTitle")
        meetlist=[]
        person_list=[]
        meet_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and r.name={r_name} and a.name={name_a} and b.name={name_b} and r.time={r_time} and r.date={r_date} and r.venue={r_venue} and c.title={title} and r.AgendaId=c.AgendaId return b.name'
        results = db.run(meet_query, name_a=p1, name_b=p2, r_name=rel, rl="meet", title=title, r_date=date, r_venue=loc,r_time=time)
        for r in results:
            person_list=r[0]
            meet=("Yes, You have meeting on"+title +" at '"+person_list+".")
            meetlist.append(meet)
        if len(meetlist)==0:
            meet="No, You have no meeting with"+p2+" on "+title+" at "+time+" in "+loc+" on "+date+"."
            meetlist.append(meet)
        return meetlist

#Find members of Projects
    def qProMem(self,title):
        print(title,"qprojectmembers")
        project_list=[]
        data=[]
        project_query='Match(a:MeetingRecord),(b:MeetingRecord) Match (b:MeetingRecord)-[r1]-(c:MeetingRecord) where type(r1)={rl1} and c.title={title} return collect(distinct b.name)'
        results = db.run(project_query, rl1="has",title=title)
        for r in results:
            project_list=r[0]
            data=project_list
            print(project_list)
        if len(data)==0:
            meet="This Project has no members"
            data.append(meet)
        return data

#Find Project names
    def qProName(self, p1):
        print(p1,"qwhatprojectname")
        project_list=[]
        data=[]
        project_query='Match (b:MeetingRecord)-[r1]->(c:MeetingRecord) where type(r1)={rl1} and c.firstSupervisor={sup} or c.secondSupervisor={sup} return collect(distinct c.title)'
        results = db.run(project_query, sup=p1, rl1="has")
        for r in results:
            project_list=r[0]
            data=(project_list)
        if len(data)==0:
            meet="You are not part of any project"
            data.append(meet)
        return data

#Find Projects name I am doing with Person
    def qPerProName(self, p1, p2):
        print(p1,p2,"qwhatperprojectname")
        project_list=[]
        data=[]
        project_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord),(c:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} and r.AgendaId=c.AgendaId return collect(distinct c.title)'
        results = db.run(project_query, name_a=p1, rl="meet",name_b=p2)
        for r in results:
            project_list=r[0]
            dt=(project_list)
            data.append(dt)
        if len(data)==0:
            meet="You are not part of any project with "+p2+"."
            data.append(meet)
        return data

#Find students of specific city,country,institute
    def qStdLoc(self,p1,loc):
        print(p1,loc)
        per_type=[]
        person=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="student" and b.City={loc} or b.Country={loc} or b.Institute={loc} Return collect(distinct b.name)'
        results = db.run(per_query, loc=loc)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)

        if len(data)==0:
            per_query='Match(b:SignUp) where b.Type="student" and b.City={loc} or b.Country={loc} or b.Institute={loc} Return collect(distinct b.name)'
            results = db.run(per_query, loc=loc)
            for r in results:
                per_type=r[0]
                per=(per_type)
                person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord)-[r1]-(c:MeetingRecord) where type(r)={rl} and type(r1)={rl} AND a.name={name_a} and c.name={name_c} return collect(distinct c.name)'
                results = db.run(person_query, name_a=p1,rl="meet",name_c=per)
                for r in results:
                    person_list=r[0] 
                    print(person_list)
                    data.append(person_list)      
        return data

#Find students do BS/MS/PHD in CS,CE,CHE,EE,ME,CV
    def qStdDegree(self,p1,degree):
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="student" and b.Degree={degree} Return collect(distinct b.name)'
        results = db.run(per_query, degree=degree)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

#Find students who are doing graduation
    def qStdDegGrad(self,p1,degree1,degree2):
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="student" and left(b.Degree,3) <>{degree1} and left(b.Degree,3) <>{degree2} Return collect(distinct b.name)'
        results = db.run(per_query,degree1=degree1,degree2=degree2)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

#Find students who do masters, phd
    def qStdDegPer(self,p1,degree):
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="student" and left(b.Degree,3) <>{degree1} and left(b.Degree,3) <>{degree2} Return collect(distinct b.name)'
        results = db.run(per_query,degree1=degree1,degree2=degree2)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

#student session
    def qStdSession(self,p1,session):
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="student" and b.Session={session} Return collect(distinct b.name)'
        results = db.run(per_query, session=session)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

#student email
    def qStdEmail(self,p1,email):
        email=email+".com"
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="student" and  right(b.email,9)={email} Return collect(distinct b.name)'
        results = db.run(per_query, email=email)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

#student ask which teacher from loc
    def qStdTechLoc(self,p1,loc):
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="teacher" and  b.City={loc} or b.Country={loc} or b.Institute={loc} Return collect(distinct b.name)'
        results = db.run(per_query,loc=loc)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

#student ask teacher as lecturar 
    def qStdTechRank(self,p1,rank):
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="teacher" and  b.rank={rank} Return collect(distinct b.name)'
        results = db.run(per_query,rank=rank)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

#student ask teacher as lecturar in loc
    def qStdTechRankLoc(self,p1,rank,loc):
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="teacher" and  b.rank={rank} and b.City={loc} or b.Country={loc} or b.Institute={loc} Return collect(distinct b.name)'
        results = db.run(per_query,rank=rank)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

    def qProSup(self,title):
        print(title,"qwhoprojectsup")
        project_list=[]
        data=[]
        project_query='Match (c:MeetingRecord) where c.title={title} return collect(distinct c.firstSupervisor)'
        results = db.run(project_query,title=title)
        for r in results:
            project_list=r[0]
            print(project_list)
            data=project_list
        if data=="":
            meet="You are not supervising any project."
            data.append(meet)
        return data

    def qProCoSup(self,title):
        print(title,"qwhoprojectcosup")
        project_list=[]
        data=[]
        project_query='Match (c:MeetingRecord) where c.title={title} return collect(distinct c.secondSupervisor)'
        results = db.run(project_query, title=title)
        for r in results:
            project_list=r[0]
            print(project_list)
            data=project_list
        if data=="":
            meet="You are not supervising any project."
            data.append(meet)
        return data

    #how many students with loc
    def qStdLocCnt(self,p1,loc):
        print(p1,loc)
        per_type=[]
        person=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="student" and b.City={loc} or b.Country={loc} or b.Institute={loc} Return collect(distinct b.name)'
        results = db.run(per_query, loc=loc)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return count( b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)

        if len(data)==0:
            per_query='Match(b:SignUp) where b.Type="student" and b.City={loc} or b.Country={loc} or b.Institute={loc} Return collect(distinct b.name)'
            results = db.run(per_query, loc=loc)
            for r in results:
                per_type=r[0]
                per=(per_type)
                person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord)-[r1]-(c:MeetingRecord) where type(r)={rl} and type(r1)={rl} AND a.name={name_a} and c.name={name_c} return count(c.name)'
                results = db.run(person_query, name_a=p1,rl="meet",name_c=per)
                for r in results:
                    person_list=r[0] 
                    print(person_list)
                    data.append(person_list)      
        return data


#how many students of session
    def qStdSesCnt(self,p1,session):
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="student" and b.Session={session} Return collect(distinct b.name)'
        results = db.run(per_query, session=session)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return count(b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

#how many emails
    def qStdEmailCnt(self,p1,email):
        email=email+".com"
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="student" and  right(b.email,9)={email} Return collect(distinct b.name)'
        results = db.run(per_query, email=email)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return count(b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

#how many lecturar by student
    def qStdTechRankCnt(self,p1,rank):
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="teacher" and  b.rank={rank} and b.City={loc} or b.Country={loc} or b.Institute={loc} Return collect(distinct b.name)'
        results = db.run(per_query,rank=rank)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return count(b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data

#student how many lecturar from lloc
    def qStdTechRankLocCnt(self,p1,rank,loc):
        per_type=[]
        data=[]
        per_query='Match(b:SignUp) where b.Type="teacher" and  b.rank={rank} and b.City={loc} or b.Country={loc} or b.Institute={loc} Return collect(distinct b.name)'
        results = db.run(per_query,rank=rank)
        for r in results:
            per_type=r[0]
            per=(per_type)
            person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return count(b.name)'
            results = db.run(person_query, name_a=p1,rl="meet",name_b=per)
            for r in results:
                person_list=r[0] 
                print(person_list)
                data.append(person_list)
        return data


    def qMemCnt(self,title):
        print(title,"qhowmember")
        project_list=[]
        data=[]
        project_query='Match(a:MeetingRecord),(b:MeetingRecord) Match (b:MeetingRecord)-[r1]-(c:MeetingRecord) where type(r1)={rl1} and c.title={title} return count(b.name)'
        results = db.run(project_query, rl1="has",title=title)
        for r in results:
            project_list=r[0]
            data=project_list
            print(project_list)
        if len(data)==0:
            meet="This Project has no members"
            data.append(meet)
        return data

    def qPrjCnt(self,p1):
        print(p1,"qhowprojects")
        project_list=[]
        data=[]
        project_query='Match (a:MeetingRecord)-[r1]->(c:MeetingRecord) where type(r1)={rl1} and c.firstSupervisor={name_a} or c.secondSupervisor={name_a} return count(c.title)'
        results = db.run(project_query, rl1="has",name_a=p1)
        for r in results:
            project_list=r[0]
            print(project_list)
            data=project_list
        if data=="":
            meet="You are not supervising any project."
            data.append(meet)
        return data

    #check my reg       
    def qStdWhatMyReg(self, p1):
        per_type=[]
        print(p1,"reg")
        person_query='Match(a:SignUp) where a.name={name_a} return a.Registration_Number'
        results = db.run(person_query, name_a=p1)
        for r in results:
            per_type=r[0]
        return per_type

#check my email        
    def qStdWhatMyEmail(self, p1):
        per_type=[]
        person_query='Match(a:SignUp) where a.name={name_a} return a.Email'
        results = db.run(person_query, name_a=p1)
        for r in results:
            per_type=r[0]
        return per_type

#check my phone        
    def qStdWhatMyPhone(self, p1):
        per_type=[]
        person_query='Match(a:SignUp) where a.name={name_a} return a.Tel'
        results = db.run(person_query, name_a=p1)
        for r in results:
            per_type=r[0]
        return per_type
#######################################################################################################################################################
#Find email of student
    def qStdWhatEmail(self,p1,p2):
        print("check what is email")
        per_type=[]
        prs1=[]
        prs1=p2.split(" ",1)
        print(prs1[0],"split string")
        check=""
        person=[]
        person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct 1)'
        results = db.run(person_query, name_a=p1, name_b=p2,rl="meet")
        for r in results:
            check=r[0] 
        if len(check)!=0:
            print("if check is 1")
            per_query='Match(a:SignUp) where a.firstName={name_a} and a.Type="student"  Return collect(distinct a.Email)'
            results = db.run(per_query, name_a=prs1[0])
            for r in results:
                per_type=r[0]
                print(per_type)
                per=(per_type)
                person.append(per)
        return person

#Find degree of student
    def qStdWhatDegree(self,p1,p2):
        per_type=[]
        person=[]
        prs1=[]
        prs1=p2.split(" ",1)
        print(prs1[0],"split string")
        check=""
        person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct 1)'
        results = db.run(person_query, name_a=p1, name_b=p2,rl="meet")
        for r in results:
            check=r[0] 
        if len(check)!=0:
            print("if check is 1")
            per_query='Match(a:SignUp) where a.firstName={name_a} and a.Type="student"  Return collect(distinct a.Degree)'
            results = db.run(per_query, name_a=prs1[0])
            for r in results:
                per_type=r[0]
                print(per_type)
                per=(per_type)
                person.append(per)
        return person

#what city of student
    def qStdWhatCity(self,p1,p2):
        per_type=[]
        person=[]
        prs1=[]
        prs1=p2.split(" ",1)
        print(prs1[0],"split string")
        check=""
        person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct 1)'
        results = db.run(person_query, name_a=p1, name_b=p2,rl="meet")
        for r in results:
            check=r[0] 
        if len(check)!=0:
            print("if check is 1")
            per_query='Match(a:SignUp) where a.firstName={name_a} and a.Type="student"  Return collect(distinct a.City)'
            results = db.run(per_query, name_a=prs1[0])
            for r in results:
                per_type=r[0]
                print(per_type)
                per=(per_type)
                person.append(per)
        return person

#what city of student
    def qStdWhatCountry(self,p1,p2):
        per_type=[]
        person=[]
        prs1=[]
        prs1=p2.split(" ",1)
        print(prs1[0],"split string")
        check=""
        person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct 1)'
        results = db.run(person_query, name_a=p1, name_b=p2,rl="meet")
        for r in results:
            check=r[0] 
        if len(check)!=0:
            print("if check is 1")
            per_query='Match(a:SignUp) where a.firstName={name_a} and a.Type="student"  Return collect(distinct a.Country)'
            results = db.run(per_query, name_a=prs1[0])
            for r in results:
                per_type=r[0]
                print(per_type)
                per=(per_type)
                person.append(per)
        return person

#what city of student
    def qStdWhatPhone(self,p1,p2):
        per_type=[]
        person=[]
        prs1=[]
        prs1=p2.split(" ",1)
        print(prs1[0],"split string")
        check=""
        person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)={rl} and a.name={name_a} and b.name={name_b} return collect(distinct 1)'
        results = db.run(person_query, name_a=p1, name_b=p2,rl="meet")
        for r in results:
            check=r[0] 
        if len(check)!=0:
            print("if check is 1")
            per_query='Match(a:SignUp) where a.firstName={name_a} and a.Type="student"  Return collect(distinct a.Tel)'
            results = db.run(per_query, name_a=prs1[0])
            for r in results:
                per_type=r[0]
                print(per_type)
                per=(per_type)
                person.append(per)
        return person

#what available time of teacher
    def qStdWhatTechTime(self,p1):
        print(p1,"check available in infer")
        time1=[]
        time2=[]
        per_type=[]
        person=[]
        person_query='Match(a:SignUp) where a.name={name_a} and a.type="teacher" Return a.availablefrom, a.availableto'
        results = db.run(person_query, name_a=p1)
        print(results)
        for r in results:
            time1=r[0] 
            time2=r[1]
            per_type=(+p2+"available from: "+time1+" to "+time2+".")
            person.append(per_type)
        return person


#student check teacher email        
    def qStdWhatTechEmail(self,p1):
        print("check available in infer")
        per_type=[]
        person=[]
        person_query='Match(a:SignUp) where a.name={name_a} and a.type="teacher" Return a.Email'
        results = db.run(person_query, name_a=p1)
        # print(results)
        for r in results:
            per_type=r[0] 
            person.append(per_type)
        return person

#what city of student
    def qStdWhatTechCountry(self,p1):
        per_type=[]
        print(p1,"p1 p2")
        person=[]
        person_query='Match(a:SignUp) where a.name={name_a} and a.type="teacher" Return collect(distinct a.Country)'
        results = db.run(person_query, name_a=p1)
        for r in results:
            per_type=r[0] 
            per=(per_type)
            person.append(per)
        return person

#what city of student
    def qStdWhatTechPhone(self,p1,p2):
        per_type=[]
        print(p1,p2,"p1 p2")
        person=[]
        person_query='Match(a:SignUp) where a.name={name_a} and a.type="teacher" Return collect(distinct a.Tel)'
        results = db.run(person_query, name_a=p1, name_b=p2)
        for r in results:
            per_type=r[0] 
            per=(per_type)
            person.append(per)
        return person

    def qWhatLoc(self, p1, p2, rel):
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

    def qWhatTime(self, p1, p2, rel):
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

    def qWhatAgenda(self, p1, p2):
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

    def qWhatAgendaTime(self, p1, p2,time):
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


    def qWhatAgendaDate(self, p1, p2,date):
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


    def qWhatAgendaVenue(self, p1, p2,venue):
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

    def qWhatAgendaDateVenue(self, p1, p2,date,venue):
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

    def qWhatAgendaAll(self, p1, p2,time,date,venue):
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

    def qWhatPerPrjName(self, p1, p2):
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

    def qWhatPrjMem(self,title):
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

    def qWhatPrjName(self, p1):
        print(p1,"qwhatprojectname")
        project_list=[]
      
        data=[]
        project_query='Match (c:MeetingRecord) where c.firstSupervisor={sup} or c.secondSupervisor={sup} return collect(distinct c.title)'
        results = db.run(project_query, sup=p1)
        for r in results:
            project_list=r[0]
            #meet=("The names of project supervised by you are "+project_list+".")
            #data.append(project_list)
            data=project_list
        if len(data)==0:
            meet="You are not supervising any project"
            data.append(meet)
        return data


    def qWhatAgendaTimeVenue(self, p1, p2,time,venue):
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

    def qWhatAgendaDateTime(self, p1, p2,date,time):
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

#what city of student
    def qStdWhatTechCity(self,p1,p2):
        per_type=[]
        print(p1,p2,"p1 p2")
        person=[]
        person_query='Match(a:MeetingRecord)-[r]-(b:MeetingRecord) where type(r)="meet" and a.name={name_a} and b.name={name_b} and b.type="Teacher" Return collect(distinct b.city)'
        results = db.run(person_query, name_a=p1, name_b=p2)
        for r in results:
            per_type=r[0] 
            per=(per_type)
            person.append(per)
        return person


#rank of teacher
    def qStdWhatTechRank(self,p1):
        print(p1,p2,"check available in infer")
        per_type=[]
        person=[]
        person_query='Match(a:SignUp) where a.name={name_a} and a.type="teacher" Return a.Rank'
        results = db.run(person_query, name_a=p1)
        # print(results)
        for r in results:
            per_type=r[0] 
            person.append(per_type)
        return person







nlp = spacy.load('en_core_web_sm')







