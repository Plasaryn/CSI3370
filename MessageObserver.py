class MessageObserver:
    def __init__(self, observable):

        # Get the observable eventStart date

        observable.geteventStart(self)
    def update(self, observable, args: object):
        
        # Update data of the observable
        if (isinstance(args, str)):
            args (str)
            print("Message changed to: " + args)
        else:
            print("Message cannot be changed!")