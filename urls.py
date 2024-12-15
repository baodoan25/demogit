from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views, api_views



urlpatterns = [
    path('api/first_api_view/', api_views.first_api_view),
    path('', views.index),
    path('', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('book-search/', views.book_search, name='book_search'),
    path('publishers/<int:pk>/',views.publisher_edit, name='publisher_edit'),
    path('publishers/new/',views.publisher_edit, name='publisher_create'),
]