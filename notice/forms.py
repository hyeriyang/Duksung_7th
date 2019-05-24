from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):
    class Meta:
        model=Notice 
        fields=['title','body','file']

    def __init__(self,*args,**kwargs):
        super(NoticeForm,self).__init__(*args,*kwargs)
        self.fields['file'].required=False
