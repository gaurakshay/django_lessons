from django.forms import ModelForm, modelformset_factory
from extra_views import InlineFormSet

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


class EmptyDepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = []


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_code', 'department_name', 'department_chair']


class DepartmentInline(InlineFormSet):
    model = Department
    form_class = DepartmentForm
    # extra = 1


# Add model form set for the department model.
# DepartmentFormset = modelformset_factory(model=Department, form=DepartmentForm)
