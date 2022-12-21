from django.urls import path

from blogs import views


app_name = 'blogs'

urlpatterns = [
    path('', views.home_page),
    path('post/<slug:slug>', views.PostView.as_view(), name='post'),
    path('featured/', views.FeaturedListView.as_view(), name='featured'),
    path('category/<slug:slug>', views.CategoryListView.as_view(), name='category'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
]
