from django.forms import ModelForm

from class_management.models import Student, Instructor, Course


class StudentForm(ModelForm):
    # model = Student
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'stud_pic', 'courses']


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name']
        # fields = ['first_name', 'last_name', 'course_offered']


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_dept_code', 'course_num_code', 'course_name', 'course_seats', 'course_description']
