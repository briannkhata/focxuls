from django.urls import path
from .import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('', views.endoints),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('usertypes/', views.Usertype.as_view()),
    path('files/', views.File.as_view()),
    path('usertypes/<int:file_id>/', views.Usertype.as_view()),
    path('files/<int:file_id>/', views.File.as_view()),

]
