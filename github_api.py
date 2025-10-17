from utils import * 
from dispather import  * 
from handlers import * 
import requests 


def GetApiInfo(username):
    if (CheckUsername(username ) == False ) :
        while CheckUsername(username) == False : 
            print("Enter correct username")
            username = get_username() 
    r = requests.get("https://api.github.com/users/{username}/events".format(username = username) )
   
    try : 
        r.raise_for_status()
    except requests.exceptions.HTTPError as err : 
            print(err)
            return
    
    return r 

def GetResult (events , repos) : 
    for event , n in events.items(): 
        h = get_handler(event ,handle_unknown) 
        h(event , n , repos[event]) 


def GetEventsUser(json):
    events = {}
    for event in json : 
        if event['type'] not in events.keys() : 
            events[event['type']] = 1
        else : 
            events[event['type']] += 1
    return events

def GetReposUser(json) : 
    repos = {}
    for event in json : 
        repos[event['type']] = event['repo']['name']
    return repos

def GetUnknownEvents(events , json) : 
    unknowns = set()
    for event in json : 
        if event['type'] not in events.keys() : 
            unknowns.add(event['type'])
    return unknowns