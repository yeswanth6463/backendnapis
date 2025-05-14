from rest_framework import serializers
from .models import (
    student,
    teacher,
    course_category,
    course,
    Chapter,
    course_video,
    Common_user,

)
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def validate_email(self, value):
        if student.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("Email already exists."))
        return value

    def validate_phone_number(self, value):
        if student.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(_("Phone number already exists."))
        return value

class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def validate_email(self, value):
        if teacher.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("Email already exists."))
        return value

    def validate_phone_number(self, value):
        if teacher.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError(_("Phone number already exists."))
        return value

class course_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = course_category
        fields = '__all__'
        extra_kwargs = {
            'description': {'write_only': True}
        }

class course_videoSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_video
        fields = ['id', 'video_name', 'video']

class ChapterSerializer(serializers.ModelSerializer):
    videos = course_videoSerializer(many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = ['id', 'title', 'chapter_type', 'videos']

class courseSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = course
        fields = ['id', 'name', 'description', 'category', 'image', 'module', 'chapters']
        extra_kwargs = {
            'description': {'write_only': True}
        }

class Common_user_serializers(serializers.ModelSerializer):
    class Meta:
        model = Common_user
        fields = ['id', 'name', 'email', 'password', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }
