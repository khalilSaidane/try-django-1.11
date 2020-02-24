from django import forms
from .models import Menu
from restaurents.models import Restaurant


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            'name',
            'restaurant',
            'contents',
            'excludes',
            'is_public',
        ]

    # Personalise the list of restaurants
    def __init__(self,user=None, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = Restaurant.objects.filter(user=user)
