from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers

from ads import views

router = routers.SimpleRouter()
router.register('location', views.LocationViewSet)

urlpatterns = [
    path('', views.root),
    path('cat/', views.CatListView.as_view()),
    path('cat/<int:pk>/', views.CatDetailView.as_view()),
    path('cat/create/', views.CatCreateView.as_view()),
    path('cat/<int:pk>/update/', views.CatUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CatDeleteView.as_view()),
    path('ad/', views.AdListView.as_view()),
    path('ad/<int:pk>/', views.AdDetailView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', views.AdLoadImageView.as_view()),
    path('user/', views.UserListView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
