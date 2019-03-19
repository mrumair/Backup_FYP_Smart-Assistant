from neo4jrestclient import client
from py2neo import Graph
import re
import spacy
import en_core_web_sm
from dateTimeVal import *

graph1 = Graph("http://localhost:11008", username="neo4j", password="123")
  

KVBit = ""
def meet_list(p,rel):
    person_list=[]
    venue_list=[]
    time_list=[]
    date_list=[]
    meeting_list=[] 
    mlist_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name} AND type(r)={rl} AND r.name={r_name} And r.venue is not null AND r.time is not null RETURN a.name,r.venue,r.time , b.name , r.date' 
    results = graph1.run(mlist_query,rl="meet",p_name=p,r_name=rel)
    for r in results:
        person_list=r[0]
        venue_list=r[1]
        #date_list=r[2]
        time_list=r[2]
        member_list = r[3]
        date_list = r[4]
        meet=("You have meeting with "+member_list+" at "+time_list+" in "+venue_list+" on "+ str(date_list)+"!")
        meeting_list.append(meet)
    return meeting_list


def meet_list_rescheduled(p,rel):
    person_list=[]
    
    meeting_list= []
    mlist_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name} AND type(r)={rl} AND r.name={r_name} And r.venue is not null AND r.time is not null RETURN b.name' 
    results = graph1.run(mlist_query,rl="meet",p_name=p,r_name=rel)
    for r in results:
        person_list=r[0]
        print(person_list , "person_list")
        
        meet=(person_list)
        print(meet , "meet")
        meeting_list.append(meet)
        print(meeting_list , "meeting_list")
        uniquelist=[]
        for x in meeting_list:
            if x not in uniquelist:
                uniquelist.append(x)

                print(uniquelist , "Unique")
    return uniquelist




def meet_dateTime_name(p,rel):
    person_list=[]
    
    meeting_list= []
    mlist_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name} AND type(r)={rl} AND r.name={r_name} And r.venue is not null AND r.time is not null  RETURN b.name '
    results = graph1.run(mlist_query,rl="meet",p_name=p,r_name=rel )
    for r in results:
        person_list=r[0]
        


    # print(person_list , "person_list")
        
        meet=(person_list)
        meeting_list.append(meet)
    return meeting_list


def meet_dateTime_time(p,rel):

    time_list = []
   
    
    meeting_list= []
    mlist_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name} AND type(r)={rl} AND r.name={r_name} And r.venue is not null AND r.time is not null RETURN r.time ' 
    results = graph1.run(mlist_query,rl="meet",p_name=p,r_name=rel)
    for r in results:
        
        time_list = r[0]
   


    # print(person_list , "person_list")
        
        meet=(time_list)
        meeting_list.append(meet)
    return meeting_list

def meet_dateTime_date(p,rel):
    person_list=[]
    date_list =[]
    time_list = []
    venue_list = []
    
    meeting_list= []
    mlist_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name} AND type(r)={rl} AND r.name={r_name} And r.venue is not null AND r.time is not null  RETURN  r.date ' 
    results = graph1.run(mlist_query,rl="meet",p_name=p,r_name=rel )
    for r in results:
       
        date_list= r[0]
       
    


    # print(person_list , "person_list")
        
        meet=(date_list)
        meeting_list.append(meet)
    return meeting_list

def meet_dateTime_Venue(p,rel):
    
    venue_list = []
    
    meeting_list= []
    mlist_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name} AND type(r)={rl} AND r.name={r_name} And r.venue is not null AND r.time is not null  RETURN  r.venue' 
    results = graph1.run(mlist_query,rl="meet",p_name=p,r_name=rel )
    for r in results:
        venue_list = r[0]
        meet=(venue_list)
        meeting_list.append(meet)
    return meeting_list



def changeMeet(p ,  mname , time , date , venue  , stime , sdate , svenue , relName):
    print("Call Scheduling")
    print(p , mname ,time , date , venue , stime , sdate , svenue , relName , "ChangeMeet Data")
    mlist_query = 'Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name} AND b.name = {rmname} AND type(r)={rl} And r.name = {rel} And r.time = {rtime} AND r.date= {rdate} AND r.venue = {rvenue} set  r.venue={rsvenue} , r.time = {rstime} , r.date = {rsdate} return b , r, a'
    results = graph1.run(mlist_query , rel = relName , rl = "meet" , p_name = p , rtime = time , rdate = date , rvenue = venue , rmname = mname  , rstime = stime , rsdate = sdate , rsvenue = svenue)
    print(results.data())


def deleteMeet(p , mname , time , date , venue):
    mlist_query = 'Match (a:MeetingRecord)-[r]- (b:MeetingRecord) where a.name={p_name}  AND b.name = {rmname}  AND r.date = {rdate} AND r.venue = {rvenue}  And r.time = {rtime} Delete  r'
    results = graph1.run(mlist_query , rl = "meet" , p_name = p , rtime = time , rdate = date , rvenue = venue , rmname = mname)
    print(results.data())
    print("CAlled Deletion")




def TodayMeetings(p):
    person_list=[]
    venue_list=[]
    time_list=[]
    date_list=[]
    meeting_list=[] 
    CurrentDate = DTValidate.CovertDate()
    print(CurrentDate)
    mlist_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name}  AND r.date = {rdate} And r.venue is not null AND r.time is not null RETURN a.name,r.venue,r.time , b.name , r.date' 
    results = graph1.run(mlist_query,rl="meet",p_name=p , rdate = CurrentDate)
    for r in results:
        person_list=r[0]
        venue_list=r[1]
        time_list=r[2]
        member_list = r[3]
        date_list = r[4]
        meet=("You have meeting with "+member_list+" at "+time_list+" in "+venue_list+" on "+ str(date_list)+"!")
        meeting_list.append(meet)
    return meeting_list




def ReschuleMeetingList(p):
    person_list=[]
    venue_list=[]
    time_list=[]
    date_list=[]
    meeting_list=[] 
    CurrentDate = DTValidate.CovertDate()
    print(CurrentDate)
    mlist_query='Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name}  AND r.date >= {rdate} And r.venue is not null AND r.time is not null RETURN a.name,r.venue,r.time , b.name , r.date' 
    results = graph1.run(mlist_query,rl="meet",p_name=p , rdate = CurrentDate)
    for r in results:
        person_list=r[0]
        venue_list=r[1]
        time_list=r[2]
        member_list = r[3]
        date_list = r[4]
        meet=("You have meeting with "+member_list+" at "+time_list+" in "+venue_list+" on "+ str(date_list)+"!")
        meeting_list.append(meet)
    return meeting_list

def KnowledgeValidate(p , time , date , venue  , relName):
    print("Call Knowledge")
    print(p ,time , date , venue ,  relName , "ChangeMeet Data")
    mlist_query = 'Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name}  AND type(r)={rl} And r.name = {rel} And r.time = {rtime} AND r.date= {rdate} AND r.venue = {rvenue} return b , r, a'
    results = graph1.run(mlist_query , rel = relName , rl = "meet" , p_name = p , rtime = time , rdate = date , rvenue = venue  )
    if not results.data():
        print("List is empty")
        KVBit = 0
    else:
        KVBit =1
    print(results.data())
    print(KVBit)
    return KVBit



nlp = spacy.load('en_core_web_sm')

KnowledgeValidate ('abcd' , '16:20' , '16 March 2019','PU' , 'meeting')
