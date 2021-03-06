from django import forms
from .models import AllCodes, Codes, Category


class AllCodesForm(forms.ModelForm):

    class Meta:
        model = AllCodes
        fields = ['body', 'category', 'title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-3 py-1 rounded text-sm'}),
            'category': forms.SelectMultiple(attrs={'class': 'rounded w-full text-sm'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AllCodesForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-1 rounded text-sm', 'autocomplete': 'off'}),
        }

