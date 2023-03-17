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
        self.__mark=[]
        self.__average=0

    def change_mark(self,i,x):
        self.__mark[i]=x
        
    def get_id(self) -> str:
        return self.__id
    
    def add_mark(self,x):
        self.__mark.append(x)
    
    def get_mark(self) -> list:
        return self.__mark

    def add_average(self,x):
        self.__average=x

    def get_average(self) -> float:
        return self.__average
    
    def show(self):
        return self.id,self.name,self.dob