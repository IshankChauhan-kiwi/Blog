from django.urls import path

from . import views
from .views import SignUpView, IndexView, DetailView, AddPostView, UpdatePostView

urlpatterns=[
    path('signup/', SignUpView.as_view(), name="signup"),
    path('', IndexView.as_view(), name="index"),
    path('article/<int:pk>', DetailView.as_view(), name="detail"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('profile/', views.Profile, name='profile'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='update'),
]