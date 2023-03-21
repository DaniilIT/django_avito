from django.urls import path

from .views import root, CatView, CatDetailView, AdView, AdDetailView

urlpatterns = [
    path('', root),
    path('cat/', CatView.as_view()),
    path('cat/<int:pk>/', CatDetailView.as_view()),
    path('ad/', AdView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
]
