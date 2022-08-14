import os
os.system("pip3 install sidservee amino.fix")
from os import path
import json
THIS_FOLDER = path.dirname(path.abspath(__file__)) # Current Directory path
emailfile=path.join(THIS_FOLDER,"accounts.json") 
dictlist=[]
import sidserver
import time
import aminofix as amino
app_name=""
heroku_key=""
c=sidserver.Client(app_name=app_name,key=heroku_ksy)
def threadit(acc : dict): # Defining the main 
    email=acc["email"] # Assigns the value of 
    password=acc["password"] # Assigns the 
    client=amino.Client(acc["device"])
    print(c.coin_gen(sid=client.sid,comId="3"))

def yo():
    print(f"{len(dictlist)} accounts loaded")
    for amp in dictlist:
        threadit(amp)
        
yo()  
