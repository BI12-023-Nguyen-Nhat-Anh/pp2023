class subjects:
    def __init__(self,id,name,credit):
        self.__id=id
        self.__name=name
        self.__credit=credit

    def get_info(self):
        return self.__id, self.__name, self.__crerdit
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_credit(self):
        return self.__credit