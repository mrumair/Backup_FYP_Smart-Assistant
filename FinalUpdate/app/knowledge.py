from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from meetList import *
import en_core_web_sm

cBit3 = 3
class kv_spacy:

    def __init__(self ):

        self.cBit2 = 0

    def foo(self):
        cBit3=self.cBit2
        return cBit3

#FUNCTION FOR KNOWLEDGE VALIDATION DURING SCHEDULING OF NEXT MEETING AFTER PROCESSING THE USER INPUT
    def function_kv_spacy(gloVar , docx12):
        cBit3 = 0
        relationpropertydate = ""
        institute = ""
        timeProperty = ""
        person = ""
        value_doc = docx12
        nlp = spacy.load('en_core_web_sm')
        docx1 = nlp(value_doc)
        for token in docx1:
            subject = (token.text , token.pos_ , token.tag_ , token.dep_)
            print(subject )
            pos = (token.pos_)
            if pos is 'PRON'  :
                nodetodraw = token.text
                print(nodetodraw , "is node")
        for token in docx1.ents:
            entity = (token.label_ )
            if entity is 'ORG':
                organization = token.text
                print(organization , "is an organization")
                institute = organization
            if entity is 'LOC':
                location = token.text
                print(location , "is an location")
            if entity is 'DATE':
                date = token.text
                print(date , "is a Date")
                relationpropertydate = date
            if entity is 'PERSON':
                
                person = token.text
                print(person , "is a person")
                personData = person
                print(personData)
            if entity is 'NORP':
                nationalities = token.text
                print(nationalities , "is a nationality")

            if entity is 'FAC':
                fac = token.text
                print(fac , "is a building")

            if entity is 'GPE':
                gpe = token.text
                print(gpe , "is a institute")
                institute = gpe

            if entity is 'PRODUCT':
                produxt = token.text
                print(produxt , "is a product")
            if entity is 'EVENT':
                event = token.text
                print(event , "is a event")
            if entity is 'WORK_OF_ART':
                woa = token.text
                print(woa , "is a work of art")
            if entity is 'LAW':
                law = token.text
                print(law , "is a Law")

            if entity is 'LANGUAGE':
                lang = token.text
                print(lang , "is a Language")
            if entity is 'TIME':

                time = token.text
                print(time , "is a Time")
                timeProperty = time
                

            print(entity)
            if entity is 'PERCENT':
                percent = token.text
                print(percent , "is a percent")

            if entity is 'MONEY':
                money = token.text
                print(money , "is a money")

            if entity is 'QUANTITY':
                quant = token.text
                print(quant , "is a quantity")

            if entity is 'ORDINAL':
                ordinal = token.text
                print(ordinal , "is a ordinal")
            if entity is 'CARDINAL':
                cardinal = token.text
                print(cardinal , "is a CARDINAL")

        print(institute)
        print(timeProperty)
        print(relationpropertydate)
        print(person)
        print(gloVar)
        #CALL THE FUNCTION OF KNOWLEDGE VALIDATE
        cBit2 = KnowledgeValidate(gloVar , timeProperty , relationpropertydate , institute , 'meeting')
        print(cBit2)

        return cBit2





    
        


# kv_spacy.function_kv_spacy ("abcd" ,"You have meeting with Safa Zahoor at 16:20 in PU on 14 March 2019!" )
