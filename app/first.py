import spacy

from spacy import displacy 
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I am student in Uet. You Learn more from failure than success. The purpose of Software engineering is to control complexoity , not to create it and spacy is more cool and easy than NLTK that is also an NLP tool')
#for num , sentence  in enumerate(doc.sents):
 #   print(f' {num} :{sentence}')


#for token in doc:
 #   print(token.text)


#[token.text for token in doc ]
#doc.text.split(" ")


#for word in doc:
#	print(word.text , word.shape)
#	print(word.text , word.shape_)

#ex_doc = nlp("Hello hello HELLO HeLLO")
#for word in ex_doc:
	#print(word.text , word.shape_)
#	print("Token =>" , word.text , "SHAPE IS " , word.shape_ , word.is_alpha , word.is_stop)

#ex1 = nlp("He drinks a drink")
#ex1 = nlp ("I fish a fish")
#for word in ex1:
#	print(word.text , word.pos_ , word.tag_)


#exercies1 = nlp("all the faith he had had had had no effect on outcome of his life")

#for word in exercies1:
#	print((word.text , word.tag_ , word.pos_))
#exercies2 = nlp ("The man the professor the student has studied room.")


#ex3 = nlp ("Rabeeya likes Hanan")
#for word in ex3  :
#	print((word.text , word.tag_ , word.pos_ , word.dep_))

#displacy.render(ex3 , style = 'dep', jupyter = True)

#docs = nlp ("study studying studious studio student")
#docs = nlp("I live in Lahore and Studied in UET since 2015 and i use Internet and i have meeting with Hanan tomorrow")
#for word in docs:
#	print(word.text , word.lemma_ , word.pos_)
#for word in docs.ents:
#	print(word.text , word.label_)
#displacy.render(doc , style = "ent" , jupyter= True)


inputs = []
for i in range();
    x = raw_input()
    inputs.append(x)


# print all inputs
for inp in inputs:
    print(inp)

# Access a specific input
print(inp[0])
print(inp[1])