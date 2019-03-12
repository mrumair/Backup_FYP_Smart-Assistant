from neo4jrestclient import client
from py2neo import Graph
import re
import spacy
import en_core_web_sm
from dateTimeVal import *

graph1 = Graph("http://localhost:11012", username="neo4j", password="neo4j")
  

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



def changeMeet(p , rel , mname , time , date , venue  , sname , stime , sdate , svenue):
    mlist_query = 'Match (a:MeetingRecord)-[r]-(b:MeetingRecord) where a.name={p_name} and b.name = {rmname} AND type(r)={rl} AND r.name={r_name} And r.time = {rstime} AND r.date= {rsdate} AND r.venue = {rsvenue} set  r.venue={rvenue} , r.time = {rtime} , r.date = {rdate} return b , r, a'
    results = graph1.run(mlist_query , rl = "meet" , p_name = p , r_name = rel , rtime = time , rdate = date , rvenue = venue , rmname = mname  , rsname = sname , rstime = stime , rsdate = sdate , rsvenue = svenue)
    print(results.data())


def deleteMeet(p , mname , time , date , venue):
    mlist_query = 'Match (a:MeetingRecord)-[r]- (b:MeetingRecord) where a.name={p_name}  AND b.name = {rmname}  AND r.date = {rdate} AND r.venue = {rvenue}  And r.time = {rtime} Delete  r'
    results = graph1.run(mlist_query , rl = "meet" , p_name = p , rtime = time , rdate = date , rvenue = venue , rmname = mname)
    print(results.data())
    print("CAlled Deletion")


def TodayMeet(p ):
    person_list= []
    venue_list = []
    time_list = []
    date_list = []
    Member_List = []
    meeting_list= []

    CurrentDate = DTValidate.CovertDate()
    print(CurrentDate)
    
    mlist_query = 'Match (a:MeetingRecord)-[r]- (b:MeetingRecord) where a.name={p_name}  AND r.date = {rdate} return  a.name  , r.date , r.time , r.venue , b.name'
    results = graph1.run(mlist_query  , p_name = p , rdate = CurrentDate)
    print(results.data())
    print('Todays Meeting')
    for r in results:
        person_list=r[0]
        venue_list=r[1]
        #date_list=r[2]
        time_list=r[2]
        Member_List = r[3]
        date_list = r[4]
        meet=("You have meeting with "+member_list+" at "+time_list+" in "+venue_list+" on "+ str(date_list)+"!")
        meeting_list.append(meet)
    return meeting_list


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


def KnowledgeValidate(p , date , time ):
    mlist_query = ''


nlp = spacy.load('en_core_web_sm')

meet_list('abcd'  , 'meeting')
