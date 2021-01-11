class dictself(dict):
    def __setitem__(self,key,value):
        super().__setitem__(key,eval(value))