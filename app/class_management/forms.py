from django.forms import ModelForm

from class_management.models import Student, Instructor, Course, Department


class StudentForm(ModelForm):
    """
    This is the ModelForm for the student.
    """
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'stud_pic', 'courses']


class InstructorForm(ModelForm):
    """
    This is the ModelForm for the instructor.
    """
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name', 'course_offered']


class CourseForm(ModelForm):
    """
    This is the ModelForm for the course.
    """
    class Meta:
        model = Course
        fields = ['course_dept_code', 'course_num_code', 'course_name', 'course_seats', 'course_description']


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_code', 'department_name', 'department_chair']
