from django.forms import ModelForm
from .models import Room, User

class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude=['participants','host']

class UpdateUser(ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']




