
class Item:
    def __init__(self, name, type, others):
        self.name = name
        self.type = type
        self.others = others 
        self.calculate_size()

    def calculate_size(self):
        self.size = len(self.name) + len(self.type)

class Storage:
    def __init__(self, host, port, protocol,max_size):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.container = []
        self.max_size = max_size
        

    def add_element(self, item):
       if isinstance(item):
           raise TypeError("invalid type of object")
       self.data.append(item)
        
       return item

       
    def calculate_size(self):
        self.size = sum([item.size for item in self.container])
        if self.size>self.max_size:
            raise memoryError
        return self.size
try:        
    storage = ("hjn",101,"http",10)
    
    item1 = Item("abc","type1",{"age":24})
    item2 = Item("xyz","type2",{"age":22})
    
    storage.add_element(item1)
    storage.add_element(item2)
    
    print(storage.add_element(item2))
    print("max_size:",storage.max_size)
    print(storage.calculate_size())
except (TypeError,MemoryError ):
    print(f"error")
  
