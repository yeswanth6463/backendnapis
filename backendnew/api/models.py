from django.db import models
from django.core import serializers
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Common_user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number=models.BigIntegerField()
    university = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    university = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10, choices=[('student', 'Student'), ('teacher', 'Teacher')])

    def __str__(self):
        return self.name

    def to_json(self):
        return serializers.serialize('json', [self])

class teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=[('student', 'Student'), ('teacher', 'Teacher')])

    def __str__(self):
        return self.name

    def to_json(self):
        return serializers.serialize('json', [self])

class course_category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def to_json(self):
        return serializers.serialize('json', [self])

class course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(course_category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    module  = models.IntegerField()
    duration =models.IntegerField()

    def __str__(self):
        return self.name

    def to_json(self):
        return serializers.serialize('json', [self])

class Chapter(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=100)
    chapter_type = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.title} ({self.chapter_type})"

class course_video(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='videos')
    video_name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.video_name

class quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    video = models.ForeignKey(course_video, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def to_json(self):
        return serializers.serialize('json', [self])

class quiz_result(models.Model):
    quiz = models.ForeignKey(quiz, on_delete=models.CASCADE)
    score = models.IntegerField()


