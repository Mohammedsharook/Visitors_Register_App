from .models import VisitorDetails
from django import forms
import re

class VisitorForm(forms.ModelForm):
    class Meta:
        model = VisitorDetails
        fields = ['visitor_name', 'visitor_location', 'visitor_mobile_number']


    def clean_visitor_mobile_number(self):
        visitor_mobile_number = self.cleaned_data['visitor_mobile_number']
        if not re.match(r'^[0-9]+$', visitor_mobile_number):
            raise forms.ValidationError("Mobile number should contain only digits.")
        
        if len(visitor_mobile_number) != 10:
            raise forms.ValidationError("Mobile number should have exactly 10 digits.")
        
        return visitor_mobile_number


