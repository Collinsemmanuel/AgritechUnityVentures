# core/urls.py

from django.urls import path, include, re_path
from rest_framework import routers
from .views import UserViewSet, ProjectViewSet, LoanViewSet, BlogPostViewSet, about_us, services, home

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'blogposts', BlogPostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('about_us/', about_us, name='about_us'),
    path('services/', services, name='services'),
    path('', home, name='home')
]
