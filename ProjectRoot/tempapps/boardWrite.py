from django import forms

class myForm(forms.Form):
    user = forms.CharField(label='작성자', max_length=10, 
                           widget=forms.TextInput(attrs={'class':'form-control', 'id':'user'}))
    password = forms.CharField(label='패스워드', 
                               widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'pass'}))
    title = forms.CharField(label='제목', 
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='내용', 
                              widget=forms.Textarea(attrs={'class':'form-control'}))
    file = forms.FileField(label='첨부파일', 
                           widget=forms.FileInput(attrs={'class':'form-control'}), required=False)