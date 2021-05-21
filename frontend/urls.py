from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name=''),
    # path('login', index),
    # path('register', index),
    # path('edit/<int:pk>', TodoDetailView.as_view()),
    # path('delete/<int:pk>', TodoDetailView.as_view()),
]
