from chats.models import Chat
from django import forms

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['provider', 'identifier']
    # choices = []
    # for provider in PROVIDERS:
    #     choices.append((provider, PROVIDERS[provider]['title']))
    #
    # provider = forms.ChoiceField(choices=choices)
    # identifier = forms.CharField(label='Your name', max_length=100)