"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mysite import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>/', views.BookDetailView.as_view()),
    path('author/', views.AuthorListView.as_view()),
    path('author/<int:pk>/', views.AuthorDetailView.as_view()),
    path('publisher/', views.PublisherListView.as_view()),
    path('publisher/<int:pk>/', views.PublisherDetailView.as_view())
]
