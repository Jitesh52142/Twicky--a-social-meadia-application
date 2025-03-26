from . import views
from django.urls import path


urlpatterns = [
    path('', views.Twickylist, name = 'Twickylist'),
    path('Create/', views.Twicky_create, name = 'Twicky_create'),
    path('<int:tweet_id>/edit/', views.Twicky_edit, name = 'Twicky_edit'),
    path('<int:tweet_id>/delete/', views.Twicky_delete, name = 'Twicky_delete'),
        # Add the register URL pattern
    path('register/', views.register, name='register'),
    
]
