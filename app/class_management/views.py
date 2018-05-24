# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import formset_factory, modelformset_factory, widgets, TextInput
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView, FormView
from django.views.generic.edit import DeleteView
from extra_views import ModelFormSetView, InlineFormSetView

from class_management.forms import StudentForm, InstructorForm, CourseForm, \
    DepartmentForm
from class_management.models import Student, Instructor, Course, Department, PhoneNumber


class ImageResponseMixin(object):
    pass
    # def render_to_response(self, context, **kwargs):
    #     """
    #     Create an image response.
    #     :param context:
    #     :param kwargs:
    #     :return:
    #     """
    #     print(self.request.GET)
    #     if 'image' in self.request.GET.get('export', ''):
    #         student = self.object
    #         image = FileWrapper(open(student.stud_pic.file))
    #         response = HttpResponse(f.read(), content_type="image/png")
    #         response['Content-Disposition'] = 'attachment; filename=image.png'
    #         # response['Content-Type'] = 'image/png'
    #         return response
    #     else:
    #         return super(ImageResponseMixin, self).render_to_response(context, **kwargs)


class StudentListView(ListView):
    """
    List view to display all the students in the system.
    """
    model = Student
    template_name = 'class_management/student_list.html'


class StudentDetailView(ImageResponseMixin, DetailView):
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

    def form_invalid(self, form):
        """
        Handle an invalid form from the user.
        :param form: The form that was submitted for this call.
        :return: Response with error details.
        """
        response = super(StudentEditView, self).form_invalid(form)
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
        response = super(StudentEditView, self).form_valid(form)
        if self.request.is_ajax():
            student = Student.objects.get(student_id=self.object.pk)
            data = {
                'message': "Successfully submitted form data.",
                'pk': self.object.pk,
                'name': student.first_name + " " + student.last_name,
                'courses': student.course_list(),
            }
            return JsonResponse(data)
        else:
            return response


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
        pk = self.object.pk  # Save the primary key before the object is deleted.
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


# class CourseAddView(CreateView):
#     """
#     Add course views using AJAX call.
#     Overrides form_invalid and form_valid methods of the super.
#
#     """
#     template_name = 'class_management/generic_edit.html'
#     form_class = CourseForm
#     success_url = 'class_management/courses.html'
#
#     def form_invalid(self, form):
#         response = super(CourseAddView, self).form_invalid(form)
#         if self.request.is_ajax():
#             return JsonResponse(form.errors, status=400)
#         else:
#             return response
#
#     def form_valid(self, form):
#         response = super(CourseAddView, self).form_valid(form)
#         if self.request.is_ajax():
#             print(form.cleaned_data)
#             data = {
#                 'message': "Successfully submitted form data.",
#                 'pk': self.object.pk,
#             }
#             return JsonResponse(data)
#         else:
#             return response


class CourseDeleteView(DeleteView):
    """
    Delete view for the instructor, uses modal to confirm deletion.
    """
    model = Course
    success_url = reverse_lazy('courses_list')
    template_name = 'class_management/courses.html'

    def delete(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        pk = self.object.pk  # Save the primary key before the object is deleted.
        self.object.delete()
        data = {
            'message': "Deletion successful.",
            'pk': pk,
        }
        return JsonResponse(data)


class AjaxMixin(object):
    def form_invalid(self, form):
        response = super(AjaxMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'message': "Ajax call successful.",
            }
            return JsonResponse(data)
        else:
            return response


class DepartmentListView(ListView):
    template_name = 'class_management/dept_list.html'
    model = Department


# class DepartmentAddView(FormView):
#     DepartmentFormset = modelformset_factory(model=Department, form=DepartmentForm)
#     form_class = DepartmentFormset
#     template_name = 'class_management/dept_edit.html'
#     success_url = reverse_lazy('dept_list')
#
#     def get_context_data(self, **kwargs):
#         DepartmentFormset = modelformset_factory(model=Department, form=DepartmentForm)
#         data = super(DepartmentAddView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['departments'] = DepartmentFormset(self.request.POST)
#         else:
#             data['departments'] = DepartmentFormset()
#         return data
#
#     def form_valid(self, form_):
#         context = self.get_context_data()
#         departments = context['departments']
#         departments.save()
#
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_success_url(self):
#         return reverse_lazy('dept_list')


class DepartmentAddView(ModelFormSetView):
    model = Department
    template_name = 'class_management/dept_edit.html'
    fields = '__all__'


class PhoneAddView(InlineFormSetView):
    model = Student
    inline_model = PhoneNumber
    template_name = 'class_management/phone_view.html'
    fields = ['area_code', 'first_three', 'last_four']
    factory_kwargs = {
        'widgets': {
            'area_code': TextInput(),
            'first_three': TextInput(),
            'last_four': TextInput(),
        },
        'extra': 1,
    }
