from django.db import models
import datetime
import os
from django.conf import settings

class Post(models.Model):
    names = models.CharField(max_length=10) # 작성자
    passwords = models.CharField(max_length=50) # 비밀번호
    titles = models.CharField(max_length=50) # 제목
    contents = models.TextField() # 내용
    postdate = models.DateTimeField(default=datetime.datetime.now) # 작성일
    visitcount = models.IntegerField(default=0) # 조회수
    files = models.FileField(blank=True, null=True) # 파일첨부
    
    def __str__(self):
        return self.titles
    
    def delete(self, *args, **kargs):
        if self.files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.files.path))
        super(Post, self).delete(*args, **kargs)