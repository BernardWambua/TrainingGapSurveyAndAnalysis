from django import forms

class JobTypeUploadForm(forms.Form):
    file = forms.FileField()
    
class TechnicalSkillsUploadForm(forms.Form):
    file = forms.FileField()