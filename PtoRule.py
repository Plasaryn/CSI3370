class PtoRule:

    def __init__(self, minDaysAway: int):
        self.minDaysAway = minDaysAway
    
    def getMinDaysAway(self) -> int:
        return self.minDaysAway
    
    def setMinDaysAway(self, minDaysAway):
        # Textual for now; Can implement into GUI, input
        # minDates
        minDaysAway = input()
        
        self.minDaysAway = minDaysAway