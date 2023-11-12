from PTOMS import PTOMS

class PtoRule:

    def __init__(self, minDaysAway: int, ptoRule):
        self.minDaysAway = minDaysAway
    
    def getMinDatesAway(self) -> PTOMS:
        return self.minDaysAway
    
    def setMinDatesAway(self, minDatesAway):
        # Textual for now; Can implement into GUI, input
        # minDates
        minDatesAway = input()
        
        self._minDatesAway = minDatesAway
