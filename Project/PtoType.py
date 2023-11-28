from enum import Enum
class PtoType(Enum):
    PTO = 1
    Sick = 2
    def __str__(self):
        return self.name
    
    def pto(self):
        return self.value[0]
    
    def sick(self):
        return self.value[1]

    #Enum class of options for PtoRequest

