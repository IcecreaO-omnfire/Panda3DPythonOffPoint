class selfobject():
    def __init__(self,**obconstruct):
        self.key=[]
        self.values=[]
        for transmit in obconstruct:
            self.set(transmit)
    def set(self,varin):
        exec("self."+varin[0]+" ="+varin[1])
        self.key.insert(len(self.key),varin[0])
        self.values.insert(len(self.key),varin[1])
            
