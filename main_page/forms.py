from django.forms import ModelForm

from .models import Message

class MessageForm(ModelForm):
    # msg =
    class Meta:
        model = Message
        fields = ['name', 'email', 'msg']
