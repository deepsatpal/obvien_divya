# pip install polyfuzz                     ###### install the module.

###   import modules ###
from polyfuzz import PolyFuzz
import pandas as pd
import numpy as np
from nltk.corpus import wordnet
from rapidfuzz import fuzz
from polyfuzz.models import BaseMatcher
import nltk
# nltk.download('omw-1.4')

# list1=["company",
#         "email",
#         "identification_number",
#         "zip_code",
#         "country",
#         "city",
#         "address",
#         "telephone_number",
#         "last_name",
#         "first_name",
#         "birth",
#         "nationality",
#         "family_name",
#         "state",
#         "citizenship", 
#         "location",
#         "vat number",
#         "place",
#         "federal",
#         "sex",
#         "employer",
#         "education",
#         "martial",
#         "fax",
#         "occupation",
#         "current"
#         ]
# ##### Taslist #####
# taslist=[{"company":"tesla "},
#         {"email address":"abc@codenomad.net "},
#         {"vat identification number":"555555 "},
#         {"postal code":" 143526"},
#         {"city":"toronto"},
#         {"country":"canada "},
#         {"address":" pata nai"},
#         {"place":" othe e "},
#         {"Telephone number":" 12345555"},
#         {"last name":"fish "},
#         {"family name":" jorge"},
#         {"first name":"jelly"},
#         {"date of birth":"13582001 "},
#         {"location":" pata nhi"},
#         {"citizenship":" pr"},
#         {"nationality":" canadian"},
#         {"federal state":"okay"}]

# ##### create a function for get synonym of word #####
# synonym={}

# def match_genre(list1):
#         global synonym
#         for genre in list1:
#                 synonym[genre]=[]
#                 for syn in wordnet.synsets(genre):
#                         for l in syn.lemmas():
#                                 synonym[genre].append(l.name())
#         # print(synonym)
# match_genre(list1)

# #### create a function for checking similarity between words ####
# doc1=[]
# doc2=[]
# def similarity_func():
#         global doc1
#         global doc2
#         for element in taslist:
#                 for i,j in element.items():
#                         doc1.append(i)
#                 for key ,value in synonym.items():                
#                         for j in value:
#                                 doc2.append(j)
#                                 model = PolyFuzz("TF-IDF")
#                                 model.match(doc1,doc2)
#                                 output=model.get_matches()
                         

#         print('==========================>ORIGINAL-OUTPUT',output)
#         df =output
#         res=df[df["Similarity"]>0.50]
#         print(',,,,,,,,,,,,,,,,,,,,,,,/RESULT',res)
#         get_value = res['From'].values
#         for i in taslist:
#                 for k , v in i.items():
#                         for i in get_value:
#                                 if k == i:
#                                         print(k,':',v)

# similarity_func()



###  List of e-application form ####

e_application_list=["surname",
                    "name",
                    "birth",
                    "place",
                    "country",
                    "current",
                    "nationality",
                    "sex",
                    "martial",
                    "occupation",
                    "employer",
                    "educational",
                    "address",
                    "zip_code",
                    "city",
                    "phone",
                    "country",
                    "fax",
                    "email"]


#### Taslist based on e-application form #####

taslist_2=[{"company":"Tesla "},
        {"email address":"abc@gmail.com "},
        {"vat identification number":"123456789"},
        {"postal code":"145623"},
        {"city":"toronto"},
        {"country":"canada "},
        {"address":"newcolony"},
        {"place":"bhjkl "},
        {"Telephone number":" 015869547845"},
        {"last name":"fish "},
        {"family name":"jorge "},
        {"first name":" jelly"},
        {"date of birth":"1245678 "},
        {"location":"uyrtuiid "},
        {"citizenship":"pr "},
        {"nationality":"canadian "},
        {"federal state":"i dont know "},
        {"surname":"123458542474544545"},
        {"surname at birth":" john"},
        {"name":"rohan"},
        {"place of birth":"punjab"},
        {"country of birth":"india"},
        {"martial status":"unmarried"},
        {"current occupation":"developer"},
        {"employer/educational":"datascience"},
        {"fax":"faxid@65673643238363767"}
        ]
#### create a function for get synonym of e-application form ####
second_synonym={}

def matcher_func():
  for words in e_application_list:
    second_synonym[words]=[]
    for syn in wordnet.synsets(words):
      for l in syn.lemmas():
        second_synonym[words].append(l.name())
matcher_func()

#### checking the similarity of words #####

def similar_func():
        doc3=[]
        doc4=[]
        for element in taslist_2:
          for keys,values in element.items():
                doc3.append(keys)
          for key ,value in second_synonym.items():                
                for j in value:
                  doc4.append(j)
                  model = PolyFuzz("TF-IDF")
                  model.match(doc3,doc4)
                  output=model.get_matches()
                      

        # print("================>ORIGINAL",output)
        df =output
        res=df[df["Similarity"]>0.50]
        print('................./RESULT',res)
        get_value=res["From"].values
        print("-----------------------------/",df)
        for d in taslist_2:
          for k  , v in d.items():
            for i in get_value:
              if k == i :
                print(k,":",v)

similar_func()