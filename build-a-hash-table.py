** start of main.py **

class HashTable:
    def __init__(self):
        self.collection={}
    
    def hash(self,string):
        sum1=[]
        for a in list(string):
            sum1.append(ord(a))
        sum1=sum(sum1)
        return sum1
    
    def add(self,key,value):
        hashed_key=self.hash(key)
        print(hashed_key)
        if hashed_key in self.collection:
            self.collection[hashed_key][key]=value
        else:
            self.collection[hashed_key]={key:value}

        print(self.collection)

    def remove(self,key):
        hashed_key=self.hash(key)
        print(hashed_key)
        if hashed_key not in self.collection:
            return None
        print(self.collection[hashed_key])
        if len(self.collection[hashed_key])>1:
            self.collection[hashed_key].pop(key)
        else:
            self.collection.pop(hashed_key)

    def lookup(self,key):
        hashed_key=self.hash(key)
        if hashed_key not in self.collection:
            return None
        return self.collection[hashed_key][key]

a=HashTable()
a.add("dear","friend")
a.add("raed","sport")
a.remove("dear")
print(a.collection)

** end of main.py **

