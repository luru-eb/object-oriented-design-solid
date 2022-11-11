class Merbership:
    def login(self, username: str, password: str) -> bool:
        pass
    def logout(self, username: str) -> None:
        pass
    def register(self, username: str, password: str, email: str) -> int:
        pass
    def forgot_password(self, username: str) -> None:
        pass
    def reset_password(self, username: str) -> None:
        pass


class MembershipOnlyLogin(Merbership):
    def login(self, username: str, password: str) -> bool:
        if username == 'admin' and password == 'supersecretpassword':
            return True
        return False
    def logout(self, username: str) -> None:
        self.remove_cookie(username)
    def register(self, username: str, password: str, email: str) -> int:
        pass
    def forgot_password(self, username: str) -> None:
        pass
    def reset_password(self, username: str) -> None:
        pass