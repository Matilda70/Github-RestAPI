#Get access to API

import requests 


def CheckUsername(username) -> bool :
    with open ("github_reserved_names.txt" , "r" ) as file : 
        for line in file : 
            if username == line : 
                return False 
    file.close()
    if (username == "" or username[0].isalpha() == False or username[0].isdigit() == True or len(username) > 39 or len(username) < 1
        or username[-1] == '-' or username[0] == '-' or username.find('--') != -1 ) : 
        return False
    return True 


def GetEvents(request) -> None : 
    json = request.json()
    res = {}
    for event in json : 
        if event["type"] in res : 
            res[event["type"]] += 1
        else : 
            res[event["type"]] = 1
    
    for key , value in res.items() : 
        print(f"{key} : {value}")


def get_username() -> str : 
    return input("Enter username : ")


def GetInfoEvents() -> None :
    username = get_username().strip()

    # обработка в случае неправильного имени пользователя 
    if (CheckUsername(username ) == False ) :
        while CheckUsername(username) == False : 
            username = get_username() 
    r = requests.get("https://api.github.com/users/{username}/events/public".format(username = username) )
    
    try : 
        r.raise_for_status()
    except requests.exceptions.HTTPError as err : 
            print(err)
            return
    
    if (r.json() == []) : 
        print("{username} not found or has no public events")
        return 
    
    GetEvents(r) 
    
    
 


def main() :
    GetInfoEvents()  
    
if __name__ == "__main__" : 
    main()   






