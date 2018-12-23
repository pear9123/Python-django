from django.urls import path
from . import views

app_name = 'hello_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailsView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultView.as_view(), name='results'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]
