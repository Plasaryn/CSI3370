from datetime import date
class EStartObserver:
    def __init__(self, observable):

        # Get the observable eventStart date

        observable.geteventStart(self)
    def update(self, observable, args: object):
        
        # Update data of the observable
        if (isinstance(args, date)):
            args (date)
            print("Start Date changed to: " + args)
        else:
            print("Date cannot be changed!")