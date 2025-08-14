from django.forms import ModelForm, TextInput, Textarea, EmailInput, HiddenInput
from .models import Comments
from captcha.fields import CaptchaField

class CommentsForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comments

        fields = ['username', 'email', 'text', 'reply']

        widgets = {
            "username": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите Никнейм..."
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Введите Емейл..."
            }),
            "text": Textarea(attrs={
                "class": "form-control text-field",
                "placeholder": "Введите сообщение...",
                "id" :"exampleFormControlTextarea1",
                "rows": "3",
                "style": "width: 50%;"
            }),
            'reply': HiddenInput()
        }