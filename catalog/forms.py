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
            raise ValidationError('The "leg 2" value must not be less than 1')
        return second_leg_data
