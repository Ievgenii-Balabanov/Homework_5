from catalog.models import Person

from django import forms
from django.core.exceptions import ValidationError


class Triangle(forms.Form):
    first_leg = forms.IntegerField(
        label="First leg", max_value=50, required=True, widget=forms.TextInput(attrs={"placeholder": "First leg"})
    )
    second_leg = forms.IntegerField(
        label="Second leg", max_value=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Second leg"})
    )

    def clean_first_leg(self):
        first_leg_data = self.cleaned_data["first_leg"]
        if first_leg_data <= 0:
            raise ValidationError('The "leg 1" value must not be less than 1')
        return first_leg_data

    def clean_second_leg(self):
        second_leg_data = self.cleaned_data["second_leg"]
        # if isinstance(second_leg_data, int):
        if second_leg_data <= 0:
            raise ValueError('The "leg 2" value must not be less than 1')
        return second_leg_data


# class PersonForm(forms.Form):
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     email = forms.EmailField()
#
#     def clean(self):
#         super().clean()
#         if self.cleaned_data.get("first_name") == "Ievgenii":
#             raise ValidationError("First name couldn't be 'Ievgenii!")
#
#     def clean_first_name(self):
#         if self.cleaned_data.get("first_name") == "Igor":
#             raise ValidationError("First name couldn't be 'Igor!")
#         return self.cleaned_data.get("first_name")


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email"]

    def clean(self):
        super().clean()
        if len(self.cleaned_data.get("first_name")) and len(self.cleaned_data.get("last_name")) < 2:
            raise ValidationError("Both First and Last name must contain at least 2 characters!")

    def clean_first_name(self):
        if self.cleaned_data.get("first_name") == "Vladimir":
            raise ValidationError("First name couldn't be 'Vladimir!")
        return self.cleaned_data.get("first_name")

    def clean_last_name(self):
        if self.cleaned_data.get("last_name") == "Putin":
            raise ValidationError("Specified Last name is forbidden because Putin is a war criminal!")
        return self.cleaned_data.get("last_name")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.endswith(".ru"):
            raise ValidationError("Forbidden domain name '.ru'!")
        return self.cleaned_data.get("email")
