from AuthorizationLevel import AuthorizationLevel

class User:

    def __init__(self, userID: int, username: str, password: str, authLevel: str):
        self.userID = userID
        self.username = username
        self.password = password
        self.authLevel = authLevel
