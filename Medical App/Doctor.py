import nltk
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import random
import string
import mysql.connector
import threading



f=open('try.txt' ,'r' ,errors ='ignore')
m=open('modules.txt' ,'r' ,errors = 'ignore')
checkpoint = "./chatbot_weights.ckpt"

raw=f.read()
rawone=m.read()
raw=raw.lower()
rawone=rawone.lower()
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
sent_tokensone = nltk.sent_tokenize(rawone) 
word_tokensone = nltk.word_tokenize(rawone)

sent_tokens[:2]
sent_tokensone[:2]

word_tokens[:5]
word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="hospital_db"
    )

mycursor = mydb.cursor()
sql = "SELECT * FROM patient_data"
mycursor.execute(sql)
myresult = mycursor.fetchone()

def save():
            mycursor = mydb.cursor()
            sql = "INSERT INTO patient_data (Report) VALUES (%s)"
            val =(chat.get())
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            


GREETING_INPUTS = ("hello", "hi","hii","greetings", "sup","hey","sap")
GREETING_RESPONSES = ["hi " +myresult[3] + ", checking of Vitals please( Weight(kg) )", "hey " +myresult[3] + ", checking of Vitals please( Weight(kg) )","hi there " +myresult[3] + ", checking of Vitals please( Weight(kg) )", "hello " +myresult[3] + ", checking of Vitals please( Weight(kg) )"]
NURSE_W =["25kg","26kg","27kg","28kg","29kg","30kg","31kg","32kg","33kg","34kg","35kg","36kg","37kg","38kg","39kg","40kg","41kg","42kg","43kg","43kg","44kg","45kg","46kg","47kg","48kg","49kg","50kg","51kg","52kg","53kg","54kg","55kg","56kg","57kg","58kg","59kg","60kg","61kg","62kg","63kg","64kg","65kg","66kg","67kg","68kg","69kg","70kg","71kg","72kg","73kg","74kg","75kg","76kg","77kg","78kg","79kg","80kg"]
NURSE_K = ["Please input your Temperature ºC"]
NURSE_T =["36c","37c"]
NURSE_R = ["Your Temperature is normal, Please input Blood Pressure (bp)"]
NURSE_TH = ["38c","39c","40c","41c","42c"]
NURSE_RH = ["Your Temperature is High (Patient need infusion), Please input Blood Pressure (bp)"]
NURSE_TL = ["28c","29c","30c","31c","32c","33c","34c","35c",]
NURSE_RL = ["Your Temperature is Low (Patient need Tsiponshi), Please input Blood Pressure (bp)"]
NURSE_BN =["70bp","71bp","72bp","73bp","74bp","75bp","76bp","77bp","78bp","79bp","80bp","81bp","82bp","83bp","84bp","85bp","86bp","87bp","88bp","89bp","90bp"]
NURSE_BNR = ["Your Blood Pressure is Normal.  " + myresult[3] + ", What wrong with you?"]
LAB_T = ["p","P","positive","POSITIVE"]
LAB_R =["POSITIVE, Please input the test result"]
LAB_TN = ["n","N","negative","NEGATIVE"]
LAB_RN = ["NEGATIVE, Please input the test result"]






def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def NURSE(sentence):
    for word in sentence.split():
        if word.lower() in NURSE_W:
            return random.choice(NURSE_K)

def Temp(sentence):
    for word in sentence.split():
        if word.lower() in NURSE_T:
            return random.choice(NURSE_R)

def TempHigh(sentence):
    for word in sentence.split():
        if word.lower() in NURSE_TH:
            return random.choice(NURSE_RH)

def TempLow(sentence):
    for word in sentence.split():
        if word.lower() in NURSE_TL:
            return random.choice(NURSE_RL)

def BloodP(sentence):
    for word in sentence.split():
        if word.lower() in NURSE_BN:
            return random.choice(NURSE_BNR)

def LabT(sentence):
    for word in sentence.split():
        if word.lower() in LAB_T:
            return random.choice(LAB_R)

def Lab2(sentence):
    for word in sentence.split():
        if word.lower() in LAB_TN:
            return random.choice(LAB_RN)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response



def responseone(user_response):
    robo_response=''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokensone[idx]
        return robo_response



def chat(user_response):
    user_response=user_response.lower()
    keyword = " Malaria "
    keywordone = " Cholera "


    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            return "You are welcome.."
        else:
            if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1):
                return responseone(user_response)
                sent_tokensone.remove(user_response)

            elif(greeting(user_response)!=None):
                return greeting(user_response)
            elif(NURSE(user_response)!=None):
                return NURSE(user_response)
            elif(Temp(user_response)!=None):
                return Temp(user_response)
            elif(TempHigh(user_response)!=None):
                return TempHigh(user_response)
            elif(TempLow(user_response)!=None):
                return TempLow(user_response)
            elif(BloodP(user_response)!=None):
                return BloodP(user_response)
            elif(LabT(user_response)!=None):
                return LabT(user_response)
            elif(Lab2(user_response)!=None):
                return Lab2(user_response)
            else:
                return response(user_response)
                sent_tokens.remove(user_response)
    


    else:
        flag=False
        return "Bye! take care.."
    save()

    
        
        
        
