from django.shortcuts import render
from rest_framework import viewsets, status, generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import student, teacher,  course_category, Common_user,  course_video, Chapter, course
from .serializers import studentSerializer, teacherSerializer, course_categorySerializer, Common_user_serializers, course_videoSerializer, ChapterSerializer, courseSerializer
from rest_framework import generics



class StudentListCreateView(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = teacher.objects.all()
    serializer_class = teacherSerializer
    
class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = teacher.objects.all()
    serializer_class = teacherSerializer

class TeacherView(generics.ListCreateAPIView):
    queryset = teacher.objects.all()
    serializer_class = teacherSerializer

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = teacher.objects.all()
    serializer_class = teacherSerializer
    
class CourseCategoryView(generics.ListCreateAPIView):
    queryset = course_category.objects.all()
    serializer_class = course_categorySerializer

class CourseCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = course_category.objects.all()
    serializer_class = course_categorySerializer

class LoginUserAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user_type = request.data.get('user_type')

        if user_type == 'student':
            user = student.objects.filter(email=email, password=password).first()
            serializer_class = studentSerializer
            print("student dashboard")
        elif user_type == 'teacher':
            user = teacher.objects.filter(email=email, password=password).first()
            serializer_class = teacherSerializer
            print("teacher dashboard")
        else:
            return Response({'error': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)

        if user:
            serializer = serializer_class(user)
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterUserAPIView(APIView):
        
    def post(self, request):
        name= request.data.get('name')
        phone_number= request.data.get('phone')
        email = request.data.get('email')
        password = request.data.get('password')
        user_type = request.data.get('user_type')

        if user_type == 'student':
            user = student(name=name, phone_number=phone_number, email=email, password=password, user_type=user_type)
            user.save()
            return Response({'message': 'Student registered successfully'}, status=status.HTTP_201_CREATED)
        elif user_type == 'teacher':
            user = teacher(name=name, phone_number=phone_number, email=email, password=password, user_type=user_type)
            user.save()
            return Response({'message': 'Teacher registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)

class common_user_register_view(APIView):
      def post(self, request):
        name= request.data.get('name')
        phone_number= request.data.get('phone')
        email = request.data.get('email')
        password = request.data.get('password')
        commonuser = Common_user(name=name, phone_number=phone_number, email=email, password=password)
        commonuser.save()
        data = {
            'id': commonuser.id,
            'name': commonuser.name,
            'phone_number': commonuser.phone_number,
            'email': commonuser.email,
        }
        return Response({'message': 'Common user registered successfully', 'user': data}, status=status.HTTP_201_CREATED)

class common_user_login_view(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            commonuser = Common_user.objects.get(email=email, password=password)
            data = {
                'id': commonuser.id,
                'name': commonuser.name,
                'phone_number': commonuser.phone_number,
                'email': commonuser.email,
            }
            return Response({'message': 'Common user logged in successfully', 'user': data}, status=status.HTTP_200_OK)
        except Common_user.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

class common_user_login_listview(generics.ListAPIView):
    queryset = Common_user.objects.all()
    serializer_class = Common_user_serializers

class CourseVideoListAPIView(generics.ListCreateAPIView):
    queryset = course_video.objects.all()
    serializer_class = course_videoSerializer

class CourseVideoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = course_video.objects.all()
    serializer_class = course_videoSerializer

class ChapterListCreateAPIView(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class ChapterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class CourseListAPIView(generics.ListAPIView):
    queryset = course.objects.all()
    serializer_class = courseSerializer

class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = course.objects.all()
    serializer_class = courseSerializer
    
