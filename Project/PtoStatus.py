from enum import Enum
class PtoStatus(Enum):
    Approved = 1
    Denied = 2
    Pending = 3
    def __str__(self):
        return self.name
        
    def approved(self):
        return self.value[0]
    
    def denied(self):
        return self.value[1]
        
    def pending(self):
        return self.value[2]

    #Enum class of options for PtoStatus
