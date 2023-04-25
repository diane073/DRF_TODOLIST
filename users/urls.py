from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='signup'),
    path('mock/', views.mockView.as_view(), name = 'mock'),
    #access token 발급 = login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]