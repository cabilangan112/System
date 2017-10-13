from django import forms
from .models import student

class StudentForm(forms.ModelForm):
	class Meta:
		model = student
		fields = ['First_name',
		'Last_name',
		'MI',
		'Sex',
		'Professor',
		'course',
		'grade',
		]