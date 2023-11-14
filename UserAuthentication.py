# add getId()
from UserAuthenticationSession import UserAuthenticationSession
class UserAuthentication:
    def __init__(self,
                 username: str,
                 passwordHash, str):
        self.username = username
        self.passwordHash = passwordHash

    def validateAuthentication(self, entered_username, entered_password):
        # return bool regarding match of username and password stored in system
        return entered_username == self.username and entered_password == self.passwordHash
    
    def getId():
        # placeholder int for session id
        return 9987
