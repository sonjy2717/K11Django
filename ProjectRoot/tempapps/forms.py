from django import forms
'''
장고에서 제공하는 Form기능을 사용하려면 우선 forms.Form 클래스를 상속한다.
각 변수명은 해당 input태그의 name속성 값으로 사용된다.
태그 생성시 required 속성이 포함되어 기본적인 빈값 검증을 하게된다.
'''
class QuestionForm(forms.Form):
    # <input type="text" /> 를 생성.
    user_id = forms.CharField(label='아이디', max_length=10)
    # 가장 기본적인 input태그를 생성. 타이틀은 title로 표시됨
    title = forms.CharField()
    # 여러줄의 텍스트를 입력할 수 있는 <textarea>를 생성
    content = forms.CharField(widget=forms.Textarea)
    # 기본적인 input 태그를 생성하되 type="email"로 생성
    email = forms.EmailField()
    # <input type="checkbox">를 생성. 유효성 검증을 하지 않는다.
    my_check = forms.BooleanField(required=False)
    
    ####################################################
    
    data01 = ['유비', '관우', '장비']
    data02 = [
        ('red', '빨강'), ('green', '녹색'), ('blue', '파랑'), ('black', '검정')
    ]
    # <input type="text" name="form1" required id="id_form1">  
    form1 = forms.CharField(widget=forms.TextInput)
    
    # <input type="number" name="form2" required id="id_form2">
    form2 = forms.CharField(widget=forms.NumberInput)
    
    # <input type="password" name="form3" required id="id_form3">
    '''
        추가적인 속성을 부여할때는 위젯에 attrs을 기술한다.
    '''
    form3 = forms.CharField(
        widget=forms.PasswordInput(attrs={'size':10})
    )
    
    # <textarea name="form4" cols="40" rows="10" required id="id_form4"></textarea>
    form4 = forms.CharField(widget=forms.Textarea)
    
    '''
    select 태그를 표현한다.(1개 선택)
        choices : select의 option태그를 구성하는 데이터로 사용한다.
            순서대로 value와 text로 사용된다.
        initial : 해당 태그의 default값으로 사용한다. 주로 수정에서
            활용하면 된다.
        <select name="form5" id="id_form5">
            <option value="red">빨강</option>
            .....
            <option value="blue" selected>파랑</option>
        </select>
    '''
    form5 = forms.ChoiceField(
        widget=forms.Select,
        choices=data02,
        initial='blue'
    )
    
    '''(멀티 선택)
    select태그를 표현하는 것은 5번과 동일하지만 multiple속성을 부여하여
    2개 이상의 항목을 선택할 수 있게 한다.
    또한 default값을 표현하기 위해 2개 이상의 항목을 선택할 수 있어야
    하므로 리스트를 사용해야 한다.
    '''
    form6 = forms.MultipleChoiceField(
        widget=forms.SelectMultiple,
        choices=data02,
        initial=['black', 'green']
    )
    
    '''
    <div id="id_form7">
    <div>
        <label for="id_form7_0">
            <input type="radio" name="form7" value="red" required id="id_form7_0">빨강
        </label>
    </div>
    <div>
        <label for="id_form7_1">
            <input type="radio" name="form7" value="green" required id="id_form7_1">녹색
        </label>
    </div>
    라디오 버튼을 표현한다.(1개 선택)
    '''
    form7 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=data02,
        initial='blue'
    )
    
    '''
    체크박스를 표현한다.(멀티 선택)ㅓ
    추가적인 속성을 부여할때는 attrs={'class':'red'} 와 같이 기술한다.
    '''
    form8 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class':'red'}), 
        choices=data02,
        initial=['black', 'green'], 
    )
    
    # 파일
    # <input type="file" name="form9" required id="id_form9">
    form9 = forms.CharField(
        widget=forms.FileInput(attrs={'class':'blue'}),
        label='파일첨부', 
    )