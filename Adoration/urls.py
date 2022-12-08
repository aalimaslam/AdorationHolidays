from django.urls import path
from Adoration import views
urlpatterns = [
    path('',views.Main,name = 'Main')
]

# 404 handler