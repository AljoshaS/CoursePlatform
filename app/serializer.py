from rest_framework import serializers
from .models import Attendance, File, Instructor, Student, Course, Assistant

class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Instructor
        fields='__all__'

    def create(self, validated_data):
        return Instructor.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields='__all__'

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model=Course
        fields='__all__'
    
    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model=File
        fields='__all__'
    
    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class AttendanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Attendance
        fields='__all__'

    def create(self, validated_data):
        return Attendance.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class AssistantSerializer(serializers.ModelSerializer):

    class Meta:
        model=Assistant
        fields='__all__'

    def create(self, validated_data):
        return Assistant.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)