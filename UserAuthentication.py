<<<<<<< Updated upstream
# add getId()

=======
# un-comment below if you want to try the tests at the bottom of this file
# from UserAuthenticationSession import UserAuthenticationSession
>>>>>>> Stashed changes
class UserAuthentication:
    def __init__(self,
                 username: str,
                 passwordHash: str):
        self.username = username
        self.passwordHash = passwordHash

    def validateAuthentication(self, entered_username, entered_password):
        # return bool regarding match of username and password stored in system
        return entered_username == self.username and entered_password == self.passwordHash
    
    def getId():
        # placeholder int for session id. What is this used for?
        return 9987


# testing stuff
# session = UserAuthenticationSession()
# session.tryAuthentication("admin", "suchaweakpassword1")
# session2 = UserAuthenticationSession()
# session2.tryAuthentication("", "")