from enum import Enum
# import UserAuthentication

class AuthenticationLevel(Enum):
    # two different user types
    user = 1 
    admin = 2


class UserAuthenticationSession:

    def __init__(self):
        self.id = 0 # default value for user id
        self.isAuthenticated = False # default for authentication state
        self.authenticationLevel = None # 

    def tryAuthentication(self, username, password):
        # NOTE: improve later. Perhaps use a dicitonary or list to store user creds
        if username == "admin" and password == "suchaweakpassword1":
            # if an admin user, use enumerated type to specify
            self.authenticationLevel = AuthenticationLevel.admin
            # admin authenticated
            self.isAuthenticated = True
            print('admin')
        elif username == 'johndoe' and password == 'weakerpassword1':
            # other standard user authentication.
            self.authenticationLevel = AuthenticationLevel.user 
            # johndoe (user) authenticated
            self.isAuthenticated = True
            # return self.isAuthenticated
            print('user')
        else:
            # if username and password are not found, authenticaiton will fail
            self.isAuthenticated = False
            self.authenticationLevel = None
            print("Authentication failed!")




