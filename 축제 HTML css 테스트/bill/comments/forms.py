from django.forms import ModelForm
from comments.models import *

class Form(ModelForm):
    class Meta:
        model = CommentsData
        fields = ['nickname','comments']
