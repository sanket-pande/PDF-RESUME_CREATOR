from resume.models import *
from django.contrib.auth import authenticate

class UserAuthManager:

    def __init__(self, user= None):
        if user:
            self.user = user

    def register_user(self, first_name, last_name, email, password):
        try:
            user = User.objects.create_user(email, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            self.user = user
            return True
        except Exception as e:
            print(e)
            return False

    def login_user(self, email, password):
        return authenticate(username=email, password=password)

    def is_authenticated(self):
        return self.user and self.user.is_authenticated




        

    
        
    