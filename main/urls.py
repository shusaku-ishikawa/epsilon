from django.urls import path, include
from main import views

app_name = 'main'
urlpatterns = [
    path('login/', views.Login.as_view(), name = 'login'),
    path('top/', views.Top.as_view(), name = 'top'),
    path('logout/', views.Logout.as_view(), name = 'logout'),
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('', views.ListCompany.as_view(), name = 'list_company'),
    path('companies/<int:pk>', views.DetailCompany.as_view(), name = 'detail_company'),
    path('profile/<int:pk>', views.Profile.as_view(), name = 'profile'),
]