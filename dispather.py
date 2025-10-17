registry = {} 

def register(event) :
    def decorator(f):
        registry[event] = f 
        return f
    return decorator 

def get_handler(event_name , default) : 
    return registry.get(event_name , default)
