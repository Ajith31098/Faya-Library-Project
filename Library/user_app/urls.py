
from django.urls import include, path
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app import views

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.Registration_view.as_view(), name='register'),
    path('userapproval_list/', views.User_approval_list_view.as_view(),
         name='userapproval_list'),
    path('userapproval_list/<int:pk>/',
         views.User_approval_view.as_view(), name='userapproval'),
    path('logout/', views.Logout_view.as_view(), name='logout'),
]
