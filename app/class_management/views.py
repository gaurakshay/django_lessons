# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView, FormView
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import FormMixin, ModelFormMixin

from class_management.forms import StudentForm, InstructorForm, CourseForm
from class_management.models import Student, Instructor, Course, Department


class StudentListView(ListView):
    model = Student
    template_name = 'class_management/student_list.html'


class StudentDetailView(DetailView):
    model = Student
    pic = model.stud_pic
    template_name = 'class_management/student_detail.html'


class StudentEditView(UpdateView):
    template_name = 'class_management/generic_edit.html'
    model = Student
    form_class = StudentForm


class StudentAddView(CreateView):
    template_name = 'class_management/generic_edit.html'
    model = Student
    form_class = StudentForm


class WelcomeView(TemplateView):
    template_name = "class_management/welcome.html"


# def welcome(request):
#     return render(request, 'class_management/welcome.html')


class InstructorListView(ListView):
    model = Instructor
    template_name = 'class_management/instructor_list.html'


class InstructorEditView(UpdateView):
    template_name = 'class_management/instructor_detail.html'
    model = Instructor
    form_class = InstructorForm

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = InstructorForm(request.POST or None)
            if form.is_valid():
                form.save()
                return super(InstructorEditView, self).form_valid(form)
            return super(InstructorEditView, self).form_invalid(form)
        return HttpResponseForbidden


class InstructorFormView(FormView):
    form_class = InstructorForm
    template_name = 'class_management/instructor_detail.html'


class InstructorAddView(CreateView):
    template_name = 'class_management/generic_edit.html'
    model = Instructor
    form_class = InstructorForm


# class CourseListView(SingleObjectTemplateResponseMixin, ListView):
# class CourseListView(ModelFormMixin, ListView):
# class CourseListView(FormMixin, ListView):
# class CourseListView(DetailView):
class CourseListView(CreateView):
    template_name = 'class_management/courses.html'
    model = Course
    form_class = CourseForm

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context

    # def get_queryset(self):
    #     return Course.objects.all()

    success_url = 'class_management/courses.html'

    def form_invalid(self, form):
        response = super(CourseListView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
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


class CourseView(TemplateView):
    template_name = 'class_management/courses.html'

# def courses(request):
#     return render(request, 'class_management/courses.html')


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
            # course_names = [{'name': course.course_name} for course in Course.objects.all()]
            course_names = [course.course_name for course in Course.objects.all()]
            data = json.dumps(course_names)
            return HttpResponse(data, content_type='application/json')
        return HttpResponseForbidden


#
# def ajax_courses(request):
#     course_list = Course.objects.all()
#     course_names = list()
#     for course in course_list:
#         course_names.append(course.course_name)
#     data = json.dumps(course_names)
#     # return course_names
#     # return r"HELLO"
#     # todo_items = ['Mow Lawn', 'Buy Groceries', ]
#     # data = json.dumps(todo_items)
#     return HttpResponse(data, content_type='application/json')
