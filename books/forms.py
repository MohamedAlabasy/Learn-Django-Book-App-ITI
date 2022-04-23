from django import forms
from django.core.exceptions import ValidationError
from .models import Book


class CreateBooks(forms.ModelForm):
    class Meta:
        model = Book
        # fields = "__all__"
        fields = [
            "name",
            "summary",
            "image",
            "price",
            "appropriate",
            "author",
        ]


class UpdateBooks(forms.ModelForm):
    class Meta:
        model = Book
        # fields = "__all__"
        fields = [
            "name",
            "summary",
            "image",
            "price",
            "appropriate",
            "author",
        ]


# class CreateBooks(forms.Form):
#     name = forms.CharField(label='Enter book Name', widget=forms.TextInput)
#     summary = forms.CharField(label='Enter book Summary')
#     summary = forms.DateField(label='Data')
#     image = forms.URLField(label='Enter Book image')
#     price = forms.IntegerField(label='Enter Book Price')
#     appropriate = forms.CharField(label='Enter Book Appropriate')
#     author = forms.IntegerField(label='Enter Book Author Name')

#     # custom ValidationError

#     def clean_price(self):
#         if self.cleaned_data['price'] == 0:
#             raise ValidationError("Your price must be more than 0 ")
#         return self.changed_data["price"]
