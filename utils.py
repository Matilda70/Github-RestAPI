def get_username() -> str : 
    return input("Enter username : ")

def CheckUsername(username) : 
    with open ("github_reserved_names.txt" , "r" ) as file : 
        for line in file : 
            if username == line.strip() : 
                return False 
    file.close()
    if (username == "" or username[0].isalpha() == False or username[0].isdigit() == True or len(username) > 39 or len(username) < 1
        or username[-1] == '-' or username[0] == '-' or username.find('--') != -1 ) : 
        return False
    return True

def IsEmptyJsom(json) : 

    if (json == []) : 
        return True 
    return False

def ShowUnknowns(unknowns) :
    if (len(unknowns) > 0) : 
        print("UNKNOWNS events:") 
        for event in unknowns : 
            print(f"-{event}") 