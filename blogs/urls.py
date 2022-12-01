from django.urls import path

from blogs import views


app_name = 'blogs'

urlpatterns = [
    path('', views.home_page),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post'),
]
