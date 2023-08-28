from django.urls import path
from .views import login, signup, test_token

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('test_token/', test_token, name='test_token'),
]
