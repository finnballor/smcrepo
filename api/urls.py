
from django.urls import path 
from . import views
urlpatterns = [
  path('', views.courseList, name='course-listpage' ),
 path('course-list/', views.courseList, name='course-list' ),
 path('add-course/',  views.addCourse , name='add-course'   ),
 path('update-course/<str:pk>/', views.updateCourse, name='update-course' ),
 path('delete-course/<str:pk>/',   views.deleteCourse,  name='delete-course'   ),

# teacher section start
 path('teacher-list/', views.teacherList, name='teacher-list' ),
 path('add-teacher/',  views.addTeacher , name='add-teacher'   ),
 path('update-teacher/<str:pk>/', views.updateTeacher, name='update-teacher' ),
 path('delete-teacher/<str:pk>/',   views.deleteTeacher,  name='delete-teacher'   )







# teacher section end
 

]



