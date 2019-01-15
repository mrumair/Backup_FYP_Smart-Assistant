#from spacy import displacy

#nlp = spacy.load('en_core_web_sm')
#text = u"""In ancient Rome, some neighbors live in three adjacent houses. In the center is the house of Senex, who lives there with wife Domina, son Hero, and several slaves, including head slave Hysterium and the musical's main character Pseudolus. A slave belonging to Hero, Pseudolus wishes to buy, win, or steal his freedom. One of the neighboring houses is owned by Marcus Lycus, who is a buyer and seller of beautiful women; the other belongs to the ancient Erronius, who is abroad searching for his long-lost children (stolen in infancy by pirates). One day, Senex and Domina go on a trip and leave Pseudolus in charge of Hero. Hero confides in Pseudolus that he is in love with the lovely Philia, one of the courtesans in the House of Lycus (albeit still a virgin)."""
#doc = nlp(text)
#sentence_spans = list(doc.sents)
#displacy.serve(sentence_spans, style='dep')

from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from py2neo.cypher import cypher_escape
db = GraphDatabase("http://localhost:7474", username="neo4j", password="neo4j")
 
# Create some nodes with labels

s = "Marco"
q = '"MATCH (a)-[:%s]->(b) RETURN a, b" % cypher_escape(rel_type)'
# "db" as defined above
results = db.query(q, returns=(client.Node, str, client.Node))
for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))

