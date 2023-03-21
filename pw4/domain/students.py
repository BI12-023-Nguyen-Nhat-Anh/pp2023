class person:
    def __init__(self,name,dob):
        self.__name=name
        self.__dob=dob

    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
class students(person):
    def __init__(self,id,name,dob):
        super().__init__(name,dob)
        self.__id=id
        self.__mark={}
        self.__average=0

    def get_id(self):
        return self.__id
    
    def add_mark(self,n,x):
        self.__mark[n]
    
    def get_mark(self):
        return self.__mark

    def add_average(self,x):
        self.__average=x

    def get_average(self):
        return self.__average
    
    def show(self):
        return self.id,self.name,self.dob