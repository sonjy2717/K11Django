from django.urls import path
from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls), # 관리자 모드
#     path('', views.main, name='main'), # 로켓화면 대신 메인화면으로 대체할 예정
    
#     # 방법2 : 2개의 파일에 작성
#     path('livepolls/', views.index, name='index'), # 등록된 투표의 질문을 출력
#     #path('livepolls/<int:question_id>/', views.detail, name='detail'),
#     #path('livepolls/<int:question_id>/results/', views.result, name='result'),
#     #path('livepolls/<int:question_id>/vote/', views.vote, name='vote'),
# ]

# app_name은 차후 URL처리를 위한 네임스페이스로 활용된다.
app_name = 'livepolls'

# 네임스페이스로 처리되므로 livepolls/를 제외한 URL패턴을 기술하면 된다.
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), # /livepolls/일련번호/
    path('<int:question_id>/results/', views.results, name='results'), # /livepolls/일련번호/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # /livepolls/일련번호/vote/
]

