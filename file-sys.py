# file-system:
# a virtual system that illustates the file-system

# definition of file class
class file:
    def __init__ (self, name, _type, data=None):
        self.name = name
        self._type = _type
        
    def __str__(self):
        return f"{self.name}.{self._type}"
        
    
    def data_insert(self, data):
        self.data = data
        
    def read_data(self):
        return self.data
        

# Example of file:
temp1 = file("temp1", "txt")
temp1.data_insert("this is just a temp file..")
print(f"File name: {temp1}")
print(temp1.read_data())

