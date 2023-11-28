from enum import Enum

class AuthenticationLevel(Enum):
    # two different user types
    user = 1 
    admin = 2

class UserAuthentication:
    
    def __init__(self,
                 username: str,
                 password: str):
        self.username = username
        self.password = password
        self.id = 0 # default value for user id
        self.isAuthenticated = False # default for authentication state
        self.authenticationLevel = None 

    # was self, username, password as parameters
    def tryAuthentication(self, username, password):
        while True:
            print("Enter your username. ")
            username = input()
            print("Enter your password. ")
            password = input()
            # user's entered username and password are sent to 
            if self.validateAuthentication(username, password) == True:
                break            

    # username and password are sent here for authentication 
    def validateAuthentication(self, username, password):
        # nested dictionaries for usernames and passwords
        stdUsers = {
        "user1": {
            "name": "scott",
            "password": "test123"
        }, 
        "user2": {
            "name": "jared",
            "password": "hello123"
        },
        "user3": {
            "name": "craig",
            "password": "testing123"
        }, 
        "user4": {
            "name": "tyler",
            "password": "password123"
        },
        "user5": {
            "name": "anderson",
            "password": "password321"
        }
    }
        admins = {
        "admin1": {
            "name" :"admin1",
            "password": "strongestpassword"
        },
        "admin2": {
            "name": "admin2",
            password: "notsostrong"
        }
    }

        # check for username and password within stdUser nested dict
        for user, credentials in stdUsers.items():
            if credentials['name'] == username and credentials['password'] == password:
                AuthenticationLevel.user
                print("User credentials passed!")
                return True
        
        # check for username and password within admins nested dict
        for user, credentials in admins.items():
            if credentials['name'] == username and credentials['password'] == password:
                AuthenticationLevel.admin
                print("Admin credentials passed!")
                return True

        # failed to log in, no user type    
        print("Authentication failed!")
        return False, None
    
    def getId():
        # is this necessary??
        return 9987


# UNCOMMENT TO TEST CODE
# create instance of UserAuthentication class, use empty username and password 
# guy = UserAuthentication("","")
# guy.tryAuthentication("","")