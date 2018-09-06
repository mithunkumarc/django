from django import forms
from studentapp.models import Student


#using model forms
#forms.Form for django forms
class StuForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
