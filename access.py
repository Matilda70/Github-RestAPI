#Get access to API

from github_api import *


def GetResult(events , repos) : 
    for event , n  in events.items() : 
        h = get_handler(event ,handle_unknown) 
        h(event , n , repos[event])
        
def GetEvents() -> None : 
    username = get_username().strip()
    json = GetApiInfo(username).json()
    if (IsEmptyJsom(json)) : 
        print("Events not found or user not authorized in github")
        return
    events = GetEventsUser(json)
    repos  = GetReposUser(json)
    unknowns = GetUnknownEvents(events , json)
    GetResult(events , repos) 
    ShowUnknowns(unknowns)
     
def main() :
    GetEvents() 
    
if __name__ == "__main__" : 
    main()











