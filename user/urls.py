from django.urls import path
from .views import login, signup, test_token
from .views import LoginUserAPIView, ListUsersAPIView, LogoutUserAPIView

app_name = 'user'

urlpatterns = [
    path('logout/', LogoutUserAPIView.as_view(), name='logout'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('test_token/', test_token, name='test_token'),
    path('login_2/', LoginUserAPIView.as_view(), name='login_2'),
    path('list/', ListUsersAPIView.as_view(), name='users'),
]
