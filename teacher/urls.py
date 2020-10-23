from django.urls import path, include , re_path
from . import views
from django.conf.urls import url

app_name = "teacher"


urlpatterns = [
    path('',views.TeacherHomeView,name='teacherhome'),
    path('login/',views.TeacherLoginView,name='login'),
    path('logout/',views.TeacherLogoutView,name='logout'),
    path('add/',views.StudentAddView,name='addstudent'),
    path('search/',views.StudentListView,name='search'),
    re_path(r'^delete/(?P<id>\d+)/$',views.StudentDeleteView),
    path('detail/',views.StudentDetialView,name='detail')

]
