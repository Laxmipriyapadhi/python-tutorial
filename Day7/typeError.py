class Item:
    def __init__(self, name, type, others):
        self.name = name
        self.type = type
        self.others = others 
        self.calculate_size()

    def calculate_size(self):
        self.size = len(self.name) + len(self.type)

class Storage:
    def __init__(self, host, port, protocol,max_size=10):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.container = []
        self.max_size = 10
        self.current_size =7

    def add_element(self, item):
       if not isinstance(item,Item):
           raise TypeERROR("invalid type of object")
try:
       if self.current_size + item.size > self.max_size:
         raise MemoryERROR(" max size exceed")
       self.container.append(item)
       self.current_size += item.size

except:
    def calculate_size(self):
        return sum(item.size for item in self.container)
try:    
      storage = Storage(host="ghjhhb",port=555,protocol="https",max_size=10)
     
      item1 = Item("abc","type1",{"age":24})
      storage.add_element(item1)
      item2 = Item("xyz","type2",{"age":22})
      storage.add_element(item2)
      print("Max_size:",storage.max_size)
      print("Current size:",storage.current_size)
      print("New item size:",item2.size)
except MemoryERROR as x:
    print("Found error:{x}")
    
finally:
    print("Execution completed")
