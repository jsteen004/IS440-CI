class People:
    name = ''
    age = 0
    __weight = 0
    __university = ''
    def __init__(self, n, a, w, u):
        self.name = n
        self.age = a
        self.__weight = w
        self.__university = u
    
    def get_weight(self):
        return self.__weight
    
    def lose_weight(self, w):
        self.__weight = self.__weight -w
    
    def speak (self):
        print("%s said: I'm currently studying at %s" %(self.name, self.__university))