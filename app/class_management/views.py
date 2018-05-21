# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView, FormView
from django.views.generic.edit import DeleteView

from class_management.forms import StudentForm, InstructorForm, CourseForm
from class_management.models import Student, Instructor, Course, Department


class StudentListView(ListView):
    """
    List view to display all the students in the system.
    """
    model = Student
    template_name = 'class_management/student_list.html'


class StudentDetailView(DetailView):
    """
    Detail view to display the details of the student.
    """
    model = Student
    pic = model.stud_pic
    template_name = 'class_management/student_detail.html'


class StudentEditView(UpdateView):
    """
    Edit view for the student, displays form to edit the student.
    """
    template_name = 'class_management/generic_edit.html'
    model = Student
    form_class = StudentForm


class StudentAddView(CreateView):
    """
    Add view for the student, form is displayed to add the entry.
    """
    template_name = 'class_management/generic_edit.html'
    model = Student
    form_class = StudentForm


class WelcomeView(TemplateView):
    """
    The virtual home page for the app.
    """
    template_name = "class_management/welcome.html"


class InstructorListView(ListView):
    """
    List view for the instructors in the system.
    """
    model = Instructor
    template_name = 'class_management/instructor_list.html'


class InstructorEditView(UpdateView):
    """
    Edit view for the instructor. Uses a modal to display the form
    to edit.
    """
    template_name = 'class_management/instructor_detail.html'
    model = Instructor
    form_class = InstructorForm

    success_url = 'class_management/courses.html'

    def form_invalid(self, form):
        """
        Handle an invalid form from the user.
        :param form: The form that was submitted for this call.
        :return: Response with error details.
        """
        response = super(InstructorEditView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        """
        Handle the valid ajax request.
        :param form: Form that was submitted for this request.
        :return: Success message and other relevant info for further processing.
        """
        response = super(InstructorEditView, self).form_valid(form)
        if self.request.is_ajax():
            instructor = Instructor.objects.get(id=self.object.pk)
            data = {
                'message': "Successfully submitted form data.",
                'pk': self.object.pk,
                'name': instructor.first_name + " " + instructor.last_name,
                'courses': instructor.course_list(),
            }
            return JsonResponse(data)
        else:
            return response


class InstructorDeleteView(DeleteView):
    """
    Delete view for the instructor, uses modal to confirm deletion.
    """
    model = Instructor
    success_url = reverse_lazy('instructor_list')
    template_name = 'class_management/instructor_list.html'

    def delete(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        pk = self.object.pk
        self.object.delete()
        data = {
            'message': "Successfully deleted the instructor.",
            'pk': pk,
        }
        return JsonResponse(data)


class InstructorAddView(CreateView):
    """
    View to add a new instructor to the system.
    """
    template_name = 'class_management/generic_edit.html'
    model = Instructor
    form_class = InstructorForm


class CourseListView(CreateView):
    """
    Create view for the course.
    """
    template_name = 'class_management/courses.html'
    model = Course
    form_class = CourseForm

    def get_context_data(self, **kwargs):
        """
        Get the context and then add all the courses available in the system.
        This will then be used to display the list of all the courses in the system.
        :param kwargs:
        :return: context.
        """
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

    success_url = 'class_management/courses.html'

    def form_invalid(self, form):
        """
        Handle invalid request from the user.
        :param form:
        :return: Error messages.
        """
        response = super(CourseListView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        """
        Handle valid request from the user.
        :param form:
        :return: JSONRESPONSE with success message and other relevant info for further processing.
        """
        response = super(CourseListView, self).form_valid(form)
        if self.request.is_ajax():
            # print(form.cleaned_data)
            course = model_to_dict(Course.objects.get(pk=self.object.pk))
            department = Department.objects.get(department_code=course['course_dept_code'])
            data = {
                'message': "Successfully submitted form data.",
                'pk': self.object.pk,
                'obj': course,
                'dept': department.department_name,
            }
            return JsonResponse(data)
        else:
            return response


class CourseUpdateAjax(CreateView):
    template_name = 'class_management/generic_edit.html'
    form_class = CourseForm
    success_url = 'class_management/courses.html'

    def form_invalid(self, form):
        response = super(CourseUpdateAjax, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(CourseUpdateAjax, self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data.",
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class CourseQueryView(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            course_names = [course.course_name for course in Course.objects.all()]
            data = json.dumps(course_names)
            return HttpResponse(data, content_type='application/json')
        return HttpResponseForbidden
