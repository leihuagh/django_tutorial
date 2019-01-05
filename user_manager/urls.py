from django.urls import path

from . import views
from django.conf.urls import url

from user_manager.views import login, login_validate



app_name = 'post'
urlpatterns = [
    url(r'^login/validate', login_validate),
    url(r'^login/', login),

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]