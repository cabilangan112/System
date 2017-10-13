from django import forms
from .models import faculty

class facultyForm(forms.ModelForm):
  class Meta:
    model = faculty
    exclude = ()