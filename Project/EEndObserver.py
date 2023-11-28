from datetime import date
class EEndObserver:
    def __init__(self, observable):

        # Get the observable eventEnd date

        observable.geteventEnd(self)
    def update(self, observable, args: object):
        
        # Update data of the observable
        if (isinstance(args, date)):
            args (date)
            print("End Date changed to: " + args)
        else:
            print("Date cannot be changed!")
    
    