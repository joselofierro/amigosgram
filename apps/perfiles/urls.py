from django.urls import path


from apps.perfiles.views import *

app_name = 'users'
urlpatterns = [
    path('<str:username>/', UserDetailView.as_view(), name='detail'),
    path('login', LoginUserView.as_view(), name="login"),
    path('logout', logout_user, name="logout"),
    path('signup', SignUpView.as_view(), name="sign_up"),
    path('update_profile', UpdateProfileView.as_view(), name='update_profile')
]
