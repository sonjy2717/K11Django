from django.contrib import admin

from livepolls.models import Choice, Question

# Register your models here.
'''
models.py에서 테이블을 생성하면 관리자 모드에 적용하기 위해
아래와 같이 등록절차가 필요하다.
'''
admin.site.register(Question)
admin.site.register(Choice)