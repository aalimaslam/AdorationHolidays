from django.urls import path
from Adoration import views
urlpatterns = [
    path('',views.Main,name = 'Main'),
    
    path('packages/<int:pk>/',views.packageDetails,name = 'PackageDetails')
]
