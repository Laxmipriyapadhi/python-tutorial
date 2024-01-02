class Item:
    def __init__(self, name, type, others):
        self.name = name
        self.type = type
        self.others = others 
        self.size = self.calculate_size()

    def calculate_size(self):
        self.size = len(self.name) + len(self.type)
item_data = {
    "name": "pinky",
    "type": "xyz",
    "others":{"city":"bbsr" , "age" : 24}
    }
example_item = Item(**item_data)
print("item name:{example_item.name}")
print("item type:{example_item.type}")
print("item size:{example_item.size}")
print("item data:{example_item.others}")      
    
class Storage:
    def __init__(self, host, port, protocol):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.container = []

    def add_element(self, item):
        self.container.append(item)

    def calculate_size(self):
        return sum(item.size for item in self.container)
total_size = ("localhost","7676","http")
print("total size of the storage container:{total_size}")
