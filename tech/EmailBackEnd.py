from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model



class EmailBackEnd(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user=UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        
        else:
            print('entering else block')
            if user.check_password(password):
                return user
        return None






