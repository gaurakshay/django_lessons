from django.conf.urls import url, include

from class_management.views import StudentListView, StudentDetailView, StudentEditView, InstructorListView, \
    InstructorEditView, StudentAddView, InstructorAddView, CourseListView, CourseQueryView, WelcomeView, \
    CourseUpdateAjax, InstructorDeleteView

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
                url(r'^$', InstructorEditView.as_view(), name='instructor_edit'),  # Edit view.
                url(r'^delete/', InstructorDeleteView.as_view(), name='instructor_delete')  # Delete view.
            ])),
        ])),

        # TODO update the course views.
        url(r'^courses/$', CourseListView.as_view(), name='courses'),  # Course view.
        # View the courses by running a AJAX query to fetch the course details.
        url(r'^ajax_courses/$', CourseQueryView.as_view(), name='ajax_courses'),
        url(r'^course_update_ajax/$', CourseUpdateAjax.as_view(), name='course_update_ajax')  # Edit view.
    ])),
]
