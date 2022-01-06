from django import forms

# 게시판의 글쓰기 페이지 UI 구현
class myForm(forms.Form):
    '''
        attrs 속성으로 각 폼에 class를 부여한다.
        첨부파일의 경우 필수 사항이 아니므로 required=False를 추가한다.
        입력폼의 타이틀 부분을 한글로 처리하기 위해 label을 추가한다.
    '''
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