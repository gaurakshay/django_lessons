from django.conf.urls import url, include

from class_management.views import StudentListView, StudentDetailView, StudentEditView, InstructorListView, \
    InstructorEditView, StudentAddView, InstructorAddView, CourseListView, WelcomeView, \
    InstructorDeleteView, DepartmentListView, DepartmentAddView, PhoneAddView, \
    CourseDeleteView

urlpatterns = [
    url(r'^mgmt/', include([
        url(r'^$', WelcomeView.as_view(), name='welcome'),  # Home page.

        url(r'^students/', include([  # URLs related to Students.
            url(r'^$', StudentListView.as_view(), name='student_list'),  # List view.
            url(r'^add/$', StudentAddView.as_view(), name='student_add'),  # Add view.
            url(r'^(?P<pk>\d+)/', include([
                url(r'^$', StudentDetailView.as_view(), name='student_details'),  # Detail view.
                url(r'^edit/$', StudentEditView.as_view(), name='student_edit'),  # Edit view.
            ])),
        ])),

        url(r'^instructors/', include([  # URLs related to Instructors.
            url(r'^$', InstructorListView.as_view(), name='instructor_list'),  # List view.
            url(r'^add/$', InstructorAddView.as_view(), name='instructor_add'),  # Add view.
            url(r'^(?P<pk>\d+)/', include([
                url(r'^$', InstructorEditView.as_view(), name='instructor_edit'),  # Edit view + Detail view.
                url(r'^delete/', InstructorDeleteView.as_view(), name='instructor_delete')  # Delete view.
            ])),
        ])),

        # TODO update the course views.
        url(r'^courses/', include([
            url(r'^$', CourseListView.as_view(), name='course_list'),
            url(r'^(?P<pk>\d+)/delete/$', CourseDeleteView.as_view(), name='course_delete'),
        ])),

        url(r'^dept/', include([
            url(r'^browse/$', DepartmentListView.as_view(), name='dept_list'),
            url(r'^add/$', DepartmentAddView.as_view(), name='dept_add'),
        ])),

        url(r'^(?P<pk>\d+)/phones/$', PhoneAddView.as_view(), name='phone_view'),

    ])),
]
