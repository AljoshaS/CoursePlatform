from django.contrib import admin
from .models import Instructor, Student, Course, Attendance, File, Assistant
# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
    @admin.display(description='name')
    def name(self,obj):
        return obj.name

    list_display=('name','surename','phone','email')
    list_filter=('skills','instructor_of_courses')
    search_fields=('name','surename','instructor_of_courses','skills')

class StudentAdmin(admin.ModelAdmin):
    @admin.display(description='name')
    def name(self,obj):
        return obj.name

    list_display=('name','surename','phone','email')
    search_fields=('name','surename')

class CourseAdmin(admin.ModelAdmin):
    @admin.display(description='name')
    def name(self,obj):
        return obj.name
    
    list_display=('name','start_date','end_date','instructor','number_of_classes')
    list_filter=('instructor','name')
    search_fields=('name','instructor','number_of_classes','start_date','end_date')

class FileAdmin(admin.ModelAdmin):
    @admin.display(description='name')
    def name(self,obj):
        return obj.name
    
    list_display=('name','date','instructor','type_of_file','course')
    list_filter=('instructor','name')
    search_fields=('name','instructor')

class AttendanceAdmin(admin.ModelAdmin):
    @admin.display(description='name')
    def name(self,obj):
        return obj.name
    
    list_display=('date','instructor','student','attendance')
    list_filter=('instructor','student','date','attendance')
    search_fields=('instructor','student','date','attendance')

class AssistantAdmin(admin.ModelAdmin):
    @admin.display(description='name')
    def name(self,obj):
        return obj.name

    list_display=('name','surename','phone','email')
    list_filter=('skills','assistant_of_courses')
    search_fields=('name','surename','assistant_of_courses','skills')
    
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(File,FileAdmin)
admin.site.register(Assistant,AssistantAdmin)
