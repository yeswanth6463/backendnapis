from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentListCreateView.as_view(), name='student-list'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('teacher/', views.TeacherView.as_view(), name='teacher-list'),
    path('teacher/<int:pk>/', views.TeacherView.as_view(), name='teacher-detail'),
    path('coursecategory/', views.CourseCategoryView.as_view(), name='coursecategory-list'),
    path('course/', views.CourseListAPIView.as_view(), name='course-list'),
    path('course/<int:pk>/', views.CourseDetailAPIView.as_view(), name='course-detail'),
    path('coursecategory/<int:pk>/', views.CourseCategoryView.as_view(), name='coursecategory-detail'),
    path('login/', views.LoginUserAPIView.as_view(), name='login'),
    path('register/', views.RegisterUserAPIView.as_view(), name='register'),
    path('commonuserregister', views.common_user_register_view.as_view(), name='commonuserregister'),
    path('commonuserlogin', views.common_user_login_view.as_view(), name='commonuserlogin'),
    path('commonuserlist', views.common_user_login_listview.as_view(), name='commonlist'),
    path('coursevideo/', views.CourseVideoListAPIView.as_view(), name='coursevideo-list'),
    path('coursevideo/<int:pk>/', views.CourseVideoDetailAPIView.as_view(), name='coursevideo-detail'),
    path('chapters/', views.ChapterListCreateAPIView.as_view(), name='chapter-list'),
    path('chapters/<int:pk>/', views.ChapterDetailAPIView.as_view(), name='chapter-detail'),
    
]
