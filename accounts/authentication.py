from accounts.models import User, Token

class PasswordlessAuthenticationBackend(object):

    def authenticate(self, uid):
        try:
            print("try ", uid)
            token = Token.objects.get(uid=uid)
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            print("User Not Exist ", uid)
            return User.objects.create(email=token.email)
        except Token.DoesNotExist:
            print("Token Not Exist ", uid)
            return None
        else:
            print('uid', uid)

    def get_user(self, email):
        try:
            print("here~~")
            return User.objects.get(email=email)
        except User.DoesNotExist:
            print("here~~ except")
            return None
