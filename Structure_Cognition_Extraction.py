#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter.filedialog import *
from tkinter.messagebox import *
import chardet
from gensim import corpora, models
#from settings import stopwords
import codecs
import sys, os
import os.path
import nltk
import re
import requests
import numpy
from numpy import *
import nltk
import scipy
from tkinter import Tk
from tkinter.filedialog import *
from tkinter.messagebox import *
from settings import stem
from nltk.corpus import stopwords
from nltk.stem import  SnowballStemmer

stemmer = SnowballStemmer(stem)
import matplotlib.pyplot as plt
import matplotlib as mpl

#________________________________________________________________________________
# TASK EXECUTION ASPECTS:

# Step 2. Structure and Cognition Aspect Extraction

# MAIN STAGES:
# STAGE 1. DML taxonomy (RTCC) (1.1.) Reading and (1.2) Stemming
# STAGE 2. Tasks Corpus Reading, Preprocessing and English language filtering
# STAGE 3. Find and Count words in the Task that match the DML Taxonomy keywords
# STAGE 4. Writing of Matched words and their Number in the *.csv file
#_________________________________________________________________________________

def word_count(stopword):

#___________________STAGE 1.1. Reading DML taxonomy (RTCC)________________________    
#____________________Capacities (Adjectives)_____________________________________ 
   path='C:/Users/DML_Tasks/Adjectives'
   
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'CognitiveAdjectives.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   C_Adj=s1
   
   BC_Adj = [1 for i in range(len(s1))]
   print(BC_Adj)
   
  #________________________________________________________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'RoutineAdjectives.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   R_Adj=s1
   BR_Adj = [1 for i in range(len(s1))]
   #________________________________________________________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'SemiCognitiveAdjectives.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   SC_Adj=s1
   BSC_Adj = [1 for i in range(len(s1))]
   #print(BSC_Adj)

#____________________Choices (Adverbs)____________________________________________________
   
   path='C:/Users/ninar/DML_Tasks/Adverbs'
   
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'CognitiveAdverbs.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   C_Adv=s1
   BC_Adv = [1 for i in range(len(s1))]
  #________________________________________________________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'RoutineAdverbs.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   R_Adv=s1
   BR_Adv = [1 for i in range(len(s1))]
   #________________________________________________________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'SemiCognitiveAdverbs.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   SC_Adv=s1
   BSC_Adv = [1 for i in range(len(s1))]

#____________________Resources (Nouns)____________________________________________________
   
   path='C:/Users//DML_Tasks/Nouns'
   
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'CognitiveNouns.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   C_Noun=s1
   BC_Noun = [1 for i in range(len(s1))]
  #________________________________________________________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'RoutineNouns.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   R_Noun=s1
   BR_Noun = [1 for i in range(len(s1))]
   #________________________________________________________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'SemiCognitiveNouns.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   SC_Noun=s1
   BSC_Noun = [1 for i in range(len(s1))]

#____________________Techniques (Verbs)____________________________________________________
   
   path='C:/Users/DML_Tasks/Verbs'
   
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'CognitiveVerbs.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   C_Verb=s1
   BC_Verb = [1 for i in range(len(s1))]
  #________________________________________________________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'RoutineVerbs.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   R_Verb=s1
   BR_Verb = [1 for i in range(len(s1))]
   #________________________________________________________
   a1=sorted(os.listdir(path))
   for i in a1[0:1]:
      filename=path+'/'+'SemiCognitiveVerbs.txt'
      #print(filename)
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         d={}
         s1=[]
         
                     
         for line in file_object:
            line = line.rstrip('\n\r')
            #print(line)
            s1.append(line)
   #print(s1)
   SC_Verb=s1
   BSC_Verb = [1 for i in range(len(s1))]
   
   #_________________________________________________________ 
   k_b=0
   path='C:/Users/Texts'
   k=0
   fb=open('C:/Users/DML_Statistics.doc', 'wb')
   a=sorted(os.listdir(path))
   
#___________________STAGE 1.2. Stemming DML taxonomy (RTCC)_______________________________________   
   #k_w=0
   #k_o=0
   
   C_Adj_stem=[stemmer.stem(w).lower() for w in C_Adj if len(w) >1 and w.isalpha()]
   R_Adj_stem=[stemmer.stem(w).lower() for w in R_Adj if len(w) >1 and w.isalpha()]
   SC_Adj_stem=[stemmer.stem(w).lower() for w in SC_Adj if len(w) >1 and w.isalpha()]
   C_Adv_stem=[stemmer.stem(w).lower() for w in C_Adv if len(w) >1 and w.isalpha()]
   R_Adv_stem=[stemmer.stem(w).lower() for w in R_Adv if len(w) >1 and w.isalpha()]
   SC_Adv_stem=[stemmer.stem(w).lower() for w in SC_Adv if len(w) >1 and w.isalpha()]
   C_Noun_stem=[stemmer.stem(w).lower() for w in C_Noun if len(w) >1 and w.isalpha()]
   R_Noun_stem=[stemmer.stem(w).lower() for w in R_Noun if len(w) >1 and w.isalpha()]
   SC_Noun_stem=[stemmer.stem(w).lower() for w in SC_Noun if len(w) >1 and w.isalpha()]
   C_Verb_stem=[stemmer.stem(w).lower() for w in C_Verb if len(w) >1 and w.isalpha()]
   R_Verb_stem=[stemmer.stem(w).lower() for w in R_Verb if len(w) >1 and w.isalpha()]
   SC_Verb_stem=[stemmer.stem(w).lower() for w in SC_Verb if len(w) >1 and w.isalpha()]

#_________STAGE 2. Tasks Corpus Reading, Preprocessing and English language filtering ______________
   
  
   for i in a[0:124733]:
      print('# Doc'+str(i))
      e=[]
      enc=0
      
      filename=path+'/'+str(i)
      
      with codecs.open(filename, encoding = 'UTF-8') as file_object:
         
         for line in file_object:
            line = line.rstrip('\n')
            a = line.strip()
            #print(a)
            
            if len(a)==0:
               enc=enc+1
            
            if enc==0:
            
               if len(line.strip())!=0:
                  
                  k=k+1
                  text=line.strip()
                  text=text.lower()
                                    
                  text1=''
                  text2=''
                  text3=''
                  text4=''
                  text5=''
                  text6=''
                  text7=''
                  text8=''
                  text9=''
                  text10=''
                  text11=''
                  text12=''
                  text13=''
                  
                  word=nltk.word_tokenize(text)
                  ooo=len(word)
                  filename1=str(i)
                  fb.write(bytes(str(filename1)+'. '+str(ooo)+'.', 'UTF-8'))
                  word_stem=[stemmer.stem(w).lower() for w in word if len(w) >1 and w.isalpha()]
                  #print(word_stem)
                  stopWordsG = set(stopwords.words('english'))
                  stopword=[stemmer.stem(w).lower() for w in stopWordsG]

                  stopwords_e = [w for w in word_stem if w in stopword]
                  n_eng=len(stopwords_e) / len(word) * 100
                  #print(n_eng)
                  stopWordsG = set(stopwords.words('german'))
                  stopwords_g = [w for w in word_stem if w in stopWordsG]
                  n_ger=len(stopwords_g) / len(word) * 100
                  #print(n_ger)
                  if n_ger>n_eng:
                     kkk="German"
                  else:
                     kkk="English"
                  #print(kkk)
                  word_stop=[ w for w in word_stem if w not in stopword]
                  
                  m=word_stop
                  #print(m)
                  da={}
                  ds={}
                  dv={}
                  d={}
                  b=[]
                  oo1=[]
                  oo2=[]
                  oo3=[]
                  oo4=[]
                  oo5=[]
                  oo6=[]
                  oo7=[]
                  oo8=[]
                  oo9=[]
                  oo10=[]
                  oo11=[]
                  oo12=[]
                  yy=[]

# ________STAGE 3. Find and count words in the Task  that match the DML Taxonomy keywords_________
                  try:
                     #print("lll")
                     oo1=[w for w in m if w in C_Adj_stem]
                     #print(oo1)
                     b.append(sum([BC_Adj[C_Adj_stem.index(w)] for w in m  if w in C_Adj_stem]))
                     #print("b=",b)
                     yy.append(sum([m.count(w) for w in C_Adj_stem]))
                     
                     #print('C_Adj=',  yy[0])
                  except:
                     pass
                  try:
                     b.append(sum([BR_Adj[R_Adj_stem.index(w)] for w in m  if w in R_Adj_stem]))
                     oo2=[w for w in m  if w in R_Adj_stem]
                     #print(oo2)
                     #print("b=",b)
                     text5 = re.findall(r'preapproved', text)
                     if text5!='':
                        oo2.append(text5)
                     text6 = re.findall(r'pre-approved', text)
                     if text6!='':
                        oo2.append(text6)
                     text7 = re.findall(r'pre approved', text)
                     if text7!='':
                        oo2.append(text7)
                     text13 = re.findall(r'offline change', text)
                     if text13!='':
                        oo2.append(text13)
                     
                     #print(oo2)
                     a3=len(text5+text6+text7+text13)
                     yy.append(sum([m.count(w) for w in  R_Adj_stem])+a3)
                     #print('R_Adj=', yy[1])
                  except:
                     pass
                  try:
                     b.append(sum([BSC_Adj[SC_Adj_stem.index(w)] for w in m  if w in SC_Adj_stem]))
                     oo3=[w for w in m  if w in SC_Adj_stem]
                     #print(oo3)
                     #print("b=",b)
                     yy.append(sum([m.count(w) for w in  SC_Adj_stem]))
                     #print('SC_Adj=',  yy[2])
                  except:
                     pass      
                  try:
                     b.append(sum([BC_Adv[C_Adv_stem.index(w)] for w in m  if w in C_Adv_stem]))
                     oo4=[w for w in m  if w in C_Adv_stem]
                     #print(oo4)
                     #print("b=",b)
                     yy.append(sum([m.count(w) for w in  C_Adv_stem]))
                     #print('C_Adv=', yy[3])
                     #print(yy)
                  except:
                     pass
                  try:
                     b.append(sum([BR_Adv[R_Adv_stem.index(w)] for w in m  if w in R_Adv_stem]))
                     oo5=[w for w in m  if w in R_Adv_stem]
                     #print(oo5)
                     #print("b=",b)
                     
                     yy.append(sum([m.count(w) for w in  R_Adv_stem]))
                     #print('R_Adv=', yy[4])
                     #print(yy)
                  except:
                     pass
                  try:
                     b.append(sum([BSC_Adv[SC_Adv_stem.index(w)] for w in m  if w in SC_Adv_stem]))
                     oo6=[w for w in m  if w in SC_Adv_stem]
                     #print(oo6)
                     #print("b=",b)
                     yy.append(sum([m.count(w) for w in  SC_Adv_stem]))
                     #print('SC_Adv=', yy[5])
                     #print(yy)
                  except:
                     pass
                  try:
                     b.append(sum([BC_Noun[C_Noun_stem.index(w)] for w in m  if w in C_Noun_stem]))
                     oo7=[w for w in m  if w in C_Noun_stem]
                     #print(oo7)
                     #print("b=",b)
                     text1 = re.findall(r'hotfix pso offline downtime', text)
                     if text1!='':
                        oo7.append(text1)
                     text8 = re.findall(r'pse', text)
                     if text8!='':
                        oo7.append(text8)
                     text9 = re.findall(r'ccab', text)
                     if text9!='':
                        oo7.append(text9)
                     text10 = re.findall(r'cab', text)
                     if text10!='':
                        oo7.append(text10)
                     text11 = re.findall(r'it-serverfarm', text)
                     if text11!='':
                        oo7.append(text11)
                     text12 = re.findall(r'switch', text)
                     if text12!='':
                        oo7.append(text12)
                     a2=len(text1+text8+text9+text10+text11+text12)
                     yy.append(sum([m.count(w) for w in  C_Noun_stem])+a2)
                     #print('C_Noun=', yy[6])
                     #print(yy)
                  except:
                     pass
                  try:
                     b.append(sum([BR_Noun[R_Noun_stem.index(w)] for w in m  if w in R_Noun_stem]))
                     oo8=[w for w in m  if w in R_Noun_stem]
                     #print(oo8)
                     #print("b=",b)
                     text2 = re.findall(r'no PSO', text)
                     text3 = re.findall(r'no impact', text)
                     text4 = re.findall(r'no downtime', text)
                     a2=len(text2+text3+text4)
                     yy.append(sum([m.count(w) for w in  R_Noun_stem])+a2)
                     #print('R_Noun=', yy[7])
                     #print(yy)
                  except:
                     pass
                  try:
                     b.append(sum([BSC_Noun[SC_Noun_stem.index(w)] for w in m  if w in SC_Noun_stem]))
                     oo9=[w for w in m  if w in SC_Noun_stem]
                     #print(oo9)
                     #print("b=",b)
                     
                     yy.append(sum([m.count(w) for w in  SC_Noun_stem]))
                     #print('SC_Noun=', yy[8])
                     #print(yy)
                  except:
                     pass
                  try:
                     b.append(sum([BC_Verb[C_Verb_stem.index(w)] for w in m  if w in C_Verb_stem]))
                     oo10=[w for w in m  if w in C_Verb_stem]
                     #print(oo10)
                     #print("b=",b)
                     yy.append(sum([m.count(w) for w in  C_Verb_stem]))
                     #print('C_Verb=', yy[9])
                     #print(yy)
                  except:
                     pass
                  try:
                     b.append(sum([BR_Verb[R_Verb_stem.index(w)] for w in m  if w in R_Verb_stem]))
                     oo11=[w for w in m  if w in R_Verb_stem]
                     #print(oo11)
                     #print("b=",b)
                     yy.append(sum([m.count(w) for w in  R_Verb_stem]))
                     #print('R_Verb=', yy[10])
                     #print(yy)
                  except:
                     pass
                  try:
                     b.append(sum([BSC_Verb[SC_Verb_stem.index(w)] for w in m  if w in SC_Verb_stem]))
                     oo12=[w for w in m  if w in SC_Verb_stem]
                     #print(oo12)
                     #print("b=",b)
                     yy.append(sum([m.count(w) for w in  SC_Verb_stem]))
                     #print('SC_Verb=', yy[11])
                     #print(yy)
                  except:
                     pass
                  #print(b)
                  ee=max(b)

#___________________STAGE 4 Writing of Matched words and their number in the *csv file____________________________

                  fb.write(bytes('num. length. lang. CognitiveAdjectives. Words. RoutineAdjectives.Words. SemiCognitiveAdjectives.Words.CognitiveAdverbs.Words.RoutineAdverbs.Words.SemiCognitiveAdverbs.Words.CognitiveNouns.Words.RoutineNouns.Words.SemiCognitiveNouns.Words.CognitiveVerbs.Words.RoutineVerbs.Words.SemiCognitiveVerbs. Words'+'\n', 'UTF-8'))
                  fb.write(bytes(str(kkk)+'.'+str(yy[0])+'.'+str(oo1)+'.'+str(yy[1])+'.'+str(oo2)+'.'+str(yy[2])+'.'+str(oo3)+'.'+str(yy[3])+'.'+str(oo4)+'.'+str(yy[4])+'.'+str(oo5)+'.'+str(yy[5])+'.'+str(oo6)+'.'+str(yy[6])+'.'+str(oo7)+'.'+str(yy[7])+'.'+str(oo8)+'.'+str(yy[8])+'.'+str(oo9)+'.'+str(yy[9])+'.'+str(oo10)+'.'+str(yy[10])+'.'+str(oo11)+'.'+str(yy[11])+'.'+str(oo12), 'UTF-8'))
                  fb.write(bytes('\n', 'UTF-8'))
 
                     
       
   
   fb.close()
   
stopwords1=['the', 'a', 'in ', 'for', 'to', 'of', 'and', 'ABC', 'of', 'on', 'at', 
         'or', 'if', 'end', 'were','each', 'was', 'as','has', 'how', 'it', 
           'may', 'often', 'be',  'done', 'these', 'all', 'etc', 'made',
          'make', ' the', 'about', 'also', 'always', 'as', 'can',
           'but', 'do', 'get', 'go', 'how', 'is', 'it',  'just', 'lot', 'able',
           'off', 'them', 'they', 'this', 'thus',  'up', 'us', 'very',
           'why', 'your', 'need', ' must', 'now', 'so', 'some',
           'became', 'still', 'stay', 'take', 'took', 'want', 'say',
           'while', 'who', 'you', 'thank', 'new', 'psi', 'busy', 'any',
           'only','a','about','above','after','again','against','all','am','an',
           'and','any','are','aren’t','as','at','be','because','been','before',
           'being','below','between','both','but','by','can’t','cannot','could',
           'couldn’t','did','didn’t','do','does','doesn’t','doing','don’t','down','during',
           'each','few','for','from','further','had','hadn’t','has','hasn’t','have','haven’t',
           'having','he','he’d','he’ll','he’s','her','here','here’s','hers','herself','him','himself',
           'his','how','how’s','i','I’d','I’ll','I’m','I’ve','if','in','into','is','isn’t','it','it’s','its','itself',
           'let’s','me','more','most','mustn’t','my','myself','no','nor','not','of','off','on','once',
           'only','or','other','ought','our','ours','ourselves','out','over','own','same','shan’t',
           'she','she’d','she’ll','she’s','should','shouldn’t','so','some','such','than','that','that’s',
           'the','their','theirs','them','themselves','then','there','there’s','these','they','they’d',
           'they’ll','they’re','they’ve','this','those','through','to','too','under','until','up','very',
           'was','wasn’t','we','we’d','we’ll','we’re','we’ve','were','weren’t','what','what’s','when',
           'when’s','where','where’s','which','while','who','who’s','whom','why','why’s','with','won’t',
           'would','wouldn’t','you','you’d','you’ll','you’re','you’ve','your','yours','yourself','yourselves'
           'get', 'our', 'out', 'set', 'such', 'take', 'have', 'did',
           'than', 'their', 'then', 'well', 'in', 'when', 'his', 'even',
           'what', 'due', 'via', 'from', 'do', 'does', 'thus', 'sit',
           'he', 'an', 'over', 'had', 'would', 'whoever', 'after',
           'with', 'which', 'within', 'where', 'come', 'more',
           'there', 'their', 'be', 'between', 'been',  'through',
           'can', 'is', 'this', 'we', 'will', 'give', 'without', 'by',  'itself', 'http'
           'about', 'does', 'not', 'that', 'no', 'but', 'are', 'keep','mr', 'ms', 'ayakkab', 'allah', 'bunyamin', '\ufeff']
stem='english'


word_count(stopwords)
