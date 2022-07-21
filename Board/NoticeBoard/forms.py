from .models import *
from django.forms import *

class BoardForm(ModelForm):
   
    class Meta:
        model = BoardNotice
        fields =  [
            'title',
            'text',
            'category'
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")
        if title is None:
            raise ValidationError(
                "Title cannot be empty"
            )
        if text is not None and len(text) < 20:
            raise ValidationError(
                "Text must be at least 20 characters long."
            )
        return cleaned_data

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['response_user', 'text', 'response_to']