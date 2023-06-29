"""
URL configuration for APImenu project.

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
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from Menu.views import (
    EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView,
    RestaurantListCreateView, RestaurantRetrieveUpdateDestroyView,
    MenuListCreateView, MenuRetrieveUpdateDestroyView,
    MenuItemListCreateView, MenuItemRetrieveUpdateDestroyView,
    VoteListCreateView, VoteRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/employees/', EmployeeListCreateView.as_view(), name='employee-list'),
    path('api/v1/employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
    path('api/v1/restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list'),
    path('api/v1/restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyView.as_view(), name='restaurant-detail'),
    path('api/v1/menus/', MenuListCreateView.as_view(), name='menu-list'),
    path('api/v1/menus/<int:pk>/', MenuRetrieveUpdateDestroyView.as_view(), name='menu-detail'),
    path('api/v1/menu-items/', MenuItemListCreateView.as_view(), name='menu-item-list'),
    path('api/v1/menu-items/<int:pk>/', MenuItemRetrieveUpdateDestroyView.as_view(), name='menu-item-detail'),
    path('api/v1/votes/', VoteListCreateView.as_view(), name='vote-list'),
    path('api/v1/votes/<int:pk>/', VoteRetrieveUpdateDestroyView.as_view(), name='vote-detail'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
