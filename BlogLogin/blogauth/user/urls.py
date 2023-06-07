from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('login/', login_system),
    path('logout/', logout_system),
    path('register/', register),
    path('post/create/', create_post),
    path('post/my/list/', my_posts),
    path('user/<int:id>', profile_detail),
    path('post/like/<int:id>', like_post),
]
