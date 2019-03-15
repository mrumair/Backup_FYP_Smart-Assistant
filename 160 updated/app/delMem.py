from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from meetList import *
import en_core_web_sm

class Del_spacy:
    def function_del_spacy(gloVar , docx12):
        relationpropertydate = ""
        institute = ""
        timeProperty = ""

        value_doc = docx12
        nlp = spacy.load('en_core_web_sm')
        docx1 = nlp(value_doc)
#docx1 = nlp("I am Rabeeya Saleem and have a meeting with Taliah Tajammal at 8pm on 22 december in PU")
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
        #       post.functiona(organization)
            if entity is 'LOC':
                location = token.text
                print(location , "is an location")
        #       post.functiona(location)
            if entity is 'DATE':
                date = token.text
                print(date , "is a Date")
                relationpropertydate = date
             
        #       post.functiona(date)
            if entity is 'PERSON':
                
                person = token.text
                print(person , "is a person")
                personData = person
                print(personData)
                #post.functiona(person)

                
                #entity1 = token.text

            if entity is 'NORP':
                nationalities = token.text
                print(nationalities , "is a nationality")
        #       post.functiona(nationalities)

            if entity is 'FAC':
                fac = token.text
                print(fac , "is a building")
        #       post.functiona(fac)

            if entity is 'GPE':
                gpe = token.text
                print(gpe , "is a institute")
                institute = gpe
        #       post.functiona(gpe)

            if entity is 'PRODUCT':
                produxt = token.text
                print(produxt , "is a product")
        #       post.functiona(product)

            if entity is 'EVENT':
                event = token.text
                print(event , "is a event")
        #       post.functiona(event)

            if entity is 'WORK_OF_ART':
                woa = token.text
                print(woa , "is a work of art")
        #       post.functiona(woa)

            if entity is 'LAW':
                law = token.text
                print(law , "is a Law")
        #       post.functiona(law)

            if entity is 'LANGUAGE':
                lang = token.text
                print(lang , "is a Language")
        #       post.functiona(lang)

            if entity is 'TIME':
                # time = token.text
                # print(time , "is a Time")

                # timeProperty = time

                time = token.text
                print(time , "is a Time")
                timeProperty = time
                

            print(entity)
            if entity is 'PERCENT':
                percent = token.text
                print(percent , "is a percent")
        #       post.functiona(percent)

            if entity is 'MONEY':
                money = token.text
                print(money , "is a money")
        #       post.functiona(money)

            if entity is 'QUANTITY':
                quant = token.text
                print(quant , "is a quantity")
        #       post.functiona(quant)

            if entity is 'ORDINAL':
                ordinal = token.text
                print(ordinal , "is a ordinal")
        #       post.functiona(ordinal)

            if entity is 'CARDINAL':
                cardinal = token.text
                print(cardinal , "is a CARDINAL")
        #       post.functiona(cardinal)

        print(institute)
        print(timeProperty)
        print(relationpropertydate)
        print(person)
        print(gloVar )


        deleteMeet(gloVar , person , timeProperty , relationpropertydate , institute )


    
        

Del_spacy.function_del_spacy("Rabeeya" ,"You have meeting with Safa Zahoor at 18:30 in UET on 15 April 2019!")
