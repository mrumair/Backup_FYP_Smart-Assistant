
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
