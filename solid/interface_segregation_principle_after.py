class UserLogin:
    def login(self, username: str, password: str) -> bool:
        pass
    def logout(self, username: str) -> None:
        pass


class UserRegister:
    def register(self, username: str, password: str, email: str) -> int:
        pass


class UserPassword:
    def forgot_password(self, username: str) -> None:
        pass
    def reset_password(self, username: str) -> None:
        pass

class Merbership(UserLogin, UserRegister, UserPassword):
    pass


class MembershipOnlyLogin(UserLogin):
    pass
    