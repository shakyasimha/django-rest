from django.urls import path 
from . import views 

urlpatterns = [
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>/', views.BookDetailView.as_view()),
    path('author/', views.AuthorListView.as_view()),
    path('author/<int:pk>/', views.AuthorDetailView.as_view()),
    path('publisher/', views.PublisherListView.as_view()),
    path('publisher/<int:pk>/', views.PublisherDetailView.as_view()),
]