
class AuthConfig:
    username: str = ""
    password: str = ""
    client_id: str = "ro.customer.client"
    client_secret: str = ""
    scope: str = "api"
    grant_type: str = "password"

    def __init__(self,**kwargs):
        # CloudMore Username
        self.username = kwargs.get("username")
        # CloudMore Password
        self.password = kwargs.get("password")
        # API Secret
        self.client_secret = kwargs.get("client_secret")
