from django import forms
from sp_app.models import Projects
# from sp_app.models import User
#
# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'


class ProjectForm(forms.ModelForm):
    describe = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 4}))
    class Meta:
        model = Projects
        fields = '__all__'