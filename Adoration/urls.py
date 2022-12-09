from django.urls import path
from Adoration import views
urlpatterns = [
    path('',views.Main,name = 'Main')
    
    path('<str:package>/',views.packageDetails,name = 'PackageDetails')
]
