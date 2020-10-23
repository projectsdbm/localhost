from django.urls import path, include
from . import views

app_name = 'student'

urlpatterns = [

    path('search/',views.StudentSearchView,name='search')

]
