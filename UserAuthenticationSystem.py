from User import User

class UserAuthenticationSystem:
    
    def __init__(self):
        self.usersList: list[User] = []


    # username and password are sent here for authentication 
    def validateAuthentication(self, username: str, password: str):

        # check for username and password match in users list
        for user in self.usersList:
            if user.username == username and user.password == password:
                return user

