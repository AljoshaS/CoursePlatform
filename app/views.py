from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Assistant, Instructor, Student, Attendance, Course, File
from .serializer import InstructorSerializer, StudentSerializer, CourseSerializer, FileSerializer, AttendanceSerializer, AssistantSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.github import views as github_views
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from dj_rest_auth.registration.views import SocialConnectView
from django.views.generic import TemplateView


# Create your views here.

class InstructorView(APIView):

    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        instructor=Instructor.objects.all()
        return instructor

    def get(self, request, *args, **kwargs):
        try:
            id=request.GET["instructorId"]
            if id!=None:
                instructor=instructor.objects.get(id=id)
                instructor_serializer=InstructorSerializer(instructor)
            
        except:
            instructor=self.get_queryset()
            instructor_serializer=InstructorSerializer(instructor, many=True)

        return Response(instructor_serializer.data)
    
    def post(self, request):
        instructor_serializer=InstructorSerializer(data=request.data)
        if instructor_serializer.is_valid():
            instructor_serializer.save()
            return Response(instructor_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        instructor = Instructor.objects.get(id=request.GET['instructorId'])
        instructor.delete()
        return Response({"info": "The entry is deleted"})
    
    def patch(self, request):
        instructor=Instructor.objects.get(id=request.data['id'])
        instructor_serializer=InstructorSerializer(instructor, data=request.data)
        if instructor_serializer.is_valid():
            instructor_serializer.save()
            return Response(instructor_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)

class StudentView(APIView):

    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        student=Student.objects.all()
        return student

    def get(self, request, *args, **kwargs):
        try:
            id=request.GET["studentId"]
            if id!=None:
                student=student.objects.get(id=id)
                student_serializer=StudentSerializer(student)
            
        except:
            student=self.get_queryset()
            student_serializer=StudentSerializer(student, many=True)

        return Response(student_serializer.data)
    
    def post(self, request):
        student_serializer=StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        student = Student.objects.get(id=request.GET['studentId'])
        student.delete()
        return Response({"info": "The entry is deleted"})
    
    def patch(self, request):
        student=Student.objects.get(id=request.data['id'])
        student_serializer=StudentSerializer(student, data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)

class CourseView(APIView):

    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        course=Course.objects.all()
        return course

    def get(self, request, *args, **kwargs):
        try:
            id=request.GET["courseId"]
            if id!=None:
                course=Course.objects.get(id=id)
                course_serializer=CourseSerializer(course)
            
        except:
            course=self.get_queryset()
            course_serializer=CourseSerializer(course, many=True)

        return Response(course_serializer.data)
    
    def post(self, request):
        course_serializer=CourseSerializer(data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        course = Course.objects.get(id=request.GET['courseId'])
        course.delete()
        return Response({"info": "The entry is deleted"})
    
    def patch(self, request):
        course=Course.objects.get(id=request.data['id'])
        course_serializer=CourseSerializer(course, data=request.data)
        if course_serializer.is_valid():
            course_serializer.save()
            return Response(course_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)

class FileView(APIView):
    permission_classes=(IsAuthenticated,)
    parser_class=(FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer= FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        file = File.objects.get(id=request.GET['fileId'])
        file.delete()
        return Response({"info": "The entry is deleted"})

    def get_queryset(self):
        file=File.objects.all()
        return file

    def get(self, request, *args, **kwargs):
        try:
            id=request.GET["fileId"]
            if id!=None:
                file=File.objects.get(id=id)
                file_serializer=FileSerializer(file)
            
        except:
            file=self.get_queryset()
            file_serializer=FileSerializer(file, many=True)

        return Response(file_serializer.data)   

    def patch(self, request):
        file=File.objects.get(id=request.data['id'])
        file_serializer=FileSerializer(file, data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)

class AttendanceView(APIView):
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        attendance=Attendance.objects.all()
        return attendance

    def get(self, request, *args, **kwargs):
        try:
            id=request.GET["attendanceId"]
            if id!=None:
                attendance=Attendance.objects.get(id=id)
                attendance_serializer=AttendanceSerializer(attendance)
            
        except:
            attendance=self.get_queryset()
            attendance_serializer=AttendanceSerializer(attendance, many=True)

        return Response(attendance_serializer.data)   
    
    def post(self, request):
        attendance_serializer=AttendanceSerializer(data=request.data)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return Response(attendance_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        attendance = Attendance.objects.get(id=request.GET['attendanceId'])
        attendance.delete()
        return Response({"info": "The entry is deleted"})
    
    def patch(self, request):
        attendance=Attendance.objects.get(id=request.data['id'])
        attendance_serializer=AttendanceSerializer(attendance, data=request.data)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return Response(attendance_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)

class AssistantView(APIView):

    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        assistant=Assistant.objects.all()
        return assistant

    def get(self, request, *args, **kwargs):
        try:
            id=request.GET["assistantId"]
            if id!=None:
                assistant=Assistant.objects.get(id=id)
                assistant_serializer=AssistantSerializer(assistant)
            
        except:
            assistant=self.get_queryset()
            assistant_serializer=AssistantSerializer(assistant, many=True)

        return Response(assistant_serializer.data)    
    
    def post(self, request):
        assistant_serializer=AssistantSerializer(data=request.data)
        if assistant_serializer.is_valid():
            assistant_serializer.save()
            return Response(assistant_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        assistant = Assistant.objects.get(id=request.GET['assistantId'])
        assistant.delete()
        return Response({"info": "The entry is deleted"})
    
    def patch(self, request):
        assistant=Assistant.objects.get(id=request.data['id'])
        assistant_serializer=AssistantSerializer(assistant, data=request.data)
        if assistant_serializer.is_valid():
            assistant_serializer.save()
            return Response(assistant_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error":"Issue detected"}, status=status.HTTP_400_BAD_REQUEST)

class Home(TemplateView):
    template_name = "home.html"

def home(request):
   return render(request,'downloadhome.html')


    

