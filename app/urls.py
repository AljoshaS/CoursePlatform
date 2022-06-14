from django.urls import path
from .views import InstructorView, StudentView, CourseView, FileView, Home, AssistantView, AttendanceView
from django.conf import settings
from django.conf.urls.static import static
from django_downloadview import ObjectDownloadView
from .models import File
download = ObjectDownloadView.as_view(model=File, file_field=
'file')


urlpatterns=[
    path('instructors/', InstructorView.as_view()),
    path('students/', StudentView.as_view()),
    path('courses/', CourseView.as_view()),
    path('files/', FileView.as_view()),
    path('assistants/', AssistantView.as_view()),
    path('attendance/', AttendanceView.as_view()),
    path('homepage/', Home.as_view(), name='home'),
    path('download/', download, name="default")
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
    
    
    






