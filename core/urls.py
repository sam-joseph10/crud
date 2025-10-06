from django.urls import path
from .views import Home,login
from .views import Signup,Add_student,Delete_student,Editstudent,Login
from core import views
urlpatterns = [
         path('',Signup.as_view(), name='Signup'),
         path('login/',Login.as_view(), name='login'),
        path('home/',Home.as_view(),name='home'),
        path('logout/',views.Logout,name='logout'),
        path('add_student/', Add_student.as_view(), name='add_student'),
        path('delete_student/', Delete_student.as_view(), name='delete_student'),
        path('edit_student/<int:id>/', Editstudent.as_view(), name='edit_student'),

       
]
