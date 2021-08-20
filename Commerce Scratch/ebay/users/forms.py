from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class user_register_form(UserCreationForm):
    class Meta:
        model =get_user_model()
        fields = ['username']