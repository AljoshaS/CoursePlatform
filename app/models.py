from django.db import models
from django.utils.timezone import now

# Create your models here.
attendance_choices=(
    ('absent','Absent'),
    ('present','Present')
)

file_choises=(
    ('homework','Homework'),
    ('ClassVideo','classvideo')
)

class Instructor(models.Model):
    name=models.CharField(max_length=50)
    surename=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    skills=models.TextField()
    education=models.TextField()
    years_experience=models.IntegerField()
    instructor_of_courses=models.TextField()

    def __str__ (self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=50)
    surename=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    born_date=models.DateField()
    comment=models.TextField(null=True, blank=True)

    def __str__ (self):
        return self.name

class Assistant(models.Model):
    name=models.CharField(max_length=50)
    surename=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    skills=models.TextField()
    education=models.TextField()
    years_experience=models.IntegerField()
    assistant_of_courses=models.TextField()

    def __str__ (self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=50)
    start_date=models.DateField()
    end_date=models.DateField()
    time_of_begining=models.TimeField(null=True)
    time_of_end=models.TimeField(null=True)
    number_of_classes=models.IntegerField()
    number_of_students=models.IntegerField(null=True)
    instructor=models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)
    assistant=models.ForeignKey(Assistant, on_delete=models.CASCADE, null=True, blank=True)
    students = models.ManyToManyField(Student, blank=True)

    def __str__ (self):
        return self.name

class Attendance(models.Model):
    instructor=models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    date=models.DateField(null=True)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    attendance=models.CharField(max_length=50, choices=attendance_choices, blank=True)
    comment=models.TextField(null=True, blank=True)

class File(models.Model):
    name=models.CharField(max_length=50, unique=True)
    date=models.DateField(null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    instructor=models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True, blank=True)
    type_of_file=models.CharField(max_length=50, choices=file_choises, blank=True)
    video_of_class=models.FileField(db_column='file_url', blank=True, upload_to='files/')
    link_for_homework=models.URLField(null=True, blank=True)

    def __str__ (self):
        return self.name



